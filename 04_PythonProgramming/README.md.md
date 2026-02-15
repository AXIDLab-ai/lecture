# 📘 파이썬 프로그래밍 (Python Programming)

![Institution](https://img.shields.io/badge/TUKorea-한국공학대학교-blue)
![Department](https://img.shields.io/badge/Department-IT경영전공-green)
![Course Type](https://img.shields.io/badge/Type-교양필수-red)
![Target](https://img.shields.io/badge/Target-1학년-orange)

**한국공학대학교 IT경영전공 파이썬 프로그래밍 실습 강의 아카이브입니다.**
본 레포지토리는 강의 자료 배포 및 수강생들의 프로젝트 결과물 관리를 위해 운영됩니다.

---

## 📅 강의 개요 (Course Overview)

파이썬 프로그래밍의 기초부터 실전 프로젝트까지 체계적으로 학습하는 실습 중심 강의입니다.

* **강의명:** 파이썬 프로그래밍 (Python Programming)
* **수강 대상:** IT경영전공 2학년 (전공선택)
* **교수자:** [강송희] (dellabee@tukorea.ac.kr)
* **강의실/시간:** [강의실 호수] / [요일 및 시간]

### 🎯 학습 목표
1. 파이썬 기본 문법과 자료구조 완전 마스터
2. GUI 프로그래밍과 데이터베이스 연동 실습
3. 객체지향 프로그래밍을 통한 실전 시스템 개발
4. 데이터 분석 및 시각화 프로젝트 완성
5. 취업 포트폴리오로 활용 가능한 종합 프로젝트 제작

---

## 📂 저장소 구조 (Repository Structure)

```text
root/
├── 00_Syllabus/          # 강의 계획서 및 일정
├── 01_Lecture_Notes/     # 주차별 강의 자료 (PDF/PPT)
├── 02_Student_Projects/  # 학생 팀 프로젝트 결과물 (Final)
├── 03_Weekly_Assignments/ # 주차별 과제 제출 폴더
└── 04_Final_Projects/    # 최종 프로젝트
```
---
## 🛠️ 사용 도구 (Tools & Tech Stack)
본 수업에서 사용하는 주요 도구 및 언어입니다.

**IDE/Editor**: IDLE, VS Code, PyCharm Community

**라이브러리**:
```
기본 내장: turtle, tkinter, sqlite3, random, math
고급: pandas, matplotlib, opencv-python (Week 14)
```

**데이터베이스**: SQLite (파일 기반)

**버전관리**: Git & GitHub

## 📢 과제 및 프로젝트 제출 가이드 (Submission Guide)
학생들은 아래 절차(GitHub Flow)에 따라 과제를 제출해야 합니다.

**Fork**: 이 레포지토리를 자신의 계정으로 Fork 합니다.

**Clone**: Fork 한 레포지토리를 로컬(내 컴퓨터)로 Clone 합니다.

```bash
git clone https://github.com/[본인ID]/PythonProgramming.git
```

**Branch**: 작업을 위한 브랜치를 생성합니다. (규칙: week01-name)

**Commit & Push**: 과제를 수행 후 커밋하고 본인 원격 저장소로 푸시합니다.

**제출 경로**: 03_Weekly_Assignments/Week_XX/[학번_이름]/ 폴더 생성 후 업로드

**Pull Request (PR)**: 원본 레포지토리(Main)로 PR을 보냅니다.

**PR 제목**: [Week 0X] 학번 이름 과제 제출

## 🚫 주의사항 (Notice)
**저작권 준수**: 강의 자료를 외부 커뮤니티나 불특정 다수에게 무단 배포하는 것을 금지합니다.

**표절 금지**: 과제 및 프로젝트 소스코드 표절 시 0점 처리됩니다. (코드 유사도 검사 진행 예정)

**파일명 규칙**: 모든 제출 파일은 영문 작성을 권장하며, 공백 대신 언더바(_)를 사용하세요.

**제출 기한**: 매주 **일요일 23:59**까지

## 📬 Contact
수업 관련 질문은 Issues 탭을 이용하거나 이메일(dellabee@tukorea.ac.kr)로 문의 바랍니다.

---

## 📅 주차별 강의 계획 (14주)

| 주차 | | 주제 | | 주요 내용 | | 산출물 | |
|------|------|-----------|--------|
| 1 | 파이썬 들여다보기 | 설치, IDLE, 첫 프로그램 | Hello World |
| 2 | 쓸만한 프로그램 | input/print, 계산기 | 환율/BMI 계산기 |
| 3 | 변수와 데이터형 | int/float/str/bool | 개인정보 관리 |
| 4 | 연산자 | 산술/비교/논리 연산자 | 과학 계산기 |
| 5 | 조건문 | if/elif/else | 메뉴 시스템 |
| 6 | 반복문 | for/while/break/continue | 패턴 출력 |
| 7 | 리스트와 튜플 | 리스트 메서드, 2차원 리스트 | 화면 보호기 |
| 8 | 딕셔너리와 집합 | 딕셔너리 메서드, 집합 연산 | 텍스트 분석 |
| 9 | 함수와 모듈 | 함수 정의, 모듈 import | 사용자 모듈 |
| 10 | tkinter GUI | 위젯, 레이아웃, 이벤트 | GUI 계산기 |
| 11 | 파일 입출력 | 텍스트/CSV/JSON 처리 | 메모장 프로그램 |
| 12 | 객체지향 프로그래밍 | 클래스, 상속, 다형성 | 학생 관리 시스템 |
| 13 | 데이터베이스 | SQLite, SQL 문법 | 주소록/재고관리 |
| 14 | 미니 프로젝트 | 종합 프로젝트 | 개인 프로젝트 완성 |

## 🎯 최종 프로젝트 가이드

**Week 14**에서 다음 중 하나를 선택하여 완성합니다:

1. **개인 일정 관리 프로그램** (GUI + JSON)
2. **학생 성적 관리 시스템** (OOP + SQLite)
3. **간단한 게임** (GUI + 로직)
4. **텍스트 분석 도구** (파일 + 자료구조)
5. **자유 프로젝트** (교수 승인 필요)

**평가 기준**:
- 기능 완성도 (50%)
- 코드 품질 및 주석 (20%)
- 사용자 인터페이스 (20%)
- 창의성 및 응용력 (10%)

**제출물**:
- 완성된 프로그램 파일
- 실행 결과 스크린샷
- 코드 설명 문서 (README.md)
- GitHub Repository 링크