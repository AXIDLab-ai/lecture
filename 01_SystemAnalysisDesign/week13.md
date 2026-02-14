# Week 13: 시스템 구현 및 운영 🚀

> **한국공학대학교 | 시스템 분석 및 설계 | 강송희 교수**

---

## 📌 학습 목표

- ✅ SDLC 후반부 프로세스(구현, 테스트, 배포)의 체계적 수행 방법 습득
- ✅ 시스템 성능 지표와 비즈니스 KPI를 활용한 성과 측정 능력 개발
- ✅ DevOps 문화와 CI/CD 파이프라인 구축을 통한 효율적 개발 운영 이해
- ✅ 컨테이너화 기술과 모니터링 도구를 활용한 현대적 시스템 운영 기법 학습
- ✅ 체계적인 유지보수 전략과 SLA 관리를 통한 안정적 서비스 운영 역량 배양

---

## 🔧 SDLC 후반부 프로세스

### 1. 구현 (Implementation) 💻

#### 코딩 단계
```
개발 프로세스
├─ 상세 설계서 → 코드 변환
├─ 코딩 표준 준수
├─ 주석 및 문서화
└─ 코드 리뷰 (Peer Review)
```

**주요 활동**
- **모듈 개발**: 설계서 기반 프로그래밍
- **코딩 컨벤션**: 일관된 스타일 유지
- **버전 관리**: Git을 통한 소스 관리
- **코드 품질**: SonarQube 등 정적 분석

#### 빌드 프로세스
```bash
# 빌드 자동화 예시 (Maven)
mvn clean compile
mvn test
mvn package
mvn deploy
```

#### 단위 테스트 (Unit Testing)
```java
@Test
public void 주문금액계산_정상케이스() {
    // Given
    Order order = new Order();
    order.addItem("상품A", 10000, 2);
    
    // When
    int totalAmount = order.getTotalAmount();
    
    // Then
    assertEquals(20000, totalAmount);
}
```

### 2. 통합 테스트 (Integration Testing) 🔗

#### 통합 테스트 유형
- **Big Bang**: 모든 모듈 동시 통합
- **Top-Down**: 상위 모듈부터 점진적 통합
- **Bottom-Up**: 하위 모듈부터 점진적 통합
- **Sandwich**: Top-Down + Bottom-Up 조합

#### API 통합 테스트 예시
```javascript
describe('주문 API 통합 테스트', () => {
  test('주문 생성 → 결제 → 배송 프로세스', async () => {
    // 주문 생성
    const order = await createOrder(orderData);
    expect(order.status).toBe('CREATED');
    
    // 결제 처리
    const payment = await processPayment(order.id);
    expect(payment.status).toBe('COMPLETED');
    
    // 배송 시작
    const delivery = await startDelivery(order.id);
    expect(delivery.status).toBe('SHIPPED');
  });
});
```

### 3. 시스템 테스트 (System Testing) 🖥️

#### 테스트 유형별 수행
```
시스템 테스트 범위
├─ 기능 테스트 (Functional)
│  ├─ 사용자 시나리오 테스트
│  ├─ 업무 프로세스 테스트
│  └─ 인터페이스 테스트
│
└─ 비기능 테스트 (Non-Functional)
   ├─ 성능 테스트 (Performance)
   ├─ 부하 테스트 (Load)
   ├─ 보안 테스트 (Security)
   └─ 사용성 테스트 (Usability)
```

#### 성능 테스트 도구
- **JMeter**: 웹 애플리케이션 부하 테스트
- **k6**: 현대적 성능 테스트 도구
- **Gatling**: 고성능 부하 테스트

### 4. 배포 (Deployment) 🚀

#### Blue-Green 배포
```yaml
# Blue-Green 배포 전략
Current Production (Blue):
  - Version: 1.0
  - Traffic: 100%

New Version (Green):
  - Version: 2.0
  - Traffic: 0%

# 배포 후 즉시 전환
Switch Traffic: Blue (0%) → Green (100%)
```

#### Canary 배포
```yaml
# Canary 배포 단계
Phase 1: New Version → 5% Traffic
Phase 2: Monitor metrics → 25% Traffic  
Phase 3: Validation success → 100% Traffic
```

