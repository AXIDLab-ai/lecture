[← Week 9](./week9.html) · [목차](./lectureMap.html) · [다음: Week 11 →](./week11.html)

# Week 10: 시스템 요구사항 구조화 3 - 저장소 통합설계 및 질의 🗄️

---

## 📌 학습 목표

- ✅ RDBMS와 NoSQL 데이터베이스의 특징과 차이점 이해
- ✅ 데이터 저장소 선택을 위한 체계적 기준 습득
- ✅ ETL 프로세스를 통한 데이터 통합 방법론 학습
- ✅ SQL 기본 명령어 활용 능력 개발
- ✅ 현대적 데이터 아키텍처 설계 능력 배양

---

## 🔍 RDBMS vs NoSQL 비교

### RDBMS (Relational Database Management System) 📊

#### 특징
- **구조화된 데이터**: 테이블 기반 스키마
- **ACID 속성**: 트랜잭션 보장
- **SQL 표준**: 표준화된 질의 언어
- **정규화**: 데이터 중복 최소화

#### 장점 ✨
- **데이터 일관성 보장**
- **복잡한 쿼리 지원**
- **성숙한 생태계**
- **트랜잭션 처리**

#### 단점 ⚠️
- **수직적 확장만 가능**
- **스키마 변경 어려움**
- **대용량 데이터 처리 한계**

### NoSQL (Not Only SQL) 🌐

#### 특징
- **유연한 스키마**: 스키마리스 또는 동적 스키마
- **수평적 확장**: 분산 처리 지원
- **다양한 데이터 모델**: 문서, 키-값, 그래프 등
- **높은 성능**: 특정 용도 최적화

#### 장점 ✨
- **확장성**: 수평적 확장 용이
- **유연성**: 스키마 변경 자유
- **성능**: 특정 패턴에 최적화
- **비용 효율성**: 오픈소스 솔루션 다수

---

## 🗃️ NoSQL 데이터베이스 유형

### 1. Key-Value Store 🗝️

#### 특징
- **단순한 구조**: 키-값 쌍으로 저장
- **빠른 조회**: O(1) 시간 복잡도
- **캐싱**: 주로 캐시 용도로 활용

#### 대표 제품
- **Redis**: 인메모리 캐시
- **DynamoDB**: AWS 관리형 서비스
- **Riak**: 분산 키-값 저장소

#### 사용 사례
```
사용자 세션 관리
쇼핑카트 정보
실시간 추천 시스템
```

### 2. Document Database 📄

#### 특징
- **JSON/XML**: 문서 형태로 저장
- **중첩 구조**: 복합 데이터 표현
- **인덱싱**: 문서 내 필드 검색

#### 대표 제품
- **MongoDB**: 범용 문서 DB
- **CouchDB**: RESTful 인터페이스
- **Amazon DocumentDB**: MongoDB 호환

#### 사용 사례
```json
{
  "고객ID": "C001",
  "이름": "김철수",
  "주소": {
    "시": "서울",
    "구": "강남구"
  },
  "주문이력": [
    {"상품": "노트북", "날짜": "2024-03-15"},
    {"상품": "마우스", "날짜": "2024-03-20"}
  ]
}
```

### 3. Column-Family 📊

#### 특징
- **컬럼 지향**: 컬럼 단위 저장
- **압축**: 높은 압축률
- **분석**: OLAP 워크로드 최적화

#### 대표 제품
- **Cassandra**: 분산 컬럼 DB
- **HBase**: Hadoop 생태계
- **BigTable**: Google 클라우드

#### 사용 사례
```
시계열 데이터 (IoT 센서)
로그 데이터 분석
실시간 분석 대시보드
```

### 4. Graph Database 🕸️

#### 특징
- **그래프 구조**: 노드와 엣지
- **관계 중심**: 연결성 분석
- **순회**: 그래프 탐색 최적화

#### 대표 제품
- **Neo4j**: 네이티브 그래프 DB
- **Amazon Neptune**: 관리형 그래프 DB
- **ArangoDB**: 멀티모델 DB

#### 사용 사례
```
소셜 네트워크 분석
추천 시스템
사기 탐지
지식 그래프
```

---

## ⚖️ 데이터 저장소 선택 기준

### CAP 정리 🔺

#### Consistency (일관성) 🎯
- **정의**: 모든 노드가 동일한 데이터를 가짐
- **예시**: 은행 계좌 잔고

