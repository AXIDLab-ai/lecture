# Week 14: Prototyping

[← 이전: Week 13](./week13.md) | [목차](./README.md)

---

## 📌 학습 목표

- 프로토타입 전략 (Lo-Fi/Mid-Fi/Hi-Fi) 이해 및 선택
- 도구 선택 매트릭스 활용 능력 배양
- AI 도구 (Claude, Cursor, GitHub Copilot) 활용한 프로토타이핑
- 우선순위 결정 프레임워크 (MoSCoW, RICE, Kano) 습득
- 개발 프로세스 플로우 (Design-Dev-Test Loop) 이해
- 리소스 배분 및 대응 전략 수립
- 스프린트 로드맵 작성 및 관리
- 프로토타입 테스팅 시나리오 설계
- 최종 산출물 품질 기준 적용
- LLM을 활용한 효율적 프로토타이핑 기법 습득

---

## 📚 주요 내용

### 1. 프로토타입 전략

#### 1.1 Fidelity Level (충실도 수준)

**Lo-Fi (Low Fidelity)**:
- **특징**: 종이 스케치, 간단한 박스, 텍스트 플레이스홀더
- **목적**: 빠른 아이디어 검증, 레이아웃 구조 확인
- **소요 시간**: 1-3시간
- **도구**: 종이, 화이트보드, Balsamiq, Whimsical
- **장점**: 빠르고 저비용, 변경 용이, 팀 브레인스토밍 촉진
- **단점**: 시각적 완성도 낮음, 인터랙션 제한적

**Mid-Fi (Medium Fidelity)**:
- **특징**: 기본 스타일 적용, 실제 콘텐츠 일부 포함, 클릭 가능한 프로토타입
- **목적**: 기능 검토, 사용자 플로우 검증, 팀 리뷰
- **소요 시간**: 1-2일
- **도구**: Figma, Sketch, Adobe XD
- **장점**: 기능 중심 검토, 사용자 테스트 가능
- **단점**: 최종 디자인과 차이 있음

**Hi-Fi (High Fidelity)**:
- **특징**: 최종 디자인에 가까운 형태, 실제 데이터, 세밀한 인터랙션
- **목적**: 최종 검토, 사용자 테스트, 개발 가이드
- **소요 시간**: 3-7일
- **도구**: Figma (Advanced Prototyping), Framer, ProtoPie
- **장점**: 실제 제품에 가까움, 정확한 피드백 수집
- **단점**: 시간 소요, 변경 비용 높음

#### 1.2 프로토타입 유형

**Click-through Prototype**:
- 화면 간 내비게이션만 구현
- 데이터 입력 없음
- 빠른 플로우 검증
- **예시**: Figma Prototype, InVision

**Interactive Prototype**:
- 폼 입력, 드래그 앤 드롭, 애니메이션 포함
- 사용자 액션에 따른 반응 구현
- 사용자 테스트에 적합
- **예시**: Framer, ProtoPie, Principle

**Functional Prototype**:
- 실제 데이터 연동 (API)
- 백엔드 로직 일부 구현
- 기술적 검증 및 MVP 개발
- **예시**: React/Vue.js 코드, CodePen

#### 1.3 선택 기준

| 목적 | 추천 Fidelity | 소요 시간 | 적합한 단계 |
|------|---------------|-----------|-------------|
| 아이디어 검증 | Lo-Fi | 1-3시간 | 초기 기획 |
| 기능 검토 | Mid-Fi | 1-2일 | 상세 기획 |
| 사용자 테스트 | Hi-Fi | 3-7일 | 개발 직전 |
| 투자 피칭 | Hi-Fi | 5-10일 | 투자 유치 |

---

### 2. 도구 선택 매트릭스

#### 2.1 프로토타이핑 도구 비교

| 도구 | Fidelity | Learning Curve | 협업 | 가격 (월) | 추천 용도 |
|------|----------|----------------|------|-----------|-----------|
| **Figma** | Mid-Hi | 중간 | 우수 (실시간) | Free~$15 | 전반적 디자인 & 프로토타입 |
| **Framer** | Hi | 높음 (코딩) | 보통 | $5~$20 | 고급 인터랙션, 개발자 친화적 |
| **Adobe XD** | Mid-Hi | 중간 | 보통 | Free~$10 | Adobe 생태계 사용자 |
| **Sketch** | Mid-Hi | 중간 | 플러그인 필요 | $9 | macOS 사용자 |
| **Balsamiq** | Lo | 낮음 | 보통 | $9 | 빠른 Lo-Fi 와이어프레임 |
| **ProtoPie** | Hi | 높음 | 보통 | $25 | 복잡한 인터랙션 |
| **Axure RP** | Mid-Hi | 높음 | 보통 | $29 | 복잡한 조건 로직 |
| **InVision** | Mid | 낮음 | 우수 | Free~$15 | 간단한 Click-through |

#### 2.2 선택 기준

**팀 크기별**:
- 1-3명: Figma (무료 플랜)
- 4-10명: Figma Pro
- 10명+: Enterprise 플랜

**프로젝트 복잡도별**:
- 간단한 웹사이트: Figma
- 복잡한 앱: Framer, ProtoPie
- 데이터 중심: Axure RP

**개발 연동**:
- React/Vue: Framer (코드 내보내기)
- 일반: Figma (Zeplin 플러그인)

---

### 3. AI 도구 활용

#### 3.1 Claude 활용 예시

**1. User Story 생성**

