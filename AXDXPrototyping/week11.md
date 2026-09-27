[← 이전: Week 4](./week4.md) | [목차](./lectureMap.md) | [다음: Week 12 →](./week12.md)

# Week 11: Conceptual Design
---

## 📌 학습 목표

- User Journey Map을 활용한 사용자 경험 시각화
- Persona 정의 및 공감 능력 배양
- 와이어프레임 설계 원칙 이해 및 적용
- 접근성 체크리스트 (WCAG 2.1) 이해
- 반응형 디자인 (Mobile/Tablet/Desktop) 전략 수립
- 컴포넌트 라이브러리 및 디자인 시스템 구축
- 스타일 토큰 (Color, Spacing, Typography) 정의

---

## 📚 주요 내용

### 1. User Journey Map (사용자 여정 맵)

#### 1.1 정의 및 목적

**정의**:
- 사용자가 서비스와 상호작용하는 전체 과정을 시간 순서대로 시각화한 도구

**목적**:
- 사용자 경험의 전체 흐름 파악
- Pain Point 및 Delight Moment 식별
- 개선 기회 발견

#### 1.2 구성 요소

**필수 요소**:
- **Persona**: 대상 사용자
- **Scenario**: 상황/맥락
- **Phases**: 단계 (인지 → 탐색 → 구매 → 사용 → 재구매)
- **Touchpoints**: 접점 (웹, 앱, 이메일, 고객센터 등)
- **Actions**: 사용자 행동
- **Thoughts**: 생각 및 감정
- **Pain Points**: 불편 사항
- **Opportunities**: 개선 기회

#### 1.3 작성 예시: 온라인 쇼핑몰

**Persona**: 직장인 김민지 (32세, 의류 쇼핑 선호)

| 단계 | Touchpoints | Actions | Thoughts | Emotions | Pain Points | Opportunities |
|------|-------------|---------|----------|----------|-------------|---------------|
| **인지** | SNS 광고 | 광고 클릭 | "신상품이 나왔네?" | 호기심 | 광고가 모호함 | 명확한 가치 전달 |
| **탐색** | 모바일 웹 | 상품 검색, 필터링 | "내 스타일이 있을까?" | 기대감 | 로딩이 느림, 필터 부족 | 검색 성능 개선, AI 추천 |
| **비교** | 상품 상세 페이지 | 리뷰 읽기, 비교 | "사이즈가 맞을까?" | 불안감 | 사이즈 정보 불충분 | 가상 피팅, 상세 사이즈표 |
| **구매** | 장바구니, 결제 | 쿠폰 적용, 결제 | "배송은 빨라야 할텐데" | 기대 + 조급함 | 결제 단계가 복잡함 | 원클릭 결제, 명확한 배송 안내 |
| **수령** | 배송 알림, 상품 개봉 | 택배 수령, 착용 | "맘에 들까?" | 설렘 + 불안 | 포장 상태 불량 | 프리미엄 포장, 언박싱 경험 |
| **사후** | 앱 푸시, 이메일 | 리뷰 작성, 재방문 | "다음에 또 살까?" | 만족 / 실망 | 리뷰 작성 동기 부족 | 리뷰 리워드, 개인화 추천 |

---

### 2. Persona (페르소나)

#### 2.1 정의 및 중요성

**정의**:
- 실제 사용자 데이터를 기반으로 만든 대표 사용자 프로필

**중요성**:
- 팀 전체가 동일한 사용자상을 공유
- 의사 결정 기준 제공
- 공감 능력 향상

#### 2.2 Persona 구성 요소

**기본 정보**:
- 이름, 나이, 직업, 거주지
- 사진 (실제 또는 스톡 이미지)

**인구통계 (Demographics)**:
- 소득 수준, 학력, 가족 구성

**심리통계 (Psychographics)**:
- 가치관, 라이프스타일, 취미
- 목표 및 동기

**행동 패턴 (Behaviors)**:
- 제품/서비스 사용 빈도
- 선호 채널 (모바일, 웹, 오프라인)
- 구매 의사결정 패턴

**Pain Points & Needs**:
- 불편 사항
- 해결하고 싶은 문제
- 기대하는 해결책

#### 2.3 Persona 작성 예시

---

**Persona 1: 효율형 프로젝트 매니저 "이지훈"**

**기본 정보**:
- 나이: 35세
- 직업: IT 스타트업 PM
- 거주지: 서울 강남
- 소득: 연 6,000만원

**특징**:
- "시간은 금이다. 모든 것은 자동화되어야 한다."
- 새로운 생산성 도구에 관심 많음
- 데이터 기반 의사결정 선호

**일상**:
- 하루 평균 20개 이상의 회의
- Slack, Jira, Notion 등 여러 도구 사용 중
- 모바일로 이동 중에도 업무 체크

