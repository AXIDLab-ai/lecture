# Week 04. 디버깅, 리팩토링, 배포, 실험 설계까지 마무리하기

## 0. 이번 주 목표

이번 주는 프로토타입을 배포하고, 실험 가능한 서비스로 정리한다.  
좋은 시연은 화면이 예쁜 것이 아니라, “무엇을 검증하려고 만들었는가”가 분명한 것이다.

이번 주가 끝나면 다음 산출물을 만든다.

```text
배포 URL
테스트 통과 결과
docs/
  debug_log.md
  regression_tests.md
  experiment_plan.md
  final_presentation_outline.md
README.md
```

---

## 1. 사전 준비

프로젝트 폴더에서 시작한다.

```bash
cd axdx-prototype
```

현재 상태 확인:

```bash
git status
npm test
npm run build
```

---

## 2. Step 1. 전체 테스트 실행하기

배포 전에는 반드시 테스트를 먼저 실행한다.

```bash
npm test
```

빌드도 확인한다.

```bash
npm run build
```

### 체크포인트

- 테스트가 모두 통과하는가?
- TypeScript 오류가 없는가?
- 빌드가 성공하는가?
- 브라우저 콘솔 오류가 없는가?
- 빈 상태와 오류 상태가 보이는가?

---

## 3. Step 2. 실패 테스트를 AI와 함께 디버깅하기

테스트가 실패하면 바로 코드를 고치지 않는다.  
먼저 실패 원인을 정리한다.

### 3.1 디버깅 프롬프트

```text
다음 테스트 실패 로그를 분석해줘.
바로 코드를 고치지 말고 먼저 원인을 3가지 후보로 나눠 설명해줘.
그 다음 가장 가능성 높은 원인부터 수정안을 제시해줘.

테스트 실패 로그:
[로그 붙여넣기]

관련 테스트 코드:
[테스트 코드 붙여넣기]

관련 구현 코드:
[구현 코드 붙여넣기]
```

### 3.2 `docs/debug_log.md` 작성

```bash
touch docs/debug_log.md
```

양식:

```md
# Debug Log

## 문제 1
- 발생한 오류:
- 관련 테스트:
- 원인 후보:
  1.
  2.
  3.
- 최종 원인:
- 수정 내용:
- 다시 실행한 테스트:
- 배운 점:
```

---

## 4. Step 3. 리팩토링 전 회귀 테스트 고정하기

리팩토링은 기능 추가가 아니다.  
먼저 기존 동작을 보호하는 테스트를 고정한다.

### 4.1 회귀 테스트 제안 프롬프트

```text
다음 코드에서 리팩토링 전에 반드시 보호해야 할 회귀 테스트를 제안해줘.
정상 케이스, 엣지 케이스, 실패 케이스를 포함해줘.

코드:
[리팩토링할 코드 붙여넣기]

출력 형식:
| Test ID | 유형 | 보호할 동작 | 입력 | 기대 결과 |
|---|---|---|---|---|
```

### 4.2 `docs/regression_tests.md` 작성

```bash
touch docs/regression_tests.md
```

예시:

```markdown
# Regression Tests

| Test ID | 유형 | 보호할 동작 | 입력 | 기대 결과 |
|---|---|---|---|---|
| RT-01 | 정상 | 과제 저장 | "MIS 과제" | 목록에 추가됨 |
| RT-02 | 엣지 | 공백 입력 차단 | "   " | 저장 버튼 비활성화 |
| RT-03 | 실패 | 없는 과제 완료 처리 | missing-id | 에러 반환 |
```

### 4.3 리팩토링 규칙

- 테스트를 먼저 통과시킨다.
- 한 번에 하나의 관심사만 고친다.
- 함수 이름을 더 명확히 바꾼다.
- 중복을 줄인다.
- UI와 비즈니스 로직을 분리한다.
- 테스트를 통과시키기 위해 요구사항을 삭제하지 않는다.

---

## 5. Step 4. README 완성하기

`README.md`를 다음 구조로 정리한다.

