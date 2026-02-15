# Week 9: 함수와 모듈

**[← Week 8](./week8.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 10 →](./week10.md)**

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **함수 정의와 호출**: 재사용 가능한 함수를 설계하고 효율적으로 활용합니다
2. **매개변수 완전 정복**: 기본값, 가변 인자(*args, **kwargs)를 자유자재로 다룹니다
3. **스코프 이해**: 지역 변수와 전역 변수의 차이점을 명확히 구분합니다
4. **고급 함수 기법**: 람다 함수, 재귀 함수, 내장 함수를 활용합니다
5. **모듈화 프로그래밍**: 코드를 체계적으로 분리하고 재사용성을 극대화합니다
6. **표준 라이브러리 활용**: math, random, datetime 등 핵심 모듈을 마스터합니다

---

## 📚 핵심 개념 요약

### 1. 함수(Function)란?
```
🎯 함수 = 특정 작업을 수행하는 재사용 가능한 코드 블록
🔄 입력(매개변수) → 처리 → 출력(반환값)
📦 코드의 모듈화와 재사용성 향상
🎪 def 키워드로 정의: def function_name(parameters):
```

### 2. 함수의 구조

```python
def function_name(parameter1, parameter2="기본값"):
    """독스트링: 함수 설명"""
    # 함수 본체
    result = parameter1 + parameter2
    return result  # 반환값 (선택적)
```

### 3. 매개변수 종류

| 종류 | 문법 | 설명 | 예시 |
|------|------|------|------|
| **위치 인자** | `def func(a, b):` | 순서대로 전달 | `func(1, 2)` |
| **키워드 인자** | `def func(a, b):` | 이름으로 전달 | `func(b=2, a=1)` |
| **기본값 인자** | `def func(a, b=10):` | 기본값 설정 | `func(1)` |
| **가변 위치 인자** | `def func(*args):` | 여러 개 위치 인자 | `func(1, 2, 3)` |
| **가변 키워드 인자** | `def func(**kwargs):` | 여러 개 키워드 인자 | `func(a=1, b=2)` |

### 4. 스코프(Scope) 규칙

| 스코프 | 범위 | 설명 | 예시 |
|--------|------|------|------|
| **Local** | 함수 내부 | 함수 안에서만 접근 가능 | `def func(): x = 10` |
| **Enclosing** | 중첩 함수 | 외부 함수에서 접근 가능 | 클로저 |
| **Global** | 모듈 전체 | 전역 변수 | `global x` |
| **Built-in** | 파이썬 내장 | 내장 함수들 | `print, len, max` |

### 5. 주요 내장 함수

| 함수 | 기능 | 예시 | 결과 |
|------|------|------|------|
| **len()** | 길이 반환 | `len([1,2,3])` | `3` |
| **max()** | 최댓값 | `max(1,2,3)` | `3` |
| **min()** | 최솟값 | `min(1,2,3)` | `1` |
| **sum()** | 합계 | `sum([1,2,3])` | `6` |
| **sorted()** | 정렬된 리스트 | `sorted([3,1,2])` | `[1,2,3]` |
| **map()** | 함수 적용 | `map(str, [1,2,3])` | `['1','2','3']` |
| **filter()** | 조건 필터링 | `filter(lambda x: x>0, [-1,1,2])` | `[1,2]` |

---

## 💻 실습 세션 (2시간)

### Part 1: 함수 기초 (30분)

#### 🎪 함수 정의와 호출