#### Rolling 배포
```yaml
# Rolling 업데이트 (Kubernetes)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 25%
      maxSurge: 25%
```

---

## 📊 KPI 및 성과 측정

### 1. 시스템 성능 지표 ⚡

#### 응답시간 (Response Time)
```
성능 목표 설정
├─ 웹 페이지 로딩: < 3초
├─ API 응답: < 500ms
├─ 데이터베이스 쿼리: < 100ms
└─ 파일 업로드: < 10초
```

#### 처리량 (Throughput)
- **TPS (Transactions Per Second)**: 초당 처리 건수
- **RPS (Requests Per Second)**: 초당 요청 수
- **동시 사용자**: Concurrent Users

#### 가용성 (Availability)
```
가용성 계산
Uptime / (Uptime + Downtime) × 100%

목표 수준
├─ 99.9% (연간 8.76시간 다운타임)
├─ 99.95% (연간 4.38시간 다운타임)  
└─ 99.99% (연간 52.56분 다운타임)
```

### 2. 비즈니스 KPI 💼

#### ROI (Return on Investment)
```
ROI 계산 공식
ROI = (이익 - 투자비용) / 투자비용 × 100%

측정 요소
├─ 개발 비용 절감
├─ 운영 효율성 향상  
├─ 매출 증대 효과
└─ 고객 만족도 개선
```

#### 사용자 만족도
- **NPS (Net Promoter Score)**: 고객 추천 의향
- **CSAT (Customer Satisfaction)**: 고객 만족도
- **CES (Customer Effort Score)**: 고객 노력도

#### 업무 효율성
```
효율성 지표
├─ 업무 처리 시간 단축 (%)
├─ 인력 투입 시간 절감 (시간)
├─ 오류 발생률 감소 (%)
└─ 자동화율 증가 (%)
```

---

## 🔄 DevOps 실무

### 1. CI/CD (Continuous Integration/Continuous Deployment) 🔁

#### CI/CD 파이프라인 구조
```
Development → Build → Test → Deploy → Monitor
     │           │       │       │        │
     ├─ Git      ├─ Maven ├─ Unit  ├─ Blue- ├─ Logging
     ├─ Branch   ├─ Docker├─ Integ.├─ Green ├─ Metrics
     └─ Commit   └─ Build └─ E2E   └─ Deploy└─ Alerts
```

#### GitHub Actions 예시
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup Java
      uses: actions/setup-java@v3
      with:
        java-version: '17'
    - name: Run Tests
      run: ./gradlew test
    
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to Production
      run: kubectl apply -f deployment.yaml
```

### 2. 자동화 파이프라인 도구 🛠️

#### Jenkins
```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t myapp:latest .'
                sh 'kubectl apply -f k8s/'
            }
        }
    }
    
    post {
        failure {
            emailext to: 'dev-team@company.com',
                     subject: 'Build Failed: ${env.JOB_NAME}',
                     body: 'Build failed. Please check the logs.'
        }
    }
}
```

#### GitLab CI
```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:
  stage: test
  script:
    - npm install
    - npm test
    - npm run e2e

deploy:
  stage: deploy
  script:
    - kubectl set image deployment/app app=$DOCKER_IMAGE
  only:
    - main
```

### 3. 컨테이너화 (Docker & Kubernetes) 📦

#### Docker 예시
```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install --only=production

COPY . .
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

CMD ["npm", "start"]
```

#### Kubernetes 배포
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: web-app:latest
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "200m"
```

### 4. 모니터링 도구 📈

#### Prometheus + Grafana
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'web-app'
    static_configs:
      - targets: ['web-app:3000']
