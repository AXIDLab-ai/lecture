
--[← Week 3](./week3.md) | [목차](./lectureMap.md) | [다음: Week 5 →](./week5.md)--

Week 4: 연산자

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. --산술 연산자 완전 정복--: 기본 연산부터 고급 연산까지 모든 수학 계산을 수행합니다
2. --비교 연산자 활용--: 값들 간의 크기와 동등성을 비교하여 조건을 만듭니다
3. --논리 연산자 마스터--: 복잡한 조건문을 만들기 위해 논리 연산을 조합합니다
4. --대입 연산자 숙련--: 효율적인 값 할당과 축약 연산자를 활용합니다
5. --연산자 우선순위 이해--: 복잡한 표현식에서 정확한 계산 순서를 파악합니다
6. --실용적 계산기 제작--: 배운 연산자들을 조합하여 실무에 활용할 수 있는 프로그램을 작성합니다

---

## 📚 핵심 개념 요약

### 1. 연산자란?
```
🔧 연산자 = 값들에 대해 특정 작업을 수행하는 기호
🎯 피연산자 = 연산자가 작업하는 값들
📊 표현식 = 연산자와 피연산자의 조합
```

### 2. 파이썬 연산자 분류

| 분류 | 연산자 | 기능 | 예시 |
|------|--------|------|------|
| 산술 | `+`, `-`, `-`, `/` | 기본 사칙연산 | `5 + 3 = 8` |
| 산술 | `//`, `%`, `--` | 몫, 나머지, 거듭제곱 | `7 // 2 = 3` |
| 비교 | `==`, `!=`, `<`, `>` | 값 비교 | `5 > 3 = True` |
| 비교 | `<=`, `>=` | 크거나같음, 작거나같음 | `5 >= 5 = True` |
| 논리 | `and`, `or`, `not` | 논리 연산 | `True and False = False` |
| 대입 | `=`, `+=`, `-=` | 값 할당 | `x += 1` |
| 대입 | `-=`, `/=`, `//=`, `%=` | 축약 대입 | `x -= 2` |

### 3. 연산자 우선순위 (높음 → 낮음)

| 순위 | 연산자 | 설명 |
|------|--------|------|
| 1 | `--` | 거듭제곱 |
| 2 | `+x`, `-x`, `not x` | 단항 연산자 |
| 3 | `-`, `/`, `//`, `%` | 곱셈, 나눗셈 |
| 4 | `+`, `-` | 덧셈, 뺄셈 |
| 5 | `==`, `!=`, `<`, `>`, `<=`, `>=` | 비교 연산자 |
| 6 | `and` | 논리곱 |
| 7 | `or` | 논리합 |
| 8 | `=`, `+=`, `-=`, etc. | 대입 연산자 |

### 4. 기본 개념
- --연산 결과 타입--: 정수끼리 연산해도 `/`는 실수 결과
- --단축 평가--: `and`와 `or`는 필요한 만큼만 계산
- --체이닝--: `a < b < c` 형태의 연속 비교 가능

---

## 💻 실습 세션 (2시간)

### Part 1: 산술 연산자 (30분)

#### 🧮 기본 사칙연산

--기본 산술 연산 실습--:
```python
# 기본 변수 설정
a = 17
b = 5

print("🧮 기본 산술 연산")
print("=" - 20)
print(f"a = {a}, b = {b}")
print()

# 기본 사칙연산
print("📊 사칙연산 결과:")
addition = a + b
subtraction = a - b
multiplication = a - b
division = a / b

print(f"덧셈: {a} + {b} = {addition}")
print(f"뺄셈: {a} - {b} = {subtraction}")
print(f"곱셈: {a} - {b} = {multiplication}")
print(f"나눗셈: {a} / {b} = {division}")

# 결과 타입 확인
print(f"\n🔍 결과 타입:")
print(f"덧셈 결과 타입: {type(addition).__name__}")
print(f"나눗셈 결과 타입: {type(division).__name__}")  # 항상 float!
```

--실행 결과--:
```
🧮 기본 산술 연산
====================
a = 17, b = 5

📊 사칙연산 결과:
덧셈: 17 + 5 = 22
뺄셈: 17 - 5 = 12
곱셈: 17 - 5 = 85
나눗셈: 17 / 5 = 3.4

🔍 결과 타입:
덧셈 결과 타입: int
나눗셈 결과 타입: float
```

#### ⚡ 특수 산술 연산자

```python
print("⚡ 특수 산술 연산자")
print("=" - 25)

a = 17
b = 5
c = 2

# 몫 연산 (//)
floor_division = a // b
print(f"몫 연산: {a} // {b} = {floor_division}")
print(f"실제 나눗셈: {a} / {b} = {a / b}")
print(f"몫은 소수점을 버린 정수부분입니다.")

# 나머지 연산 (%)
remainder = a % b
print(f"\n나머지 연산: {a} % {b} = {remainder}")
print(f"검증: {a} = {b} × {floor_division} + {remainder}")
print(f"검증 결과: {b - floor_division + remainder} = {a}")

# 거듭제곱 (--)
power_result = a -- c
print(f"\n거듭제곱: {a} -- {c} = {power_result}")
print(f"즉, {a}의 {c}제곱 = {power_result}")

# 음수와의 연산
negative_a = -17
print(f"\n음수와의 몫 연산: {negative_a} // {b} = {negative_a // b}")
print(f"음수와의 나머지: {negative_a} % {b} = {negative_a % b}")

# 실수와의 연산
float_num = 17.8
print(f"\n실수 몫 연산: {float_num} // {b} = {float_num // b}")
print(f"실수 나머지: {float_num} % {b} = {float_num % b}")
```