```python
print("🎪 함수 정의와 호출")
print("=" * 18)

# 1. 가장 간단한 함수
print("📝 기본 함수 정의")

def say_hello():
    """인사하는 함수"""
    print("안녕하세요!")

# 함수 호출
print("함수 호출 결과:")
say_hello()
say_hello()
say_hello()

print("=" * 30)

# 2. 매개변수가 있는 함수
print("📥 매개변수 함수")

def greet(name):
    """이름을 받아서 인사하는 함수"""
    print(f"안녕하세요, {name}님!")

def greet_with_time(name, time):
    """이름과 시간을 받아서 인사하는 함수"""
    print(f"{time}에 {name}님께 인사드립니다!")

# 함수 호출
print("매개변수 함수 호출:")
greet("김철수")
greet("이영희")
greet_with_time("박민수", "오전")
greet_with_time("최지원", "저녁")

print("=" * 30)

# 3. 반환값이 있는 함수
print("📤 반환값 함수")

def add(a, b):
    """두 수를 더하는 함수"""
    result = a + b
    return result

def multiply(a, b):
    """두 수를 곱하는 함수"""
    return a * b  # 바로 반환

def get_circle_area(radius):
    """원의 넓이를 계산하는 함수"""
    pi = 3.14159
    area = pi * radius * radius
    return area

# 반환값 사용
print("반환값 함수 사용:")
sum_result = add(10, 20)
print(f"10 + 20 = {sum_result}")

product = multiply(5, 6)
print(f"5 × 6 = {product}")

circle_area = get_circle_area(3)
print(f"반지름 3인 원의 넓이: {circle_area:.2f}")

# 반환값으로 계산 연속하기
final_result = multiply(add(2, 3), add(4, 6))
print(f"(2+3) × (4+6) = {final_result}")

print("=" * 30)

# 4. 여러 값을 반환하는 함수
print("📦 다중 반환값 함수")

def get_name_age():
    """이름과 나이를 반환하는 함수"""
    return "김철수", 25

def divide_with_remainder(a, b):
    """나눗셈의 몫과 나머지를 반환"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

def get_statistics(numbers):
    """숫자 리스트의 통계를 반환"""
    if not numbers:
        return 0, 0, 0, 0
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum

# 다중 반환값 사용
print("다중 반환값 사용:")
name, age = get_name_age()
print(f"이름: {name}, 나이: {age}")

q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = 몫 {q}, 나머지 {r}")

# 튜플로도 받을 수 있음
result_tuple = divide_with_remainder(23, 7)
print(f"23 ÷ 7 결과 튜플: {result_tuple}")

# 통계 예제
scores = [85, 92, 78, 96, 88, 73, 91]
total, avg, max_score, min_score = get_statistics(scores)
print(f"점수 통계:")
print(f"  총합: {total}")
print(f"  평균: {avg:.1f}")
print(f"  최고: {max_score}")
print(f"  최저: {min_score}")

print("=" * 30)

# 5. 독스트링(Docstring)과 함수 정보
print("📖 독스트링과 함수 정보")

def calculate_bmi(weight, height):
    """
    BMI(Body Mass Index)를 계산하는 함수
    
    매개변수:
        weight (float): 체중(kg)
        height (float): 키(m)
    
    반환값:
        float: BMI 값
        str: BMI 분류
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "저체중"
    elif bmi < 25:
        category = "정상"
    elif bmi < 30:
        category = "과체중"
    else:
        category = "비만"
    
    return bmi, category

# 함수 정보 확인
print("함수 정보:")
print(f"함수명: {calculate_bmi.__name__}")
print(f"독스트링: {calculate_bmi.__doc__}")

# BMI 계산 사용
weight = 70
height = 1.75
bmi_value, bmi_category = calculate_bmi(weight, height)
print(f"\nBMI 계산 결과:")
print(f"체중: {weight}kg, 키: {height}m")
print(f"BMI: {bmi_value:.1f} ({bmi_category})")

print("=" * 30)

# 6. 실생활 함수 예제
print("🏠 실생활 함수 예제")

def calculate_monthly_payment(principal, annual_rate, years):
    """월 대출 상환금을 계산하는 함수"""
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    
    if monthly_rate == 0:
        return principal / num_payments
    
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
                     ((1 + monthly_rate)**num_payments - 1)
    
    return monthly_payment

def convert_temperature(temp, from_unit, to_unit):
    """온도 단위를 변환하는 함수"""
    # 먼저 섭씨로 변환
    if from_unit == "F":  # 화씨 → 섭씨
        celsius = (temp - 32) * 5/9
    elif from_unit == "K":  # 켈빈 → 섭씨
        celsius = temp - 273.15
    else:  # 이미 섭씨
        celsius = temp
    
    # 목표 단위로 변환
    if to_unit == "F":  # 섭씨 → 화씨
        return celsius * 9/5 + 32
    elif to_unit == "K":  # 섭씨 → 켈빈
        return celsius + 273.15
    else:  # 섭씨 그대로
        return celsius

def format_currency(amount):
    """금액을 화폐 형식으로 포맷팅"""
    return f"{amount:,.0f}원"

# 실생활 함수 사용
print("💰 대출 계산기:")
loan_amount = 300000000  # 3억원
interest_rate = 3.5      # 연 3.5%
loan_years = 30          # 30년

monthly_pay = calculate_monthly_payment(loan_amount, interest_rate, loan_years)
print(f"대출금액: {format_currency(loan_amount)}")
print(f"연이율: {interest_rate}%")
print(f"대출기간: {loan_years}년")
print(f"월 상환금: {format_currency(monthly_pay)}")

print(f"\n🌡️ 온도 변환기:")
temperatures = [
    (25, "C", "F"),   # 섭씨 → 화씨
    (77, "F", "C"),   # 화씨 → 섭씨
    (300, "K", "C"),  # 켈빈 → 섭씨
    (0, "C", "K")     # 섭씨 → 켈빈
]

for temp, from_u, to_u in temperatures:
    converted = convert_temperature(temp, from_u, to_u)
    print(f"{temp}°{from_u} = {converted:.1f}°{to_u}")

print("=" * 30)

# 7. 함수 호출 방법들
print("📞 함수 호출 방법들")

def introduce(name, age, city, job="무직"):
    """자기소개 함수"""
    return f"안녕하세요! {name}이고, {age}살이며, {city}에 살고 있습니다. 직업은 {job}입니다."

# 위치 인자로 호출
print("위치 인자 호출:")
intro1 = introduce("김철수", 25, "서울", "개발자")
print(intro1)

# 키워드 인자로 호출
print("\n키워드 인자 호출:")
intro2 = introduce(name="이영희", age=30, city="부산", job="디자이너")
print(intro2)

# 혼합 호출 (위치 인자 먼저, 그 다음 키워드 인자)
print("\n혼합 호출:")
intro3 = introduce("박민수", 28, city="대구", job="선생님")
print(intro3)

# 기본값 활용
print("\n기본값 활용:")
intro4 = introduce("최지원", 22, "인천")  # job 생략
print(intro4)

print("=" * 30)

# 8. 함수 변수와 고차 함수 맛보기
print("🎭 함수를 변수에 저장")

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

# 함수를 변수에 저장
operation = add_numbers
result = operation(10, 5)
print(f"add_numbers를 변수에 저장: {result}")

# 함수들을 딕셔너리에 저장
operations = {
    "더하기": add_numbers,
    "곱하기": multiply_numbers,
    "빼기": subtract_numbers
}

print(f"\n계산기 시뮬레이션:")
for op_name, op_func in operations.items():
    result = op_func(12, 4)
    print(f"{op_name}: 12와 4 → {result}")

# 함수 리스트로 연속 적용
functions = [add_numbers, multiply_numbers, subtract_numbers]
x, y = 8, 3

print(f"\n{x}와 {y}에 함수들 적용:")
for i, func in enumerate(functions):
    result = func(x, y)
    print(f"함수 {i+1}: {func.__name__}({x}, {y}) = {result}")
```

