# Week 11: 데이터베이스 설계 - 최신 트렌드 🚀

> **한국공학대학교 | 시스템 분석 및 설계 | 강송희 교수**

---

## 📌 학습 목표

- ✅ 정보공학 방법론을 활용한 체계적 데이터베이스 설계 방법 습득
- ✅ 개념적, 논리적, 물리적 데이터 모델링의 차이점과 단계별 수행 방법 이해
- ✅ ERD 고급 작성 기법을 통한 복잡한 비즈니스 요구사항 모델링 능력 개발
- ✅ 클라우드, 그래프, 시계열, 벡터 데이터베이스 등 최신 트렌드 파악
- ✅ AI 시대에 적합한 데이터 저장소 선택 및 설계 역량 배양

---

## 🏗️ 정보공학 방법론 (Information Engineering)

### 정의 및 특징 📖

#### 정보공학이란?
> **기업의 정보 요구사항을 체계적으로 분석하고, 통합된 정보 아키텍처를 구축하는 방법론**

#### 핵심 원칙 🎯
- **데이터 중심 접근**: 프로세스보다 데이터 구조 우선
- **전사적 관점**: 부서별 최적화보다 전체 최적화
- **단계적 접근**: Top-Down 방식의 점진적 상세화
- **표준화**: 일관된 모델링 기법과 표기법 사용

#### IE 방법론의 장점 ✨
- **데이터 일관성** 확보
- **중복 최소화** 및 통합성 향상
- **유지보수성** 증대
- **확장성** 고려한 설계

### IE 프로세스 단계 🔄

#### 1단계: 정보전략계획 (ISP)
- 기업 목표와 IT 전략 연계
- 현행 시스템 현황 분석
- 목표 아키텍처 정의

#### 2단계: 업무영역분석 (BAA)
- 주요 업무 영역 식별
- 데이터 클래스 정의
- 업무 프로세스 모델링

#### 3단계: 업무시스템설계 (BSD)
- 상세 데이터 모델링
- 프로세스 상세 설계
- 시스템 인터페이스 설계

---

## 📊 3단계 데이터 모델링

### 1단계: 개념적 데이터 모델링 (Conceptual) 🎨

#### 목적 및 특징
- **업무 규칙 파악**: 비즈니스 요구사항 이해
- **개체 식별**: 핵심 엔티티와 관계 정의
- **기술 독립적**: 구현 기술과 무관한 추상적 모델

#### 산출물
```
개념적 ERD
├─ 핵심 엔티티 (고객, 상품, 주문)
├─ 주요 관계 (구매, 포함, 배송)
├─ 주요 속성 (고객명, 상품명, 주문일자)
└─ 비즈니스 규칙 (제약조건)
```

#### 작성 예시
```
[고객] ──구매──> [주문] ──포함──> [주문상세] ──참조──> [상품]
   │                                                    │
   └──────────────────배송지───────────────────────────┘
```

### 2단계: 논리적 데이터 모델링 (Logical) 🔧

#### 목적 및 특징
- **정규화 적용**: 데이터 중복 제거
- **상세 속성 정의**: 데이터 타입 및 제약조건
- **DBMS 독립적**: 특정 제품에 의존하지 않음

#### 정규화 과정
```
1NF → 2NF → 3NF → BCNF
 │     │     │     │
 │     │     │     └─ 함수종속성 완전 제거
 │     │     └─ 이행적 함수종속 제거
 │     └─ 부분적 함수종속 제거
 └─ 반복 그룹 제거
```

#### 논리적 ERD 예시
```sql
고객 (고객ID*, 고객명, 이메일, 연락처, 주소)
주문 (주문ID*, 고객ID, 주문일자, 배송주소, 총금액)
상품 (상품ID*, 상품명, 단가, 카테고리, 재고수량)
주문상세 (주문ID*, 상품ID*, 주문수량, 단가, 소계)
```

### 3단계: 물리적 데이터 모델링 (Physical) ⚡

#### 목적 및 특징
- **성능 최적화**: 인덱스, 파티션 설계
- **저장공간 최적화**: 데이터 타입 세밀 조정
- **DBMS 종속적**: 특정 데이터베이스 제품 고려

#### 성능 최적화 기법
```
성능 튜닝 요소
├─ 인덱스 설계 (B-Tree, Hash, Bitmap)
├─ 파티셔닝 (Range, Hash, List)
├─ 클러스터링 (데이터 물리적 배치)
├─ 비정규화 (성능을 위한 의도적 중복)
└─ 뷰 활용 (복잡 쿼리 단순화)
```

