# Week 01. 문제정의, UX 구조화, PRD, 하네스, 테스트 가능한 요구사항 만들기

## 0. 이번 주 목표

이번 주는 코드를 많이 짜는 시간이 아니다.  
좋은 AI 프로토타입은 좋은 질문에서 시작된다. 서비스가 풀 문제를 정하고, 사용자의 흐름을 이해하고, 그 문제를 테스트 가능한 요구사항으로 바꾼다. 마지막에는 AI 에이전트가 작업 범위를 벗어나지 않도록 하네스 파일을 만든다.

이번 주가 끝나면 다음 산출물을 만든다.

```text
docs/
  problem.md
  journey.md
  persona.md
  PRD.md
  acceptance_criteria.md
  test_cases.md
AGENTS.md
README.md
```

---

## 1. 사전 준비

### 1.1 설치 확인

터미널에서 다음 명령을 실행한다.

```bash
node -v
npm -v
git --version
```

정상 예시는 다음과 비슷하다.

```text
v20.x.x
10.x.x
git version 2.x.x
```

### 1.2 작업 폴더 만들기

```bash
mkdir axdx-prototype
cd axdx-prototype

mkdir docs
touch docs/problem.md
touch docs/journey.md
touch docs/persona.md
touch docs/PRD.md
touch docs/acceptance_criteria.md
touch docs/test_cases.md
touch AGENTS.md
touch README.md
```

---

## 2. 오늘 만들 서비스 예시

기본 예시는 다음 서비스로 진행한다.

> **AI Syllabus Planner**  
> 강의계획서 PDF 또는 강의 안내 텍스트를 입력하면 과제, 시험, 발표 일정을 추출하고, 마감일 기준으로 우선순위를 추천하는 대학생 시간관리 서비스

팀 프로젝트를 진행하는 경우에는 본인의 서비스 주제로 바꾸어 진행해도 된다.  
단, 4주 안에 프로토타입으로 구현 가능한 범위여야 한다.

---

## 3. Step 1. 문제정의 만들기

### 3.1 AI에게 아이디어 확장 요청하기

아래 프롬프트를 ChatGPT, Claude, Cursor Chat 중 하나에 그대로 붙여넣는다.

```text
너는 MIS 전공 서비스 기획 멘토다.
학부 4학년 예비졸업생이 4주 안에 만들 수 있는 AX/DX 서비스 프로토타입 주제를 제안해줘.

주제는 "AI Syllabus Planner"이다.
이 서비스는 강의계획서나 수업 안내 텍스트를 분석하여 과제, 시험, 발표 일정을 추출하고 학생의 시간관리를 돕는다.

다음 형식으로 문제정의를 작성해줘.

# 문제정의
## 1. 문제 상황
## 2. 핵심 사용자
## 3. 사용자가 겪는 불편
## 4. 현재 대안과 한계
## 5. 서비스 아이디어
## 6. 4주 안에 구현 가능한 최소 기능
## 7. 데이터로 검증할 수 있는 지표
## 8. 구현 범위에서 제외할 것
```

### 3.2 결과 저장

AI가 만든 결과를 검토한 뒤 `docs/problem.md`에 붙여넣는다.

```bash
code docs/problem.md
```

### 3.3 체크포인트

`docs/problem.md`가 다음 질문에 답하는지 확인한다.

- 누가 불편한가?
- 언제 불편한가?
- 지금은 어떻게 해결하고 있는가?
- 이 서비스가 있으면 무엇이 달라지는가?
- 실제로 좋아졌는지 어떤 데이터로 판단할 수 있는가?
- 4주 안에 만들지 않을 기능은 무엇인가?

---

## 4. Step 2. Persona 만들기

### 4.1 프롬프트

```text
다음 문제정의를 바탕으로 핵심 사용자 페르소나 1명을 작성해줘.

문제정의:
[docs/problem.md 내용 붙여넣기]

다음 형식으로 작성해줘.

# Persona
## 이름
## 나이 / 전공 / 학년
## 하루 일과
## 자주 사용하는 도구
## 목표
## Pain Point
## 서비스 사용 전 행동
## 서비스 사용 후 기대 변화
## 이 사용자가 절대 원하지 않는 것
```

### 4.2 결과 저장

결과를 `docs/persona.md`에 저장한다.

---

## 5. Step 3. User Journey Map 만들기

### 5.1 프롬프트

```text
다음 문제정의와 페르소나를 바탕으로 User Journey Map을 작성해줘.

문제정의:
[docs/problem.md 내용 붙여넣기]

페르소나:
[docs/persona.md 내용 붙여넣기]

다음 표 형식으로 작성해줘.

| 단계 | 사용자 행동 | 생각 | 감정 | Pain Point | 서비스 기회 |
|---|---|---|---|---|---|

단계는 최소 5개로 구성해줘.
예: 수업 시작 전, 강의계획서 확인, 과제 발견, 일정 정리, 마감 전 준비, 완료 후 회고
```

