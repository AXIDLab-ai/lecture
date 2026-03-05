[← 이전: Week 11](./week11.md) | [목차](./lectureMap.md) | [다음: Week 13 →](./week13.md)

Week 12: Detailed Design

---

## 📌 학습 목표

- RESTful API 설계 원칙 이해 및 적용
- API 엔드포인트 카탈로그 작성 능력 배양
- Request/Response 스키마 정의 역량 강화
- Error Handling 전략 수립
- Zero Trust 보안 모델 이해
- OAuth 2.0 및 OIDC 인증 체계 구축
- Token 관리 및 암호화 기법 습득

---

## 📚 주요 내용

### 1. RESTful API 설계 원칙

#### 1.1 REST 기본 개념

**REST (Representational State Transfer)**:
- 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하는 아키텍처 스타일
- 리소스(Resource) 중심 설계

**6가지 제약 조건**:
1. **Client-Server**: 역할 분리
2. **Stateless**: 무상태성 (각 요청은 독립적)
3. **Cacheable**: 캐시 가능
4. **Uniform Interface**: 일관된 인터페이스
5. **Layered System**: 계층화된 시스템
6. **Code on Demand** (선택): 서버가 클라이언트 실행 코드 전송 가능

#### 1.2 리소스 네이밍 규칙

**기본 원칙**:
- **명사 사용** (동사 X)
- **복수형 사용** (`/users`, `/items`)
- **소문자 및 하이픈** (`/user-profiles`, `/order-items`)
- **계층 구조 표현** (`/users/{id}/orders`)

**좋은 예시**:
- `GET /users` - 사용자 목록 조회
- `GET /users/{id}` - 특정 사용자 조회
- `POST /users` - 사용자 생성
- `PUT /users/{id}` - 사용자 전체 수정
- `PATCH /users/{id}` - 사용자 부분 수정
- `DELETE /users/{id}` - 사용자 삭제

**나쁜 예시**:
- `GET /getUsers` (동사 사용 X)
- `POST /user/create` (명사는 복수형, 동사 불필요)
- `GET /users/delete/123` (HTTP 메서드로 표현)

#### 1.3 HTTP 메서드 사용

| Method | 용도 | Idempotent | Safe |
|--------|------|------------|------|
| GET | 조회 (Read) | O | O |
| POST | 생성 (Create) | X | X |
| PUT | 전체 수정 (Update) | O | X |
| PATCH | 부분 수정 (Partial Update) | X | X |
| DELETE | 삭제 (Delete) | O | X |

**Idempotent (멱등성)**: 동일한 요청을 여러 번 수행해도 결과가 동일  
**Safe (안전성)**: 리소스를 변경하지 않음

---

### 2. API 엔드포인트 카탈로그 (24개)

#### 2.1 Users (사용자 관리)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| 1 | POST | `/api/v1/auth/register` | 사용자 회원가입 |
| 2 | POST | `/api/v1/auth/login` | 로그인 (액세스 토큰 발급) |
| 3 | POST | `/api/v1/auth/refresh` | 토큰 갱신 |
| 4 | POST | `/api/v1/auth/logout` | 로그아웃 |
| 5 | GET | `/api/v1/users/{id}` | 사용자 프로필 조회 |
| 6 | PATCH | `/api/v1/users/{id}` | 사용자 프로필 수정 |
| 7 | DELETE | `/api/v1/users/{id}` | 사용자 탈퇴 |

#### 2.2 Items (상품 관리)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| 8 | GET | `/api/v1/items` | 상품 목록 조회 (필터, 정렬, 페이징) |
| 9 | GET | `/api/v1/items/{id}` | 상품 상세 조회 |
| 10 | POST | `/api/v1/items` | 상품 등록 (판매자/관리자) |
| 11 | PUT | `/api/v1/items/{id}` | 상품 전체 수정 |
| 12 | PATCH | `/api/v1/items/{id}` | 상품 부분 수정 (예: 재고 수량) |
| 13 | DELETE | `/api/v1/items/{id}` | 상품 삭제 |

#### 2.3 Cart (장바구니)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| 14 | GET | `/api/v1/cart` | 장바구니 조회 |
| 15 | POST | `/api/v1/cart/items` | 장바구니에 상품 추가 |
| 16 | PATCH | `/api/v1/cart/items/{itemId}` | 장바구니 상품 수량 변경 |
| 17 | DELETE | `/api/v1/cart/items/{itemId}` | 장바구니 상품 삭제 |

#### 2.4 Orders (주문)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| 18 | GET | `/api/v1/orders` | 주문 내역 조회 |
| 19 | GET | `/api/v1/orders/{id}` | 주문 상세 조회 |
| 20 | POST | `/api/v1/orders` | 주문 생성 |
| 21 | PATCH | `/api/v1/orders/{id}/cancel` | 주문 취소 |

