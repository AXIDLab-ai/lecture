<div align="center">

# AXID Lab Lecture Archive  
### 강송희 교수 강의 아카이브

<img src="https://img.shields.io/badge/AXID-Lab-00897B?style=for-the-badge" />
<img src="https://img.shields.io/badge/Teaching-Repository-546E7A?style=for-the-badge" />
<img src="https://img.shields.io/badge/AI%20Inquiry-Resilience-00897B?style=for-the-badge" />

<br/>

**Data-driven Decisions · Field-driven Innovation · Industry-Academia Collaboration**  
**데이터 기반 의사결정 · 현장 중심 혁신 · 산학연 협력**

</div>

---

## 1. About This Repository · 저장소 소개

> **This repository is the official lecture archive of Prof. Songhee Kang and AXID Lab at Tech University of Korea.**  
> **본 저장소는 한국공학대학교 AXID Lab 강송희 교수의 공식 강의 아카이브입니다.**

It is designed for lecture material distribution, student project management, GitHub-based submissions, and practice-oriented education connected to real industrial problems.

본 저장소는 강의자료 배포, 수강생 프로젝트 관리, GitHub 기반 과제 제출, 그리고 실제 산업 문제와 연결된 실무 중심 교육을 위해 운영됩니다.

---

## 2. Teaching Philosophy · 교육 철학

<div align="center">

### AI-Inquiry Resilience  
### AI 시대의 질문 회복탄력성

</div>

In the age of generative AI, learning is not about obtaining a perfect answer with one click.  
It is about asking better questions, testing AI-generated outputs, and grounding decisions in real contexts that AI cannot simply infer.

생성형 AI 시대의 학습은 한 번의 클릭으로 완벽한 답을 얻는 일이 아닙니다.  
더 나은 질문을 만들고, AI가 만든 답을 비판적으로 검토하며, AI가 쉽게 추론할 수 없는 실제 맥락과 현장 데이터에 기반해 판단하는 과정입니다.

### Core Principles · 핵심 원칙

| Principle | English | 국문 |
|---|---|---|
| Problem Reframing | Critique why the AI-framed problem may be flawed | AI가 제시한 문제틀 자체를 비판한다 |
| Contextual Depth | Use local, field-based, and non-generic data | 현장 기반 맥락과 비일반 데이터를 활용한다 |
| Iterative Struggle | Value failed prompts, pivots, and reasoning traces | 실패한 프롬프트와 논리적 전환 과정을 평가한다 |
| Evidence-based Judgment | Link outputs to data, assumptions, and risks | 산출물을 데이터·가정·리스크와 연결한다 |

---

## 3. AXID Lab · 연구실 소개

**AXID Lab** studies how organizations make better decisions and create field-driven innovation through digital technologies, data, and AI.

**AXID Lab**은 디지털 기술, 데이터, AI를 활용해 조직이 더 나은 의사결정을 내리고 현장 중심 혁신을 만들어가는 방식을 연구합니다.

### Research Focus · 연구 초점

| Area | Description | 설명 |
|---|---|---|
| Data-driven Decisions | Evidence-based decision-making using data and AI | 데이터와 AI 기반의 증거 중심 의사결정 |
| Field-driven Innovation | Practical innovation grounded in real industrial contexts | 실제 산업 현장 문제에 기반한 실용 혁신 |
| AI Literacy & Governance | Responsible use, evaluation, and adoption of AI | 책임 있는 AI 이해·평가·도입 |
| Digital Transformation | Service, process, and organizational transformation | 서비스·프로세스·조직의 디지털 전환 |

---

## 4. Courses · 개설 강의

### Major Required · 전공 필수

| Course | Description | Tools |
|---|---|---|
| System Analysis and Design<br/>시스템분석설계 | SDLC, requirements analysis, UML modeling<br/>SDLC, 요구사항 분석, UML 모델링 | StarUML, PlantUML, GitHub |
| AX/DX Service Design & Prototype<br/>AX/DX 서비스 기획 | Service design, UX, prototyping, AI-assisted development<br/>서비스 디자인, UX, 프로토타이핑, AI 기반 개발 | Figma, LLM tools, GitHub |

### Major Elective · 전공 선택

| Course | Description | Tools |
|---|---|---|
| Management Information Systems<br/>경영정보시스템 | MIS theories and case development<br/>MIS 핵심 이론과 사례 개발 | Case templates |
| AI & Management<br/>인공지능 경영 | AI foundations, management applications, ethics<br/>AI 기초, 경영 적용, 윤리 | Scenario tools, AI tools |