**Prompt**:
```
"사용자가 상품을 검색하고 장바구니에 담는 기능의 User Story를 작성해줘.
Acceptance Criteria도 Given-When-Then 형식으로 포함해서."
```

**Output**:
```
User Story:
As a 쇼핑몰 사용자,
I want to 상품을 검색하고 장바구니에 담을 수 있어서,
So that 나중에 한꺼번에 결제할 수 있다.

Acceptance Criteria:
1. Given: 홈 화면에 있음
   When: 검색창에 "청바지" 입력 후 엔터
   Then: 검색 결과 페이지로 이동하고, 관련 상품 표시

2. Given: 검색 결과 페이지
   When: 상품 클릭
   Then: 상품 상세 페이지로 이동

3. Given: 상품 상세 페이지, 옵션 선택 완료
   When: "장바구니 담기" 버튼 클릭
   Then: 장바구니에 상품 추가, Toast 알림 표시
```

**2. API 명세 생성**

**Prompt**:
```
"쇼핑몰의 상품 목록 조회 API 명세서를 작성해줘.
Query 파라미터, Response 스키마, Error 코드까지 포함해서."
```

#### 3.2 Cursor 활용 예시

**1. 와이어프레임 → React 컴포넌트**

**Prompt** (Figma 이미지 첨부 후):
```
"이 와이어프레임을 React 컴포넌트로 변환해줘.
Tailwind CSS 사용하고, 반응형 디자인 적용."
```

**Output**:
```jsx
import React from 'react';

const ProductCard = ({ image, title, price, rating }) => {
  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-4 cursor-pointer">
      <img 
        src={image} 
        alt={title} 
        className="w-full h-48 object-cover rounded-md mb-4"
      />
      <h3 className="text-lg font-semibold mb-2 line-clamp-2">{title}</h3>
      <div className="flex items-center justify-between mb-4">
        <span className="text-xl font-bold text-blue-600">
          ₩{price.toLocaleString()}
        </span>
        <div className="flex items-center">
          <span className="text-yellow-500">★</span>
          <span className="ml-1 text-sm text-gray-600">{rating}</span>
        </div>
      </div>
      <button className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition-colors">
        장바구니 담기
      </button>
    </div>
  );
};

export default ProductCard;
```

**2. API 호출 함수 생성**

**코드 입력** (주석만):
```javascript
// Fetch product list from API with filters and pagination
```

**Cursor 제안**:
```javascript
// Fetch product list from API with filters and pagination
const fetchProducts = async (filters = {}, page = 1, limit = 20) => {
  try {
    const queryParams = new URLSearchParams({
      ...filters,
      page: page.toString(),
      limit: limit.toString(),
    });
    
    const response = await fetch(`/api/v1/items?${queryParams}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw error;
  }
};
```

#### 3.3 GitHub Copilot 활용

**상황**: 장바구니 상태 관리 (Redux)

**코드 입력**:
```javascript
// Redux slice for shopping cart
import { createSlice } from '@reduxjs/toolkit';
```

**Copilot 제안**:
```javascript
// Redux slice for shopping cart
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],
    total: 0,
    itemCount: 0,
  },
  reducers: {
    addItem: (state, action) => {
      const existingItem = state.items.find(item => item.id === action.payload.id);
      if (existingItem) {
        existingItem.quantity += 1;
      } else {
        state.items.push({ ...action.payload, quantity: 1 });
      }
      state.itemCount = state.items.reduce((sum, item) => sum + item.quantity, 0);
      state.total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    },
    removeItem: (state, action) => {
      state.items = state.items.filter(item => item.id !== action.payload);
      state.itemCount = state.items.reduce((sum, item) => sum + item.quantity, 0);
      state.total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    },
    updateQuantity: (state, action) => {
      const { id, quantity } = action.payload;
      const item = state.items.find(item => item.id === id);
      if (item) {
        item.quantity = Math.max(0, quantity);
        if (item.quantity === 0) {
          state.items = state.items.filter(i => i.id !== id);
        }
      }
      state.itemCount = state.items.reduce((sum, item) => sum + item.quantity, 0);
      state.total = state.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    },
    clearCart: (state) => {
      state.items = [];
      state.total = 0;
      state.itemCount = 0;
    },
  },
});

export const { addItem, removeItem, updateQuantity, clearCart } = cartSlice.actions;
export default cartSlice.reducer;
```

---

### 4. 우선순위 결정 프레임워크

#### 4.1 MoSCoW Method

**분류**:
- **Must-have (필수)**: 없으면 출시 불가
- **Should-have (중요)**: 있어야 하지만 우회 가능
- **Could-have (선택)**: 있으면 좋지만 없어도 됨
- **Won't-have (제외)**: 이번 버전에서는 제외

**쇼핑몰 프로토타입 예시**:

**Must-have**:
- [ ] 상품 목록 조회
- [ ] 상품 상세 보기
- [ ] 장바구니 담기
- [ ] 주문/결제 기본 플로우
- [ ] 회원가입/로그인

**Should-have**:
- [ ] 검색 기능
- [ ] 필터링 (가격, 카테고리)
- [ ] 리뷰 조회
- [ ] 주문 내역 확인

**Could-have**:
- [ ] 리뷰 작성
- [ ] 위시리스트
- [ ] 쿠폰 적용
- [ ] 추천 알고리즘

**Won't-have** (v2로 연기):
- [ ] 실시간 채팅 상담
- [ ] AR 가상 피팅
- [ ] 소셜 공유
- [ ] 다국어 지원

#### 4.2 RICE Scoring

**공식**: 
```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**요소 정의**:
- **Reach**: 영향받는 사용자 수 (월 기준)
- **Impact**: 영향 크기 (0.25=최소, 0.5=낮음, 1=보통, 2=높음, 3=최대)
- **Confidence**: 확신도 (50%=낮음, 80%=보통, 100%=높음)
- **Effort**: 개발 시간 (Person-Months)