#### 🎯 매개변수와 인자

```python
print("🎯 매개변수와 인자")
print("=" * 16)

# 1. 기본값 매개변수
print("⚙️ 기본값 매개변수")

def create_profile(name, age, city="서울", job="학생", hobby="독서"):
    """프로필을 생성하는 함수 (기본값 있음)"""
    profile = {
        "이름": name,
        "나이": age,
        "도시": city,
        "직업": job,
        "취미": hobby
    }
    return profile

# 다양한 방식으로 호출
print("다양한 호출 방식:")

# 필수 인자만 제공
profile1 = create_profile("김철수", 25)
print(f"기본값 사용: {profile1}")

# 일부 기본값 변경
profile2 = create_profile("이영희", 30, job="개발자")
print(f"일부 변경: {profile2}")

# 모든 값 제공
profile3 = create_profile("박민수", 28, "부산", "디자이너", "여행")
print(f"모든 값 제공: {profile3}")

# 키워드 인자로 순서 바꾸기
profile4 = create_profile("최지원", 22, hobby="영화감상", city="대구")
print(f"순서 변경: {profile4}")

print("=" * 30)

# 2. 매개변수 순서 규칙
print("📋 매개변수 순서 규칙")

def function_parameters_demo(required, default_param="기본값", *args, **kwargs):
    """매개변수 순서를 보여주는 함수"""
    print(f"필수 인자: {required}")
    print(f"기본값 인자: {default_param}")
    print(f"가변 위치 인자 (*args): {args}")
    print(f"가변 키워드 인자 (**kwargs): {kwargs}")
    print("-" * 30)

# 다양한 호출 테스트
print("매개변수 순서 테스트:")

function_parameters_demo("필수값")

function_parameters_demo("필수값", "변경된기본값")

function_parameters_demo("필수값", "변경된기본값", 1, 2, 3)

function_parameters_demo("필수값", "변경된기본값", 1, 2, 3, extra1="추가1", extra2="추가2")

function_parameters_demo("필수값", extra="추가정보", bonus=100)

print("=" * 30)

# 3. 실용적인 기본값 예제
print("🛠️ 실용적인 기본값 예제")

def send_email(to_address, subject, body, from_address="admin@company.com", 
               priority="normal", send_copy=True):
    """이메일 발송 함수 (실제로는 발송하지 않고 출력만)"""
    print("📧 이메일 발송 정보:")
    print(f"  받는이: {to_address}")
    print(f"  보내는이: {from_address}")
    print(f"  제목: {subject}")
    print(f"  내용: {body}")
    print(f"  우선순위: {priority}")
    print(f"  사본 보관: {send_copy}")
    print("  상태: 발송 완료")
    print()

def create_user_account(username, email, password, role="user", 
                       is_active=True, send_welcome=True):
    """사용자 계정 생성 함수"""
    account = {
        "사용자명": username,
        "이메일": email,
        "비밀번호": "*" * len(password),  # 보안상 마스킹
        "역할": role,
        "활성화": is_active,
        "환영 메일 발송": send_welcome
    }
    return account

# 이메일 발송 예제
print("이메일 발송 예제:")
send_email("user@example.com", "회의 안내", "내일 오후 2시에 회의가 있습니다.")

send_email("vip@example.com", "긴급 공지", "시스템 점검 안내", priority="high")

send_email("team@example.com", "프로젝트 업데이트", "진행 상황 공유", 
          from_address="manager@company.com", send_copy=False)

# 계정 생성 예제
print("계정 생성 예제:")
user1 = create_user_account("john_doe", "john@email.com", "secret123")
print(f"일반 사용자: {user1}")

admin = create_user_account("admin", "admin@company.com", "admin_pass", 
                           role="administrator", send_welcome=False)
print(f"관리자 계정: {admin}")

print("=" * 30)

# 4. 기본값의 함정 - 가변 객체
print("⚠️ 기본값의 함정 - 가변 객체")

# 잘못된 예제 (위험!)
def bad_function(value, my_list=[]):
    """기본값으로 가변 객체를 사용하는 잘못된 예제"""
    my_list.append(value)
    return my_list

# 문제 확인
print("잘못된 기본값 사용:")
result1 = bad_function(1)
print(f"첫 번째 호출: {result1}")

result2 = bad_function(2)
print(f"두 번째 호출: {result2}")  # 이전 값이 남아있음!

result3 = bad_function(3)
print(f"세 번째 호출: {result3}")  # 계속 누적됨!

print("같은 리스트 객체인지 확인:", result1 is result2 is result3)

# 올바른 방법
def good_function(value, my_list=None):
    """기본값 문제를 해결한 올바른 예제"""
    if my_list is None:
        my_list = []  # 매번 새로운 리스트 생성
    my_list.append(value)
    return my_list

print("\n올바른 기본값 사용:")
result4 = good_function(1)
print(f"첫 번째 호출: {result4}")

result5 = good_function(2)
print(f"두 번째 호출: {result5}")  # 독립적인 리스트

result6 = good_function(3)
print(f"세 번째 호출: {result6}")  # 각각 독립적

print("다른 리스트 객체인지 확인:", result4 is result5 is result6)

print("=" * 30)

# 5. 매개변수 언패킹
print("📦 매개변수 언패킹")

def calculate_total(price, tax_rate, discount=0, shipping=0):
    """총 비용을 계산하는 함수"""
    discounted_price = price * (1 - discount)
    tax_amount = discounted_price * tax_rate
    total = discounted_price + tax_amount + shipping
    
    return {
        "원가": price,
        "할인가": discounted_price,
        "세금": tax_amount,
        "배송비": shipping,
        "총액": total
    }

# 리스트/튜플 언패킹
print("리스트/튜플 언패킹:")
order_info = [50000, 0.1]  # 가격, 세율
result = calculate_total(*order_info, discount=0.1, shipping=3000)
print(f"주문 계산 (언패킹): {result}")

# 딕셔너리 언패킹
order_details = {
    "price": 80000,
    "tax_rate": 0.1,
    "discount": 0.15,
    "shipping": 5000
}

result2 = calculate_total(**order_details)
print(f"주문 계산 (딕셔너리 언패킹): {result2}")

# 복합 언패킹
basic_info = [100000, 0.1]  # 위치 인자
extra_info = {"discount": 0.2, "shipping": 2500}  # 키워드 인자

result3 = calculate_total(*basic_info, **extra_info)
print(f"복합 언패킹: {result3}")

print("=" * 30)

# 6. 타입 힌트 (Python 3.5+)
print("🏷️ 타입 힌트")

def calculate_interest(principal: float, rate: float, time: float) -> float:
    """
    단리 이자를 계산하는 함수
    
    Args:
        principal: 원금
        rate: 연 이율 (소수점 형태, 예: 0.05 = 5%)
        time: 기간 (년)
    
    Returns:
        float: 이자 금액
    """
    interest = principal * rate * time
    return interest

def format_person_info(name: str, age: int, scores: list = None) -> dict:
    """
    개인 정보를 포맷팅하는 함수
    
    Args:
        name: 이름
        age: 나이
        scores: 점수 리스트 (선택적)
    
    Returns:
        dict: 포맷된 개인 정보
    """
    if scores is None:
        scores = []
    
    avg_score = sum(scores) / len(scores) if scores else 0
    
    return {
        "name": name,
        "age": age,
        "scores": scores,
        "average": avg_score
    }

# 타입 힌트 함수 사용
print("타입 힌트 함수 사용:")
interest = calculate_interest(1000000, 0.035, 2)
print(f"원금 100만원, 연 3.5%, 2년 이자: {interest:,.0f}원")

person_info = format_person_info("김철수", 25, [85, 90, 88, 92])
print(f"개인 정보: {person_info}")

# 타입 힌트는 강제가 아님 - 잘못된 타입도 동작
wrong_usage = calculate_interest("100만원", "3.5%", "2년")  # 문자열로 호출
print(f"잘못된 타입 사용 (동작하지 않음): {wrong_usage}")

print("=" * 30)

# 7. 실전 예제 - 주문 처리 시스템
print("🛍️ 주문 처리 시스템")

def process_order(customer_id, items, payment_method="card", 
                 delivery_address=None, express_delivery=False, 
                 gift_wrap=False, message=""):
    """주문을 처리하는 함수"""
    
    # 기본 배송지 설정
    if delivery_address is None:
        delivery_address = "고객 등록 주소"
    
    # 주문 총액 계산
    total_amount = 0
    item_details = []
    
    for item in items:
        name = item["name"]
        price = item["price"]
        quantity = item.get("quantity", 1)
        
        item_total = price * quantity
        total_amount += item_total
        
        item_details.append({
            "상품명": name,
            "단가": price,
            "수량": quantity,
            "소계": item_total
        })
    
    # 추가 비용 계산
    delivery_fee = 5000 if express_delivery else 2500
    gift_wrap_fee = 3000 if gift_wrap else 0
    
    final_amount = total_amount + delivery_fee + gift_wrap_fee
    
    # 주문 정보 생성
    order = {
        "고객ID": customer_id,
        "상품목록": item_details,
        "상품금액": total_amount,
        "배송비": delivery_fee,
        "포장비": gift_wrap_fee,
        "총결제금액": final_amount,
        "결제방법": payment_method,
        "배송주소": delivery_address,
        "특급배송": express_delivery,
        "선물포장": gift_wrap,
        "메시지": message if message else "없음"
    }
    
    return order

# 주문 처리 예제
print("주문 처리 예제:")

# 기본 주문
items1 = [
    {"name": "노트북", "price": 1200000, "quantity": 1},
    {"name": "마우스", "price": 50000, "quantity": 2}
]

order1 = process_order("CUST001", items1)
print(f"\n기본 주문:")
for key, value in order1.items():
    if key != "상품목록":
        print(f"  {key}: {value}")

print(f"  상품목록:")
for item in order1["상품목록"]:
    print(f"    - {item['상품명']}: {item['단가']:,}원 × {item['수량']}개 = {item['소계']:,}원")

# 프리미엄 주문
items2 = [
    {"name": "아이폰", "price": 1300000, "quantity": 1}
]

order2 = process_order(
    customer_id="CUST002",
    items=items2,
    payment_method="cash",
    delivery_address="서울시 강남구 테헤란로 123",
    express_delivery=True,
    gift_wrap=True,
    message="생일 축하합니다!"
)

print(f"\n프리미엄 주문:")
for key, value in order2.items():
    if key != "상품목록":
        print(f"  {key}: {value}")
```