**목표**:
- 프로젝트 진행 상황 실시간 파악
- 팀원 간 커뮤니케이션 효율화
- 보고서 작성 시간 절감

**Pain Points**:
- 도구가 너무 많아 정보가 분산됨
- 수동 데이터 정리에 시간 소모
- 팀원들의 도구 적응 속도 느림

**선호 기능**:
- 대시보드 한눈에 보기
- 자동 리포트 생성
- Slack/Teams 연동
- 모바일 앱 필수

---

#### 2.4 Multiple Personas

**Primary Persona**: 핵심 타겟 (가장 많은 비중)
**Secondary Persona**: 부차적 타겟
**Anti-Persona**: 서비스 대상이 아닌 사용자 (예: 무료만 사용하려는 사용자)

---

### 3. 와이어프레임 (Wireframe)

#### 3.1 정의 및 Fidelity Level

**정의**:
- 화면 레이아웃과 기능 배치를 단순하게 표현한 설계도

**Fidelity 수준**:
- **Lo-Fi**: 종이 스케치, 간단한 박스 (빠른 아이디어 검증)
- **Mid-Fi**: 상세한 레이아웃, 실제 콘텐츠 일부 포함 (기능 검토)
- **Hi-Fi**: 시각 디자인 거의 완성, 인터랙션 포함 (최종 검토)

#### 3.2 와이어프레임 설계 원칙

**Visual Hierarchy (시각적 위계)**:
- 중요한 요소를 크게, 상단 또는 중앙 배치
- F-pattern, Z-pattern 고려

**Consistency (일관성)**:
- 동일한 기능은 동일한 위치 및 스타일
- 네이밍 통일

**Clarity (명확성)**:
- 모호함 제거, 명확한 라벨 사용
- 사용자가 다음 행동을 예측 가능

#### 3.3 주요 화면 와이어프레임 예시

##### 3.3.1 Home 화면

**구성**:
- Header: 로고, 검색바, 로그인/회원가입
- Hero Section: 메인 배너, CTA 버튼
- Featured Products: 추천 상품 그리드
- Footer: 링크, 고객센터, SNS

**레이아웃**:
```
+--------------------------------------------+
| [로고]  [검색바]          [로그인][회원가입] |
+--------------------------------------------+
|                                            |
|        [메인 배너 이미지]                   |
|        "새로운 컬렉션"                      |
|        [지금 쇼핑하기 버튼]                 |
|                                            |
+--------------------------------------------+
| 추천 상품                                   |
| [상품1] [상품2] [상품3] [상품4]             |
+--------------------------------------------+
| Footer: 회사소개 | 이용약관 | 고객센터       |
+--------------------------------------------+
```

##### 3.3.2 Search Results (검색 결과)

**구성**:
- Breadcrumb: Home > 검색 결과
- Filter Panel: 카테고리, 가격, 브랜드
- Sort Dropdown: 인기순, 낮은 가격순, 최신순
- Product Grid: 상품 목록 (썸네일, 제목, 가격, 평점)
- Pagination: 페이지 네비게이션

**레이아웃**:
```
+--------------------------------------------------+
| Breadcrumb: Home > 검색 결과 "청바지"             |
+--------------------------------------------------+
| Filter Panel (Left)     | Product Grid (Right)   |
|                         |                         |
| 카테고리                | Sort: [인기순 ▼]         |
| [ ] 상의 (120)          |                         |
| [x] 하의 (85)           | [상품1] [상품2] [상품3]  |
|                         | [상품4] [상품5] [상품6]  |
| 가격                    |                         |
| [슬라이더] 0-100,000원   | [더 보기 버튼]           |
+--------------------------------------------------+
```

##### 3.3.3 Product Detail (상품 상세)

**구성**:
- Image Gallery: 메인 이미지 + 썸네일
- Product Info: 제목, 가격, 할인율, 평점
- Options: 사이즈, 색상 선택
- CTA: 장바구니 담기, 바로 구매
- Tabs: 상세 정보, 리뷰, Q&A, 배송/반품
- Related Products: 연관 상품

**레이아웃**:
```
+--------------------------------------------------+
| Image Gallery (Left)    | Product Info (Right)    |
|                         |                         |
| [메인 이미지]            | 브랜드: ABC             |
|                         | 상품명: 데님 슬림핏 청바지 |
| [썸네일1][썸네일2]       | 가격: ₩79,000           |
| [썸네일3][썸네일4]       | 할인: 20% (₩63,200)     |
|                         | 평점: ★★★★☆ (4.2)      |
|                         |                         |
|                         | [장바구니 담기] [바로 구매] |
+--------------------------------------------------+
| Tabs: [상세정보] [리뷰] [Q&A] [배송/반품]         |
+--------------------------------------------------+
```

##### 3.3.4 Cart (장바구니)

