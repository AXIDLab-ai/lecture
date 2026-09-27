# Week 02. Generative UI 설계와 테스트 먼저 쓰는 프론트엔드 구현

## 0. 이번 주 목표

이번 주는 1주차에 만든 PRD를 화면으로 바꾼다.  
하지만 바로 UI부터 만들지 않는다. 먼저 “사용자가 무엇을 하면 화면이 어떻게 반응해야 하는가”를 테스트로 쓴다. 그 다음 AI 에이전트에게 테스트를 통과하는 컴포넌트를 만들게 한다.

이번 주가 끝나면 다음 산출물을 만든다.

```text
docs/
  screen_spec.md
src/
  components/
    TaskForm.tsx
    TaskForm.test.tsx
    TaskList.tsx
    TaskList.test.tsx
  App.tsx
  main.tsx
  setupTests.ts
vite.config.ts
```

---

## 1. 사전 준비

### 1.1 Vite React 프로젝트 생성

이미 프로젝트가 있다면 이 단계는 건너뛴다.  
새로 시작하는 경우 다음을 실행한다.

```bash
npm create vite@latest axdx-prototype -- --template react-ts
cd axdx-prototype
npm install
```

### 1.2 테스트 도구 설치

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom @testing-library/user-event jsdom
```

### 1.3 `package.json` 스크립트 확인

`package.json`의 `scripts`를 다음처럼 맞춘다.

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "test": "vitest",
    "test:run": "vitest run"
  }
}
```

### 1.4 `vite.config.ts` 설정

루트의 `vite.config.ts`를 다음처럼 수정한다.

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './src/setupTests.ts',
  },
})
```

### 1.5 `src/setupTests.ts` 생성

```bash
touch src/setupTests.ts
```

`src/setupTests.ts`:

```ts
import '@testing-library/jest-dom'
```

### 1.6 Tailwind CSS 선택 사항

시간이 부족하면 Tailwind 설정 없이 기본 CSS로 진행해도 된다.  
Tailwind를 쓰는 경우 다음을 실행한다.

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

`tailwind.config.js`:

```js
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

`src/index.css` 상단:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

## 2. Step 1. 화면 정의서 만들기

### 2.1 프롬프트

```text
다음 PRD와 Acceptance Criteria를 바탕으로 화면 정의서를 작성해줘.
화면별로 목적, 사용자 입력, 주요 컴포넌트, 정상 상태, 빈 상태, 오류 상태, 엣지 케이스를 포함해줘.

PRD:
[docs/PRD.md 내용 붙여넣기]

Acceptance Criteria:
[docs/acceptance_criteria.md 내용 붙여넣기]

출력 형식:
# screen_spec.md

## 화면명
- 목적:
- 사용자 입력:
- 주요 컴포넌트:
- 정상 상태:
- 빈 상태:
- 오류 상태:
- 엣지 케이스:
```

### 2.2 결과 저장

```bash
touch docs/screen_spec.md
code docs/screen_spec.md
```

AI 결과를 `docs/screen_spec.md`에 저장한다.

---

## 3. Step 2. 이번 주에 구현할 UI 범위 정하기

처음부터 큰 화면을 만들지 않는다. 가장 작은 기능 하나를 고른다.

이번 실습의 기본 구현 범위는 다음이다.

1. `TaskForm`: 과제명 입력 후 저장
2. `TaskList`: 과제 목록 표시
3. `App`: 폼과 목록 연결

추가 구현은 다음 중 하나를 선택한다.

| 기능 | 반드시 포함할 테스트 |
|---|---|
| 검색 | 공백 처리, 결과 없음 |
| 필터 | 전체/완료/미완료 전환 |
| 삭제 | 삭제 후 목록 갱신 |
| 마감일 표시 | 오늘/지남/미래 날짜 처리 |

---

## 4. Step 3. TaskForm 테스트 먼저 작성하기

파일을 만든다.

```bash
mkdir -p src/components
touch src/components/TaskForm.test.tsx
```

`src/components/TaskForm.test.tsx`에 붙여넣는다.

```tsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { TaskForm } from './TaskForm'

describe('TaskForm', () => {
  it('과제명을 입력하면 저장 버튼을 누를 수 있다', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()

    render(<TaskForm onSubmit={onSubmit} />)

    await user.type(screen.getByLabelText('과제명'), 'MIS 과제')

    expect(screen.getByRole('button', { name: '저장' })).toBeEnabled()
  })

  it('과제명이 비어 있으면 저장 버튼은 비활성화된다', () => {
    const onSubmit = vi.fn()

    render(<TaskForm onSubmit={onSubmit} />)

    expect(screen.getByRole('button', { name: '저장' })).toBeDisabled()
  })

  it('공백만 입력하면 저장 버튼은 비활성화된다', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()

    render(<TaskForm onSubmit={onSubmit} />)

    await user.type(screen.getByLabelText('과제명'), '   ')

    expect(screen.getByRole('button', { name: '저장' })).toBeDisabled()
  })

  it('100자를 초과하면 오류 메시지를 보여준다', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()
    const longText = '가'.repeat(101)

    render(<TaskForm onSubmit={onSubmit} />)

    await user.type(screen.getByLabelText('과제명'), longText)

    expect(screen.getByText('과제명은 100자 이하여야 합니다')).toBeInTheDocument()
  })

  it('정상 제출 시 onSubmit에 trim된 과제명을 전달한다', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()

    render(<TaskForm onSubmit={onSubmit} />)

    await user.type(screen.getByLabelText('과제명'), '  MIS 과제  ')
    await user.click(screen.getByRole('button', { name: '저장' }))

    expect(onSubmit).toHaveBeenCalledWith('MIS 과제')
  })
})
```

### 4.1 RED 확인

```bash
npm test
```

아직 `TaskForm.tsx`가 없기 때문에 실패해야 정상이다.  
이 단계가 TDD의 Red 단계다.

---

## 5. Step 4. AI에게 테스트 통과 컴포넌트 요청하기

### 5.1 프롬프트

```text
다음 테스트를 통과하는 React + TypeScript 컴포넌트를 작성해줘.
Tailwind CSS를 사용하되, 테스트가 찾는 label과 button name은 바꾸지 마.

요구사항:
- 과제명 입력 필드가 있어야 한다.
- label text는 "과제명"이어야 한다.
- button name은 "저장"이어야 한다.
- 과제명이 비어 있거나 공백만 있으면 저장 버튼은 disabled 상태여야 한다.
- 과제명은 100자 이하여야 한다.
- 100자를 초과하면 "과제명은 100자 이하여야 합니다" 메시지를 보여준다.
- 정상 제출 시 onSubmit(title)을 호출한다.
- title은 trim해서 전달한다.

테스트 코드:
[TaskForm.test.tsx 전체 붙여넣기]
```

### 5.2 구현 파일 만들기

```bash
touch src/components/TaskForm.tsx
```

`src/components/TaskForm.tsx`:

```tsx
import { FormEvent, useMemo, useState } from 'react'

type TaskFormProps = {
  onSubmit: (title: string) => void
}

export function TaskForm({ onSubmit }: TaskFormProps) {
  const [title, setTitle] = useState('')

  const trimmedTitle = title.trim()
  const isTooLong = title.length > 100
  const canSubmit = useMemo(() => trimmedTitle.length > 0 && !isTooLong, [trimmedTitle, isTooLong])

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (!canSubmit) return
    onSubmit(trimmedTitle)
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-3 rounded-2xl border p-4">
      <div className="space-y-1">
        <label htmlFor="task-title" className="block text-sm font-medium">
          과제명
        </label>
        <input
          id="task-title"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          className="w-full rounded-xl border px-3 py-2"
          placeholder="예: MIS 과제"
        />
      </div>

      {isTooLong && (
        <p className="text-sm text-red-600" role="alert">
          과제명은 100자 이하여야 합니다
        </p>
      )}

      <button
        type="submit"
        disabled={!canSubmit}
        className="rounded-xl border px-4 py-2 disabled:opacity-50"
      >
        저장
      </button>
    </form>
  )
}
```

### 5.3 GREEN 확인

```bash
npm test
```

모든 `TaskForm` 테스트가 통과해야 한다.

---

## 6. Step 5. TaskList 테스트 작성하기

```bash
touch src/components/TaskList.test.tsx
```

`src/components/TaskList.test.tsx`:

```tsx
import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { TaskList } from './TaskList'

const tasks = [
  { id: '1', title: 'MIS 과제', status: 'todo' as const },
  { id: '2', title: '발표 준비', status: 'done' as const },
]

describe('TaskList', () => {
  it('과제 목록을 보여준다', () => {
    render(<TaskList tasks={tasks} />)

    expect(screen.getByText('MIS 과제')).toBeInTheDocument()
    expect(screen.getByText('발표 준비')).toBeInTheDocument()
  })

  it('과제가 없으면 빈 상태 메시지를 보여준다', () => {
    render(<TaskList tasks={[]} />)

    expect(screen.getByText('아직 등록된 일정이 없습니다')).toBeInTheDocument()
  })

  it('완료된 과제는 완료 표시를 보여준다', () => {
    render(<TaskList tasks={tasks} />)

    expect(screen.getByText('완료')).toBeInTheDocument()
  })
})
```