---

### Part 2: 고급 함수 (40분)

#### 🔀 가변 인자 (*args, **kwargs)

```python
print("🔀 가변 인자 (*args, **kwargs)")
print("=" * 30)

# 1. *args - 가변 위치 인자
print("📍 *args - 가변 위치 인자")

def sum_all(*args):
    """모든 인자를 더하는 함수"""
    print(f"받은 인자들: {args}")
    print(f"인자 타입: {type(args)}")
    
    total = 0
    for num in args:
        total += num
    return total

# *args 사용 예제
print("*args 사용:")
result1 = sum_all(1, 2, 3)
print(f"sum_all(1, 2, 3) = {result1}")

result2 = sum_all(10, 20, 30, 40, 50)
print(f"sum_all(10, 20, 30, 40, 50) = {result2}")

result3 = sum_all()  # 인자가 없어도 됨
print(f"sum_all() = {result3}")

# 더 복잡한 예제
def calculate_average(*numbers):
    """평균을 계산하는 함수"""
    if not numbers:
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    print(f"숫자들: {numbers}")
    print(f"총합: {total}, 개수: {count}, 평균: {average:.2f}")
    return average

print(f"\n평균 계산:")
calculate_average(85, 92, 78, 96, 88)
calculate_average(100, 95, 90)

print("=" * 30)

# 2. **kwargs - 가변 키워드 인자
print("🗝️ **kwargs - 가변 키워드 인자")

def print_info(**kwargs):
    """키워드 인자들을 출력하는 함수"""
    print(f"받은 키워드 인자들: {kwargs}")
    print(f"인자 타입: {type(kwargs)}")
    
    print("상세 정보:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# **kwargs 사용 예제
print("**kwargs 사용:")
print_info(name="김철수", age=25, city="서울")
print()
print_info(product="노트북", price=1200000, brand="삼성", warranty=2)
print()
print_info(title="파이썬 프로그래밍")

print("=" * 30)

# 3. 일반 매개변수 + *args + **kwargs
print("🎯 복합 매개변수")

def flexible_function(required_param, default_param="기본값", *args, **kwargs):
    """모든 종류의 매개변수를 받는 함수"""
    print(f"필수 매개변수: {required_param}")
    print(f"기본값 매개변수: {default_param}")
    print(f"가변 위치 인자 (*args): {args}")
    print(f"가변 키워드 인자 (**kwargs): {kwargs}")
    print("-" * 40)

# 복합 매개변수 테스트
print("복합 매개변수 사용:")
flexible_function("필수값")

flexible_function("필수값", "변경된기본값")

flexible_function("필수값", "변경된기본값", 1, 2, 3)

flexible_function("필수값", "변경된기본값", 1, 2, 3, extra="추가", bonus=100)

flexible_function("필수값", option="옵션", debug=True)

print("=" * 30)

# 4. 실용적인 로그 함수
print("📝 실용적인 로그 함수")

def log_message(level, message, *details, **metadata):
    """로그 메시지를 출력하는 함수"""
    import datetime
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 기본 로그 출력
    print(f"[{current_time}] {level.upper()}: {message}")
    
    # 추가 상세 정보
    if details:
        print(f"  세부사항: {', '.join(map(str, details))}")
    
    # 메타데이터
    if metadata:
        print(f"  메타데이터:")
        for key, value in metadata.items():
            print(f"    {key}: {value}")
    
    print()

# 로그 함수 사용
print("로그 함수 사용:")
log_message("info", "사용자 로그인 성공")

log_message("warning", "메모리 사용량 높음", "80% 사용 중", "임계치 도달", 
           user="admin", memory_usage="80%", server="web-01")

log_message("error", "데이터베이스 연결 실패", error_code=500, 
           database="main_db", attempt=3)

print("=" * 30)

# 5. 데코레이터 스타일 함수 (심화)
print("🎭 데코레이터 스타일 함수")

def make_multiplier(*factors):
    """곱셈 함수를 만드는 함수"""
    def multiply(number):
        result = number
        for factor in factors:
            result *= factor
        return result
    
    return multiply

def create_formatter(**format_options):
    """포맷터 함수를 만드는 함수"""
    def format_text(text):
        formatted = str(text)
        
        if format_options.get("upper"):
            formatted = formatted.upper()
        elif format_options.get("lower"):
            formatted = formatted.lower()
            
        if format_options.get("prefix"):
            formatted = format_options["prefix"] + formatted
            
        if format_options.get("suffix"):
            formatted = formatted + format_options["suffix"]
            
        if format_options.get("center"):
            width = format_options.get("width", 20)
            formatted = formatted.center(width)
            
        return formatted
    
    return format_text

# 고급 함수 사용
print("고급 함수 사용:")

# 곱셈 함수 생성
double = make_multiplier(2)
triple = make_multiplier(3)
double_and_half = make_multiplier(2, 0.5)  # 2를 곱하고 0.5를 곱함 (결과적으로 동일)

print(f"double(5) = {double(5)}")
print(f"triple(4) = {triple(4)}")
print(f"double_and_half(10) = {double_and_half(10)}")

# 포맷터 생성
title_formatter = create_formatter(upper=True, prefix=">>> ", suffix=" <<<")
subtitle_formatter = create_formatter(center=True, width=30)
code_formatter = create_formatter(prefix="CODE: ", suffix=";")

text = "Hello World"
print(f"\n원본: '{text}'")
print(f"제목 형식: '{title_formatter(text)}'")
print(f"부제목 형식: '{subtitle_formatter(text)}'")
print(f"코드 형식: '{code_formatter(text)}'")

print("=" * 30)

# 6. 실전 예제 - 설정 시스템
print("⚙️ 설정 시스템")

class ConfigManager:
    """설정 관리 클래스 (클래스는 다음 주에 배우지만 미리 맛보기)"""
    
    def __init__(self):
        self.config = {}
    
    def set_config(self, **settings):
        """설정값들을 업데이트"""
        self.config.update(settings)
        print(f"설정 업데이트: {settings}")
    
    def get_config(self, *keys):
        """여러 설정값을 한번에 가져오기"""
        if not keys:
            return self.config.copy()
        
        result = {}
        for key in keys:
            result[key] = self.config.get(key)
        return result
    
    def apply_defaults(self, **defaults):
        """기본값 적용 (기존 값은 유지)"""
        for key, value in defaults.items():
            if key not in self.config:
                self.config[key] = value
        print(f"기본값 적용 완료")

# 일반 함수로도 구현
def manage_settings(action, settings_dict=None, **kwargs):
    """설정 관리 함수"""
    if not hasattr(manage_settings, 'settings'):
        manage_settings.settings = {}
    
    if action == "set":
        if settings_dict:
            manage_settings.settings.update(settings_dict)
        manage_settings.settings.update(kwargs)
        print(f"설정 저장: {dict(manage_settings.settings)}")
        
    elif action == "get":
        return manage_settings.settings.copy()
        
    elif action == "clear":
        manage_settings.settings.clear()
        print("모든 설정 삭제")

# 설정 시스템 사용
print("설정 시스템 사용:")

# 함수 방식
manage_settings("set", database_host="localhost", database_port=5432)
manage_settings("set", api_key="secret123", debug=True, max_connections=100)

current_settings = manage_settings("get")
print(f"현재 설정: {current_settings}")

manage_settings("clear")

print("=" * 30)

# 7. args와 kwargs 전달하기
print("🔄 args와 kwargs 전달하기")

def wrapper_function(func, *args, **kwargs):
    """다른 함수를 래핑하는 함수"""
    print(f"함수 '{func.__name__}' 호출 시작")
    print(f"위치 인자: {args}")
    print(f"키워드 인자: {kwargs}")
    
    try:
        result = func(*args, **kwargs)
        print(f"함수 '{func.__name__}' 호출 성공")
        return result
    except Exception as e:
        print(f"함수 '{func.__name__}' 호출 실패: {e}")
        return None

def add_three_numbers(a, b, c):
    """세 수를 더하는 함수"""
    return a + b + c

def greet_person(name, age, city="서울"):
    """인사하는 함수"""
    return f"안녕하세요! {name}님 ({age}세, {city})"

# 래퍼 함수 사용
print("래퍼 함수 사용:")
result1 = wrapper_function(add_three_numbers, 10, 20, 30)
print(f"결과: {result1}\n")

result2 = wrapper_function(greet_person, "김철수", 25, city="부산")
print(f"결과: {result2}\n")

# 에러 상황
result3 = wrapper_function(add_three_numbers, 10, 20)  # 인자 부족
print(f"결과: {result3}\n")
```