```md
# AI Syllabus Planner

## 서비스 개요
이 서비스는 강의계획서 또는 수업 안내 텍스트에서 과제, 시험, 발표 일정을 추출하고 사용자가 수정·저장할 수 있도록 돕는 AX/DX 서비스 프로토타입입니다.

## 문제 상황
학생은 여러 강의의 과제, 시험, 발표 일정을 직접 정리해야 하며 마감이 겹칠 경우 우선순위를 판단하기 어렵습니다.

## 목표 사용자
- 여러 강의를 동시에 수강하는 대학생
- 과제와 시험 일정을 자주 놓치는 학생
- 캘린더 정리에 부담을 느끼는 학생

## 핵심 기능
- 과제명 직접 입력
- 일정 목록 표시
- 완료 상태 관리
- KPI 계산을 위한 데이터 구조 설계

## 실행 방법

```bash
npm install
npm run dev
```

## 테스트 실행

```bash
npm test
```

## 빌드

```bash
npm run build
```

## 배포 URL
[여기에 Vercel URL 입력]

## 주요 문서
- docs/PRD.md
- docs/acceptance_criteria.md
- docs/test_cases.md
- docs/screen_spec.md
- docs/event_taxonomy.md
- docs/kpi.md
- docs/experiment_plan.md
```

---

## 6. Step 5. GitHub 업로드하기

### 6.1 최초 업로드

GitHub에서 새 저장소를 만든다.  
저장소 이름 예시:

```text
axdx-syllabus-planner
```

터미널에서 실행한다.

```bash
git init
git add .
git commit -m "Initial AXDX prototype"
git branch -M main
git remote add origin [GitHub 저장소 URL]
git push -u origin main
```

예시:

```bash
git remote add origin https://github.com/your-id/axdx-syllabus-planner.git
```

### 6.2 이미 git 저장소인 경우

```bash
git add .
git commit -m "Complete week04 deployment preparation"
git push
```

---

## 7. Step 6. Vercel 배포하기

### 7.1 Vercel에서 설정

1. Vercel 접속
2. New Project 선택
3. GitHub 저장소 연결
4. Framework Preset이 `Vite`인지 확인
5. Build Command가 `npm run build`인지 확인
6. Output Directory가 `dist`인지 확인
7. Deploy 클릭

### 7.2 배포 후 확인

배포 URL에 접속한 뒤 다음을 확인한다.

```text
[ ] URL 접속이 된다
[ ] 과제 입력이 된다
[ ] 저장 버튼이 조건에 따라 활성화/비활성화된다
[ ] 과제 목록이 보인다
[ ] 빈 상태가 보인다
[ ] 모바일 화면에서 크게 깨지지 않는다
[ ] 브라우저 콘솔에 심각한 오류가 없다
```

---

## 8. Step 7. 통합 테스트 관점으로 수동 점검하기

자동 E2E 도구까지 도입하지 않아도, 이번 수업에서는 다음 시나리오를 수동으로 점검하고 기록한다.

### 8.1 수동 통합 테스트 시나리오

`docs/debug_log.md` 또는 별도 캡처 자료에 기록한다.

```markdown
# Manual Integration Test

## Scenario 1. 과제 등록
- Given: 사용자가 메인 화면에 접속했다
- When: "MIS 과제"를 입력하고 저장을 누른다
- Then: 목록에 "MIS 과제"가 표시된다
- Result: Pass / Fail

## Scenario 2. 빈 입력 차단
- Given: 사용자가 메인 화면에 접속했다
- When: 과제명을 입력하지 않는다
- Then: 저장 버튼이 비활성화된다
- Result: Pass / Fail

## Scenario 3. 긴 입력 오류
- Given: 사용자가 메인 화면에 접속했다
- When: 101자 이상의 과제명을 입력한다
- Then: 오류 메시지가 표시된다
- Result: Pass / Fail
```

---

## 9. Step 8. 실험 설계 문서 작성하기

서비스 프로토타입은 끝이 아니라 실험의 시작이다.

### 9.1 좋은 실험과 나쁜 실험

나쁜 예:

```text
버튼 색을 파란색으로 바꾸면 좋아질 것이다.
```

좋은 예:

```text
과제 등록 화면에서 마감일 추천 문구를 보여주면 사용자의 마감일 입력률이 증가할 것이다.
```

### 9.2 실험 설계 프롬프트

```text
다음 서비스 프로토타입을 바탕으로 A/B 테스트 실험 설계서를 작성해줘.
단순 색상 변경이 아니라 사용자 행동을 검증할 수 있는 실험이어야 해.

서비스 설명:
[docs/PRD.md 요약 붙여넣기]

현재 구현된 기능:
- 과제명 입력
- 과제 목록 표시
- 완료 상태 설계
- KPI 계산 로직

KPI:
[docs/kpi.md 내용 붙여넣기]

출력 형식:
# experiment_plan.md
## 1. 실험 가설
## 2. 실험군과 대조군
## 3. 주요 지표
## 4. 보조 지표
## 5. 성공 기준
## 6. 예상 리스크
## 7. 데이터 수집 방식
## 8. 의사결정 기준
```