### 5.2 결과 저장

결과를 `docs/journey.md`에 저장한다.

### 5.3 좋은 Journey Map 조건

- 감정이 들어가야 한다.
- Pain Point가 구체적이어야 한다.
- 서비스가 개입할 수 있는 순간이 보여야 한다.
- “사용자가 버튼을 누른다”보다 “사용자가 왜 그 행동을 하는가”가 드러나야 한다.

---

## 6. Step 4. PRD 작성하기

### 6.1 프롬프트

```text
다음 문제정의, 페르소나, User Journey Map을 바탕으로 PRD.md 초안을 작성해줘.

문제정의:
[docs/problem.md 내용 붙여넣기]

페르소나:
[docs/persona.md 내용 붙여넣기]

User Journey Map:
[docs/journey.md 내용 붙여넣기]

PRD는 다음 구조를 따른다.

# AI Syllabus Planner PRD

## 1. 문제 정의
## 2. 목표 사용자
## 3. 핵심 가치 제안
## 4. 핵심 사용자 시나리오
## 5. MVP 기능 범위
## 6. 제외할 기능
## 7. 주요 데이터
## 8. KPI
## 9. 리스크
## 10. 향후 확장 방향
```

### 6.2 결과 저장

결과를 `docs/PRD.md`에 저장한다.

### 6.3 PRD 수동 보정

AI 결과를 그대로 믿지 말고 다음 항목을 직접 고친다.

- MVP 기능은 3개 이하로 줄인다.
- “AI가 완벽히 분석한다” 같은 문장은 제거한다.
- “사용자가 직접 수정할 수 있다” 같은 안전장치를 추가한다.
- KPI는 계산 가능한 숫자로 바꾼다.

예시 KPI:

```markdown
## KPI
1. 일정 추출 성공률: 업로드한 강의 안내 텍스트 중 일정 항목이 1개 이상 추출된 비율
2. 일정 확정률: AI가 추출한 일정 중 사용자가 수정 없이 저장한 비율
3. 과제 완료율: 생성된 과제 중 완료 처리된 과제의 비율
```

---

## 7. Step 5. Acceptance Criteria 작성하기

AI가 만든 기능 설명은 대개 모호하다.  
“사용자가 쉽게 일정을 관리한다”는 테스트할 수 없다.  
“과제명이 비어 있으면 저장 버튼이 비활성화된다”는 테스트할 수 있다.

### 7.1 프롬프트

```text
다음 PRD를 바탕으로 Acceptance Criteria를 작성해줘.
각 기준은 Given-When-Then 형식으로 작성하고, 테스트 가능한 문장으로만 써줘.

PRD:
[docs/PRD.md 내용 붙여넣기]

출력 형식:
| ID | 기능 | Given | When | Then | 우선순위 |
|---|---|---|---|---|---|

조건:
- High 우선순위는 5개 이하로 제한
- 빈 상태, 오류 상태, 엣지 케이스를 반드시 포함
- 모호한 표현 금지
```

### 7.2 예시

```markdown
| ID | 기능 | Given | When | Then | 우선순위 |
|---|---|---|---|---|---|
| AC-01 | 일정 입력 | 사용자가 과제명을 입력했다 | 저장 버튼을 누른다 | 과제 목록에 새 과제가 추가된다 | High |
| AC-02 | 일정 입력 | 과제명이 비어 있다 | 저장 버튼을 본다 | 저장 버튼은 비활성화된다 | High |
| AC-03 | 일정 입력 | 과제명이 공백만 있다 | 저장 버튼을 본다 | 저장 버튼은 비활성화된다 | High |
| AC-04 | 일정 입력 | 과제명이 100자를 초과했다 | 입력창을 본다 | "과제명은 100자 이하여야 합니다" 메시지가 표시된다 | Medium |
| AC-05 | 목록 표시 | 등록된 과제가 없다 | 목록 화면을 본다 | "아직 등록된 일정이 없습니다" 메시지가 표시된다 | Medium |
```

### 7.3 결과 저장

결과를 `docs/acceptance_criteria.md`에 저장한다.

---

## 8. Step 6. 테스트 케이스 정의하기

테스트 케이스는 세 종류로 나눈다.

### 8.1 정상 케이스

사용자가 기대한 방식으로 서비스를 사용할 때의 테스트다.

예:

- 과제명을 입력하고 저장하면 목록에 추가된다.
- 체크박스를 누르면 완료 상태가 된다.
- 필터를 누르면 완료 과제만 보인다.

### 8.2 엣지 케이스

흔하지만 놓치기 쉬운 경계 상황이다.

예:

- 과제명이 빈 문자열이다.
- 과제명이 공백만 있다.
- 과제명이 1자다.
- 과제명이 100자다.
- 과제명이 101자다.
- 마감일이 오늘이다.
- 마감일이 어제다.
- 같은 과제명을 두 번 입력한다.

### 8.3 실패 케이스