#### 물리적 설계 예시
```sql
CREATE TABLE TB_CUSTOMER (
    CUST_ID     VARCHAR(10) PRIMARY KEY,
    CUST_NM     VARCHAR(50) NOT NULL,
    EMAIL       VARCHAR(100),
    PHONE       VARCHAR(15),
    ADDR        TEXT,
    REG_DTM     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX IDX_CUST_EMAIL (EMAIL),
    INDEX IDX_CUST_PHONE (PHONE)
) PARTITION BY RANGE (YEAR(REG_DTM));
```

---

## 🎯 ERD 고급 작성 기법

### 1. Subtype / Supertype (상속 관계) 🏛️

#### 개념
- **일반화/특수화**: 공통 속성과 고유 속성 분리
- **상속**: 하위 엔티티가 상위 엔티티 속성 상속
- **다형성**: 동일한 관계가 서로 다른 하위 타입에 적용

#### 모델링 예시
```
[사람] (공통: 이름, 생년월일, 주소)
  ├─ [고객] (고유: 고객등급, 적립포인트)
  ├─ [직원] (고유: 사번, 부서, 급여)
  └─ [공급업체] (고유: 사업자번호, 계약기간)
```

#### 구현 방법
```sql
-- Single Table 방식
CREATE TABLE 사람 (
    ID VARCHAR(10) PRIMARY KEY,
    이름 VARCHAR(50),
    생년월일 DATE,
    구분 VARCHAR(10), -- 'CUSTOMER', 'EMPLOYEE', 'SUPPLIER'
    고객등급 VARCHAR(10), -- 고객용
    사번 VARCHAR(10),     -- 직원용
    사업자번호 VARCHAR(15) -- 공급업체용
);

-- Joined Table 방식  
CREATE TABLE 사람 (ID, 이름, 생년월일);
CREATE TABLE 고객 (ID, 고객등급, FOREIGN KEY (ID) REFERENCES 사람(ID));
CREATE TABLE 직원 (ID, 사번, 부서, FOREIGN KEY (ID) REFERENCES 사람(ID));
```

### 2. Aggregation (집합 관계) 📦

#### 개념
- **전체-부분 관계**: "has-a" 관계
- **약한 소유**: 부분이 독립적으로 존재 가능
- **공유 가능**: 한 부분이 여러 전체에 속할 수 있음

#### 모델링 예시
```
[대학교] ◇────── [학과]
   │                │
   └─────────────── [교수]
```

### 3. Composition (구성 관계) 🔗

#### 개념
- **강한 소유 관계**: 전체가 부분의 생명주기 관리
- **동시 소멸**: 전체 삭제 시 부분도 삭제
- **독점적**: 부분은 하나의 전체에만 속함

#### 모델링 예시
```
[주문] ♦────── [주문상세]
[건물] ♦────── [방]
[자동차] ♦──── [엔진]
```

#### 구현 방법
```sql
CREATE TABLE 주문 (
    주문ID VARCHAR(10) PRIMARY KEY,
    고객ID VARCHAR(10),
    주문일자 DATE
);

CREATE TABLE 주문상세 (
    주문ID VARCHAR(10),
    순번 INT,
    상품ID VARCHAR(10),
    수량 INT,
    PRIMARY KEY (주문ID, 순번),
    FOREIGN KEY (주문ID) REFERENCES 주문(주문ID) ON DELETE CASCADE
);
```

---

## ☁️ 데이터베이스 최신 트렌드

### 1. Cloud Database 🌐

#### AWS RDS (Relational Database Service)
```
지원 엔진
├─ MySQL / MariaDB
├─ PostgreSQL  
├─ Oracle
├─ SQL Server
└─ Aurora (AWS 자체 엔진)
```

**특징**
- **완전 관리형**: 백업, 패치, 모니터링 자동화
- **Multi-AZ**: 가용성 보장
- **Read Replica**: 읽기 성능 향상
- **Auto Scaling**: 자동 확장

#### Azure SQL Database
```
서비스 계층
├─ Basic: 개발/테스트용
├─ Standard: 일반 업무용
├─ Premium: 고성능 업무용
└─ Hyperscale: 대용량 데이터
```

#### Google Cloud SQL
- **자동 백업 및 복구**
- **고가용성 구성**
- **보안**: 암호화, VPC 지원
- **모니터링**: Cloud Monitoring 통합