### 6.1 구현 파일 만들기

```bash
touch src/components/TaskList.tsx
```

`src/components/TaskList.tsx`:

```tsx
export type TaskItem = {
  id: string
  title: string
  status: 'todo' | 'done'
}

type TaskListProps = {
  tasks: TaskItem[]
}

export function TaskList({ tasks }: TaskListProps) {
  if (tasks.length === 0) {
    return (
      <div className="rounded-2xl border border-dashed p-6 text-center text-sm text-gray-600">
        아직 등록된 일정이 없습니다
      </div>
    )
  }

  return (
    <ul className="space-y-2">
      {tasks.map((task) => (
        <li key={task.id} className="flex items-center justify-between rounded-2xl border p-3">
          <span>{task.title}</span>
          {task.status === 'done' ? (
            <span className="rounded-full border px-2 py-1 text-xs">완료</span>
          ) : (
            <span className="rounded-full border px-2 py-1 text-xs">진행 중</span>
          )}
        </li>
      ))}
    </ul>
  )
}
```

### 6.2 테스트 실행

```bash
npm test
```

---

## 7. Step 6. App에서 컴포넌트 연결하기

`src/App.tsx`를 다음으로 교체한다.

```tsx
import { useState } from 'react'
import { TaskForm } from './components/TaskForm'
import { TaskItem, TaskList } from './components/TaskList'

export default function App() {
  const [tasks, setTasks] = useState<TaskItem[]>([])

  function handleAddTask(title: string) {
    setTasks((prev) => [
      ...prev,
      {
        id: crypto.randomUUID(),
        title,
        status: 'todo',
      },
    ])
  }

  return (
    <main className="mx-auto max-w-2xl space-y-6 p-6">
      <section className="space-y-2">
        <p className="text-sm text-gray-500">AX/DX Prototype</p>
        <h1 className="text-3xl font-bold">AI Syllabus Planner</h1>
        <p className="text-gray-700">
          강의계획서에서 추출한 과제와 시험 일정을 관리하는 프로토타입입니다.
        </p>
      </section>

      <TaskForm onSubmit={handleAddTask} />
      <TaskList tasks={tasks} />
    </main>
  )
}
```

실행한다.

```bash
npm run dev
```

브라우저에서 확인한다.

```text
http://localhost:5173
```

직접 확인할 것:

- 과제명이 비어 있으면 저장 버튼이 비활성화되는가?
- 공백만 입력해도 저장 버튼이 비활성화되는가?
- 101자를 입력하면 오류 메시지가 보이는가?
- 저장하면 목록에 추가되는가?

---

## 8. Step 7. Refactor 요청하기

테스트가 통과한 뒤에만 리팩토링한다.

### 프롬프트

```text
다음 컴포넌트를 리팩토링해줘.
단, 기존 테스트가 모두 통과해야 하고, label text와 button name은 바꾸지 마.

개선 목표:
- 중복 제거
- 가독성 향상
- 접근성 유지
- 타입 안정성 유지
- 과도한 추상화 금지

코드:
[TaskForm.tsx 또는 TaskList.tsx 붙여넣기]
```

---

## 9. 이번 주 제출물

- `docs/screen_spec.md`
- `src/components/TaskForm.tsx`
- `src/components/TaskForm.test.tsx`
- `src/components/TaskList.tsx`
- `src/components/TaskList.test.tsx`
- `src/App.tsx`
- 테스트 실행 화면 캡처
- 브라우저 실행 화면 캡처

---

## 10. 평가 기준

| 항목 | 배점 |
|---|---:|
| 화면 정의서가 PRD와 연결되는가 | 20 |
| 테스트가 먼저 작성되었는가 | 25 |
| 정상/엣지/실패 케이스가 포함되었는가 | 25 |
| UI가 사용 가능한 수준인가 | 20 |
| 리팩토링 기록이 있는가 | 10 |

---

## 11. 자가 점검

```text
[ ] npm test가 통과한다
[ ] npm run dev로 화면이 열린다
[ ] 과제 입력이 가능하다
[ ] 빈 상태 메시지가 있다
[ ] 오류 메시지가 있다
[ ] 테스트에 엣지 케이스가 포함되어 있다
[ ] 테스트가 화면의 실제 사용자 행동을 검증한다
```