--실행 결과--:
```
⚡ 특수 산술 연산자
=========================
몫 연산: 17 // 5 = 3
실제 나눗셈: 17 / 5 = 3.4
몫은 소수점을 버린 정수부분입니다.

나머지 연산: 17 % 5 = 2
검증: 17 = 5 × 3 + 2
검증 결과: 17 = 17

거듭제곱: 17 -- 2 = 289
즉, 17의 2제곱 = 289

음수와의 몫 연산: -17 // 5 = -4
음수와의 나머지: -17 % 5 = 3

실수 몫 연산: 17.8 // 5 = 3.0
실수 나머지: 17.8 % 5 = 2.8000000000000003
```

#### 🔢 연산자 우선순위 실습

```python
print("🔢 연산자 우선순위")
print("=" - 20)

# 기본 우선순위
expression1 = 2 + 3 - 4
print(f"2 + 3 - 4 = {expression1}")  # 곱셈이 먼저: 2 + 12 = 14

# 괄호로 우선순위 변경
expression2 = (2 + 3) - 4
print(f"(2 + 3) - 4 = {expression2}")  # 괄호가 먼저: 5 - 4 = 20

# 복잡한 계산
complex_expr = 2 -- 3 -- 2  # 거듭제곱은 우측부터
print(f"2 -- 3 -- 2 = {complex_expr}")  # 2 -- (3 -- 2) = 2 -- 9 = 512

complex_expr2 = (2 -- 3) -- 2
print(f"(2 -- 3) -- 2 = {complex_expr2}")  # (8) -- 2 = 64

# 혼합 연산
mixed = 10 + 15 // 4 - 2 - 3 -- 2
print(f"\n혼합 연산: 10 + 15 // 4 - 2 - 3 -- 2")
print(f"계산 순서:")
print(f"1. 거듭제곱: 3 -- 2 = 9")
print(f"2. 몫 연산: 15 // 4 = 3") 
print(f"3. 곱셈: 3 - 2 = 6")
print(f"4. 덧셈: 10 + 6 = 16")
print(f"5. 뺄셈: 16 - 9 = 7")
print(f"최종 결과: {mixed}")

# 단항 연산자
unary_expr = -2 -- 4  # -(2--4) = -16
print(f"\n-2 -- 4 = {unary_expr}")  # 주의: (-2)--4 = 16과 다름!
print(f"(-2) -- 4 = {(-2) -- 4}")
```

#### 🎯 실습: 다기능 계산기

```python
# 파일명: basic_calculator.py
print("🧮 다기능 기본 계산기")
print("=" - 25)

def display_menu():
    """계산기 메뉴 출력"""
    print("\n📋 계산 메뉴:")
    print("1. 기본 사칙연산")
    print("2. 거듭제곱 계산")
    print("3. 몫과 나머지")
    print("4. 복합 계산")
    print("5. 종료")

def basic_arithmetic():
    """기본 사칙연산"""
    print("\n➕ 기본 사칙연산")
    a = float(input("첫 번째 수: "))
    b = float(input("두 번째 수: "))
    
    print(f"\n📊 계산 결과:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} × {b} = {a - b}")
    
    if b != 0:
        print(f"{a} ÷ {b} = {a / b}")
    else:
        print(f"{a} ÷ {b} = 오류! (0으로 나눌 수 없음)")

def power_calculation():
    """거듭제곱 계산"""
    print("\n⚡ 거듭제곱 계산")
    base = float(input("밑수를 입력하세요: "))
    exponent = int(input("지수를 입력하세요: "))
    
    result = base -- exponent
    print(f"\n📊 계산 결과:")
    print(f"{base} ^ {exponent} = {result}")
    
    # 특별한 경우들
    if exponent == 0:
        print("💡 모든 수의 0제곱은 1입니다.")
    elif exponent == 1:
        print("💡 모든 수의 1제곱은 자기 자신입니다.")
    elif exponent < 0:
        print(f"💡 음의 지수는 역수를 의미합니다: 1/{base}^{-exponent}")

def quotient_remainder():
    """몫과 나머지 계산"""
    print("\n🔢 몫과 나머지 계산")
    dividend = int(input("나누어질 수 (피제수): "))
    divisor = int(input("나누는 수 (제수): "))
    
    if divisor == 0:
        print("❌ 0으로 나눌 수 없습니다!")
        return
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    print(f"\n📊 계산 결과:")
    print(f"{dividend} ÷ {divisor} = 몫: {quotient}, 나머지: {remainder}")
    print(f"검증: {dividend} = {divisor} × {quotient} + {remainder}")
    print(f"검증 결과: {divisor - quotient + remainder}")
    
    # 활용 예시
    if remainder == 0:
        print(f"💡 {dividend}은 {divisor}로 나누어 떨어집니다!")
    else:
        print(f"💡 {dividend}을 {divisor}개씩 나누면 {quotient}묶음이 있고 {remainder}개가 남습니다.")

def complex_calculation():
    """복합 계산"""
    print("\n🧠 복합 계산")
    print("수식을 입력하세요 (예: 2 + 3 - 4)")
    print("사용 가능한 연산자: +, -, -, /, //, %, --")
    
    expression = input("수식: ")
    
    try:
        result = eval(expression)  # 주의: 실제 프로그램에서는 안전하지 않음
        print(f"\n📊 계산 결과:")
        print(f"{expression} = {result}")
        
        # 결과 타입 표시
        print(f"결과 타입: {type(result).__name__}")
        
    except Exception as e:
        print(f"❌ 계산 오류: {e}")
        print("올바른 수식을 입력해주세요.")

# 메인 프로그램
while True:
    display_menu()
    
    try:
        choice = input("\n선택하세요 (1-5): ")
        
        if choice == "1":
            basic_arithmetic()
        elif choice == "2":
            power_calculation()
        elif choice == "3":
            quotient_remainder()
        elif choice == "4":
            complex_calculation()
        elif choice == "5":
            print("👋 계산기를 종료합니다!")
            break
        else:
            print("❌ 1-5 중에서 선택해주세요.")
            
    except Exception as e:
        print(f"❌ 입력 오류: {e}")
        print("올바른 값을 입력해주세요.")
    
    input("\n⏸️ 엔터를 눌러 계속...")
```