#### 2.5 Reviews (리뷰)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| 22 | GET | `/api/v1/items/{itemId}/reviews` | 상품 리뷰 목록 조회 |
| 23 | POST | `/api/v1/items/{itemId}/reviews` | 리뷰 작성 |
| 24 | DELETE | `/api/v1/reviews/{id}` | 리뷰 삭제 |

---

### 3. Request/Response 스키마

#### 3.1 Request 스키마 예시

**POST `/api/v1/auth/register`**

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "SecureP@ssw0rd",
  "name": "홍길동",
  "phone": "010-1234-5678",
  "birthdate": "1990-01-01",
  "agreeTerms": true,
  "agreePrivacy": true,
  "agreeMarketing": false
}
```

**Validation Rules**:
- `email`: 필수, 이메일 형식, 중복 불가
- `password`: 필수, 8자 이상, 영문+숫자+특수문자 조합
- `name`: 필수, 2-20자
- `phone`: 필수, 010-####-#### 형식
- `agreeTerms`, `agreePrivacy`: 필수 true

#### 3.2 Response 스키마 예시

**Success Response (201 Created)**:
```json
{
  "status": "success",
  "code": 201,
  "message": "회원가입이 완료되었습니다.",
  "data": {
    "userId": "u1234567890",
    "email": "user@example.com",
    "name": "홍길동",
    "createdAt": "2026-02-14T10:30:00Z"
  }
}
```

**Error Response (400 Bad Request)**:
```json
{
  "status": "error",
  "code": 400,
  "message": "입력값이 올바르지 않습니다.",
  "errors": [
    {
      "field": "email",
      "message": "이미 사용 중인 이메일입니다."
    },
    {
      "field": "password",
      "message": "비밀번호는 8자 이상이어야 합니다."
    }
  ],
  "timestamp": "2026-02-14T10:30:00Z",
  "path": "/api/v1/auth/register"
}
```

#### 3.3 User 레코드 예시 (JSON)

```json
{
  "userId": "u1234567890",
  "email": "user@example.com",
  "name": "홍길동",
  "phone": "010-1234-5678",
  "profileImageUrl": "https://cdn.example.com/profiles/u1234567890.jpg",
  "birthdate": "1990-01-01",
  "role": "customer",
  "status": "active",
  "agreeMarketing": false,
  "createdAt": "2026-01-01T09:00:00Z",
  "updatedAt": "2026-02-14T10:30:00Z",
  "lastLoginAt": "2026-02-14T08:00:00Z"
}
```

---

### 4. Error Handling 전략

#### 4.1 HTTP 상태 코드

**Success (2xx)**:
- `200 OK`: 성공 (GET, PUT, PATCH, DELETE)
- `201 Created`: 생성 성공 (POST)
- `204 No Content`: 성공 but 반환 데이터 없음 (DELETE)

**Client Error (4xx)**:
- `400 Bad Request`: 잘못된 요청 (유효성 검증 실패)
- `401 Unauthorized`: 인증 실패 (로그인 필요)
- `403 Forbidden`: 권한 없음
- `404 Not Found`: 리소스 없음
- `409 Conflict`: 충돌 (중복 이메일 등)
- `422 Unprocessable Entity`: 의미는 맞지만 처리 불가 (비즈니스 로직 오류)
- `429 Too Many Requests`: 요청 제한 초과

**Server Error (5xx)**:
- `500 Internal Server Error`: 서버 내부 오류
- `502 Bad Gateway`: 게이트웨이 오류
- `503 Service Unavailable`: 서비스 일시 중단

#### 4.2 Error Response 표준 포맷

```json
{
  "status": "error",
  "code": 400,
  "message": "사용자 친화적 에러 메시지",
  "errors": [
    {
      "field": "필드명",
      "message": "구체적인 오류 내용"
    }
  ],
  "errorCode": "ERR_USER_001",
  "timestamp": "2026-02-14T10:30:00Z",
  "path": "/api/v1/users",
  "requestId": "req-abc123def456"
}
```

#### 4.3 Error Code 매핑

| Error Code | Description | HTTP Status |
|------------|-------------|-------------|
| ERR_AUTH_001 | 인증 토큰 만료 | 401 |
| ERR_AUTH_002 | 인증 토큰 유효하지 않음 | 401 |
| ERR_AUTH_003 | 권한 부족 | 403 |
| ERR_USER_001 | 이메일 중복 | 409 |
| ERR_USER_002 | 사용자 없음 | 404 |
| ERR_ITEM_001 | 상품 재고 부족 | 422 |
| ERR_ORDER_001 | 주문 취소 불가 상태 | 422 |
| ERR_SYSTEM_001 | 내부 서버 오류 | 500 |

---

### 5. API Versioning (버전 관리)

#### 5.1 버전 관리 전략

**URI Versioning** (권장):
- `/api/v1/users`
- `/api/v2/users`

장점: 명확하고 직관적, 캐싱 용이  
단점: URI 변경

**Header Versioning**:
```
GET /api/users
Accept: application/vnd.myapi.v1+json
```

**Query Parameter**:
- `/api/users?version=1`

#### 5.2 Breaking Change 관리

**언제 버전 올려야 하나?**:
- 필드 제거 또는 이름 변경
- 데이터 타입 변경
- 기본 동작 변경

**Deprecated 처리**:
- 구 버전 유지 기간 명시 (예: 6개월)
- Response Header에 `X-API-Deprecated: true` 포함
- 공지 및 마이그레이션 가이드 제공

---

### 6. Rate Limiting (속도 제한)

#### 6.1 제한 전략

**목적**:
- 서버 부하 방지
- 악의적 사용 차단
- 공정한 리소스 사용

**제한 기준**:
- IP 주소별
- 사용자 ID별
- API Key별

#### 6.2 제한 설정 예시

**Free Tier**:
- 100 requests/hour
- 1,000 requests/day

**Paid Tier**:
- 10,000 requests/hour
- 100,000 requests/day

#### 6.3 Response Headers

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1644836400
```