#### Availability (가용성) 🔄
- **정의**: 시스템이 항상 응답 가능
- **예시**: 웹 서비스 접근

#### Partition Tolerance (분단 내성) 🌐
- **정의**: 네트워크 분단 상황에서도 동작
- **예시**: 분산 시스템

#### CAP 선택 전략
```
CP (Consistency + Partition tolerance): MongoDB, Redis
AP (Availability + Partition tolerance): Cassandra, DynamoDB
CA (Consistency + Availability): MySQL, PostgreSQL (단일 노드)
```

### ACID vs BASE 🧪

#### ACID (RDBMS)
- **A**tomicity: 원자성
- **C**onsistency: 일관성  
- **I**solation: 격리성
- **D**urability: 지속성

#### BASE (NoSQL)
- **B**asically Available: 기본적 가용성
- **S**oft state: 유연한 상태
- **E**ventual consistency: 최종 일관성

### 선택 기준 매트릭스 📋

| 요구사항 | RDBMS | NoSQL |
|----------|-------|--------|
| **트랜잭션 보장** | ✅ | ❌/△ |
| **복잡한 쿼리** | ✅ | ❌ |
| **확장성** | ❌ | ✅ |
| **스키마 유연성** | ❌ | ✅ |
| **개발 속도** | △ | ✅ |
| **데이터 일관성** | ✅ | △ |

---

## 🔄 ETL (Extract, Transform, Load) 프로세스

### ETL 개념 및 필요성

#### 정의 📖
> **다양한 소스에서 데이터를 추출(Extract), 변환(Transform), 적재(Load)하는 프로세스**

#### 필요성 🎯
- **데이터 통합**: 이기종 시스템 연동
- **데이터 품질**: 정제 및 표준화
- **분석 준비**: 분석 가능한 형태로 변환

### ETL 단계별 상세

#### 1. Extract (추출) 📥
```
데이터 소스
├─ 관계형 DB (MySQL, PostgreSQL)
├─ NoSQL DB (MongoDB, Redis)  
├─ 파일 (CSV, JSON, XML)
├─ API (REST, GraphQL)
└─ 스트리밍 (Kafka, Kinesis)
```

#### 2. Transform (변환) 🔄
```
변환 작업
├─ 데이터 정제 (Null 처리, 중복 제거)
├─ 데이터 타입 변환 (문자 → 숫자)
├─ 데이터 표준화 (날짜 형식 통일)
├─ 계산 필드 추가 (총액 = 단가 × 수량)
├─ 데이터 검증 (범위, 형식 검사)
└─ 데이터 집계 (일별, 월별 합계)
```

#### 3. Load (적재) 📤
```
적재 방식
├─ Full Load (전체 적재)
├─ Incremental Load (증분 적재)
├─ Delta Load (변경분 적재)
└─ Upsert (삽입/업데이트)
```

### 현대적 ETL 도구 🛠️

#### 클라우드 기반
- **AWS Glue**: 서버리스 ETL
- **Azure Data Factory**: 마이크로소프트 ETL
- **Google Dataflow**: 구글 클라우드 ETL

#### 오픈소스
- **Apache Airflow**: 워크플로우 관리
- **Apache NiFi**: 데이터 플로우 자동화
- **Talend**: 데이터 통합 플랫폼

---

## 🏗️ 데이터 통합 아키텍처

### 전통적 아키텍처 📊

#### Data Warehouse
```
운영 시스템 → ETL → 데이터웨어하우스 → OLAP → 리포팅
```

#### 특징
- **배치 처리**: 정해진 시간에 일괄 처리
- **구조화**: 사전 정의된 스키마
- **OLAP**: 분석용 최적화

### 현대적 아키텍처 🚀

#### Data Lake
```
다양한 소스 → 원시 데이터 → 데이터 레이크 → 분석 도구
```

#### 특징
- **스키마 온 리드**: 읽을 때 스키마 적용
- **다양한 형태**: 정형/반정형/비정형 데이터
- **확장성**: 무제한 저장

#### Lambda Architecture
```
실시간 스트림 → 스트림 처리 → 서빙 레이어
배치 데이터 → 배치 처리 → 배치 뷰
```

---

## 💾 SQL 기초

### DDL (Data Definition Language) 🏗️

#### CREATE - 테이블 생성
```sql
CREATE TABLE 고객 (
    고객ID VARCHAR(10) PRIMARY KEY,
    고객명 VARCHAR(50) NOT NULL,
    연락처 VARCHAR(15),
    가입일 DATE DEFAULT CURRENT_DATE
);
```

