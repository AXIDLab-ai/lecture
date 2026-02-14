# Week 13: UI/UX Design & Implementation

[← 이전: Week 12](./week12.md) | [목차](./README.md) | [다음: Week 14 →](./week14.md)

---

## 📌 학습 목표

- UI/UX 디자인 목표 설정 및 디자인 원칙 적용
- 와이어프레임 주요 화면 상세 설계
- UI 컴포넌트 명세 작성 (Variants, States, Accessibility)
- 디자인 토큰 시스템 구축 및 관리
- WCAG 2.1 접근성 기준 준수
- 반응형 디자인 전략 수립
- UX 패턴 및 인터랙션 설계
- 내비게이션 아키텍처 구축
- 에러 핸들링 및 피드백 시스템 설계

---

## 📚 주요 내용

### 1. UI/UX 디자인 목표 및 원칙

#### 1.1 디자인 목표

**사용자 중심 목표**:
- **효율성**: 최소 클릭으로 목표 달성
- **명확성**: 직관적인 정보 구조
- **일관성**: 동일한 패턴 반복
- **접근성**: 모든 사용자 포용
- **즐거움**: 긍정적 감정 유발

**비즈니스 목표**:
- 전환율 향상 (CVR)
- 이탈률 감소 (Bounce Rate)
- 재방문율 증가
- 브랜드 인지도 강화

#### 1.2 주요 디자인 원칙

**Fitts's Law**:
- 타겟이 크고 가까울수록 빠르게 클릭 가능
- 적용: 중요한 버튼은 크게, 자주 사용하는 기능은 가까이

**Hick's Law**:
- 선택지가 많을수록 결정 시간 증가
- 적용: 옵션 단순화, 그룹화

**Miller's Law**:
- 단기 기억은 7±2개 항목까지 처리
- 적용: 메뉴 항목 5-9개 유지

---

### 2. 와이어프레임 주요 화면 상세

#### 2.1 Home 화면

**구성 요소**:
```
+--------------------------------------------------+
| Header                                            |
| [로고]  [검색바]         [장바구니] [로그인]      |
+--------------------------------------------------+
| Navigation Bar                                   |
| [카테고리1] [카테고리2] [카테고리3] [세일]        |
+--------------------------------------------------+
| Hero Banner                                      |
| [이미지] "신상품 출시"                            |
| [CTA: 지금 쇼핑하기]                              |
+--------------------------------------------------+
| Featured Products                                |
| [상품1] [상품2] [상품3] [상품4]                   |
+--------------------------------------------------+
| Promotion Section                                |
| "특별 할인 이벤트" [배너]                         |
+--------------------------------------------------+
| Footer                                           |
| 회사소개 | 이용약관 | 개인정보처리방침 | 고객센터  |
| SNS 아이콘                                        |
+--------------------------------------------------+
```

**인터랙션**:
- Hero Banner: 자동 슬라이드 (5초), 수동 제어 버튼
- Featured Products: Hover 시 상품 정보 미리보기
- Scroll: Infinite scroll 또는 Pagination

#### 2.2 Search Results (검색 결과)