### General Education · 교양

| Course | Description | Tools |
|---|---|---|
| Python Programming<br/>파이썬프로그래밍 | Basic programming and hands-on exercises<br/>프로그래밍 기초와 실습 | Python, notebooks, GitHub |

---

## 5. Repository Structure · 저장소 구조

```text
root/
├── 00_Professor_Info/
│   └── Profile, lab information, contact
├── 01_SystemAnalysisDesign/
│   ├── Syllabus/
│   ├── Lecture_Notes/
│   ├── Student_Projects/
│   └── Resources/
├── 02_AXDXServiceDesign_Prototype/
│   ├── Syllabus/
│   ├── Lecture_Notes/
│   ├── Student_Projects/
│   └── Design_Resources/
├── 03_ManagementInformationSystem/
├── 04_AI_Management/
├── 05_PythonProgramming/
├── 99_Shared_Resources/
│   ├── Templates/
│   ├── Guidelines/
│   └── Rubrics/
└── README.md
```

---

## 6. Submission Guide · 과제 제출 가이드

### GitHub Flow

```bash
# 1. Fork this repository
# 2. Clone your fork
git clone https://github.com/[your-id]/lecture.git

# 3. Create a working branch
git checkout -b coursename-weekXX-studentname

# 4. Add your work
git add .
git commit -m "[CourseName-WeekXX] studentname submission"

# 5. Push and open Pull Request
git push origin coursename-weekXX-studentname
```

### Submission Path · 제출 경로

```text
[CourseFolder]/Student_Projects/WeekXX/[StudentID_Name]/
```

### Pull Request Title · PR 제목

```text
[CourseName-WeekXX] 학번 이름 과제 제출
```

---

## 7. File Naming Rules · 파일명 규칙

| Rule | Example |
|---|---|
| Use English filenames when possible | `week01_prd.md` |
| Replace spaces with underscores | `service_design_v1.0.pdf` |
| Include version numbers when needed | `prototype_report_v1.1.pdf` |
| Keep names short but meaningful | `journey_map.md` |

---

## 8. Tools & Tech Stack · 주요 도구

| Category | Tools |
|---|---|
| Modeling & Design | StarUML, PlantUML, Figma, Miro, Draw.io |
| Collaboration | GitHub, Notion, Slack, Microsoft Teams |
| Programming | Python, R, SQL, JavaScript, Java, C |
| Data & Database | MySQL, PostgreSQL, MongoDB, Oracle, BigQuery |
| Cloud & AI | AWS, Google Cloud, Azure ML, OpenAI, Claude, Gemini |
| AI/ML | PyTorch, scikit-learn, Streamlit |
| Productivity | Obsidian, GitHub Projects |

---

## 9. Academic Integrity · 학습 윤리

> AI tools may assist your work, but they must not replace your thinking.  
> AI 도구는 학습을 도울 수 있지만, 사고를 대체해서는 안 됩니다.

### Required Practice · 필수 원칙

- Cite sources and references clearly.  
  출처와 참고자료를 명확히 밝힙니다.
- Record the reasoning process behind AI-assisted outputs.  
  AI 활용 산출물의 사고 과정을 기록합니다.
- Do not submit copied code, copied reports, or AI outputs without review.  
  검토 없는 복사 코드, 보고서, AI 산출물 제출을 금지합니다.
- Projects must be connected to real or plausible industrial problems.  
  모든 프로젝트는 실제 또는 현실성 있는 산업 문제와 연결되어야 합니다.

---

## 10. Contact · 연락처

| Item | Information |
|---|---|
| Professor | Prof. Dr. Songhee Kang |
| Lab | AXID Lab |
| Institution | Tech University of Korea |
| Department | IT Management |
| Email | `[dellabee]@tukorea.ac.kr` |

For course-related questions, please use the relevant course folder or GitHub Issues when available.

수업 관련 질문은 가능한 경우 해당 강의 폴더 또는 GitHub Issues를 활용해 주세요.

---

<div align="center">

### Build questions that AI cannot simply answer.  
### AI가 쉽게 답할 수 없는 질문을 만듭니다.

<img src="https://img.shields.io/badge/Updated-2026-546E7A?style=flat-square" />
<img src="https://img.shields.io/badge/Theme-Grayscale%20%2B%20Teal%20Green-00897B?style=flat-square" />

</div>