**429 Too Many Requests**:
```json
{
  "status": "error",
  "code": 429,
  "message": "요청 제한을 초과했습니다. 1시간 후 다시 시도하세요.",
  "retryAfter": 3600
}
```

---

### 7. Zero Trust 보안 아키텍처

#### 7.1 Zero Trust 개념

**원칙**: "신뢰하지 말고, 항상 검증하라 (Never Trust, Always Verify)"

**핵심 요소**:
1. **Identity Verification**: 모든 요청에 대해 인증/인가 검증
2. **Least Privilege**: 최소 권한 원칙
3. **Micro-Segmentation**: 네트워크 세분화
4. **Continuous Monitoring**: 지속적 모니터링 및 로깅

#### 7.2 적용 전략

**네트워크 계층**:
- VPN 대신 Identity-Aware Proxy 사용
- Private Subnet 및 Security Group 설정

**애플리케이션 계층**:
- API Gateway에서 인증/인가 처리
- 모든 내부 서비스 간 통신도 mTLS (Mutual TLS) 적용

**데이터 계층**:
- 암호화 (at rest & in transit)
- 접근 로그 기록

---

### 8. OAuth 2.0 및 OIDC 인증

#### 8.1 OAuth 2.0 개요

**정의**:
- 권한 부여(Authorization) 프레임워크
- 제3자 앱이 사용자 대신 리소스에 접근 허용

**주요 역할**:
- **Resource Owner**: 사용자
- **Client**: 서드파티 앱
- **Authorization Server**: 인증 서버 (예: Google, Keycloak)
- **Resource Server**: API 서버

#### 8.2 Grant Types (권한 부여 방식)

**Authorization Code Flow** (가장 안전, 웹 앱 권장):
1. 사용자가 클라이언트 앱에서 로그인 요청
2. Authorization Server로 리다이렉트
3. 사용자 로그인 및 권한 동의
4. Authorization Code 발급
5. 클라이언트가 Code를 Access Token으로 교환
6. Access Token으로 API 호출

**Client Credentials Flow** (서버 간 통신):
- Client ID + Client Secret으로 직접 토큰 발급

**Implicit Flow** (비권장, 보안 취약):
- 브라우저에서 직접 토큰 발급

#### 8.3 OIDC (OpenID Connect)

**정의**:
- OAuth 2.0 위에 인증(Authentication) 레이어 추가
- ID Token (JWT) 발급

**ID Token 구조**:
```json
{
  "iss": "https://auth.example.com",
  "sub": "u1234567890",
  "aud": "client-app-id",
  "exp": 1644836400,
  "iat": 1644832800,
  "name": "홍길동",
  "email": "user@example.com",
  "email_verified": true
}
```

#### 8.4 구현 예시

**POST `/api/v1/auth/login`**

**Request**:
```json
{
  "email": "user@example.com",
  "password": "SecureP@ssw0rd"
}
```

**Response (200 OK)**:
```json
{
  "status": "success",
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "rt_abc123def456...",
    "tokenType": "Bearer",
    "expiresIn": 3600,
    "user": {
      "userId": "u1234567890",
      "email": "user@example.com",
      "name": "홍길동",
      "role": "customer"
    }
  }
}
```

---

### 9. Token 관리

#### 9.1 JWT (JSON Web Token) 구조

**Header**:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**:
```json
{
  "sub": "u1234567890",
  "role": "customer",
  "iat": 1644832800,
  "exp": 1644836400
}
```