#### 🌟 람다 함수

```python
print("🌟 람다 함수")
print("=" * 12)

# 1. 람다 함수 기본
print("⚡ 람다 함수 기본")

# 일반 함수와 람다 함수 비교
def normal_square(x):
    return x ** 2

lambda_square = lambda x: x ** 2

print("일반 함수 vs 람다 함수:")
print(f"normal_square(5) = {normal_square(5)}")
print(f"lambda_square(5) = {lambda_square(5)}")

# 여러 매개변수 람다
add = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(f"\n람다 함수 예제:")
print(f"add(3, 4) = {add(3, 4)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

# 조건부 람다
max_of_two = lambda x, y: x if x > y else y
is_even = lambda n: n % 2 == 0

print(f"max_of_two(10, 7) = {max_of_two(10, 7)}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(5) = {is_even(5)}")

print("=" * 30)

# 2. map() 함수와 람다
print("🗺️ map() 함수와 람다")

numbers = [1, 2, 3, 4, 5]
print(f"원본 리스트: {numbers}")

# 제곱 계산
squares = list(map(lambda x: x ** 2, numbers))
print(f"제곱: {squares}")

# 화씨를 섭씨로 변환
fahrenheit_temps = [32, 68, 86, 104, 122]
celsius_temps = list(map(lambda f: (f - 32) * 5/9, fahrenheit_temps))

print(f"\n온도 변환:")
for f, c in zip(fahrenheit_temps, celsius_temps):
    print(f"{f}°F = {c:.1f}°C")

# 문자열 처리
words = ["python", "java", "javascript", "c++"]
capitalized = list(map(lambda s: s.capitalize(), words))
lengths = list(map(lambda s: len(s), words))

print(f"\n문자열 처리:")
print(f"원본: {words}")
print(f"대문자화: {capitalized}")
print(f"길이: {lengths}")

print("=" * 30)

# 3. filter() 함수와 람다
print("🔍 filter() 함수와 람다")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 숫자: {numbers}")

# 짝수 필터링
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수: {even_numbers}")

# 5보다 큰 수 필터링
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수: {greater_than_5}")

# 문자열 필터링
words = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\n과일 이름: {words}")

# 5글자 이상 필터링
long_words = list(filter(lambda w: len(w) >= 5, words))
print(f"5글자 이상: {long_words}")

# 'a'로 시작하는 단어
a_words = list(filter(lambda w: w.startswith('a'), words))
print(f"'a'로 시작: {a_words}")

# 점수 필터링 예제
students = [
    {"name": "김철수", "score": 85},
    {"name": "이영희", "score": 92},
    {"name": "박민수", "score": 78},
    {"name": "최지원", "score": 96},
    {"name": "정수진", "score": 88}
]

print(f"\n학생 성적:")
for student in students:
    print(f"  {student['name']}: {student['score']}점")

# 90점 이상 학생
high_scores = list(filter(lambda s: s["score"] >= 90, students))
print(f"\n90점 이상 학생:")
for student in high_scores:
    print(f"  {student['name']}: {student['score']}점")

print("=" * 30)

# 4. sorted() 함수와 람다
print("📊 sorted() 함수와 람다")

# 숫자 정렬
numbers = [5, 2, 8, 1, 9, 3]
print(f"원본 숫자: {numbers}")

# 기본 정렬
normal_sort = sorted(numbers)
print(f"오름차순: {normal_sort}")

# 내림차순 (람다 사용)
reverse_sort = sorted(numbers, key=lambda x: -x)
print(f"내림차순 (람다): {reverse_sort}")

# 문자열 정렬
words = ["Python", "java", "C++", "JavaScript", "go"]
print(f"\n프로그래밍 언어: {words}")

# 길이로 정렬
by_length = sorted(words, key=lambda w: len(w))
print(f"길이로 정렬: {by_length}")

# 소문자로 변환 후 정렬
by_lower = sorted(words, key=lambda w: w.lower())
print(f"대소문자 무시 정렬: {by_lower}")

# 딕셔너리 정렬
products = [
    {"name": "노트북", "price": 1200000},
    {"name": "마우스", "price": 50000},
    {"name": "키보드", "price": 150000},
    {"name": "모니터", "price": 300000}
]

print(f"\n상품 목록:")
for product in products:
    print(f"  {product['name']}: {product['price']:,}원")

# 가격으로 정렬
by_price = sorted(products, key=lambda p: p["price"])
print(f"\n가격순 정렬:")
for product in by_price:
    print(f"  {product['name']}: {product['price']:,}원")

# 이름으로 정렬
by_name = sorted(products, key=lambda p: p["name"])
print(f"\n이름순 정렬:")
for product in by_name:
    print(f"  {product['name']}: {product['price']:,}원")

print("=" * 30)

# 5. 복잡한 람다 활용
print("🧩 복잡한 람다 활용")

# 리스트 컴프리헨션과 람다 조합
numbers = range(1, 11)
print(f"숫자 범위: {list(numbers)}")

# 조건부 변환
transformed = [(lambda x: x**2 if x % 2 == 0 else x**3)(n) for n in numbers]
print(f"짝수는 제곱, 홀수는 세제곱: {transformed}")

# 문자열 처리
sentences = [
    "Hello World",
    "Python Programming",
    "Lambda Functions",
    "Data Processing"
]

print(f"\n문장들: {sentences}")

# 첫 글자와 단어 수
sentence_info = list(map(lambda s: {
    "sentence": s,
    "first_char": s[0],
    "word_count": len(s.split()),
    "length": len(s)
}, sentences))

print(f"\n문장 분석:")
for info in sentence_info:
    print(f"  '{info['sentence']}': 첫글자={info['first_char']}, "
          f"단어수={info['word_count']}, 길이={info['length']}")

# 중첩 리스트 처리
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\n행렬: {matrix}")

# 각 행의 합계
row_sums = list(map(lambda row: sum(row), matrix))
print(f"행별 합계: {row_sums}")

# 모든 원소에 2 곱하기
doubled_matrix = list(map(lambda row: list(map(lambda x: x * 2, row)), matrix))
print(f"모든 원소 × 2: {doubled_matrix}")

print("=" * 30)

# 6. 실전 예제 - 데이터 분석
print("📈 실전 예제 - 데이터 분석")

# 판매 데이터
sales_data = [
    {"product": "노트북", "category": "전자기기", "price": 1200000, "quantity": 5},
    {"product": "마우스", "category": "전자기기", "price": 50000, "quantity": 15},
    {"product": "책상", "category": "가구", "price": 300000, "quantity": 3},
    {"product": "의자", "category": "가구", "price": 150000, "quantity": 8},
    {"product": "키보드", "category": "전자기기", "price": 100000, "quantity": 10},
    {"product": "램프", "category": "가구", "price": 80000, "quantity": 12}
]

print("판매 데이터 분석:")

# 총 매출 계산
total_revenues = list(map(lambda item: {
    **item, 
    "revenue": item["price"] * item["quantity"]
}, sales_data))

print(f"\n매출 계산:")
for item in total_revenues:
    print(f"  {item['product']}: {item['revenue']:,}원")

# 고가 상품 필터링 (50만원 이상)
expensive_items = list(filter(lambda item: item["price"] >= 500000, sales_data))
print(f"\n고가 상품 (50만원 이상):")
for item in expensive_items:
    print(f"  {item['product']}: {item['price']:,}원")

# 카테고리별 총 매출
electronics = list(filter(lambda item: item["category"] == "전자기기", total_revenues))
furniture = list(filter(lambda item: item["category"] == "가구", total_revenues))

electronics_total = sum(map(lambda item: item["revenue"], electronics))
furniture_total = sum(map(lambda item: item["revenue"], furniture))

print(f"\n카테고리별 매출:")
print(f"  전자기기: {electronics_total:,}원")
print(f"  가구: {furniture_total:,}원")

# 매출 순 정렬
sorted_by_revenue = sorted(total_revenues, key=lambda item: item["revenue"], reverse=True)
print(f"\n매출 순 정렬:")
for i, item in enumerate(sorted_by_revenue[:3], 1):
    print(f"  {i}위: {item['product']} ({item['revenue']:,}원)")

print("=" * 30)

# 7. 람다의 한계와 주의사항
print("⚠️ 람다의 한계와 주의사항")

# 복잡한 로직은 일반 함수가 더 좋음
print("복잡한 로직 비교:")

# 람다로는 복잡하고 읽기 어려움
complex_lambda = lambda x: x**2 if x > 0 else (-x)**2 if x < 0 else 0

# 일반 함수로는 명확함
def complex_function(x):
    """절댓값의 제곱을 계산하는 함수"""
    if x > 0:
        return x ** 2
    elif x < 0:
        return (-x) ** 2
    else:
        return 0

test_values = [-3, -1, 0, 1, 3]
print("테스트 값들:", test_values)

lambda_results = [complex_lambda(x) for x in test_values]
function_results = [complex_function(x) for x in test_values]

print(f"람다 결과: {lambda_results}")
print(f"함수 결과: {function_results}")
print("결과 동일:", lambda_results == function_results)

# 람다는 이름이 없어서 디버깅이 어려움
print("\n함수 정보:")
print(f"일반 함수 이름: {complex_function.__name__}")
print(f"람다 함수 이름: {complex_lambda.__name__}")  # <lambda>로 표시됨

# 람다 함수 사용 권장 사항
print("\n📝 람다 함수 사용 권장사항:")
print("✅ 권장: 간단한 한 줄 로직")
print("✅ 권장: map, filter, sorted 등과 함께 사용")
print("✅ 권장: 일회성 작은 변환")
print("❌ 비권장: 복잡한 조건문이나 여러 줄 로직")
print("❌ 비권장: 반복적으로 사용되는 로직")
print("❌ 비권장: 디버깅이 중요한 복잡한 계산")
```