**예시 계산**:

| 기능 | Reach | Impact | Confidence | Effort | RICE Score |
|------|-------|--------|------------|--------|------------|
| 상품 검색 | 1,000 | 3 | 90% | 0.5 | 5,400 |
| 추천 알고리즘 | 800 | 2 | 60% | 2 | 480 |
| 리뷰 작성 | 500 | 1 | 100% | 0.5 | 1,000 |
| 소셜 로그인 | 1,000 | 1 | 90% | 1 | 900 |

**우선순위**: 상품 검색 (5,400) > 리뷰 작성 (1,000) > 소셜 로그인 (900) > 추천 알고리즘 (480)

#### 4.3 Kano Model

**분류**:

**Basic Needs (기본 기능)**:
- 없으면 불만, 있어도 만족 증가 없음
- 예시: 로그인, 상품 조회, 장바구니 기본 기능

**Performance Needs (성능 기능)**:
- 성능 향상에 따라 만족도 선형 증가
- 예시: 로딩 속도, 검색 정확도, 결제 간편성

**Excitement Needs (기쁨 기능)**:
- 없어도 문제없지만, 있으면 큰 만족 (경쟁 우위)
- 예시: AI 추천, AR 피팅, 음성 검색

**개발 전략**:
1. Basic → Performance → Excitement 순서
2. Basic 완성 후 Performance 개선으로 차별화
3. Excitement로 경쟁 우위 확보

---

### 5. 개발 프로세스 플로우

#### 5.1 Design-Dev-Test Loop

**1단계: Design (설계)**:
- [ ] 와이어프레임 작성
- [ ] UI 컴포넌트 정의
- [ ] 인터랙션 명세
- [ ] 디자인 토큰 적용
- **산출물**: Figma 파일, 디자인 스펙 문서

**2단계: Develop (개발)**:
- [ ] 프론트엔드: HTML/CSS/JavaScript (React, Vue 등)
- [ ] 백엔드: API 구현 (Node.js, Python Django 등)
- [ ] 데이터베이스: 스키마 설계 및 구축
- **산출물**: 실행 가능한 코드

**3단계: Test (테스트)**:
- [ ] Unit Test: 개별 컴포넌트/함수 검증
- [ ] Integration Test: 모듈 간 통합 검증
- [ ] E2E Test: 전체 사용자 플로우 검증
- [ ] User Test: 실제 사용자 피드백 수집
- **산출물**: 테스트 리포트, 버그 리스트

**4단계: Iterate (반복)**:
- [ ] 테스트 결과 기반 개선
- [ ] 우선순위 재조정
- [ ] 다음 기능으로 이동

#### 5.2 Acceptance Criteria

**Given-When-Then 형식**:

**예시 1: 장바구니 담기**:
```
Given: 사용자가 로그인된 상태
  And: 상품 상세 페이지에 있음
  And: 사이즈와 색상을 선택함
When: "장바구니 담기" 버튼 클릭
Then: 장바구니에 상품 추가됨
  And: 장바구니 아이콘에 수량 배지 표시
  And: Toast 알림 "장바구니에 추가되었습니다" 표시
  And: 페이지 이동 없이 같은 페이지 유지
```

**예시 2: 검색 기능**:
```
Given: 홈 화면 또는 임의의 페이지
When: 검색창에 "청바지" 입력 후 엔터 또는 검색 버튼 클릭
Then: 검색 결과 페이지로 이동
  And: 검색어와 관련된 상품 목록 표시
  And: 검색 결과 개수 표시 ("청바지 검색 결과 45개")
  And: 검색창에 입력한 검색어 유지

Given: 검색 결과가 없는 경우
When: 검색 수행
Then: "검색 결과가 없습니다" 메시지 표시
  And: 추천 키워드 또는 인기 상품 제안
```

#### 5.3 Testing Metrics

**성능 지표**:
- **Success Rate**: 목표 ≥ 85%
- **Time-to-First-Click**: 목표 ≤ 5초
- **Task Completion Time**: 각 태스크별 목표 시간 설정
- **Error Rate**: 목표 ≤ 10%
- **Drop-off Rate**: 목표 ≤ 20%

**만족도 지표**:
- **SUS (System Usability Scale)**: 목표 ≥ 70점
- **NPS (Net Promoter Score)**: 목표 ≥ 50점
- **주관적 만족도**: 5점 척도 기준 ≥ 4.0점

---

### 6. 리소스 배분

#### 6.1 Role-based Allocation

| 역할 | 책임 | 비중 | 산출물 |
|------|------|------|--------|
| **PM/PO** | 기획, 요구사항 정의, 우선순위 결정 | 20% | PRD, User Story, 백로그 |
| **UI Designer** | 와이어프레임, 시각 디자인, 프로토타입 | 30% | Figma 파일, 디자인 시스템 |
| **Frontend Dev** | UI 구현, 인터랙션 개발, API 연동 | 35% | React/Vue 코드, 컴포넌트 |
| **Backend Dev** | API 개발, 데이터베이스 설계, 인증 | 10% | API 엔드포인트, DB 스키마 |
| **Data/AI** | 추천 알고리즘, 데이터 분석 | 5% | 추천 모델, 대시보드 |