**구성**:
- 장바구니 아이템 목록 (이미지, 이름, 옵션, 수량, 가격)
- 수량 조절 버튼 (+/-)
- 삭제 버튼
- 총 금액 계산 (상품 금액 + 배송비)
- 쿠폰 입력란
- CTA: 계속 쇼핑하기, 주문하기

##### 3.3.5 Checkout (결제)

**구성**:
- Step Indicator: 1. 장바구니 → 2. 주문/결제 → 3. 완료
- 배송지 정보 입력
- 주문 상품 요약
- 결제 수단 선택 (카드, 계좌이체, 간편결제)
- 최종 금액 확인
- 개인정보 처리 동의 체크박스
- CTA: 결제하기

---

### 4. 접근성 체크리스트 (WCAG 2.1)

#### 4.1 WCAG 개요

**WCAG (Web Content Accessibility Guidelines)**:
- W3C의 웹 접근성 국제 표준
- Level A, AA, AAA (AA 준수 권장)

**4대 원칙 (POUR)**:
- **Perceivable** (인식 가능)
- **Operable** (조작 가능)
- **Understandable** (이해 가능)
- **Robust** (견고성)

#### 4.2 주요 체크리스트

**Perceivable (인식 가능)**:
- [ ] 텍스트 대체 (Alt text for images)
- [ ] 색상만으로 정보 전달 금지 (색맹 고려)
- [ ] 명암비 최소 4.5:1 (일반 텍스트), 3:1 (대형 텍스트)
- [ ] 자동 재생 동영상 음소거 또는 정지 가능

**Operable (조작 가능)**:
- [ ] 키보드만으로 모든 기능 접근 가능
- [ ] Focus 순서 논리적
- [ ] Skip to main content 링크 제공
- [ ] 제한 시간 충분 또는 연장 가능

**Understandable (이해 가능)**:
- [ ] 명확한 언어 및 간결한 문장
- [ ] 오류 메시지 구체적이고 해결 방법 제시
- [ ] Form label 명확하게 연결

**Robust (견고성)**:
- [ ] 시맨틱 HTML 사용 (header, nav, main, footer)
- [ ] ARIA 속성 적절히 사용

#### 4.3 도구 및 테스트

**자동 테스트 도구**:
- axe DevTools (Chrome Extension)
- Lighthouse (Chrome DevTools)
- WAVE (WebAIM)

**수동 테스트**:
- 스크린 리더 (NVDA, JAWS)
- 키보드 내비게이션 (Tab, Enter, Esc)
- 색상 명암비 측정 (Contrast Checker)

---

### 5. 반응형 디자인 (Responsive Design)

#### 5.1 Breakpoints (브레이크포인트)

**일반적인 Breakpoints**:
- **Mobile**: 0 ~ 767px (Small)
- **Tablet**: 768px ~ 1023px (Medium)
- **Desktop**: 1024px ~ 1439px (Large)
- **Desktop XL**: 1440px+ (Extra Large)

**설정 예시 (CSS)**:
```css
/* Mobile First */
.container {
  padding: 16px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

#### 5.2 반응형 레이아웃 전략

**Fluid Grid**:
- % 또는 fr 단위 사용
- 예: `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));`

**Flexible Images**:
- `max-width: 100%; height: auto;`

**Media Queries**:
- 화면 크기에 따라 스타일 변경

**Mobile-First Approach**:
- 모바일 기본 스타일 작성 → 큰 화면 추가

#### 5.3 반응형 패턴

**Column Drop**:
- Desktop: 3단 → Tablet: 2단 → Mobile: 1단

**Layout Shifter**:
- 화면 크기에 따라 레이아웃 재배치

**Tiny Tweaks**:
- 폰트 크기, 여백만 조정

---

### 6. 컴포넌트 라이브러리

#### 6.1 컴포넌트 분류 (Atomic Design)

**Atoms (원자)**:
- Button, Input, Label, Icon, Badge

**Molecules (분자)**:
- Input Field (Label + Input + Error Message)
- Card (Image + Title + Description + Button)

**Organisms (유기체)**:
- Header (Logo + Navigation + Search + User Menu)
- Product Grid (Multiple Cards + Pagination)

**Templates & Pages**:
- 실제 화면 조합

#### 6.2 컴포넌트 네이밍 규칙

**BEM (Block Element Modifier)**:
```html
<div class="card">
  <h3 class="card__title">Title</h3>
  <p class="card__description">Description</p>
  <button class="card__button card__button--primary">CTA</button>
</div>
```

#### 6.3 컴포넌트 문서화

**Storybook 활용**:
- 각 컴포넌트의 다양한 State 시각화
- Props, Variants 문서화
- 사용 예시 코드

---

### 7. 스타일 토큰 (Design Tokens)

#### 7.1 Color Palette

**Primary Colors**:
- Primary: `#0066CC` (브랜드 메인 컬러)
- Primary Hover: `#0052A3`
- Primary Disabled: `#99CCFF`