#### ALTER - 테이블 수정
```sql
-- 컬럼 추가
ALTER TABLE 고객 ADD COLUMN 이메일 VARCHAR(100);

-- 컬럼 수정  
ALTER TABLE 고객 MODIFY COLUMN 연락처 VARCHAR(20);

-- 컬럼 삭제
ALTER TABLE 고객 DROP COLUMN 이메일;
```

#### DROP - 테이블 삭제
```sql
DROP TABLE 고객;
```

### DML (Data Manipulation Language) 📝

#### SELECT - 데이터 조회
```sql
-- 기본 조회
SELECT 고객명, 연락처 FROM 고객;

-- 조건부 조회
SELECT * FROM 고객 WHERE 가입일 >= '2024-01-01';

-- 정렬
SELECT * FROM 고객 ORDER BY 고객명 ASC;

-- 집계
SELECT COUNT(*), AVG(주문금액) 
FROM 주문 
WHERE 주문일자 >= '2024-01-01';
```

#### INSERT - 데이터 삽입
```sql
INSERT INTO 고객 (고객ID, 고객명, 연락처) 
VALUES ('C001', '김철수', '010-1234-5678');
```

#### UPDATE - 데이터 수정
```sql
UPDATE 고객 
SET 연락처 = '010-9876-5432' 
WHERE 고객ID = 'C001';
```

#### DELETE - 데이터 삭제
```sql
DELETE FROM 고객 WHERE 고객ID = 'C001';
```

### DCL (Data Control Language) 🔐

#### GRANT - 권한 부여
```sql
GRANT SELECT, INSERT ON 고객 TO '사용자1';
```

#### REVOKE - 권한 회수
```sql
REVOKE INSERT ON 고객 FROM '사용자1';
```

### TCL (Transaction Control Language) 🔄

#### COMMIT - 트랜잭션 확정
```sql
BEGIN TRANSACTION;
UPDATE 계좌 SET 잔고 = 잔고 - 10000 WHERE 계좌번호 = 'A001';
UPDATE 계좌 SET 잔고 = 잔고 + 10000 WHERE 계좌번호 = 'A002';
COMMIT;
```

#### ROLLBACK - 트랜잭션 취소
```sql
BEGIN TRANSACTION;
DELETE FROM 고객 WHERE 고객ID = 'C001';
ROLLBACK; -- 삭제 취소
```

---

## 🛠️ SQL 실습 예제

### 온라인 쇼핑몰 데이터베이스

#### 테이블 생성
```sql
-- 고객 테이블
CREATE TABLE Customer (
    CustomerID VARCHAR(10) PRIMARY KEY,
    CustomerName VARCHAR(50) NOT NULL,
    Email VARCHAR(100),
    Phone VARCHAR(15),
    JoinDate DATE
);

-- 상품 테이블  
CREATE TABLE Product (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2),
    Category VARCHAR(50)
);

-- 주문 테이블
CREATE TABLE OrderHeader (
    OrderID VARCHAR(10) PRIMARY KEY,
    CustomerID VARCHAR(10),
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
```

#### 복합 쿼리 예제
```sql
-- 월별 매출 현황
SELECT 
    DATE_FORMAT(OrderDate, '%Y-%m') AS 월,
    COUNT(*) AS 주문건수,
    SUM(TotalAmount) AS 총매출,
    AVG(TotalAmount) AS 평균주문금액
FROM OrderHeader 
WHERE OrderDate >= '2024-01-01'
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY 월;

-- 고객별 구매이력 및 등급
SELECT 
    c.CustomerName,
    COUNT(o.OrderID) AS 주문횟수,
    SUM(o.TotalAmount) AS 총구매금액,
    CASE 
        WHEN SUM(o.TotalAmount) >= 1000000 THEN 'VIP'
        WHEN SUM(o.TotalAmount) >= 500000 THEN 'GOLD'
        ELSE 'SILVER'
    END AS 고객등급
FROM Customer c
LEFT JOIN OrderHeader o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CustomerName
ORDER BY 총구매금액 DESC;
```

---

## 📚 참고 자료

- Ralph Kimball, "The Data Warehouse Toolkit"
- Martin Fowler, "NoSQL Distilled"
- 한국데이터베이스진흥원, 『데이터베이스 설계 및 구축』

---

**© 2024-2025 한국공학대학교 경영학부 | All Rights Reserved**