### 2. Graph Database 🕸️

#### Neo4j
```cypher
-- 노드 생성
CREATE (고객:Customer {name: '김철수', age: 35})
CREATE (상품:Product {name: '노트북', price: 1500000})

-- 관계 생성  
CREATE (고객)-[:PURCHASED {date: '2024-03-15', quantity: 1}]->(상품)

-- 그래프 조회
MATCH (c:Customer)-[r:PURCHASED]->(p:Product)
WHERE c.age > 30
RETURN c.name, p.name, r.date
```

#### Amazon Neptune
- **다중 그래프 모델**: Property Graph, RDF
- **쿼리 언어**: Gremlin, SPARQL, openCypher
- **완전 관리형**: 자동 백업, 패치
- **고성능**: 읽기 전용 복제본 지원

### 3. Time-series Database ⏱️

#### InfluxDB
```sql
-- 데이터 삽입
INSERT sensor_data,device=sensor01,location=server_room temperature=23.5,humidity=45.2

-- 시계열 쿼리
SELECT MEAN("temperature") 
FROM "sensor_data" 
WHERE time >= now() - 1h 
GROUP BY time(10m)
```

**특징**
- **압축**: 시계열 데이터 특화 압축
- **보존 정책**: 자동 데이터 만료
- **Continuous Queries**: 실시간 집계
- **Grafana 연동**: 시각화 도구

#### TimescaleDB
- **PostgreSQL 확장**: SQL 호환성
- **Hypertables**: 자동 파티셔닝
- **압축**: 컬럼형 저장
- **연속 집계**: 실시간 집계 뷰

### 4. Vector Database (AI용) 🤖

#### Pinecone
```python
import pinecone

# 벡터 삽입
index.upsert(vectors=[
    ("doc1", [0.1, 0.2, 0.3, ...], {"text": "인공지능 기술"}),
    ("doc2", [0.4, 0.5, 0.6, ...], {"text": "머신러닝 알고리즘"})
])

# 유사도 검색
results = index.query(
    vector=[0.15, 0.25, 0.35, ...],
    top_k=10,
    include_metadata=True
)
```

#### Weaviate
```graphql
{
  Get {
    Article(
      nearText: {
        concepts: ["인공지능", "딥러닝"]
      }
      limit: 5
    ) {
      title
      content
      _additional {
        distance
      }
    }
  }
}
```

**사용 사례**
- **의미적 검색**: 자연어 쿼리
- **추천 시스템**: 콘텐츠 유사도
- **RAG**: 검색 증강 생성
- **이미지 검색**: 시각적 유사성

---

## 🛠️ 실습 예제: 통합 데이터 모델링

### 전자상거래 플랫폼 설계

#### 1. 개념적 모델
```
고객 ─구매→ 주문 ─포함→ 주문상세 ─참조→ 상품
 │              │                      │
 └─작성→ 리뷰 ──평가────────────────────┘
 
상품 ─속함→ 카테고리
상품 ─공급→ 판매자
```

#### 2. 논리적 모델 (3NF 적용)
```sql
고객 (고객ID*, 고객명, 이메일, 연락처, 가입일)
주문 (주문ID*, 고객ID, 주문일자, 총액, 배송상태)
상품 (상품ID*, 상품명, 단가, 카테고리ID, 판매자ID)
주문상세 (주문ID*, 상품ID*, 수량, 단가)
리뷰 (리뷰ID*, 고객ID, 상품ID, 평점, 내용, 작성일)
```

#### 3. 물리적 모델 (성능 최적화)
```sql
CREATE TABLE TB_ORDER (
    ORDER_ID VARCHAR(20) PRIMARY KEY,
    CUST_ID VARCHAR(10) NOT NULL,
    ORDER_DT DATE NOT NULL,
    TOTAL_AMT DECIMAL(12,2),
    STATUS VARCHAR(20),
    
    INDEX IDX_ORDER_CUST (CUST_ID),
    INDEX IDX_ORDER_DT (ORDER_DT)
) PARTITION BY RANGE (YEAR(ORDER_DT));
```

---

## 📚 참고 자료

- James Martin, "Information Engineering"
- Thomas Connolly, "Database Systems"
- 한국데이터베이스학회, 『데이터베이스 설계 및 구축』
- Neo4j Graph Database Manual
- InfluxData Documentation

---

**© 2024-2025 한국공학대학교 경영학부 | All Rights Reserved**