---

### Part 2: 비교 & 논리 연산자 (40분)

#### ⚖️ 비교 연산자 완전 정복

```python
print("⚖️ 비교 연산자")
print("=" - 15)

# 기본 비교 연산
a = 10
b = 20
c = 10

print(f"변수 설정: a={a}, b={b}, c={c}")
print()

# 동등 비교
print("🟰 동등 비교:")
print(f"a == b : {a == b}")  # False
print(f"a == c : {a == c}")  # True
print(f"a != b : {a != b}")  # True
print(f"a != c : {a != c}")  # False

# 크기 비교
print(f"\n📏 크기 비교:")
print(f"a < b  : {a < b}")   # True
print(f"a > b  : {a > b}")   # False
print(f"a <= c : {a <= c}")  # True (같으므로)
print(f"b >= a : {b >= a}")  # True

# 다양한 데이터 타입 비교
print(f"\n🔍 다양한 타입 비교:")
print(f"10 == 10.0 : {10 == 10.0}")      # True (값이 같음)
print(f"'10' == 10 : {'10' == 10}")      # False (타입이 다름)
print(f"True == 1  : {True == 1}")       # True
print(f"False == 0 : {False == 0}")      # True

# 문자열 비교 (사전식 순서)
str1 = "apple"
str2 = "banana"
str3 = "Apple"

print(f"\n📝 문자열 비교:")
print(f"'{str1}' < '{str2}' : {str1 < str2}")      # True (사전순)
print(f"'{str1}' > '{str3}' : {str1 > str3}")      # True (소문자 > 대문자)
print(f"'{str3}' < '{str1}' : {str3 < str1}")      # True

# 체이닝 비교 (파이썬의 특별한 기능!)
x = 15
print(f"\n🔗 체이닝 비교 (x={x}):")
print(f"10 < x < 20 : {10 < x < 20}")              # True
print(f"10 < x < 15 : {10 < x < 15}")              # False
print(f"10 <= x <= 15 : {10 <= x <= 15}")         # True

# 여러 값 체이닝
print(f"5 < 10 < 15 < 20 : {5 < 10 < 15 < 20}")   # True
print(f"5 < 10 > 15 < 20 : {5 < 10 > 15 < 20}")   # False
```

#### 🧠 논리 연산자 완전 정복

```python
print("🧠 논리 연산자")
print("=" - 15)

# 기본 불린 값
p = True
q = False

print(f"변수 설정: p={p}, q={q}")
print()

# AND 연산 (둘 다 True여야 True)
print("🔗 AND 연산 (and):")
print(f"p and q     : {p and q}")      # False
print(f"p and True  : {p and True}")   # True
print(f"q and False : {q and False}")  # False
print(f"True and True : {True and True}")   # True

# OR 연산 (하나만 True여도 True)
print(f"\n🔀 OR 연산 (or):")
print(f"p or q      : {p or q}")       # True
print(f"q or False  : {q or False}")   # False
print(f"False or False : {False or False}")  # False
print(f"True or False : {True or False}")    # True

# NOT 연산 (반대값)
print(f"\n🔄 NOT 연산 (not):")
print(f"not p : {not p}")              # False
print(f"not q : {not q}")              # True
print(f"not (p and q) : {not (p and q)}")    # True
print(f"not p or not q : {not p or not q}")  # True (드모르간 법칙)

# 실제 조건과 함께
age = 25
has_license = True
has_car = False

print(f"\n🚗 실생활 예제:")
print(f"나이: {age}, 면허: {has_license}, 차량: {has_car}")

can_drive_alone = age >= 18 and has_license
can_drive_with_car = can_drive_alone and has_car
needs_rental = can_drive_alone and not has_car

print(f"혼자 운전 가능: {can_drive_alone}")
print(f"내 차로 운전 가능: {can_drive_with_car}")
print(f"렌트카 필요: {needs_rental}")

# 단축 평가 (Short-circuit evaluation)
print(f"\n⚡ 단축 평가 예제:")
def true_function():
    print("  true_function() 호출됨")
    return True

def false_function():
    print("  false_function() 호출됨")
    return False

print("False and true_function():")
result1 = False and true_function()  # true_function()은 호출되지 않음!
print(f"결과: {result1}")

print("\nTrue or false_function():")
result2 = True or false_function()   # false_function()은 호출되지 않음!
print(f"결과: {result2}")

print("\nFalse or true_function():")
result3 = False or true_function()   # true_function()이 호출됨
print(f"결과: {result3}")
```