**구성 요소**:
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
| 가격                    | [상품7] [상품8] [상품9]  |
| [슬라이더] 0 - 100,000원 |                         |
|                         | [더 보기 버튼]           |
| 브랜드                  |                         |
| [ ] 브랜드A             |                         |
| [ ] 브랜드B             |                         |
+--------------------------------------------------+
```

**인터랙션**:
- Filter 선택 시 즉시 결과 업데이트 (Ajax)
- Sort 변경 시 애니메이션 전환
- "더 보기" 또는 Infinite Scroll

#### 2.3 Product Detail (상품 상세)

**구성 요소**:
```
+--------------------------------------------------+
| Breadcrumb: Home > 하의 > 청바지 > [상품명]       |
+--------------------------------------------------+
| Image Gallery (Left)    | Product Info (Right)    |
|                         |                         |
| [메인 이미지]            | 브랜드: ABC             |
|                         | 상품명: 데님 슬림핏 청바지 |
| [썸네일1][썸네일2]       | 가격: ₩79,000           |
| [썸네일3][썸네일4]       | 할인: 20% (₩63,200)     |
|                         | 평점: ★★★★☆ (4.2/5.0)  |
|                         |                         |
|                         | 옵션 선택:              |
|                         | 사이즈: [28][30][32]    |
|                         | 색상: [Blue][Black]     |
|                         |                         |
|                         | [장바구니 담기] [바로 구매] |
+--------------------------------------------------+
| Tabs: [상세정보] [리뷰] [Q&A] [배송/반품]         |
|                                                  |
| [선택된 탭의 콘텐츠 영역]                         |
+--------------------------------------------------+
| Related Products: "이 상품과 함께 본 상품"        |
| [상품1] [상품2] [상품3] [상품4]                   |
+--------------------------------------------------+
```

**인터랙션**:
- Image Gallery: 클릭 시 확대, 좌우 슬라이드
- 옵션 선택: 필수 선택 전 CTA 버튼 비활성화
- Tab 전환: Smooth scroll

#### 2.4 Cart (장바구니)

**구성 요소**:
```
+--------------------------------------------------+
| 장바구니 (3개 상품)                               |
+--------------------------------------------------+
| [체크박스] [이미지] [상품명] [옵션] [수량] [가격] [삭제] |
| [x]       [img]   데님 청바지  Blue/30  [2]  ₩126,400  [X] |
| [x]       [img]   화이트 티셔츠  M      [1]  ₩29,000   [X] |
| [ ]       [img]   스니커즈     280     [1]  ₩89,000   [X] |
+--------------------------------------------------+
| 쿠폰/포인트 사용                                  |
| 쿠폰: [쿠폰 선택 ▼]  포인트: [       ] P 사용     |
+--------------------------------------------------+
| 주문 금액                                         |
| 상품 금액:         ₩244,400                       |
| 배송비:            ₩3,000                         |
| 할인:              -₩10,000                       |
| 최종 결제 금액:    ₩237,400                       |
|                                                  |
| [선택 상품 삭제] [계속 쇼핑하기] [주문하기]        |
+--------------------------------------------------+
```

**인터랙션**:
- 체크박스: 전체 선택/개별 선택
- 수량 변경: +/- 버튼, 실시간 금액 업데이트
- 삭제: Confirm 모달 표시

#### 2.5 Checkout (결제)

**구성 요소**:
```
+--------------------------------------------------+
| Step Indicator: [1.장바구니] → [2.주문/결제] → [3.완료] |
+--------------------------------------------------+
| 배송지 정보                                       |
| 받는 사람: [홍길동]                               |
| 연락처: [010-1234-5678]                           |
| 주소: [서울시 강남구...]                          |
| 배송 요청사항: [부재 시 경비실에 맡겨주세요]       |
+--------------------------------------------------+
| 주문 상품 (2개)                                   |
| [상품1] 데님 청바지 x2 - ₩126,400                 |
| [상품2] 화이트 티셔츠 x1 - ₩29,000                |
+--------------------------------------------------+
| 결제 수단                                         |
| ( ) 신용카드  ( ) 계좌이체  (x) 카카오페이        |
+--------------------------------------------------+
| 최종 결제 금액: ₩158,400                          |
|                                                  |
| [x] 개인정보 처리 방침에 동의합니다.              |
| [x] 구매 조건 확인 및 결제 진행에 동의합니다.      |
|                                                  |
| [결제하기]                                        |
+--------------------------------------------------+
```

#### 2.6 Settings (설정)

**구성 요소**:
```
+--------------------------------------------------+
| 설정                                              |
+--------------------------------------------------+
| [프로필 사진]  홍길동                             |
| user@example.com                                 |
+--------------------------------------------------+
| 계정 설정                                         |
| > 개인정보 수정                                   |
| > 비밀번호 변경                                   |
| > 알림 설정                                       |
| > 배송지 관리                                     |
+--------------------------------------------------+
| 앱 설정                                           |
| > 언어: 한국어                                    |
| > 테마: 라이트 모드                               |
+--------------------------------------------------+
| 기타                                              |
| > 이용약관                                        |
| > 개인정보처리방침                                |
| > 고객센터                                        |
| > 로그아웃                                        |
| > 회원탈퇴                                        |
+--------------------------------------------------+
```

---

### 3. UI 컴포넌트 명세

#### 3.1 Button 컴포넌트

**Variants**:
- Primary: 주요 행동 (예: 구매하기)
- Secondary: 보조 행동 (예: 취소)
- Outlined: 테두리만 있는 버튼
- Text: 텍스트만 있는 버튼
- Icon Button: 아이콘만

**Sizes**:
- Small: 32px height, 12px padding
- Medium: 40px height, 16px padding
- Large: 48px height, 20px padding

**States**:
- Default
- Hover: 배경색 변경, Cursor: pointer
- Active/Pressed: 약간 어두운 색
- Disabled: 불투명도 50%, Cursor: not-allowed
- Loading: 스피너 아이콘 표시

**Accessibility**:
- aria-label 또는 텍스트 필수
- Focus 시 outline 표시
- 키보드 Enter/Space로 클릭 가능

#### 3.2 Input Field 컴포넌트

**Types**:
- Text, Email, Password, Number, Tel, Date

**Elements**:
- Label: 필수, 위치 (top/left)
- Input: placeholder, value
- Helper Text: 설명 또는 예시
- Error Message: 유효성 검증 실패 시 표시
- Icon: 왼쪽/오른쪽 아이콘 (예: 검색 아이콘)

**States**:
- Default
- Focus: border 색상 변경, label 강조
- Error: 빨간색 border, 에러 메시지 표시
- Disabled: 배경 회색, 입력 불가

**Validation**:
- 실시간 또는 onBlur 시점 검증
- 에러 메시지: 구체적이고 해결 방법 제시

#### 3.3 Card 컴포넌트

**구조**:
- Image (optional)
- Title
- Description
- Footer (optional): CTA 버튼, 메타 정보

**Variants**:
- Elevated: 그림자 있음
- Outlined: 테두리 있음
- Flat: 그림자 및 테두리 없음

**Interactive States**:
- Hover: 약간 상승 효과 (transform: translateY(-4px))
- Clickable: Cursor: pointer

---

### 4. 디자인 토큰 시스템

#### 4.1 Color Tokens

**Brand Colors**:
```css
--color-primary: #0066CC;
--color-primary-hover: #0052A3;
--color-primary-active: #003D7A;
--color-primary-disabled: #99CCFF;
```

**Semantic Colors**:
```css
--color-success: #28A745;
--color-warning: #FFC107;
--color-error: #DC3545;
--color-info: #17A2B8;
```

**Neutral Colors**:
```css
--color-text-primary: #1A1A1A;
--color-text-secondary: #4D4D4D;
--color-text-disabled: #B3B3B3;
--color-background: #FFFFFF;
--color-surface: #F5F5F5;
--color-border: #E6E6E6;
```

#### 4.2 Spacing Tokens (8px Grid System)

```css
--spacing-xs: 4px;   /* 0.25rem */
--spacing-sm: 8px;   /* 0.5rem */
--spacing-md: 16px;  /* 1rem */
--spacing-lg: 24px;  /* 1.5rem */
--spacing-xl: 32px;  /* 2rem */
--spacing-2xl: 48px; /* 3rem */
--spacing-3xl: 64px; /* 4rem */
```

#### 4.3 Typography Tokens

```css
--font-family-primary: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-family-mono: 'Fira Code', monospace;