시스템이 실패하거나 잘못된 입력을 받았을 때의 동작이다.

예:

- 네트워크 오류가 발생한다.
- 저장소가 비어 있다.
- 잘못된 날짜 형식이 들어온다.
- API 응답이 늦게 온다.

### 8.4 프롬프트

```text
다음 Acceptance Criteria를 바탕으로 테스트 케이스를 만들어줘.
정상 케이스, 엣지 케이스, 실패 케이스로 나누고, Vitest와 Testing Library로 구현 가능한 수준으로 구체화해줘.

Acceptance Criteria:
[docs/acceptance_criteria.md 내용 붙여넣기]

출력 형식:
| Test ID | 유형 | 대상 기능 | 입력 | 사용자 행동 | 기대 결과 | 우선순위 |
|---|---|---|---|---|---|---|
```

### 8.5 결과 저장

결과를 `docs/test_cases.md`에 저장한다.

---

## 9. Step 7. 하네스 파일 작성하기

하네스는 AI 에이전트가 따라야 할 작업 규칙이다. Cursor, Claude Code, Copilot Chat 등 어떤 도구를 쓰더라도 이 파일을 먼저 읽게 만든다.

### 9.1 `AGENTS.md` 작성

`AGENTS.md`에 다음 내용을 붙여넣는다.

```md
# AGENTS.md

## Project Goal
이 프로젝트는 MIS 학부생이 AX/DX 서비스 프로토타입을 4주 안에 구현하기 위한 교육용 프로젝트다.
서비스는 AI Syllabus Planner이며, 강의계획서 또는 수업 안내 텍스트에서 과제/시험/발표 일정을 추출하고 사용자가 수정·저장할 수 있게 한다.

## Source of Truth
- 요구사항은 docs/PRD.md를 기준으로 한다.
- 테스트 가능한 기준은 docs/acceptance_criteria.md를 기준으로 한다.
- 구현 우선순위는 docs/test_cases.md의 High 항목을 따른다.

## Rules
- 기능을 구현하기 전에 반드시 테스트를 먼저 작성한다.
- 테스트 파일은 src/**/*.test.ts 또는 src/**/*.test.tsx 형식을 따른다.
- 하나의 요청에서 너무 많은 파일을 수정하지 않는다.
- UI 변경 시 접근성, 빈 상태, 오류 상태를 함께 고려한다.
- 테스트가 실패하면 구현보다 실패 원인을 먼저 설명한다.
- 테스트 코드를 통과시키기 위해 요구사항을 임의로 삭제하지 않는다.

## Tech Stack
- React
- TypeScript
- Tailwind CSS
- Vitest
- Testing Library

## Definition of Done
- 관련 테스트가 통과한다.
- 엣지 케이스가 최소 2개 이상 포함된다.
- 사용자가 볼 수 있는 오류 메시지가 있다.
- PRD의 Acceptance Criteria와 연결된다.
- README에 실행 방법이 있다.
```

---

## 10. Step 8. README 초안 작성

`README.md`에 다음 내용을 붙여넣는다.

```md
# AI Syllabus Planner

## 서비스 개요
강의계획서 또는 수업 안내 텍스트에서 과제, 시험, 발표 일정을 추출하고 사용자가 수정·저장할 수 있도록 돕는 AX/DX 서비스 프로토타입입니다.

## 핵심 기능
- 일정 직접 입력
- 일정 목록 확인
- 과제 완료 처리
- KPI 계산을 위한 이벤트 설계

## 주요 문서
- docs/problem.md
- docs/persona.md
- docs/journey.md
- docs/PRD.md
- docs/acceptance_criteria.md
- docs/test_cases.md
```

---

## 11. 이번 주 제출물

- GitHub 저장소 링크 또는 압축 파일
- `docs/problem.md`
- `docs/persona.md`
- `docs/journey.md`
- `docs/PRD.md`
- `docs/acceptance_criteria.md`
- `docs/test_cases.md`
- `AGENTS.md`
- `README.md`

---

## 12. 평가 기준

| 항목 | 배점 |
|---|---:|
| 문제정의가 구체적인가 | 20 |
| Persona와 Journey Map이 문제정의와 연결되는가 | 20 |
| PRD가 MVP 범위를 잘 제한하는가 | 20 |
| Acceptance Criteria가 테스트 가능한가 | 20 |
| 테스트 케이스에 정상/엣지/실패 케이스가 포함되었는가 | 20 |

---

## 13. 자가 점검

제출 전 다음을 확인한다.

```text
[ ] docs/problem.md가 있다
[ ] docs/persona.md가 있다
[ ] docs/journey.md가 있다
[ ] docs/PRD.md가 있다
[ ] docs/acceptance_criteria.md가 있다
[ ] docs/test_cases.md가 있다
[ ] AGENTS.md가 있다
[ ] README.md가 있다
[ ] High 우선순위 기능이 5개 이하이다
[ ] 테스트 가능한 문장이 아닌 표현을 제거했다
```