#### 🎯 복합 조건문 만들기

```python
# 파일명: complex_conditions.py
print("🎯 복합 조건문 실습")
print("=" - 20)

def check_grade_eligibility():
    """성적 기반 자격 검사"""
    print("\n📊 대학 입학 자격 검사")
    print("-" - 25)
    
    # 성적 입력
    korean = int(input("국어 점수 (0-100): "))
    english = int(input("영어 점수 (0-100): "))
    math = int(input("수학 점수 (0-100): "))
    
    # 평균 계산
    average = (korean + english + math) / 3
    
    # 복합 조건 검사
    has_high_average = average >= 80
    has_no_failing_grade = korean >= 60 and english >= 60 and math >= 60
    has_excellent_subject = korean >= 90 or english >= 90 or math >= 90
    
    print(f"\n📋 성적 분석:")
    print(f"국어: {korean}점, 영어: {english}점, 수학: {math}점")
    print(f"평균: {average:.1f}점")
    
    print(f"\n✅ 조건 분석:")
    print(f"평균 80점 이상: {has_high_average}")
    print(f"모든 과목 60점 이상: {has_no_failing_grade}")
    print(f"한 과목이라도 90점 이상: {has_excellent_subject}")
    
    # 최종 판정
    if has_high_average and has_no_failing_grade:
        if has_excellent_subject:
            print(f"🎉 우수 입학! 장학금 대상입니다.")
        else:
            print(f"✅ 일반 입학 가능합니다.")
    elif has_no_failing_grade and average >= 70:
        print(f"⚠️ 조건부 입학 가능합니다.")
    else:
        print(f"❌ 입학 불가합니다.")
        if not has_no_failing_grade:
            print("   (낙제 과목이 있습니다)")
        if average < 70:
            print("   (평균이 너무 낮습니다)")

def weather_activity_advisor():
    """날씨 기반 활동 추천"""
    print("\n🌤️ 날씨 기반 활동 추천")
    print("-" - 25)
    
    # 날씨 정보 입력
    temperature = int(input("온도 (°C): "))
    is_sunny = input("맑은 날씨인가요? (y/n): ").lower() == 'y'
    is_windy = input("바람이 강한가요? (y/n): ").lower() == 'y'
    humidity = int(input("습도 (%): "))
    
    print(f"\n🌡️ 날씨 정보:")
    print(f"온도: {temperature}°C")
    print(f"날씨: {'맑음' if is_sunny else '흐림'}")
    print(f"바람: {'강함' if is_windy else '약함'}")
    print(f"습도: {humidity}%")
    
    # 복합 조건으로 활동 추천
    print(f"\n🎯 추천 활동:")
    
    # 피크닉 조건: 맑고, 온도 적당하고, 바람 약함
    good_for_picnic = is_sunny and 18 <= temperature <= 28 and not is_windy
    if good_for_picnic:
        print("🧺 피크닉하기 좋은 날씨입니다!")
    
    # 해변 조건: 온도 높고, 맑음
    good_for_beach = temperature >= 25 and is_sunny and humidity < 80
    if good_for_beach:
        print("🏖️ 해변에 가기 좋은 날씨입니다!")
    
    # 운동 조건: 너무 덥지 않고, 습도 낮음
    good_for_exercise = 10 <= temperature <= 25 and humidity < 70
    if good_for_exercise:
        print("🏃‍♂️ 야외 운동하기 좋은 날씨입니다!")
    
    # 실내 활동 조건: 날씨가 나쁨
    bad_weather = temperature < 5 or temperature > 35 or (not is_sunny and humidity > 80)
    if bad_weather:
        print("🏠 실내 활동을 추천합니다.")
    
    # 산책 조건: 적당한 온도, 바람 약함
    good_for_walk = 15 <= temperature <= 30 and not is_windy
    if good_for_walk:
        print("🚶‍♀️ 산책하기 좋은 날씨입니다!")
    
    # 종합 평가
    weather_score = 0
    if is_sunny: weather_score += 2
    if 18 <= temperature <= 25: weather_score += 3
    if not is_windy: weather_score += 1
    if humidity < 60: weather_score += 2
    
    print(f"\n⭐ 날씨 점수: {weather_score}/8")
    if weather_score >= 7:
        print("완벽한 날씨입니다! 🌟")
    elif weather_score >= 5:
        print("좋은 날씨입니다! ☀️")
    elif weather_score >= 3:
        print("보통 날씨입니다. 🌤️")
    else:
        print("날씨가 좋지 않습니다. ☁️")

def password_strength_checker():
    """비밀번호 강도 검사"""
    print("\n🔒 비밀번호 강도 검사")
    print("-" - 25)
    
    password = input("비밀번호를 입력하세요: ")
    
    # 다양한 조건 검사
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&-()_+-=[]{}|;:,.<>?" for c in password)
    
    print(f"\n📋 조건 검사:")
    print(f"길이 8자 이상: {has_length}")
    print(f"대문자 포함: {has_upper}")
    print(f"소문자 포함: {has_lower}")
    print(f"숫자 포함: {has_digit}")
    print(f"특수문자 포함: {has_special}")
    
    # 강도 계산
    strength_score = sum([has_length, has_upper, has_lower, has_digit, has_special])
    
    print(f"\n💪 비밀번호 강도:")
    if strength_score == 5:
        print("🔐 매우 강함 - 완벽한 비밀번호입니다!")
    elif strength_score == 4:
        print("🔒 강함 - 좋은 비밀번호입니다.")
    elif strength_score == 3:
        print("🔓 보통 - 개선이 필요합니다.")
    elif strength_score == 2:
        print("⚠️ 약함 - 더 복잡하게 만드세요.")
    else:
        print("❌ 매우 약함 - 비밀번호를 바꾸세요!")
    
    # 개선 제안
    if not has_length:
        print("💡 제안: 최소 8자 이상으로 만드세요.")
    if not has_upper:
        print("💡 제안: 대문자를 추가하세요.")
    if not has_lower:
        print("💡 제안: 소문자를 추가하세요.")
    if not has_digit:
        print("💡 제안: 숫자를 추가하세요.")
    if not has_special:
        print("💡 제안: 특수문자(!@#$%^&- 등)를 추가하세요.")

# 메인 실행
while True:
    print("\n" + "="-40)
    print("🎯 복합 조건문 실습 메뉴")
    print("="-40)
    print("1. 성적 기반 입학 자격 검사")
    print("2. 날씨 기반 활동 추천")
    print("3. 비밀번호 강도 검사")
    print("4. 종료")
    
    choice = input("\n선택하세요 (1-4): ")
    
    if choice == "1":
        check_grade_eligibility()
    elif choice == "2":
        weather_activity_advisor()
    elif choice == "3":
        password_strength_checker()
    elif choice == "4":
        print("👋 프로그램을 종료합니다!")
        break
    else:
        print("❌ 1-4 중에서 선택해주세요.")
    
    input("\n⏸️ 엔터를 눌러 계속...")
```