#### 6.2 리소스 부족 대응 전략

**Frontend 리소스 부족 시**:
- **AI 도구 활용**: Cursor로 코드 자동 생성
- **UI 라이브러리**: Material-UI, Ant Design, Chakra UI
- **No-code**: Webflow, Framer
- **프리랜서**: Upwork, 프리랜서 플랫폼
- **오픈소스**: GitHub에서 유사 프로젝트 참고

**Designer 리소스 부족 시**:
- **디자인 시스템**: Material Design, Bootstrap
- **Figma Community**: 무료 템플릿 활용
- **AI 도구**: Midjourney로 이미지 생성
- **아웃소싱**: 99designs, Fiverr

**Backend 리소스 부족 시**:
- **BaaS (Backend as a Service)**: Firebase, Supabase, AWS Amplify
- **Mock API**: JSON Server, Mockoon, Mirage.js
- **서버리스**: AWS Lambda, Vercel Functions, Netlify Functions
- **오픈소스**: Strapi (CMS), Hasura (GraphQL)

#### 6.3 리스크 완화

**기술적 리스크**:
- Proof of Concept (POC) 먼저 진행
- 복잡한 기능은 단계적 개발
- 백업 플랜 준비 (Plan B)

**일정 리스크**:
- Buffer Time 20% 포함
- 주간 체크인 및 조기 경보
- Scope 조정 가능성 열어둠

---

### 7. 스프린트 로드맵 (4주 프로토타입 개발)

#### 7.1 Sprint 1 (Week 1): Foundation Setup

**목표**: 기반 구조 및 핵심 화면 구현

**Task List**:
- [ ] 프로젝트 설정 (Create React App, Vite, Next.js)
- [ ] CSS 프레임워크 설정 (Tailwind CSS, Styled Components)
- [ ] 디자인 토큰 적용 (색상, 타이포그래피, 스페이싱)
- [ ] Header/Footer 컴포넌트 구현
- [ ] Home 화면 레이아웃 구현 (정적)
- [ ] 라우팅 설정 (React Router, Vue Router)
- [ ] 기본 컴포넌트 (Button, Input) 구현

**Deliverables**:
- 기본 레이아웃 완성
- 5개 주요 화면 구조 (Layout만)
- 컴포넌트 라이브러리 기초
- Git Repository 설정

**Success Criteria**:
- 모든 화면 라우팅 동작
- 반응형 기본 레이아웃
- 디자인 토큰 적용 확인

#### 7.2 Sprint 2 (Week 2): Core Features

**목표**: 핵심 기능 구현

**Task List**:
- [ ] 상품 목록 조회 (Mock Data 또는 JSON Server)
- [ ] 상품 상세 페이지 구현 (이미지 갤러리, 옵션 선택)
- [ ] 장바구니 담기 기능 (Local Storage 또는 Context API)
- [ ] 장바구니 조회 및 수량 변경
- [ ] 검색 기능 (프론트엔드 필터링)
- [ ] 기본 에러 처리 (Network, 404)

**Deliverables**:
- 핵심 사용자 플로우 동작
- 기능 데모 가능 상태
- 기본적인 상태 관리

**Success Criteria**:
- 상품 검색 → 상세 보기 → 장바구니 담기 플로우 완성
- 데이터 표시 및 상태 관리 정상 동작
- 기본적인 사용자 인터랙션 구현

#### 7.3 Sprint 3 (Week 3): Integration & Polish

**목표**: 통합 및 디테일 개선

**Task List**:
- [ ] 실제 API 연동 (Mock API → Real API)
- [ ] 로그인/회원가입 UI 및 로직 구현
- [ ] 인증 토큰 관리 (JWT, Refresh)
- [ ] 결제 플로우 구현 (PG 연동 또는 Mock)
- [ ] 전체적인 에러 핸들링 및 로딩 상태
- [ ] 반응형 디자인 적용 (Mobile, Tablet, Desktop)
- [ ] 접근성 기본 요소 적용

**Deliverables**:
- 전체 플로우 통합 완료
- 인증 시스템 동작
- 반응형 동작 확인

**Success Criteria**:
- End-to-End 플로우 (회원가입 → 로그인 → 쇼핑 → 결제) 완성
- 모든 디바이스에서 기본 기능 동작
- API 에러 처리 정상 동작

#### 7.4 Sprint 4 (Week 4): Testing & Finalization

**목표**: 테스트 및 최종 마무리

**Task List**:
- [ ] 사용자 테스트 시나리오 작성 (3개 이상)
- [ ] 5명 이상 사용자 테스트 진행
- [ ] 피드백 반영 (Hot-fix)
- [ ] 접근성 체크 (WCAG 2.1, axe DevTools)
- [ ] 성능 최적화 (Lighthouse 점수 80+ 목표)
- [ ] 최종 배포 (Vercel, Netlify, AWS S3)
- [ ] 문서화 (README, API 문서)

**Deliverables**:
- 사용자 테스트 리포트
- 배포된 프로토타입 URL
- 최종 발표 자료 (PPT)
- 기술 문서

**Success Criteria**:
- 사용자 테스트 성공률 ≥ 85%
- Lighthouse 성능 점수 ≥ 80
- 접근성 체크 Pass 85% 이상
- 프로덕션 배포 완료

---

### 8. Storyboard & Interaction Flow

#### 8.1 Storyboard 작성

**목적**: 사용자 여정을 시각적으로 표현

**구성**:

**Scene 1**: 홈 화면 진입
- **User**: 20대 직장인 김민지
- **Context**: 퇴근 후 집에서 폰으로 쇼핑
- **Action**: 메인 배너 확인, "신상품 보기" 클릭

**Scene 2**: 상품 목록 탐색
- **User**: 스크롤하며 상품 탐색
- **Thought**: "예쁜 옷이 많네, 어떤 걸 골라야 할까?"
- **Action**: 필터 적용 (가격대), 마음에 드는 상품 클릭

**Scene 3**: 상품 상세 검토
- **User**: 이미지 확대, 리뷰 읽기
- **Thought**: "사이즈가 맞을까? 다른 사람들 후기는 어떨까?"
- **Action**: 사이즈 가이드 확인, 리뷰 탭 클릭, 옵션 선택 후 장바구니 담기

**Scene 4**: 장바구니 확인
- **User**: 담긴 상품 확인, 수량 조절 고민
- **Thought**: "총 금액이 예산 내인가? 배송비는 얼마지?"
- **Action**: 수량 조정, 쿠폰 적용, "주문하기" 클릭

**Scene 5**: 결제 진행
- **User**: 배송지 확인, 결제 수단 선택
- **Thought**: "배송은 언제 올까? 카드 정보 안전한가?"
- **Action**: 기본 배송지 선택, 카카오페이 선택, "결제하기" 클릭

**Scene 6**: 주문 완료
- **User**: 주문 완료 메시지 확인
- **Emotion**: 만족감, 기대감
- **Action**: 주문 내역 보기 또는 계속 쇼핑

#### 8.2 Interaction Map

**표기법**:
- **화면**: 사각형
- **액션**: 화살표 + 라벨 (클릭, 스와이프, 입력)
- **조건 분기**: 다이아몬드 (예: 로그인 여부)
- **시스템 처리**: 원형 (API 호출, 데이터 처리)

**복잡한 플로우 예시**:
```
[홈 화면]
   ↓ 검색
[검색 결과]
   ↓ 상품 선택
[상품 상세]
   ↓ 장바구니 담기
<로그인 여부?>
   ↓ No        ↓ Yes
[로그인 페이지] [장바구니]
   ↓             ↓
[인증 완료]      [주문하기]
   ↓             ↓
[원래 페이지] → [결제 페이지]
                ↓
             [주문 완료]
```

---

### 9. 최종 산출물 체크리스트

#### 9.1 필수 산출물 (Must-have)

- [ ] **프로토타입 링크**: 
  - Figma Prototype URL 또는 배포 URL
  - 모든 핵심 플로우 동작 가능
  
- [ ] **테스트 시나리오**: 
  - 최소 3개 주요 플로우
  - 각 시나리오별 예상 시간 및 성공 기준

- [ ] **테스트 리포트**: 
  - 최소 5명 사용자 테스트
  - 정량/정성 피드백 요약
  - 개선 사항 우선순위

- [ ] **기술 스택 문서**:
  - 사용한 도구/라이브러리 목록
  - 선택 이유 및 대안 고려사항

- [ ] **LLM 활용 데모**:
  - Claude/Cursor로 생성한 코드 예시
  - AI 도구 활용 과정 문서화

#### 9.2 선택 산출물 (Nice-to-have)

- [ ] **디자인 시스템 문서**: Storybook 또는 스타일 가이드
- [ ] **API 문서**: Swagger/OpenAPI 명세
- [ ] **사용자 매뉴얼**: 주요 기능 사용법
- [ ] **개발 환경 가이드**: 로컬 개발 환경 설정
- [ ] **배포 가이드**: CI/CD 파이프라인 설정

#### 9.3 품질 기준 (Quality Criteria)

**기능적 요구사항**:
- [ ] 핵심 기능 모두 동작 (Must-have 100% 구현)
- [ ] 에러 없는 사용자 플로우
- [ ] 데이터 입력/출력 정상 동작

**비기능적 요구사항**:
- [ ] **접근성**: WCAG 2.1 AA 준수 (최소 85% 항목)
- [ ] **반응형**: Mobile/Tablet/Desktop 모두 정상 동작
- [ ] **성능**: 
  - 페이지 로딩 < 3초 (Lighthouse)
  - First Contentful Paint < 1.5초
- [ ] **에러 핸들링**: 모든 오류 케이스 처리

**사용성 요구사항**:
- [ ] 사용자 테스트 성공률 ≥ 85%
- [ ] 평균 태스크 완료 시간 ≤ 목표 시간
- [ ] SUS 점수 ≥ 70점
- [ ] NPS (Net Promoter Score) ≥ 50점

---

### 10. 프로토타입 테스팅

#### 10.1 Usability Testing 시나리오

**태스크 1: 상품 검색 및 구매**

**목표**: 사용자가 "청바지"를 검색하여 구매 프로세스 완료

**단계**:
1. 홈 화면에서 검색창 찾기
2. "청바지" 검색어 입력
3. 검색 결과에서 원하는 상품 선택
4. 상세 페이지에서 사이즈/색상 선택
5. 장바구니에 담기
6. 장바구니에서 주문하기 클릭
7. 배송지 입력 및 결제 완료

**예상 시간**: 3-5분
**성공 기준**: 주문 완료 페이지 도달

**관찰 포인트**:
- 검색 기능을 쉽게 발견했는가?
- 검색 결과 필터링을 사용했는가?
- 상품 옵션 선택에서 어려움은 없었는가?
- 결제 플로우가 직관적이었는가?
- 어느 단계에서 가장 오래 머물렀는가?

**태스크 2: 위시리스트 및 장바구니 관리**

