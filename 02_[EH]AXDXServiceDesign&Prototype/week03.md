# Week 03. 데이터 모델, API 로직, KPI 이벤트를 TDD로 구현하기

## 0. 이번 주 목표

이번 주는 화면 뒤에 있는 데이터를 설계한다.  
MIS에서 중요한 것은 “기능이 있다”가 아니라 “데이터로 판단할 수 있다”이다. 사용자가 어떤 행동을 했는지 기록하고, 그 행동이 서비스 목표와 연결되는지 확인해야 한다.

이번 주가 끝나면 다음 산출물을 만든다.

```text
docs/
  data_schema.json
  event_taxonomy.md
  kpi.md
src/
  lib/
    types.ts
    taskValidation.ts
    taskValidation.test.ts
    taskRepository.ts
    taskRepository.test.ts
    kpi.ts
    kpi.test.ts
```

---

## 1. 사전 준비

2주차 프로젝트 폴더에서 시작한다.

```bash
cd axdx-prototype
```

테스트가 실행되는지 확인한다.

```bash
npm test
```

`src/lib` 폴더를 만든다.

```bash
mkdir -p src/lib
```

---

## 2. Step 1. 데이터 스키마 설계하기

### 2.1 프롬프트

```text
다음 PRD와 화면 정의서를 바탕으로 데이터 스키마를 설계해줘.
각 엔티티는 TypeScript type과 JSON 예시를 함께 제시해줘.

PRD:
[docs/PRD.md 내용 붙여넣기]

화면 정의서:
[docs/screen_spec.md 내용 붙여넣기]

출력 형식:
# data_schema.json
# TypeScript types
# 예시 데이터
# 유효성 검증 규칙

조건:
- 4주 프로토타입이므로 복잡한 DB 설계는 피한다.
- user, task, event를 중심으로 설계한다.
- KPI 계산에 필요한 필드를 포함한다.
```

### 2.2 `docs/data_schema.json` 만들기

```bash
touch docs/data_schema.json
```

예시 내용을 붙여넣는다.

```json
{
  "users": [
    {
      "id": "user-1",
      "email": "student@example.com",
      "createdAt": "2026-05-01T00:00:00.000Z"
    }
  ],
  "tasks": [
    {
      "id": "task-1",
      "title": "MIS 과제",
      "dueDate": "2026-05-10",
      "status": "todo",
      "createdAt": "2026-05-01T00:00:00.000Z",
      "completedAt": null
    }
  ],
  "events": [
    {
      "eventName": "task_created",
      "userId": "user-1",
      "properties": {
        "taskId": "task-1"
      },
      "timestamp": "2026-05-01T00:00:00.000Z"
    }
  ]
}
```

---

## 3. Step 2. TypeScript 타입 만들기

`src/lib/types.ts`를 만든다.

```bash
touch src/lib/types.ts
```

`src/lib/types.ts`:

```ts
export type TaskStatus = 'todo' | 'done'

export type Task = {
  id: string
  title: string
  dueDate: string | null
  status: TaskStatus
  createdAt: string
  completedAt: string | null
}

export type TaskInput = {
  title: string
  dueDate: string | null
}

export type EventName =
  | 'task_created'
  | 'task_completed'
  | 'task_overdue_viewed'

export type AnalyticsEvent = {
  eventName: EventName
  userId: string
  properties: Record<string, string | number | boolean | null>
  timestamp: string
}
```

---

## 4. Step 3. 데이터 검증 테스트 먼저 쓰기

서비스의 데이터는 더럽다. 사용자는 빈 값, 이상한 날짜, 너무 긴 문자열을 넣는다.  
그래서 저장 전에 검증해야 한다.

`src/lib/taskValidation.test.ts`를 만든다.

```bash
touch src/lib/taskValidation.test.ts
```

`src/lib/taskValidation.test.ts`:

```ts
import { describe, expect, it } from 'vitest'
import { validateTaskInput } from './taskValidation'

describe('validateTaskInput', () => {
  it('정상적인 과제명은 유효하다', () => {
    expect(validateTaskInput({ title: 'MIS 과제', dueDate: '2026-05-10' })).toEqual({
      valid: true,
      errors: [],
    })
  })

  it('과제명이 비어 있으면 유효하지 않다', () => {
    expect(validateTaskInput({ title: '', dueDate: '2026-05-10' })).toEqual({
      valid: false,
      errors: ['과제명은 필수입니다'],
    })
  })

  it('공백만 있는 과제명은 유효하지 않다', () => {
    expect(validateTaskInput({ title: '   ', dueDate: '2026-05-10' })).toEqual({
      valid: false,
      errors: ['과제명은 필수입니다'],
    })
  })

  it('과제명이 100자를 초과하면 유효하지 않다', () => {
    expect(validateTaskInput({ title: '가'.repeat(101), dueDate: '2026-05-10' })).toEqual({
      valid: false,
      errors: ['과제명은 100자 이하여야 합니다'],
    })
  })

  it('날짜 형식이 잘못되면 유효하지 않다', () => {
    expect(validateTaskInput({ title: 'MIS 과제', dueDate: 'not-a-date' })).toEqual({
      valid: false,
      errors: ['마감일 형식이 올바르지 않습니다'],
    })
  })

  it('마감일은 null일 수 있다', () => {
    expect(validateTaskInput({ title: 'MIS 과제', dueDate: null })).toEqual({
      valid: true,
      errors: [],
    })
  })
})
```

### 4.1 RED 확인

```bash
npm test
```

`taskValidation.ts`가 없어서 실패해야 정상이다.

---

## 5. Step 4. 데이터 검증 함수 구현하기

`src/lib/taskValidation.ts`를 만든다.

```bash
touch src/lib/taskValidation.ts
```

`src/lib/taskValidation.ts`:

```ts
import { TaskInput } from './types'

type ValidationResult = {
  valid: boolean
  errors: string[]
}

function isValidDateString(value: string): boolean {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false

  const date = new Date(`${value}T00:00:00.000Z`)
  if (Number.isNaN(date.getTime())) return false

  const [year, month, day] = value.split('-').map(Number)
  return (
    date.getUTCFullYear() === year &&
    date.getUTCMonth() + 1 === month &&
    date.getUTCDate() === day
  )
}

export function validateTaskInput(input: TaskInput): ValidationResult {
  const errors: string[] = []

  if (input.title.trim().length === 0) {
    errors.push('과제명은 필수입니다')
  }

  if (input.title.length > 100) {
    errors.push('과제명은 100자 이하여야 합니다')
  }

  if (input.dueDate !== null && !isValidDateString(input.dueDate)) {
    errors.push('마감일 형식이 올바르지 않습니다')
  }

  return {
    valid: errors.length === 0,
    errors,
  }
}
```

### 5.1 GREEN 확인

```bash
npm test
```

---

## 6. Step 5. Mock Repository 테스트 먼저 쓰기

API 서버를 바로 만들지 않아도 된다.  
처음에는 mock repository로 데이터 저장 흐름을 구현한다.

`src/lib/taskRepository.test.ts`를 만든다.

```bash
touch src/lib/taskRepository.test.ts
```

`src/lib/taskRepository.test.ts`:

```ts
import { describe, expect, it } from 'vitest'
import { createTaskRepository } from './taskRepository'

describe('taskRepository', () => {
  it('과제를 추가하면 목록에서 조회된다', () => {
    const repository = createTaskRepository()

    const task = repository.add({ title: 'MIS 과제', dueDate: '2026-05-10' })

    expect(repository.findAll()).toContainEqual(task)
  })

  it('추가된 과제의 제목은 trim 처리된다', () => {
    const repository = createTaskRepository()

    const task = repository.add({ title: '  MIS 과제  ', dueDate: null })

    expect(task.title).toBe('MIS 과제')
  })

  it('완료 처리하면 상태가 done으로 바뀐다', () => {
    const repository = createTaskRepository()
    const task = repository.add({ title: 'MIS 과제', dueDate: null })

    repository.markDone(task.id)

    expect(repository.findById(task.id)?.status).toBe('done')
    expect(repository.findById(task.id)?.completedAt).not.toBeNull()
  })

  it('없는 ID를 완료 처리하면 에러를 반환한다', () => {
    const repository = createTaskRepository()

    expect(() => repository.markDone('missing-id')).toThrow('과제를 찾을 수 없습니다')
  })
})
```