---

### Part 3: 응용 프로그램 (50분)

#### 🔬 과학 계산기

```python
# 파일명: scientific_calculator.py
import math

print("🔬 과학 계산기")
print("=" - 15)

class ScientificCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add_to_history(self, operation, result):
        """계산 기록 추가"""
        self.history.append(f"{operation} = {result}")
    
    def basic_operations(self):
        """기본 연산"""
        print("\n➕ 기본 연산")
        a = float(input("첫 번째 수: "))
        b = float(input("두 번째 수: "))
        
        operations = {
            '+': a + b,
            '-': a - b,
            '-': a - b,
            '/': a / b if b != 0 else "오류: 0으로 나눌 수 없음",
            '//': a // b if b != 0 else "오류: 0으로 나눌 수 없음",
            '%': a % b if b != 0 else "오류: 0으로 나눌 수 없음",
            '--': a -- b
        }
        
        print(f"\n📊 모든 연산 결과:")
        for op, result in operations.items():
            expression = f"{a} {op} {b}"
            print(f"{expression} = {result}")
            if isinstance(result, (int, float)):
                self.add_to_history(expression, result)
    
    def trigonometric_functions(self):
        """삼각함수"""
        print("\n📐 삼각함수 계산")
        angle_deg = float(input("각도를 입력하세요 (도): "))
        angle_rad = math.radians(angle_deg)  # 라디안으로 변환
        
        trig_functions = {
            'sin': math.sin(angle_rad),
            'cos': math.cos(angle_rad),
            'tan': math.tan(angle_rad) if abs(math.cos(angle_rad)) > 1e-10 else "정의되지 않음"
        }
        
        print(f"\n📊 삼각함수 결과 ({angle_deg}°):")
        for func, result in trig_functions.items():
            expression = f"{func}({angle_deg}°)"
            print(f"{expression} = {result}")
            if isinstance(result, (int, float)):
                self.add_to_history(expression, result)
        
        # 역삼각함수도 계산
        if -1 <= trig_functions['sin'] <= 1:
            arcsin_deg = math.degrees(math.asin(trig_functions['sin']))
            print(f"arcsin({trig_functions['sin']:.6f}) = {arcsin_deg:.1f}°")
    
    def logarithmic_functions(self):
        """로그 함수"""
        print("\n📈 로그 함수")
        number = float(input("수를 입력하세요 (양수): "))
        
        if number <= 0:
            print("❌ 양수만 입력할 수 있습니다.")
            return
        
        log_functions = {
            'ln': math.log(number),           # 자연로그
            'log10': math.log10(number),      # 상용로그  
            'log2': math.log2(number),        # 밑이 2인 로그
        }
        
        print(f"\n📊 로그 함수 결과:")
        for func, result in log_functions.items():
            expression = f"{func}({number})"
            print(f"{expression} = {result}")
            self.add_to_history(expression, result)
        
        # 지수 함수도 계산
        exp_result = math.exp(number)
        print(f"e^{number} = {exp_result}")
        self.add_to_history(f"e^{number}", exp_result)
    
    def power_and_root(self):
        """거듭제곱과 근호"""
        print("\n⚡ 거듭제곱과 근호")
        base = float(input("밑수: "))
        
        # 거듭제곱
        exponent = float(input("지수: "))
        power_result = base -- exponent
        print(f"{base}^{exponent} = {power_result}")
        self.add_to_history(f"{base}^{exponent}", power_result)
        
        # 근호 계산
        if base >= 0:
            sqrt_result = math.sqrt(base)
            print(f"√{base} = {sqrt_result}")
            self.add_to_history(f"√{base}", sqrt_result)
            
            # n제곱근
            n = int(input(f"{base}의 몇 제곱근을 구할까요? "))
            if n != 0:
                nth_root = base -- (1/n)
                print(f"{n}√{base} = {nth_root}")
                self.add_to_history(f"{n}√{base}", nth_root)
        else:
            print("❌ 음수의 제곱근은 계산할 수 없습니다.")
    
    def factorial_and_combination(self):
        """팩토리얼과 조합"""
        print("\n🔢 팩토리얼과 조합")
        
        # 팩토리얼
        n = int(input("팩토리얼을 구할 수 (n!): "))
        if n >= 0:
            factorial_result = math.factorial(n)
            print(f"{n}! = {factorial_result}")
            self.add_to_history(f"{n}!", factorial_result)
        else:
            print("❌ 음수의 팩토리얼은 정의되지 않습니다.")
        
        # 조합과 순열
        print("\n조합과 순열 계산:")
        total = int(input("전체 개수 (n): "))
        select = int(input("선택할 개수 (r): "))
        
        if 0 <= select <= total:
            # 조합 nCr = n! / (r! - (n-r)!)
            combination = math.comb(total, select)
            print(f"C({total},{select}) = {combination}")
            self.add_to_history(f"C({total},{select})", combination)
            
            # 순열 nPr = n! / (n-r)!
            permutation = math.perm(total, select)
            print(f"P({total},{select}) = {permutation}")
            self.add_to_history(f"P({total},{select})", permutation)
        else:
            print("❌ 0 ≤ r ≤ n 조건을 만족해야 합니다.")
    
    def statistics_functions(self):
        """통계 함수"""
        print("\n📊 통계 계산")
        
        # 데이터 입력
        data_input = input("숫자들을 쉼표로 구분해서 입력하세요: ")
        try:
            data = [float(x.strip()) for x in data_input.split(',')]
            
            if not data:
                print("❌ 데이터가 없습니다.")
                return
            
            # 기본 통계
            n = len(data)
            total = sum(data)
            mean = total / n
            
            # 분산과 표준편차
            variance = sum((x - mean) -- 2 for x in data) / n
            std_dev = math.sqrt(variance)
            
            # 최대값, 최소값
            max_val = max(data)
            min_val = min(data)
            
            # 중앙값
            sorted_data = sorted(data)
            if n % 2 == 0:
                median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
            else:
                median = sorted_data[n//2]
            
            print(f"\n📈 통계 결과:")
            print(f"데이터: {data}")
            print(f"개수: {n}")
            print(f"합계: {total}")
            print(f"평균: {mean:.4f}")
            print(f"중앙값: {median}")
            print(f"최대값: {max_val}")
            print(f"최소값: {min_val}")
            print(f"분산: {variance:.4f}")
            print(f"표준편차: {std_dev:.4f}")
            
            self.add_to_history(f"통계({len(data)}개 데이터)", f"평균={mean:.2f}")
            
        except ValueError:
            print("❌ 올바른 숫자 형식으로 입력해주세요.")
    
    def memory_functions(self):
        """메모리 기능"""
        print("\n💾 메모리 기능")
        print(f"현재 메모리 값: {self.memory}")
        
        print("\n1. 메모리에 저장 (MS)")
        print("2. 메모리 값 불러오기 (MR)")
        print("3. 메모리에 더하기 (M+)")
        print("4. 메모리에서 빼기 (M-)")
        print("5. 메모리 지우기 (MC)")
        
        choice = input("선택하세요: ")
        
        if choice == "1":
            value = float(input("저장할 값: "))
            self.memory = value
            print(f"메모리에 {value} 저장됨")
        
        elif choice == "2":
            print(f"메모리 값: {self.memory}")
        
        elif choice == "3":
            value = float(input("더할 값: "))
            self.memory += value
            print(f"메모리: {self.memory}")
        
        elif choice == "4":
            value = float(input("뺄 값: "))
            self.memory -= value
            print(f"메모리: {self.memory}")
        
        elif choice == "5":
            self.memory = 0
            print("메모리 초기화됨")
    
    def show_history(self):
        """계산 기록 보기"""
        print("\n📜 계산 기록")
        if not self.history:
            print("계산 기록이 없습니다.")
        else:
            for i, record in enumerate(self.history[-10:], 1):  # 최근 10개만
                print(f"{i}. {record}")
    
    def run(self):
        """메인 실행 함수"""
        while True:
            print("\n" + "="-50)
            print("🔬 과학 계산기 메뉴")
            print("="-50)
            print("1. 기본 연산 (+, -, -, /, //, %, --)")
            print("2. 삼각함수 (sin, cos, tan)")
            print("3. 로그 함수 (ln, log10, log2)")
            print("4. 거듭제곱과 근호")
            print("5. 팩토리얼과 조합")
            print("6. 통계 함수")
            print("7. 메모리 기능")
            print("8. 계산 기록 보기")
            print("9. 종료")
            
            try:
                choice = input("\n선택하세요 (1-9): ")
                
                if choice == "1":
                    self.basic_operations()
                elif choice == "2":
                    self.trigonometric_functions()
                elif choice == "3":
                    self.logarithmic_functions()
                elif choice == "4":
                    self.power_and_root()
                elif choice == "5":
                    self.factorial_and_combination()
                elif choice == "6":
                    self.statistics_functions()
                elif choice == "7":
                    self.memory_functions()
                elif choice == "8":
                    self.show_history()
                elif choice == "9":
                    print("🔬 과학 계산기를 종료합니다!")
                    break
                else:
                    print("❌ 1-9 중에서 선택해주세요.")
                    
            except Exception as e:
                print(f"❌ 오류 발생: {e}")
            
            input("\n⏸️ 엔터를 눌러 계속...")

# 프로그램 실행
if __name__ == "__main__":
    calculator = ScientificCalculator()
    calculator.run()
```