**목표**: 여러 상품을 비교하고 장바구니 수량 조절

**단계**:
1. 카테고리에서 여성 의류 선택
2. 마음에 드는 상품 3개를 위시리스트에 추가
3. 그 중 2개를 장바구니에 담기
4. 장바구니에서 수량을 각각 2개, 1개로 조정
5. 총 결제 금액 확인

**예상 시간**: 2-3분

**태스크 3: 고객 지원**

**목표**: 주문 관련 문의하기

**단계**:
1. 프로필 메뉴에서 주문 내역 확인
2. 특정 주문의 배송 상태 확인
3. 고객센터 또는 문의하기 기능 찾기
4. 질문 작성 및 전송

**예상 시간**: 2-3분

#### 10.2 Testing Metrics 측정

**정량적 (Quantitative) 지표**:

| 지표 | 측정 방법 | 목표 값 |
|------|-----------|---------|
| 완료 시간 | 스톱워치 측정 | 태스크 1: ≤ 5분 |
| 클릭 수 | 화면 녹화 분석 | 태스크 1: ≤ 15클릭 |
| 오류 횟수 | 잘못된 클릭 집계 | ≤ 2회/태스크 |
| 성공률 | 완료한 사용자 비율 | ≥ 85% |
| 페이지 이탈률 | 중간에 포기한 비율 | ≤ 20% |

**정성적 (Qualitative) 지표**:

| 지표 | 측정 방법 | 목표 |
|------|-----------|------|
| 주관적 만족도 | 5점 척도 설문 | ≥ 4.0점 |
| 사용 편의성 | SUS 설문 (10문항) | ≥ 70점 |
| 추천 의향 | NPS 설문 | ≥ 50점 |
| 인지된 난이도 | 5점 척도 | ≤ 2.0점 |

**데이터 수집 도구**:
- 화면 녹화: OBS, Loom
- 설문: Google Forms, Typeform
- 분석: Hotjar, FullStory

#### 10.3 A/B Testing (선택사항)

**예시: CTA 버튼 위치 테스트**

**Version A**: "장바구니 담기" 버튼 우측 상단
**Version B**: "장바구니 담기" 버튼 옵션 선택 바로 아래

**측정 지표**:
- 클릭률 (CTR): (버튼 클릭 수 / 페이지 뷰) × 100%
- 전환율 (CVR): (장바구니 담기 성공 / 버튼 클릭) × 100%
- 사용자 선호도: 설문 조사

**통계적 유의성**:
- 최소 샘플 크기: 100명/버전
- 신뢰 수준: 95%
- 테스트 기간: 1-2주

---

### 11. LLM 활용 프로토타이핑

#### 11.1 Claude 활용 시나리오

**시나리오 1: 요구사항 문서 생성**

**Input**:
```
"온라인 쇼핑몰의 장바구니 기능에 대한 상세한 요구사항 명세서를 작성해줘.
기능 요구사항, 비기능 요구사항, 예외 상황, 테스트 케이스까지 포함해서."
```

**Output 예시**:
```markdown
# 장바구니 기능 요구사항 명세서

## 기능 요구사항 (Functional Requirements)

### FR-CART-001: 상품 추가
- 사용자는 상품 상세 페이지에서 상품을 장바구니에 추가할 수 있다.
- 사이즈, 색상 등 필수 옵션 선택 후 추가 가능
- 동일 상품 추가 시 수량 증가

### FR-CART-002: 수량 변경
- 사용자는 장바구니에서 상품 수량을 변경할 수 있다.
- +/- 버튼 또는 직접 입력으로 수량 조절
- 수량 0 설정 시 상품 삭제 확인

## 비기능 요구사항 (Non-functional Requirements)

### NFR-CART-001: 성능
- 장바구니 페이지 로딩 시간 < 2초
- 수량 변경 시 즉시 반영 (< 500ms)

### NFR-CART-002: 데이터 보존
- 로그인 사용자: 서버에 영구 저장
- 비로그인 사용자: 로컬스토리지에 7일간 보관
```

**시나리오 2: 테스트 케이스 생성**

**Input**:
```
"로그인 기능에 대한 테스트 케이스를 작성해줘.
정상 케이스, 예외 케이스, 보안 테스트까지 포함해서."
```

#### 11.2 Cursor 활용 시나리오

**시나리오 1: 컴포넌트 자동 생성**

**Input** (자연어 주석):
```javascript
// 상품 카드 컴포넌트
// 프로퍼티: image, title, price, rating, onAddToCart
// 호버 시 그림자 효과
// 장바구니 버튼 클릭 시 onAddToCart 콜백 호출
// Tailwind CSS 사용
```

**Cursor 생성 결과**:
```jsx
import React from 'react';

const ProductCard = ({ 
  image, 
  title, 
  price, 
  rating, 
  onAddToCart 
}) => {
  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 p-4 cursor-pointer">
      <div className="relative">
        <img 
          src={image} 
          alt={title} 
          className="w-full h-48 object-cover rounded-md mb-4"
        />
      </div>
      <h3 className="text-lg font-semibold mb-2 line-clamp-2 text-gray-900">
        {title}
      </h3>
      <div className="flex items-center justify-between mb-4">
        <span className="text-xl font-bold text-blue-600">
          ₩{price.toLocaleString()}
        </span>
        <div className="flex items-center">
          <div className="flex text-yellow-400">
            {[...Array(5)].map((_, i) => (
              <svg
                key={i}
                className={`w-4 h-4 ${
                  i < Math.floor(rating) ? 'fill-current' : 'text-gray-300'
                }`}
                viewBox="0 0 20 20"
              >
                <path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/>
              </svg>
            ))}
          </div>
          <span className="ml-1 text-sm text-gray-600">
            ({rating})
          </span>
        </div>
      </div>
      <button 
        onClick={onAddToCart}
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors duration-200 font-medium"
      >
        장바구니 담기
      </button>
    </div>
  );
};

export default ProductCard;
```