### 6.1 RED 확인

```bash
npm test
```

---

## 7. Step 6. Mock Repository 구현하기

`src/lib/taskRepository.ts`를 만든다.

```bash
touch src/lib/taskRepository.ts
```

`src/lib/taskRepository.ts`:

```ts
import { Task, TaskInput } from './types'

export function createTaskRepository() {
  let tasks: Task[] = []

  return {
    add(input: TaskInput): Task {
      const task: Task = {
        id: crypto.randomUUID(),
        title: input.title.trim(),
        dueDate: input.dueDate,
        status: 'todo',
        createdAt: new Date().toISOString(),
        completedAt: null,
      }
      tasks = [...tasks, task]
      return task
    },

    findAll(): Task[] {
      return tasks
    },

    findById(id: string): Task | undefined {
      return tasks.find((task) => task.id === id)
    },

    markDone(id: string): void {
      const exists = tasks.some((task) => task.id === id)
      if (!exists) throw new Error('과제를 찾을 수 없습니다')

      tasks = tasks.map((task) =>
        task.id === id
          ? { ...task, status: 'done', completedAt: new Date().toISOString() }
          : task,
      )
    },
  }
}
```

### 7.1 테스트 실행

```bash
npm test
```

---

## 8. Step 7. 이벤트 택소노미 만들기

KPI는 그냥 숫자가 아니다. 사용자의 행동을 이벤트로 기록해야 계산할 수 있다.

### 8.1 프롬프트

```text
다음 서비스의 KPI를 측정하기 위한 이벤트 택소노미를 작성해줘.
각 이벤트는 event_name, trigger, properties, example payload, related KPI를 포함해줘.

서비스 설명:
[docs/PRD.md 요약 붙여넣기]

KPI 후보:
- 일정 추출 성공률
- 일정 확정률
- 과제 완료율
- D+7 재사용률

출력 형식:
| event_name | trigger | properties | example payload | related KPI |
|---|---|---|---|---|
```

### 8.2 `docs/event_taxonomy.md` 작성

```bash
touch docs/event_taxonomy.md
```

예시:

```markdown
# Event Taxonomy

| event_name | trigger | properties | related KPI |
|---|---|---|---|
| task_created | 사용자가 과제를 등록함 | task_id, due_date, created_at | 과제 등록 수 |
| task_completed | 사용자가 과제를 완료 처리함 | task_id, completed_at | 완료율 |
| task_overdue_viewed | 사용자가 지연 과제를 봄 | overdue_count | 지연 과제 인지율 |
```

---

## 9. Step 8. KPI 문서 작성하기

`docs/kpi.md`를 만든다.

```bash
touch docs/kpi.md
```

`docs/kpi.md`:

```markdown
# KPI 정의

## 1. Task Completion Rate
- 정의: 생성된 과제 중 완료 처리된 과제의 비율
- 계산식: 완료 과제 수 / 전체 과제 수
- 목표: 70%

## 2. AI Accuracy
- 정의: AI가 추출한 일정 중 사용자가 수정 없이 확정한 일정의 비율
- 계산식: 수정 없이 저장된 일정 수 / AI가 추출한 일정 수
- 목표: 85%

## 3. Retention D+7
- 정의: 가입 후 7일 뒤에도 일정을 추가하거나 완료 처리한 사용자 비율
- 계산식: D+7 활성 사용자 수 / 가입 사용자 수
- 목표: 30%
```

---

## 10. Step 9. KPI 계산 함수 TDD