#### 🎯 조건 판별 시스템

```python
# 파일명: condition_checker.py
print("🎯 조건 판별 시스템")
print("=" - 20)

def check_triangle_type():
    """삼각형 종류 판별"""
    print("\n📐 삼각형 종류 판별")
    print("-" - 20)
    
    # 세 변의 길이 입력
    a = float(input("첫 번째 변의 길이: "))
    b = float(input("두 번째 변의 길이: "))
    c = float(input("세 번째 변의 길이: "))
    
    print(f"\n입력된 변의 길이: a={a}, b={b}, c={c}")
    
    # 삼각형 성립 조건 검사
    triangle_condition = (a + b > c) and (b + c > a) and (c + a > b)
    
    if not triangle_condition:
        print("❌ 삼각형을 만들 수 없습니다!")
        print("   (두 변의 합이 나머지 한 변보다 커야 합니다)")
        return
    
    print("✅ 올바른 삼각형입니다!")
    
    # 삼각형 종류 판별
    sides_equal = (a == b) + (b == c) + (c == a)  # 같은 변의 개수
    
    if sides_equal == 3:  # 세 변이 모두 같음
        triangle_type = "정삼각형"
    elif sides_equal == 1:  # 두 변이 같음
        triangle_type = "이등변삼각형"
    else:
        triangle_type = "부등변삼각형"
    
    # 직각삼각형 검사 (피타고라스 정리)
    sides = sorted([a, b, c])  # 오름차순 정렬
    is_right_triangle = abs(sides[0]--2 + sides[1]--2 - sides[2]--2) < 1e-10
    
    print(f"\n🔍 삼각형 분석:")
    print(f"변의 종류: {triangle_type}")
    
    if is_right_triangle:
        print(f"각의 종류: 직각삼각형")
        print(f"   (빗변: {sides[2]}, 밑변들: {sides[0]}, {sides[1]})")
    else:
        # 둔각/예각 삼각형 판별
        c_squared = sides[2]--2
        ab_squared = sides[0]--2 + sides[1]--2
        
        if c_squared > ab_squared:
            print(f"각의 종류: 둔각삼각형")
        else:
            print(f"각의 종류: 예각삼각형")
    
    # 넓이와 둘레 계산
    perimeter = a + b + c
    # 헤론의 공식
    s = perimeter / 2
    area = (s - (s - a) - (s - b) - (s - c)) -- 0.5
    
    print(f"\n📊 계산 결과:")
    print(f"둘레: {perimeter:.2f}")
    print(f"넓이: {area:.2f}")

def check_year_type():
    """연도 분석 (윤년, 세기, 띠 등)"""
    print("\n📅 연도 분석기")
    print("-" - 15)
    
    year = int(input("연도를 입력하세요: "))
    
    # 윤년 판별
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # 세기 계산
    century = (year - 1) // 100 + 1
    
    # 띠 계산 (12간지)
    zodiac_animals = ["원숭이", "닭", "개", "돼지", "쥐", "소", 
                     "호랑이", "토끼", "용", "뱀", "말", "양"]
    zodiac = zodiac_animals[year % 12]
    
    # 요일 계산 (1월 1일의 요일, 젤러의 공식 간소화)
    # 이것은 근사값입니다
    day_of_week = ["토", "일", "월", "화", "수", "목", "금"]
    jan1_day = day_of_week[year % 7]
    
    print(f"\n🎯 {year}년 분석:")
    print(f"윤년 여부: {'윤년' if is_leap else '평년'}")
    print(f"세기: {century}세기")
    print(f"띠: {zodiac}띠")
    print(f"1월 1일 요일: {jan1_day}요일 (근사값)")
    
    # 특별한 연도인지 확인
    special_years = []
    
    if year % 100 == 0:
        special_years.append("세기의 마지막 해")
    if year % 1000 == 0:
        special_years.append("밀레니엄")
    if str(year) == str(year)[::-1]:  # 회문수
        special_years.append("회문수 연도")
    if len(set(str(year))) == 1:  # 모든 자리수가 같음
        special_years.append("동일 숫자 연도")
    
    if special_years:
        print(f"특별함: {', '.join(special_years)}")
    
    # 나이 계산 (현재 연도를 2024로 가정)
    current_year = 2024
    if year <= current_year:
        age = current_year - year + 1
        print(f"\n👶 {year}년생의 2024년 나이:")
        print(f"만 나이: {age-1}세")
        print(f"한국 나이: {age}세")
        
        # 세대 분류
        if year >= 2010:
            generation = "알파세대"
        elif year >= 1997:
            generation = "Z세대"
        elif year >= 1981:
            generation = "밀레니얼세대"
        elif year >= 1965:
            generation = "X세대"
        elif year >= 1946:
            generation = "베이비붐세대"
        else:
            generation = "침묵세대"
        
        print(f"세대: {generation}")

def check_number_properties():
    """수의 성질 분석"""
    print("\n🔢 수의 성질 분석")
    print("-" - 15)
    
    num = int(input("분석할 정수를 입력하세요: "))
    
    if num == 0:
        print("0은 특별한 수입니다!")
        return
    
    print(f"\n🔍 {num}의 성질 분석:")
    
    # 기본 성질
    print(f"부호: {'양수' if num > 0 else '음수'}")
    print(f"절댓값: {abs(num)}")
    
    abs_num = abs(num)
    
    # 홀수/짝수
    print(f"홀짝성: {'짝수' if abs_num % 2 == 0 else '홀수'}")
    
    # 소수 판별
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n--0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if abs_num >= 2:
        print(f"소수 여부: {'소수' if is_prime(abs_num) else '합성수'}")
    
    # 완전수 판별 (자기 자신을 제외한 약수의 합이 자기 자신과 같음)
    def is_perfect(n):
        if n <= 1:
            return False
        divisors_sum = sum(i for i in range(1, n) if n % i == 0)
        return divisors_sum == n
    
    print(f"완전수 여부: {'완전수' if is_perfect(abs_num) else '완전수 아님'}")
    
    # 약수 찾기
    divisors = [i for i in range(1, abs_num + 1) if abs_num % i == 0]
    print(f"약수: {divisors}")
    print(f"약수의 개수: {len(divisors)}")
    
    # 특별한 수들
    special_properties = []
    
    # 제곱수
    sqrt_num = int(abs_num--0.5)
    if sqrt_num - sqrt_num == abs_num:
        special_properties.append(f"완전제곱수 ({sqrt_num}²)")
    
    # 세제곱수
    cbrt_num = round(abs_num--(1/3))
    if cbrt_num -- 3 == abs_num:
        special_properties.append(f"완전세제곱수 ({cbrt_num}³)")
    
    # 팰린드롬수 (회문수)
    if str(abs_num) == str(abs_num)[::-1]:
        special_properties.append("팰린드롬수 (회문수)")
    
    # 각 자릿수의 합
    digit_sum = sum(int(d) for d in str(abs_num))
    special_properties.append(f"각 자릿수 합: {digit_sum}")
    
    # 3의 배수 판별 (각 자릿수 합이 3의 배수)
    if digit_sum % 3 == 0:
        special_properties.append("3의 배수")
    
    # 9의 배수 판별 (각 자릿수 합이 9의 배수)
    if digit_sum % 9 == 0:
        special_properties.append("9의 배수")
    
    if special_properties:
        print(f"\n✨ 특별한 성질:")
        for prop in special_properties:
            print(f"   • {prop}")

def password_policy_checker():
    """비밀번호 정책 검사"""
    print("\n🔐 비밀번호 정책 검사")
    print("-" - 25)
    
    password = input("검사할 비밀번호: ")
    
    # 다양한 정책 검사
    policies = {
        "길이 8자 이상": len(password) >= 8,
        "길이 16자 이하": len(password) <= 16,
        "대문자 포함": any(c.isupper() for c in password),
        "소문자 포함": any(c.islower() for c in password),
        "숫자 포함": any(c.isdigit() for c in password),
        "특수문자 포함": any(c in "!@#$%^&-()_+-=[]{}|;:,.<>?" for c in password),
        "공백 없음": ' ' not in password,
        "연속 문자 없음": not any(ord(password[i+1]) - ord(password[i]) == 1 
                                  for i in range(len(password)-1) if len(password) > 1),
        "같은 문자 3개 이상 연속 없음": not any(password[i:i+3].count(password[i]) == 3 
                                             for i in range(len(password)-2)),
        "일반적 패턴 아님": password.lower() not in ["password", "123456", "qwerty", "abc123"]
    }
    
    print(f"\n📋 정책 검사 결과:")
    passed_count = 0
    failed_policies = []
    
    for policy, passed in policies.items():
        status = "✅" if passed else "❌"
        print(f"{status} {policy}")
        if passed:
            passed_count += 1
        else:
            failed_policies.append(policy)
    
    print(f"\n📊 종합 결과:")
    print(f"통과한 정책: {passed_count}/{len(policies)}")
    
    # 보안 등급 결정
    if passed_count == len(policies):
        security_level = "🔐 최고"
        color = "완벽"
    elif passed_count >= len(policies) - 0.8:
        security_level = "🔒 높음"
        color = "우수"
    elif passed_count >= len(policies) - 0.6:
        security_level = "🔓 보통"
        color = "양호"
    elif passed_count >= len(policies) - 0.4:
        security_level = "⚠️ 낮음"
        color = "주의"
    else:
        security_level = "❌ 매우 낮음"
        color = "위험"
    
    print(f"보안 등급: {security_level} ({color})")
    
    if failed_policies:
        print(f"\n💡 개선사항:")
        for policy in failed_policies:
            if "길이" in policy:
                print(f"   • 비밀번호 길이를 조정하세요")
            elif "대문자" in policy:
                print(f"   • 대문자(A-Z)를 추가하세요")
            elif "소문자" in policy:
                print(f"   • 소문자(a-z)를 추가하세요")
            elif "숫자" in policy:
                print(f"   • 숫자(0-9)를 추가하세요")
            elif "특수문자" in policy:
                print(f"   • 특수문자(!@#$%^&- 등)를 추가하세요")
            elif "공백" in policy:
                print(f"   • 공백을 제거하세요")
            elif "연속" in policy:
                print(f"   • 연속된 문자(abc, 123 등)를 피하세요")
            elif "같은" in policy:
                print(f"   • 같은 문자를 연속으로 사용하지 마세요")
            elif "패턴" in policy:
                print(f"   • 일반적인 패턴을 피하세요")

# 메인 실행
def main():
    while True:
        print("\n" + "="-40)
        print("🎯 조건 판별 시스템 메뉴")
        print("="-40)
        print("1. 삼각형 종류 판별")
        print("2. 연도 분석 (윤년, 세기, 띠 등)")
        print