**Signature**:
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

#### 9.2 Access Token vs Refresh Token

| 항목 | Access Token | Refresh Token |
|------|--------------|---------------|
| 용도 | API 호출 인증 | Access Token 갱신 |
| 유효 기간 | 짧음 (15분~1시간) | 김 (7일~30일) |
| 저장 위치 | 메모리 또는 SessionStorage | HttpOnly Cookie (권장) |
| 노출 위험 | 높음 (짧은 수명으로 완화) | 낮음 (보안 저장) |

#### 9.3 Token Refresh Flow

1. 클라이언트가 API 호출 (Access Token 첨부)
2. 서버가 401 Unauthorized 응답 (Token Expired)
3. 클라이언트가 Refresh Token으로 갱신 요청
4. 서버가 새로운 Access Token 발급
5. 재시도

**POST `/api/v1/auth/refresh`**

**Request**:
```json
{
  "refreshToken": "rt_abc123def456..."
}
```

**Response (200 OK)**:
```json
{
  "status": "success",
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600
  }
}
```

#### 9.4 Token Revocation (토큰 무효화)

**로그아웃 시**:
- Refresh Token을 블랙리스트에 추가 (Redis)
- Access Token은 만료 시까지 유효 (짧은 수명이므로 허용)

---

### 10. 암호화 (Encryption)

#### 10.1 데이터 암호화

**at Rest (저장 시)**:
- 비밀번호: bcrypt, Argon2 (단방향 해시)
- 민감 정보: AES-256 (양방향 암호화)
- 데이터베이스: TDE (Transparent Data Encryption)

**in Transit (전송 시)**:
- HTTPS (TLS 1.3)
- mTLS (서버 간 통신)

#### 10.2 비밀번호 해싱 예시

**bcrypt (Node.js)**:
```javascript
const bcrypt = require('bcrypt');
const saltRounds = 10;

// 해싱
const hashedPassword = await bcrypt.hash('SecureP@ssw0rd', saltRounds);
// 결과: $2b$10$abcdefghijklmnopqrstuvwxyz...

// 검증
const isMatch = await bcrypt.compare('SecureP@ssw0rd', hashedPassword);
// true
```

#### 10.3 민감 정보 암호화 (AES-256)

**암호화 대상**:
- 주민등록번호, 카드번호
- API Key, Secret

**Key 관리**:
- AWS KMS, Google Cloud KMS 사용
- 환경 변수에 직접 저장 금지
- 정기적으로 Key Rotation

---

## 🛠️ 실습 과제

### 과제 1: API 엔드포인트 카탈로그 작성
- 자신의 프로젝트에 필요한 최소 15개 엔드포인트 정의 (Method, Path, Description)

### 과제 2: Request/Response 스키마 작성
- 핵심 엔드포인트 5개에 대한 상세 Request Body, Response Body, Validation Rules 문서화

### 과제 3: Error Handling 전략 수립
- 프로젝트 Error Code 체계 정의 (최소 10개)
- 표준 Error Response 포맷 작성

### 과제 4: 인증 플로우 설계
- OAuth 2.0 / JWT 기반 로그인/로그아웃/토큰 갱신 플로우 다이어그램 작성

---

## 📖 참고 자료

- **도서**:
  - "RESTful Web APIs" - Leonard Richardson
  - "Zero Trust Networks" - Evan Gilman
- **온라인 리소스**:
  - REST API Tutorial - restfulapi.net
  - OAuth 2.0 - oauth.net
  - JWT.io - JWT Debugger
- **도구**:
  - Postman / Insomnia: API 테스트
  - Swagger / OpenAPI: API 문서화
  - Keycloak: 오픈소스 Identity Provider

---

## 🔄 복습 체크리스트

- [ ] RESTful API 설계 원칙 이해
- [ ] 리소스 네이밍 및 HTTP 메서드 사용
- [ ] API 엔드포인트 카탈로그 작성 능력
- [ ] Request/Response 스키마 정의 역량
- [ ] Error Handling 전략 수립
- [ ] OAuth 2.0 및 OIDC 인증 플로우 이해
- [ ] JWT 구조 및 Token 관리
- [ ] Zero Trust 보안 아키텍처 개념
- [ ] 암호화 기법 (bcrypt, AES-256, HTTPS)

---

## 📝 다음 주 예습

**Week 13: UI/UX Design & Implementation**
- UI 컴포넌트 명세
- 디자인 토큰 시스템
- 인터랙션 패턴
- 내비게이션 아키텍처
- 에러 핸들링 및 피드백 시스템

---

[← 이전: Week 11](./week11.md) | [목차](./README.md) | [다음: Week 13 →](./week13.md)

**Last Updated**: 2026-02-14