`src/lib/kpi.test.ts`를 만든다.

```bash
touch src/lib/kpi.test.ts
```

`src/lib/kpi.test.ts`:

```ts
import { describe, expect, it } from 'vitest'
import { calculateCompletionRate } from './kpi'
import { Task } from './types'

const baseTask = {
  dueDate: null,
  createdAt: '2026-05-01T00:00:00.000Z',
  completedAt: null,
} satisfies Pick<Task, 'dueDate' | 'createdAt' | 'completedAt'>

describe('calculateCompletionRate', () => {
  it('전체 과제 중 완료 과제 비율을 계산한다', () => {
    const tasks: Task[] = [
      { ...baseTask, id: '1', title: 'A', status: 'done', completedAt: '2026-05-02T00:00:00.000Z' },
      { ...baseTask, id: '2', title: 'B', status: 'todo' },
    ]

    expect(calculateCompletionRate(tasks)).toBe(0.5)
  })

  it('과제가 없으면 0을 반환한다', () => {
    expect(calculateCompletionRate([])).toBe(0)
  })

  it('모든 과제가 완료되면 1을 반환한다', () => {
    const tasks: Task[] = [
      { ...baseTask, id: '1', title: 'A', status: 'done', completedAt: '2026-05-02T00:00:00.000Z' },
      { ...baseTask, id: '2', title: 'B', status: 'done', completedAt: '2026-05-03T00:00:00.000Z' },
    ]

    expect(calculateCompletionRate(tasks)).toBe(1)
  })
})
```

`src/lib/kpi.ts`를 만든다.

```bash
touch src/lib/kpi.ts
```

`src/lib/kpi.ts`:

```ts
import { Task } from './types'

export function calculateCompletionRate(tasks: Task[]): number {
  if (tasks.length === 0) return 0
  const doneCount = tasks.filter((task) => task.status === 'done').length
  return doneCount / tasks.length
}
```

테스트 실행:

```bash
npm test
```

---

## 11. Step 10. AI 에이전트에게 구현 요청하기

다음 프롬프트는 앞으로 데이터 로직을 추가할 때 계속 사용한다.

```text
다음 테스트를 기준으로 구현 파일을 작성해줘.

규칙:
- 테스트를 수정하지 마.
- 테스트가 실패할 경우 원인을 먼저 설명해.
- 엣지 케이스 처리를 코드에 명시해.
- TypeScript 타입을 느슨하게 만들지 마.
- any를 사용하지 마.

테스트 코드:
[테스트 코드 붙여넣기]
```

---

## 12. 이번 주 제출물

- `docs/data_schema.json`
- `docs/event_taxonomy.md`
- `docs/kpi.md`
- `src/lib/types.ts`
- `src/lib/taskValidation.ts`
- `src/lib/taskValidation.test.ts`
- `src/lib/taskRepository.ts`
- `src/lib/taskRepository.test.ts`
- `src/lib/kpi.ts`
- `src/lib/kpi.test.ts`
- 테스트 실행 결과 캡처

---

## 13. 평가 기준

| 항목 | 배점 |
|---|---:|
| 데이터 스키마가 서비스 기능과 연결되는가 | 20 |
| 입력 검증 테스트가 충분한가 | 25 |
| 엣지 케이스가 포함되는가 | 20 |
| KPI 계산 로직이 테스트 가능한가 | 20 |
| 이벤트 택소노미가 분석 가능하게 설계되었는가 | 15 |

---

## 14. 자가 점검

```text
[ ] src/lib/types.ts가 있다
[ ] validateTaskInput 테스트가 통과한다
[ ] 빈 문자열, 공백, 101자, 잘못된 날짜 테스트가 있다
[ ] taskRepository 테스트가 통과한다
[ ] 없는 ID 처리 테스트가 있다
[ ] calculateCompletionRate 테스트가 통과한다
[ ] docs/event_taxonomy.md가 있다
[ ] docs/kpi.md가 있다
```