### 9.3 `docs/experiment_plan.md` 작성

```bash
touch docs/experiment_plan.md
```

예시:

```markdown
# Experiment Plan

## 1. 실험 가설
과제 등록 화면에서 "마감일을 함께 입력하면 우선순위 추천이 더 정확해집니다"라는 안내 문구를 보여주면 마감일 입력률이 증가할 것이다.

## 2. 실험군과 대조군
- Control: 과제명 입력창만 표시
- Variant: 과제명 입력창 아래에 마감일 입력 유도 문구 표시

## 3. 주요 지표
- Due Date Input Rate = 마감일이 있는 과제 수 / 전체 생성 과제 수

## 4. 보조 지표
- Task Completion Rate
- Task Creation Rate

## 5. 성공 기준
Variant의 Due Date Input Rate가 Control 대비 15% 이상 높다.

## 6. 예상 리스크
- 안내 문구가 화면을 복잡하게 만들 수 있다.
- 학생이 마감일을 모르는 상태에서는 입력률이 증가하지 않을 수 있다.

## 7. 데이터 수집 방식
task_created 이벤트에 due_date_present 속성을 추가한다.

## 8. 의사결정 기준
성공 기준을 만족하면 안내 문구를 기본 UI로 채택한다.
```

---

## 10. Step 9. 최종 발표 구성하기

`docs/final_presentation_outline.md`를 만든다.

```bash
touch docs/final_presentation_outline.md
```

아래 구조를 붙여넣는다.

```markdown
# Final Presentation Outline

## 1. 문제 상황
- 누가 어떤 상황에서 불편한가?

## 2. 목표 사용자
- Persona 요약

## 3. 기존 해결 방식의 한계
- 수동 캘린더 입력
- 카카오톡/공지사항 확인
- 과제 마감 누락

## 4. 서비스 제안
- AI Syllabus Planner

## 5. 핵심 기능 시연
- 과제 입력
- 목록 표시
- 완료 처리 또는 KPI 계산

## 6. 테스트 케이스와 엣지 케이스
- 빈 입력
- 공백 입력
- 100자 초과
- 없는 ID 처리

## 7. KPI와 이벤트 설계
- Task Completion Rate
- AI Accuracy
- Retention D+7

## 8. 배포 URL
- Vercel URL

## 9. 실험 설계
- 가설
- Control / Variant
- 성공 기준

## 10. 한계와 개선 방향
- PDF 파싱은 mock 처리
- 실제 캘린더 연동은 후속 과제
- 사용자 테스트 필요
```

---

## 11. Step 10. 최종 점검표

제출 전 아래 표를 `README.md` 또는 제출 문서에 포함한다.

```markdown
# Final Checklist

| 항목 | 완료 |
|---|---|
| PRD가 있다 |  |
| Acceptance Criteria가 있다 |  |
| 테스트 케이스 문서가 있다 |  |
| 컴포넌트 테스트가 있다 |  |
| 데이터 검증 테스트가 있다 |  |
| KPI 계산 테스트가 있다 |  |
| 배포 URL이 있다 |  |
| 실험 설계 문서가 있다 |  |
| README에 실행 방법이 있다 |  |
```

---

## 12. 이번 주 제출물

- GitHub 저장소 링크
- 배포 URL
- 테스트 실행 결과 캡처
- 빌드 성공 캡처
- `docs/debug_log.md`
- `docs/regression_tests.md`
- `docs/experiment_plan.md`
- `docs/final_presentation_outline.md`
- 최종 발표 자료

---

## 13. 평가 기준

| 항목 | 배점 |
|---|---:|
| 배포된 프로토타입이 실제로 작동하는가 | 25 |
| 테스트와 엣지 케이스가 충분한가 | 25 |
| KPI와 실험 설계가 설득력 있는가 | 25 |
| 발표가 문제-해결-검증 흐름을 갖추었는가 | 25 |

---

## 14. 자가 점검

```text
[ ] npm test가 통과한다
[ ] npm run build가 통과한다
[ ] GitHub에 최신 코드가 올라가 있다
[ ] Vercel URL이 접속된다
[ ] README에 실행 방법이 있다
[ ] 실험 설계가 단순 색상 변경에 그치지 않는다
[ ] 발표가 기능 나열이 아니라 문제-해결-검증 흐름이다
```