**시나리오 2: API 연동 코드**

**Input**:
```javascript
// 상품 목록을 가져오는 React Hook
// useQuery 사용, 로딩/에러 상태 관리
// 필터링 파라미터 지원 (category, priceMin, priceMax)
```

**Cursor 생성 결과**:
```javascript
import { useQuery } from 'react-query';
import { useState } from 'react';

const useProducts = (initialFilters = {}) => {
  const [filters, setFilters] = useState(initialFilters);

  const { data, isLoading, error, refetch } = useQuery(
    ['products', filters],
    async () => {
      const queryParams = new URLSearchParams();
      
      Object.entries(filters).forEach(([key, value]) => {
        if (value !== undefined && value !== '') {
          queryParams.append(key, value);
        }
      });

      const response = await fetch(`/api/v1/items?${queryParams}`);
      
      if (!response.ok) {
        throw new Error('Failed to fetch products');
      }

      return response.json();
    },
    {
      staleTime: 5 * 60 * 1000, // 5분
      cacheTime: 10 * 60 * 1000, // 10분
    }
  );

  const updateFilters = (newFilters) => {
    setFilters(prev => ({ ...prev, ...newFilters }));
  };

  return {
    products: data?.data || [],
    total: data?.total || 0,
    isLoading,
    error,
    filters,
    updateFilters,
    refetch,
  };
};

export default useProducts;
```

#### 11.3 GitHub Copilot 활용

**상황**: 폼 유효성 검사

**코드 시작**:
```javascript
const validateForm = (formData) => {
  const errors = {};
  
  // 이메일 유효성 검사
```

**Copilot 자동 완성**:
```javascript
const validateForm = (formData) => {
  const errors = {};
  
  // 이메일 유효성 검사
  if (!formData.email) {
    errors.email = '이메일은 필수 항목입니다.';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.email = '올바른 이메일 형식을 입력해주세요.';
  }

  // 비밀번호 유효성 검사
  if (!formData.password) {
    errors.password = '비밀번호는 필수 항목입니다.';
  } else if (formData.password.length < 8) {
    errors.password = '비밀번호는 8자 이상이어야 합니다.';
  } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/.test(formData.password)) {
    errors.password = '비밀번호는 대소문자, 숫자, 특수문자를 포함해야 합니다.';
  }

  // 이름 유효성 검사
  if (!formData.name) {
    errors.name = '이름은 필수 항목입니다.';
  } else if (formData.name.length < 2) {
    errors.name = '이름은 2자 이상이어야 합니다.';
  }

  // 전화번호 유효성 검사
  if (!formData.phone) {
    errors.phone = '전화번호는 필수 항목입니다.';
  } else if (!/^010-\d{4}-\d{4}$/.test(formData.phone)) {
    errors.phone = '전화번호 형식이 올바르지 않습니다. (010-0000-0000)';
  }

  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};
```

---

### 12. 협업 및 버전 관리

#### 12.1 Git Workflow

**브랜치 전략**:
```
main (프로덕션)
├── develop (개발 통합)
│   ├── feature/user-auth
│   ├── feature/product-list
│   └── feature/cart-management
└── hotfix/critical-bug
```

**커밋 메시지 컨벤션**:
```
type(scope): subject

feat(auth): 소셜 로그인 기능 추가
fix(cart): 수량 변경 시 총액 계산 오류 수정
docs(api): API 문서 업데이트
style(ui): 버튼 스타일 통일
refactor(cart): 장바구니 상태 관리 Redux로 변경
test(auth): 로그인 테스트 케이스 추가
```

#### 12.2 코드 리뷰 체크리스트

**기능**:
- [ ] 요구사항에 맞게 구현되었는가?
- [ ] Edge Case 처리되었는가?
- [ ] 에러 핸들링 적절한가?

**품질**:
- [ ] 코드 가독성 좋은가?
- [ ] 중복 코드 없는가?
- [ ] 성능 이슈 없는가?

**보안**:
- [ ] 사용자 입력 검증하는가?
- [ ] 민감 정보 노출 없는가?
- [ ] XSS, CSRF 방어되는가?

---

### 13. 배포 및 모니터링

#### 13.1 배포 전략

**프론트엔드 배포**:
- **Vercel**: Next.js 최적화, 자동 배포
- **Netlify**: JAMstack, Form 처리
- **AWS S3 + CloudFront**: 대용량 정적 사이트

**백엔드 배포**:
- **Heroku**: 간단한 배포, 무료 티어
- **AWS EC2**: 유연한 설정, 확장성
- **Docker + Kubernetes**: 컨테이너 기반, 마이크로서비스

#### 13.2 환경 설정

**Environment Variables**:
```bash
# .env.production
REACT_APP_API_URL=https://api.myshop.com
REACT_APP_PAYMENT_KEY=pk_live_xxxxx
REACT_APP_GA_TRACKING=GA-XXXXX-X

# .env.development  
REACT_APP_API_URL=http://localhost:3001
REACT_APP_PAYMENT_KEY=pk_test_xxxxx
REACT_APP_GA_TRACKING=
```