--font-size-xs: 12px;   /* 0.75rem */
--font-size-sm: 14px;   /* 0.875rem */
--font-size-base: 16px; /* 1rem */
--font-size-lg: 18px;   /* 1.125rem */
--font-size-xl: 20px;   /* 1.25rem */
--font-size-2xl: 24px;  /* 1.5rem */
--font-size-3xl: 30px;  /* 1.875rem */
--font-size-4xl: 36px;  /* 2.25rem */

--font-weight-regular: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;

--line-height-tight: 1.25;
--line-height-normal: 1.5;
--line-height-relaxed: 1.75;
```

#### 4.4 Shadow Tokens

```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
```

---

### 5. 접근성 (WCAG 2.1)

#### 5.1 4대 원칙 (POUR)

**Perceivable (인식 가능)**:
- 시각적 정보를 대체 수단으로 제공
- 색상만으로 정보 전달 금지
- 충분한 명암비 제공

**Operable (조작 가능)**:
- 키보드로 모든 기능 접근 가능
- 충분한 시간 제공
- 발작 유발 콘텐츠 지양

**Understandable (이해 가능)**:
- 명확한 언어 사용
- 예측 가능한 기능
- 입력 도움 및 오류 식별

**Robust (견고성)**:
- 다양한 보조 기술과 호환
- 시맨틱 마크업 사용

#### 5.2 주요 체크리스트

**시각적 접근성**:
- [ ] Alt text for images
- [ ] 색상만으로 정보 전달 금지 (색맹 고려)
- [ ] 명암비 최소 4.5:1 (일반 텍스트), 3:1 (대형 텍스트)
- [ ] 자동 재생 동영상 음소거 또는 정지 가능

**키보드 접근성**:
- [ ] 키보드만으로 모든 기능 접근 가능
- [ ] Focus 순서 논리적
- [ ] Skip to main content 링크 제공
- [ ] Focus indicator 명확히 표시

**콘텐츠 접근성**:
- [ ] 명확한 언어 및 간결한 문장
- [ ] 오류 메시지 구체적이고 해결 방법 제시
- [ ] Form label 명확하게 연결

**기술적 접근성**:
- [ ] 시맨틱 HTML 사용 (header, nav, main, footer)
- [ ] ARIA 속성 적절히 사용

#### 5.3 키보드 내비게이션

**주요 키**:
- Tab: 다음 요소로 이동
- Shift + Tab: 이전 요소로 이동
- Enter: 버튼 클릭, 링크 이동
- Esc: 모달 닫기, 메뉴 닫기
- Arrow Keys: 메뉴 내 이동

**Tab Order**:
- 논리적 순서 (위→아래, 좌→우)
- Skip to Main Content 링크 제공
- Focus 시 명확한 outline 표시

#### 5.4 스크린 리더 지원

**Semantic HTML**:
```html
<header>
  <nav aria-label="Main Navigation">
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>Title</h1>
    <p>Content</p>
  </article>