```

#### ELK Stack (Elasticsearch, Logstash, Kibana)
```yaml
# logstash.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [fileset][module] == "nginx" {
    if [fileset][name] == "access" {
      grok {
        match => { "message" => "%{NGINXACCESS}" }
      }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
```

---

## 🛠️ 유지보수 및 시스템 운영

### 1. 유지보수 유형별 전략 🔧

#### 예방 유지보수 (Preventive)
- **정기 점검**: 시스템 성능 모니터링
- **보안 패치**: 정기적 보안 업데이트
- **백업 관리**: 데이터 백업 및 복구 테스트
- **용량 계획**: 리소스 사용률 분석

#### 적응 유지보수 (Adaptive)
- **환경 변화 대응**: OS, 미들웨어 업그레이드
- **법규 대응**: 개인정보보호법, 접근성 준수
- **기술 스택 업데이트**: 프레임워크 버전 업그레이드

#### 완전화 유지보수 (Perfective)
- **성능 개선**: 응답시간 최적화
- **기능 개선**: 사용성 향상
- **리팩토링**: 코드 품질 개선

#### 긴급 유지보수 (Corrective)
- **장애 대응**: 24/7 모니터링 및 즉시 대응
- **핫픽스**: 긴급 버그 수정
- **롤백**: 문제 발생 시 이전 버전 복구

### 2. SLA (Service Level Agreement) 📋

#### SLA 구성 요소
```
SLA 항목
├─ 가용성: 99.9% 이상
├─ 응답시간: 평균 2초 이하
├─ 처리량: 1,000 TPS 이상
├─ 복구시간: 장애 발생 시 30분 이내
└─ 데이터 백업: 일 1회 이상
```

#### SLA 모니터링
```yaml
# SLA 메트릭 예시
availability:
  target: 99.9%
  measurement: uptime_percentage
  period: monthly

response_time:
  target: "< 2000ms"
  percentile: 95th
  measurement: api_response_time

throughput:
  target: "> 1000 TPS"
  measurement: requests_per_second
  peak_hours: "09:00-18:00"
```

### 3. 인시던트 관리 🚨

#### 인시던트 대응 프로세스
```
인시던트 발생 → 탐지 → 분류 → 대응 → 해결 → 사후분석
     │           │      │      │      │      │
     ├─ 알림     ├─모니터├─우선 ├─팀    ├─복구  ├─포스트
     ├─ 로그     ├─대시  ├─순위 ├─배정  ├─검증  ├─모템
     └─ 사용자   └─보드  └─분류 └─대응  └─종료  └─개선
```

#### 우선순위 분류
```
Priority 1 (Critical): 서비스 완전 중단
├─ 대응 시간: 15분 이내
├─ 해결 목표: 1시간 이내
└─ 에스컬레이션: CTO 즉시 보고

Priority 2 (High): 주요 기능 장애
├─ 대응 시간: 30분 이내  
├─ 해결 목표: 4시간 이내
└─ 에스컬레이션: 개발팀장 보고

Priority 3 (Medium): 일부 기능 오류
├─ 대응 시간: 2시간 이내
├─ 해결 목표: 1일 이내
└─ 에스컬레이션: 일일 보고

Priority 4 (Low): 사소한 개선사항
├─ 대응 시간: 다음 영업일
├─ 해결 목표: 1주일 이내
└─ 에스컬레이션: 주간 보고
```

#### 인시던트 커뮤니케이션
```markdown
# 인시던트 보고서 템플릿

## 📋 인시던트 개요
- **발생 시간**: 2024-03-15 14:30:00 KST
- **영향 범위**: 전체 사용자 로그인 불가
- **우선순위**: P1 (Critical)
- **상태**: 해결 완료

## 🔍 원인 분석
- **근본 원인**: 데이터베이스 커넥션 풀 고갈
- **직접 원인**: 장시간 실행 쿼리로 인한 커넥션 점유

## 🛠️ 해결 조치
1. 커넥션 풀 크기 확대 (20 → 50)
2. 쿼리 타임아웃 설정 (30초)
3. 데이터베이스 인덱스 추가

## 📈 예방 조치
- 커넥션 풀 모니터링 알림 추가
- 쿼리 성능 정기 검토 프로세스 수립
- 부하 테스트 시나리오 개선
```

---

## 📚 참고 자료

- Martin Fowler, "Continuous Integration"
- Gene Kim, "The DevOps Handbook" 
- ITIL Foundation, "Service Operation"
- Kubernetes Documentation
- Prometheus Best Practices Guide

---

**© 2024-2025 한국공학대학교 경영학부 | All Rights Reserved**