#### 13.3 모니터링 설정

**성능 모니터링**:
- Google Analytics: 사용자 행동 분석
- Google PageSpeed Insights: 성능 측정
- Sentry: 에러 추적 및 알림

**비즈니스 지표**:
- 전환율 (홈 → 상품 상세 → 장바구니 → 결제)
- 이탈률 (각 단계별)
- 평균 주문 금액 (AOV)

---

## 🛠️ 실습 과제

### 과제 1: 프로토타입 전략 수립
- 자신의 프로젝트에 적합한 Fidelity Level 선택 및 근거 작성
- MoSCoW 또는 RICE로 기능 우선순위 매기기 (최소 15개 기능)

### 과제 2: Hi-Fi 프로토타입 개발
- Figma 또는 코드로 완전한 프로토타입 구현
- 핵심 사용자 플로우 3개 이상 동작 가능
- 반응형 디자인 적용

### 과제 3: AI 도구 활용 실습
- Claude로 User Story 5개 생성
- Cursor로 React 컴포넌트 3개 생성
- 생성 과정 및 결과물 문서화

### 과제 4: 사용자 테스트 진행
- 최소 5명 사용자 테스트 진행
- 테스트 시나리오 3개 작성
- 정량/정성 피드백 포함한 테스트 리포트 작성

### 과제 5: 최종 발표 자료
- 프로젝트 개요 (2분)
- 핵심 기능 시연 (5분)
- 사용자 테스트 결과 (2분)
- 향후 계획 (1분)
- **총 10분 발표**

---

## 📖 참고 자료

- **도서**:
  - "The Lean Startup" - Eric Ries
  - "Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days" - Jake Knapp
  - "Hooked: How to Build Habit-Forming Products" - Nir Eyal

- **온라인 리소스**:
  - Figma Learn: figma.com/learn
  - Cursor Documentation: cursor.sh/docs
  - React Documentation: react.dev
  - Vue.js Guide: vuejs.org/guide
  - Claude Documentation: docs.anthropic.com

- **도구 및 서비스**:
  - **디자인**: Figma, Framer, ProtoPie
  - **개발**: Cursor, GitHub Copilot, CodeSandbox
  - **배포**: Vercel, Netlify, Heroku
  - **테스트**: Maze, UserTesting, Lookback
  - **모니터링**: Google Analytics, Sentry, Hotjar

---

## 🔄 복습 체크리스트

- [ ] 프로토타입 Fidelity 수준 (Lo/Mid/Hi) 이해 및 선택 능력
- [ ] 도구 선택 기준 및 매트릭스 활용
- [ ] MoSCoW, RICE, Kano 우선순위 결정 프레임워크 적용
- [ ] Design-Dev-Test Loop 프로세스 이해
- [ ] 리소스 배분 전략 및 부족 시 대응 방안
- [ ] 4주 스프린트 로드맵 작성 및 관리
- [ ] 사용자 테스트 시나리오 설계 및 진행
- [ ] 최종 산출물 체크리스트 적용
- [ ] LLM (Claude, Cursor) 활용 프로토타이핑
- [ ] Git Workflow 및 협업 프로세스 이해

---

## 🎓 과정 총정리

### 축하합니다! 🎉

**AX/DX 서비스 기획 과정**을 성공적으로 완주하셨습니다!

#### 학습 여정 요약

**Phase 1: Foundation (Week 1-2)**
- ✅ AX/DX 개념 및 산업 적용 사례 이해
- ✅ 프로젝트 캔버스를 통한 아이디어 구체화
- ✅ SMART 목표 설정 및 팀 구성

**Phase 2: Analysis & Strategy (Week 3-4)**
- ✅ 사용자 문제 정의 및 요구사항 분석
- ✅ 비즈니스 모델 설계 및 시장 규모 추정
- ✅ 핵심 지표(KPI) 설정

**Phase 3: Design & Implementation (Week 11-14)**
- ✅ 사용자 중심 설계 (Persona, Journey Map)
- ✅ 기술 아키텍처 및 API 설계
- ✅ UI/UX 디자인 및 접근성 준수
- ✅ 프로토타입 개발 및 사용자 검증

#### 습득한 핵심 역량

**1. 기획 역량**:
- 문제 정의 및 솔루션 설계
- 비즈니스 모델 수립
- 요구사항 분석 및 우선순위 결정

**2. 디자인 역량**:
- 사용자 중심 설계
- 와이어프레임 및 프로토타입 제작
- 접근성 및 반응형 디자인

**3. 기술 역량**:
- API 설계 및 보안 고려사항
- 프론트엔드 개발 (React/Vue)
- AI 도구 활용 개발 효율화

**4. 검증 역량**:
- 사용자 테스트 설계 및 진행
- 데이터 기반 의사결정
- 반복 개선 프로세스

#### 다음 단계 로드맵

**1. MVP (Minimum Viable Product) 개발**:
- 프로토타입 → 실제 서비스 전환
- 핵심 기능 중심 빠른 출시
- 실제 사용자 피드백 수집

**2. 시장 검증**:
- PMF (Product-Market Fit) 확인
- 사용자 행동 데이터 분석
- 비즈니스 모델 검증 및 수정

**3. 투자 유치**:
- 사업계획서 작성
- 트랙션 지표 준비 (MAU, Revenue, NPS)
- 투자자 피칭 (Seed, Pre-A, Series A)

**4. 스케일업**:
- 팀 확장 (개발, 마케팅, 영업)
- 기술 아키텍처 확장 (MSA, Dev