#### 🌐 지역 변수와 전역 변수

```python
print("🌐 지역 변수와 전역 변수")
print("=" * 24)

# 1. 기본 스코프 개념
print("📍 기본 스코프 개념")

# 전역 변수
global_var = "나는 전역 변수입니다"
global_number = 100

def show_scope():
    """스코프를 보여주는 함수"""
    # 지역 변수
    local_var = "나는 지역 변수입니다"
    local_number = 200
    
    print("함수 내부에서:")
    print(f"  전역 변수: {global_var}")
    print(f"  전역 숫자: {global_number}")
    print(f"  지역 변수: {local_var}")
    print(f"  지역 숫자: {local_number}")

# 함수 호출
print("스코프 테스트:")
show_scope()

print("\n함수 외부에서:")
print(f"  전역 변수: {global_var}")
print(f"  전역 숫자: {global_number}")

# 지역 변수에 접근 시도 (오류 발생)
try:
    print(f"  지역 변수: {local_var}")  # NameError 발생
except NameError as e:
    print(f"  지역 변수 접근 오류: {e}")

print("=" * 30)

# 2. 변수 shadowing (가림 현상)
print("👥 변수 Shadowing")

name = "전역 이름"
age = 25

def introduce():
    """같은 이름의 지역 변수가 전역 변수를 가리는 예제"""
    name = "지역 이름"  # 전역 변수를 가림
    print(f"함수 내부 - 이름: {name}, 나이: {age}")

def introduce_with_global():
    """전역 변수를 명시적으로 사용하는 예제"""
    global name
    print(f"global 사용 - 이름: {name}, 나이: {age}")
    name = "변경된 전역 이름"  # 전역 변수 수정

print("Shadowing 테스트:")
print(f"함수 호출 전 - 이름: {name}, 나이: {age}")

introduce()
print(f"introduce() 후 - 이름: {name}, 나이: {age}")  # 전역 변수 그대로

introduce_with_global()
print(f"introduce_with_global() 후 - 이름: {name}, 나이: {age}")  # 전역 변수 변경됨

print("=" * 30)

# 3. global 키워드
print("🌍 global 키워드")

counter = 0  # 전역 카운터

def increment_counter():
    """카운터를 증가시키는 함수"""
    global counter
    counter += 1
    print(f"카운터 증가: {counter}")

def reset_counter():
    """카운터를 리셋하는 함수"""
    global counter
    counter = 0
    print("카운터 리셋")

def show_counter():
    """카운터 값을 표시하는 함수 (읽기 전용)"""
    print(f"현재 카운터: {counter}")

# 카운터 테스트
print("카운터 테스트:")
show_counter()

increment_counter()
increment_counter()
increment_counter()

show_counter()
reset_counter()
show_counter()

# 전역 변수 여러 개 다루기
user_name = "Guest"
user_level = 1
user_score = 0

def user_login(name):
    """사용자 로그인"""
    global user_name, user_level, user_score
    user_name = name
    user_level = 1
    user_score = 0
    print(f"로그인 완료: {user_name} (레벨 {user_level}, 점수 {user_score})")

def user_level_up():
    """레