</main>

<footer>
  <p>&copy; 2026 Company</p>
</footer>
```

**ARIA Attributes**:
- `aria-label`: 요소 설명
- `aria-labelledby`: 다른 요소의 ID 참조
- `aria-describedby`: 추가 설명
- `aria-hidden="true"`: 스크린 리더에서 숨김
- `role="button"`: 역할 명시

#### 5.5 명암비 (Contrast Ratio)

**WCAG AA 기준**:
- 일반 텍스트: 4.5:1 이상
- 대형 텍스트 (18px+ 또는 14px+ bold): 3:1 이상
- UI 컴포넌트: 3:1 이상

**테스트 도구**:
- WebAIM Contrast Checker
- Chrome DevTools Lighthouse
- Colour Contrast Analyser (CCA)

---

### 6. 반응형 디자인

#### 6.1 Breakpoints 전략

**Mobile First Approach**:
```css
/* Mobile (기본) */
.container {
  padding: 16px;
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

#### 6.2 Mobile vs Desktop 차이점

| 요소 | Mobile | Desktop |
|------|--------|---------|
| Navigation | Hamburger Menu | Full Menu Bar |
| Layout | 1 Column | 2-3 Columns |
| Image Size | Smaller | Larger |
| Touch Target | 최소 44x44px | 마우스 클릭 |
| Interaction | Swipe, Tap | Click, Hover |
| Font Size | 16px+ (iOS 줌 방지) | 14px+ |

#### 6.3 Responsive Images

**Picture Element**:
```html
<picture>
  <source media="(min-width: 1024px)" srcset="https://example.com/image-desktop.jpg">
  <source media="(min-width: 768px)" srcset="https://example.com/image-tablet.jpg">
  <img src="https://example.com/image-mobile.jpg" alt="Description">
</picture>
```

#### 6.4 Flexible Layout

**CSS Grid**:
```css
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}
```

**Flexbox**:
```css
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

### 7. UX 패턴

#### 7.1 Pull-to-Refresh (모바일)

**동작**:
- 화면 최상단에서 아래로 당김
- 로딩 인디케이터 표시
- 데이터 갱신 완료 후 원위치

**구현 고려사항**:
- 당김 거리: 최소 60px
- 저항감: elastic 효과
- 피드백: 진동 또는 사운드 (optional)

#### 7.2 Swipe-to-Delete

**동작**:
- 리스트 아이템을 좌측으로 스와이프
- 삭제 버튼 노출
- 확인 모달 또는 Undo 옵션 제공

**구현**:
```css
.list-item {
  transform: translateX(0);
  transition: transform 0.3s ease;
}

.list-item.swiped {
  transform: translateX(-80px);
}
```

#### 7.3 Touch Target Rules

**최소 크기**: 
- iOS: 44x44px
- Android: 48x48dp
- Web: 44x44px

**간격**: 최소 8px 여백

**예시**:
```css
.touch-target {
  min-height: 44px;
  min-width: 44px;
  margin: 4px; /* 8px 간격 확보 */
}
```

---

### 8. 내비게이션 아키텍처

#### 8.1 Global Navigation

**위치**: Header (고정)

**항목**:
- Logo (홈으로 이동)
- 주요 카테고리 (3-5개)
- 검색
- 장바구니
- 로그인/프로필

**모바일 처리**:
```
Desktop: [로고] [메뉴1] [메뉴2] [메뉴3] [검색] [장바구니] [로그인]
Mobile:  [☰] [로고]                     [검색] [장바구니]
```

#### 8.2 Local Navigation

**위치**: 특정 섹션 내

**예시**:
- 상품 상세 페이지의 Tabs (상세정보, 리뷰, Q&A)
- 설정 페이지의 메뉴 목록

#### 8.3 3-Click Rule

**원칙**: 사용자가 목표까지 최대 3번 클릭 이내 도달

**예외**: 복잡한 구조에서는 명확한 경로가 더 중요

**Breadcrumb 활용**:
```
Home > 카테고리 > 서브카테고리 > 상품
```

**예시**:
```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/category/fashion">패션</a></li>
    <li><a href="/category/fashion/pants">바지</a></li>
    <li aria-current="page">청바지</li>
  </ol>
</nav>
```

---

### 9. Empty State & Error Handling

#### 9.1 Empty State

**상황**: 데이터가 없을 때
- 장바구니 비어있음
- 검색 결과 없음
- 알림 없음

**디자인**:
- 아이콘 또는 일러스트
- 명확한 메시지
- CTA 버튼

**예시**:
```html
<div class="empty-state">
  <svg class="empty-icon">...</svg>
  <h3>장바구니가 비어 있습니다</h3>
  <p>마음에 드는 상품을 담아보세요!</p>
  <button class="btn-primary">쇼핑 계속하기</button>
</div>
```

#### 9.2 Error Handling

**유형**:
- 네트워크 오류: "인터넷 연결을 확인해주세요."
- 서버 오류: "일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
- 권한 오류: "로그인이 필요합니다."
- 입력 오류: "이메일 형식이 올바르지 않습니다."

**디자인**:
- 에러 아이콘 (⚠️, ❌)
- 구체적인 메시지
- 해결 방법 또는 재시도 버튼

---

### 10. 피드백 시스템

#### 10.1 Inline Feedback

**Form Validation**:
- 실시간 또는 onBlur 검증
- 에러 메시지: 빨간색, 아이콘 포함
- 성공 메시지: 초록색, 체크 아이콘

**예시**:
```html
<div class="input-group">
  <label for="email">이메일</label>
  <input type="email" id="email" class="error">
  <span class="error-message">
    <svg class="error-icon">⚠️</svg>
    올바른 이메일 형식을 입력해주세요.
  </span>
</div>
```

#### 10.2 Toast Notification

**특징**:
- 화면 하단 또는 상단에 짧게 표시
- 자동 사라짐 (3-5초)
- 액션 버튼 포함 가능 (예: Undo)
- 화면 위에 떠있음 (Overlay)

**예시**:
```html
<div class="toast success">
  <svg class="toast-icon">✓</svg>
  <span>장바구니에 상품이 추가되었습니다.</span>
  <button class="toast-action">보기</button>
  <button class="toast-close">×</button>
</div>
```

**CSS**:
```css
.toast {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  box-shadow: var(--shadow-lg);
  border-radius: 8px;
  padding: 16px;
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { transform: translate(-50%, 100%); }
  to { transform: translate(-50%, 0); }
}
```

#### 10.3 Modal Dialog

**용도**:
- 중요한 확인 (예: 삭제 확인)
- 추가 정보 입력 (예: 배송지 추가)
- 에러 알림 (치명적 오류)

**구조**:
```html
<div class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h2>배송지 추가</h2>
      <button class="modal-close">×</button>
    </div>
    <div class="modal-content">
      <!-- 폼 또는 내용 -->
    </div>
    <div class="modal-actions">
      <button class="btn-secondary">취소</button>
      <button class="btn-primary">저장</button>
    </div>
  </div>
</div>
```

**접근성**:
- 모달 열림 시 focus를 모달 내부로 이동
- Esc 키로 닫기 가능
- 배경 클릭 시 닫기 (optional)
- aria-modal="true", role="dialog"

---

### 11. 마스터 템플릿 & 사용자 플로우

#### 11.1 마스터 템플릿

**공통 레이아웃 요소**:
- Header: 모든 페이지 공통
- Footer: 모든 페이지 공통
- Container: 최대 너비 제한, 중앙 정렬

**페이지별 템플릿**:
- Landing Page: Hero + Features + CTA
- List Page: Filter + Grid + Pagination
- Detail Page: Image Gallery + Info + Tabs
- Form Page: Progressive Form + Validation

#### 11.2 사용자 플로우 다이어그램

**예시: 상품 구매 플로우**
```
[홈 화면]
   ↓ (검색 또는 카테고리)
[검색 결과 / 목록]
   ↓ (상품 클릭)
[상품 상세]
   ↓ (장바구니 담기)
[장바구니]
   ↓ (주문하기)
[결제]
   ↓ (결제 완료)
[주문 완료]
```

**조건 분기 예시**:
```
[상품 상세]
   ↓
[로그인 여부 확인]
   ↓ (Yes)      ↓ (No)
[장바구니 담기] → [로그인 페이지]
                    ↓
                [로그인 후 원래 페이지 복귀]
```

---

### 12. 인터랙션 패턴

#### 12.1 Loading States

**Skeleton UI**:
- 콘텐츠 로딩 중 구조만 표시
- 실제 레이아웃과 유사한 형태

```css
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

**Spinner**:
```html
<div class="loading-spinner" aria-label="로딩 중"></div>
```

#### 12.2 Hover Effects

**Card Hover**:
```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
```

**Button Hover**:
```css
.btn-primary {
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: var(--color-primary-hover);
}
```

#### 12.3 Focus States

```css
.focusable:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* 마우스 클릭 시에는 outline 숨김 */
.focusable:focus:not(:focus-visible) {
  outline: none;
}
```

---

### 13. 성능 최적화

#### 13.1 이미지 최적화

**Lazy Loading**:
```html
<img src="https://example.com/image.jpg" alt="상품 이미지" loading="lazy">
```

**WebP 포맷 사용**:
```html
<picture>
  <source srcset="https://example.com/image.webp" type="image/webp">
  <img src="https://example.com/image.jpg" alt="상품 이미지">
</picture>
```

#### 13.2 CSS 최적화

**Critical CSS**:
- Above-the-fold 콘텐츠에 필요한 CSS만 인라인
- 나머지는 비동기 로딩

**CSS 압축**:
- Minification
- 사용하지 않는 CSS 제거 (PurgeCSS)

#### 13.3 JavaScript 최적화

**Code Splitting**:
```javascript
// 동적 import로 필요할 때만 로딩
const Modal = lazy(() => import('./components/Modal'));
```

**Bundle 분석**:
- webpack-bundle-analyzer 사용
- 큰 라이브러리 대안 고려

---

## 🛠️ 실습 과제

### 과제 1: 와이어프레임 블루프린트 작성
- 핵심 화면 7개 Hi-Fi 와이어프레임 작성 (Figma)
- Home, Search, Detail, Cart, Checkout, Settings, Profile

### 과제 2: UI 컴포넌트 라이브러리 구축
- Button, Input, Card 등 주요 컴포넌트 Variants/States 정의
- Figma Component 또는 Storybook 활용

### 과제 3: 디자인 토큰 시스템 정의
- Color, Spacing, Typography, Shadow 토큰 문서화
- CSS 변수 또는 JSON 형태로 정의

### 과제 4: 사용자 플로우 다이어그램
- 핵심 시나리오 2개 플로우 다이어그램 작성
- 조건 분기 포함 (로그인 여부, 권한 등)

### 과제 5: 접근성 체크리스트 적용
- WCAG 2.1 기준으로 와이어프레임 검토
- 개선 사항 문서화

---

## 📖 참고 자료

- **도서**:
  - "Designing Interfaces" - Jenifer Tidwell
  - "Refactoring UI" - Adam Wathan & Steve Schoger
  - "Don't Make Me Think" - Steve Krug
- **온라인 리소스**:
  - Material Design - design.google
  - Human Interface Guidelines - Apple
  - Inclusive Components - inclusive-components.design
  - A11y Project - a11yproject.com
- **도구**:
  - Figma: 와이어프레임, 프로토타입
  - Storybook: 컴포넌트 문서화
  - axe DevTools: 접근성 테스트
  - Contrast Checker: 명암비 측정

---

## 🔄 복습 체크리스트

- [ ] UI/UX 디자인 목표 및 원칙 (Fitts's, Hick's, Miller's Law) 이해
- [ ] 와이어프레임 Fidelity 단계별 작성 능력
- [ ] UI 컴포넌트 명세 (Variants, States, Accessibility) 작성
- [ ] 디자인 토큰 시스템 구축 및 CSS 변수 적용
- [ ] WCAG 2.1 접근성 체크리스트 적용 능력
- [ ] 반응형 디자인 Breakpoints 전략 수립
- [ ] UX 패턴 (Pull-to-Refresh, Swipe-to-Delete) 구현
- [ ] 내비게이션 아키텍처 (Global/Local, 3-Click Rule) 설계
- [ ] Empty State & Error Handling 디자인
- [ ] 피드백 시스템 (Inline, Toast, Modal) 구축

---

## 📝 다음 주 예습

**Week 14: Prototyping**
- 프로토타입 전략 (Lo-Fi/Mid-Fi/Hi-Fi)
- 도구 선택 매트릭스
- 우선순위 결정 (MoSCoW, RICE, Kano)
- 개발 프로세스 플로우
- 리소스 배분 및 스프린트 로드맵
- 사용자 테스트 시나리오
- AI 도구 활용 프로토타이핑

---

[← 이전: Week 12](./week12.md) | [목차](./README.md) | [다음: Week 14 →](./week14.md)

**Last Updated**: 2026-02-14