**Neutral Colors**:
- Black: `#000000`
- Gray 900: `#1A1A1A`
- Gray 700: `#4D4D4D`
- Gray 500: `#808080`
- Gray 300: `#B3B3B3`
- Gray 100: `#E6E6E6`
- White: `#FFFFFF`

**Semantic Colors**:
- Success: `#28A745`
- Warning: `#FFC107`
- Error: `#DC3545`
- Info: `#17A2B8`

#### 7.2 Spacing (여백)

**8px Grid System**:
- xs: 4px (0.25rem)
- sm: 8px (0.5rem)
- md: 16px (1rem)
- lg: 24px (1.5rem)
- xl: 32px (2rem)
- 2xl: 48px (3rem)
- 3xl: 64px (4rem)

#### 7.3 Typography

**Font Family**:
- Primary: 'Pretendard', -apple-system, sans-serif
- Monospace: 'Fira Code', monospace

**Font Sizes**:
- xs: 12px (0.75rem)
- sm: 14px (0.875rem)
- base: 16px (1rem)
- lg: 18px (1.125rem)
- xl: 20px (1.25rem)
- 2xl: 24px (1.5rem)
- 3xl: 30px (1.875rem)
- 4xl: 36px (2.25rem)

**Font Weights**:
- Regular: 400
- Medium: 500
- SemiBold: 600
- Bold: 700

**Line Heights**:
- Tight: 1.25
- Normal: 1.5
- Relaxed: 1.75

#### 7.4 Border Radius

- None: 0
- sm: 4px
- md: 8px
- lg: 12px
- full: 9999px (원형)

---

### 8. 프로토타입 링크 전략

#### 8.1 Figma Prototype 설정

**Interaction**:
- On Click → Navigate to
- On Hover → 오버레이 표시
- Scroll → 스크롤 영역 설정

**Transition**:
- Instant (즉시)
- Dissolve (페이드)
- Slide (슬라이드)
- Duration: 300ms (기본)

**Starting Frame**:
- 프로토타입 시작 화면 지정

#### 8.2 유저 테스트 시나리오

**태스크 예시**:
1. "홈페이지에서 '여성 의류' 카테고리로 이동하세요."
2. "검색 기능을 사용하여 '청바지'를 검색하세요."
3. "마음에 드는 상품을 장바구니에 담으세요."
4. "결제 과정을 완료하세요."

**관찰 포인트**:
- 완료 시간
- 클릭 실수 횟수
- 어려움을 느낀 지점
- 사용자 피드백

---

## 🛠️ 실습 과제

### 과제 1: User Journey Map 작성
- Primary Persona 기준으로 주요 사용자 여정 맵 작성 (최소 5단계)

### 과제 2: Persona 정의
- Primary Persona 1명 + Secondary Persona 1명 상세 작성

### 과제 3: 와이어프레임 설계
- 핵심 화면 5개 Mid-Fi 와이어프레임 작성 (Figma 또는 Sketch)

### 과제 4: 접근성 체크
- 작성한 와이어프레임에 대해 WCAG 체크리스트 적용 및 개선 사항 문서화

### 과제 5: 스타일 토큰 정의
- 프로젝트 Color Palette, Spacing, Typography 토큰 정의 문서

---

## 📖 참고 자료

- **도서**:
  - "Don't Make Me Think" - Steve Krug
  - "The Design of Everyday Things" - Don Norman
- **온라인 리소스**:
  - Nielsen Norman Group - UX Research
  - Smashing Magazine - Web Design
  - A11y Project - Accessibility Guide
- **도구**:
  - Figma / Sketch: 와이어프레임 & 프로토타입
  - Miro: User Journey Map
  - axe DevTools: 접근성 테스트

---

## 🔄 복습 체크리스트

- [ ] User Journey Map 구성 요소 이해 및 작성
- [ ] Persona 정의 및 활용 역량
- [ ] 와이어프레임 Fidelity 수준 이해
- [ ] 주요 화면 와이어프레임 설계 능력
- [ ] WCAG 2.1 접근성 체크리스트 적용
- [ ] 반응형 디자인 Breakpoints 설정
- [ ] 컴포넌트 라이브러리 구조화
- [ ] 디자인 토큰 시스템 정의

---

## 📝 다음 주 예습

**Week 12: Detailed Design**
- RESTful API 설계 원칙
- 엔드포인트 카탈로그 작성
- Request/Response 스키마
- Error Handling 전략
- Zero Trust 보안 모델
- OAuth 2.0/OIDC 인증

---

[← 이전: Week 4](./week04.md) | [목차](./README.md) | [다음: Week 12 →](./week12.md)

**Last Updated**: 2026-02-14
