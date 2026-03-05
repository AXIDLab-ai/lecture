# Week 3: 변수와 데이터형

--[← Week 2](./week2.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 4 →](./week4.md)--

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. --변수 개념 완전 이해--: 변수의 역할과 메모리에서의 동작 원리를 이해합니다
2. --데이터 타입 구분--: 정수, 실수, 문자열, 불린형의 특성과 차이점을 파악합니다
3. --올바른 변수명 작성--: 파이썬 변수명 규칙과 관례를 준수하여 변수를 선언할 수 있습니다
4. --타입 체크와 변환--: type() 함수로 데이터 타입을 확인하고 적절한 형변환을 수행합니다
5. --실무 응용 능력--: 다양한 데이터 타입을 활용하여 실용적인 프로그램을 작성합니다

---

## 📚 핵심 개념 요약

### 1. 변수란 무엇인가?
```
🏷️ 변수 = 데이터를 저장하는 메모리 공간의 이름
```

- --변수--: 값을 저장하고 참조할 수 있는 저장공간
- --할당--: `=` 연산자로 변수에 값을 저장하는 것
- --참조--: 변수명을 사용하여 저장된 값에 접근하는 것

### 2. 파이썬의 4가지 기본 데이터 타입

| 타입 | 영문명 | 설명 | 예시 |
|------|--------|------|------|
| 정수형 | int | 소수점이 없는 숫자 | `42`, `-17`, `0` |
| 실수형 | float | 소수점이 있는 숫자 | `3.14`, `-2.5`, `0.0` |
| 문자열 | str | 텍스트 데이터 | `"Hello"`, `'파이썬'` |
| 불린형 | bool | 참/거짓 값 | `True`, `False` |

### 3. 변수명 규칙
✅ --할 수 있는 것--:
- 영문자, 숫자, 밑줄(_) 사용
- 첫 글자는 영문자나 밑줄
- 대소문자 구분 (name ≠ Name)

❌ --할 수 없는 것--:
- 숫자로 시작 (1name ❌)
- 예약어 사용 (if, for, while 등)
- 공백이나 특수문자 사용

### 4. 형변환 함수
| 함수 | 기능 | 예시 |
|------|------|------|
| `int()` | 정수로 변환 | `int("123")` → 123 |
| `float()` | 실수로 변환 | `float("3.14")` → 3.14 |
| `str()` | 문자열로 변환 | `str(123)` → "123" |
| `bool()` | 불린으로 변환 | `bool(1)` → True |

---

## 💻 실습 세션 (2시간)

### Part 1: 변수 선언과 사용 (30분)

#### 🏷️ 변수 만들기 기초

--기본 변수 선언--:
```python
# 다양한 타입의 변수 선언
name = "김파이썬"        # 문자열
age = 25               # 정수
height = 175.5         # 실수
is_student = True      # 불린

print("이름:", name)
print("나이:", age)
print("키:", height)
print("학생 여부:", is_student)
```

--실행 결과--:
```
이름: 김파이썬
나이: 25
키: 175.5
학생 여부: True
```

#### 🔄 변수 값 변경하기

```python
# 변수 값 변경 예제
score = 85
print("처음 점수:", score)

score = 90  # 값 변경
print("수정된 점수:", score)

score = score + 5  # 기존 값을 이용한 변경
print("보너스 점수 추가:", score)

# 축약 연산자 사용
score += 3  # score = score + 3과 동일
print("최종 점수:", score)
```

--실행 결과--:
```
처음 점수: 85
수정된 점수: 90
보너스 점수 추가: 95
최종 점수: 98
```

#### 👥 여러 변수 동시 할당

```python
# 방법 1: 개별 할당
x = 10
y = 20
z = 30

# 방법 2: 동시 할당 (튜플 언패킹)
a, b, c = 100, 200, 300
print(f"a={a}, b={b}, c={c}")

# 방법 3: 같은 값 할당
p = q = r = 0
print(f"p={p}, q={q}, r={r}")

# 방법 4: 변수 값 교환
num1 = 5
num2 = 10
print(f"교환 전: num1={num1}, num2={num2}")

num1, num2 = num2, num1  # 파이썬의 편리한 기능!
print(f"교환 후: num1={num1}, num2={num2}")
```

--실행 결과--:
```
a=100, b=200, c=300
p=0, q=0, r=0
교환 전: num1=5, num2=10
교환 후: num1=10, num2=5
```

#### 🎯 실습: 개인 정보 관리

```python
# 파일명: personal_info.py
print("📝 개인 정보 관리 시스템")
print("=" - 30)

# 개인 정보 변수들
full_name = "홍길동"
korean_name = "홍길동"
english_name = "Hong Gildong"
birth_year = 1995
current_year = 2024
phone_number = "010-1234-5678"
email = "hong@example.com"
address = "서울시 강남구"
job = "학생"
hobby = "독서"
is_married = False
has_car = True

# 계산된 정보
current_age = current_year - birth_year
birth_century = "20세기" if birth_year < 2000 else "21세기"

# 정보 출력
print("👤 기본 정보")
print("-" - 20)
print(f"성명: {full_name}")
print(f"영문명: {english_name}")
print(f"출생년도: {birth_year}년 ({birth_century})")
print(f"현재 나이: {current_age}세")
print()

print("📞 연락처 정보")
print("-" - 20)
print(f"휴대폰: {phone_number}")
print(f"이메일: {email}")
print(f"주소: {address}")
print()

print("💼 기타 정보")
print("-" - 20)
print(f"직업: {job}")
print(f"취미: {hobby}")
print(f"결혼 여부: {'기혼' if is_married else '미혼'}")
print(f"차량 소유: {'있음' if has_car else '없음'}")

# 변수 값 수정해보기
print("\n🔄 정보 업데이트")
print("-" - 20)
job = "개발자"  # 직업 변경
current_age += 1  # 생일이 지남
has_car = False  # 차량 매각

print(f"새 직업: {job}")
print(f"새 나이: {current_age}세")
print(f"차량 소유 상태: {'있음' if has_car else '없음'}")
```

---

### Part 2: 데이터 타입 실습 (40분)

#### 🔢 정수형 (int) 완전 정복

```python
# 다양한 방식의 정수 표현
decimal_num = 42        # 10진수
binary_num = 0b101010   # 2진수 (42와 같음)
octal_num = 0o52        # 8진수 (42와 같음)
hex_num = 0x2A          # 16진수 (42와 같음)

print("10진수 42:", decimal_num)
print("2진수 0b101010:", binary_num)
print("8진수 0o52:", octal_num)
print("16진수 0x2A:", hex_num)
print("모두 같은 값인가?", decimal_num == binary_num == octal_num == hex_num)

# 정수의 특성
big_number = 999999999999999999999999999999  # 파이썬은 무제한 정수!
print("큰 숫자:", big_number)
print("타입:", type(big_number))

# 정수 연산
a = 17
b = 5
print(f"\n정수 연산 ({a}, {b}):")
print(f"덧셈: {a} + {b} = {a + b}")
print(f"뺄셈: {a} - {b} = {a - b}")
print(f"곱셈: {a} - {b} = {a - b}")
print(f"나눗셈: {a} / {b} = {a / b}")      # 결과는 실수!
print(f"몫: {a} // {b} = {a // b}")         # 정수 나눗셈
print(f"나머지: {a} % {b} = {a % b}")       # 나머지
print(f"거듭제곱: {a} -- {b} = {a -- b}")   # 거듭제곱
```

#### 🎯 정수 실습: 시간 계산기

```python
# 파일명: time_calculator.py
print("⏰ 시간 계산기")
print("=" - 20)

# 현재 시간 (초 단위로 입력)
total_seconds = int(input("총 초를 입력하세요: "))

# 시간 단위로 변환
hours = total_seconds // 3600          # 1시간 = 3600초
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60      # 1분 = 60초
seconds = remaining_seconds % 60

print(f"\n📊 변환 결과:")
print(f"{total_seconds}초 = {hours}시간 {minutes}분 {seconds}초")

# 다른 단위로도 표현
days = hours // 24
remaining_hours = hours % 24

if days > 0:
    print(f"또는 {days}일 {remaining_hours}시간 {minutes}분 {seconds}초")

# 1년은 몇 초인지 계산
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

seconds_per_year = (seconds_per_minute - minutes_per_hour - 
                   hours_per_day - days_per_year)

print(f"\n💡 참고: 1년은 {seconds_per_year:,}초입니다!")

if total_seconds >= seconds_per_year:
    years = total_seconds // seconds_per_year
    print(f"입력하신 시간은 약 {years}년입니다!")
```

#### 🌊 실수형 (float) 완전 정복

```python
# 다양한 실수 표현
normal_float = 3.14159
scientific1 = 1.23e4      # 1.23 × 10^4 = 12300
scientific2 = 5.67e-3     # 5.67 × 10^-3 = 0.00567

print("일반 실수:", normal_float)
print("과학적 표기법 1:", scientific1)
print("과학적 표기법 2:", scientific2)

# 실수의 정밀도 문제
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")  # 0.30000000000000004
print(f"정확히 0.3인가? {result == 0.3}")  # False!

# 해결 방법: round() 함수
rounded_result = round(result, 1)
print(f"반올림한 결과: {rounded_result}")
print(f"이제 0.3인가? {rounded_result == 0.3}")  # True!

# 실수 관련 유용한 함수들
import math

number = 16.789
print(f"\n실수 {number}에 대한 연산:")
print(f"올림: {math.ceil(number)}")      # 17
print(f"내림: {math.floor(number)}")     # 16
print(f"반올림: {round(number)}")        # 17
print(f"소수점 2자리: {round(number, 2)}")  # 16.79
print(f"절댓값: {abs(-number)}")         # 16.789
print(f"제곱근: {math.sqrt(number)}")    # 4.098...
```

#### 🎯 실수 실습: 원의 넓이와 둘레

```python
# 파일명: circle_calculator.py
import math

print("🔵 원의 넓이와 둘레 계산기")
print("=" - 30)

# 반지름 입력
radius = float(input("반지름을 입력하세요 (cm): "))

# 계산
area = math.pi - radius -- 2      # 넓이 = π × r²
circumference = 2 - math.pi - radius  # 둘레 = 2 × π × r

# 결과 출력
print(f"\n📊 계산 결과:")
print(f"반지름: {radius} cm")
print(f"지름: {radius - 2} cm")
print(f"넓이: {area:.2f} cm²")
print(f"둘레: {circumference:.2f} cm")

# 추가 정보
if radius > 0:
    print(f"\n💡 추가 정보:")
    print(f"파이(π) 값: {math.pi:.10f}")
    print(f"넓이/둘레 비율: {area/circumference:.3f}")
    
    # 넓이가 100 이상이면 큰 원
    if area >= 100:
        print("🔴 이것은 큰 원입니다!")
    else:
        print("🔵 이것은 작은 원입니다!")
```

#### 📝 문자열 (str) 완전 정복

```python
# 다양한 문자열 표현
single_quote = '안녕하세요'
double_quote = "Hello"
triple_quote = """여러 줄
문자열
입니다"""

print("작은따옴표:", single_quote)
print("큰따옴표:", double_quote)
print("삼중따옴표:")
print(triple_quote)

# 문자열 내 따옴표 사용
sentence1 = "He said 'Hello'"  # 큰따옴표 안에 작은따옴표
sentence2 = 'She said "Hi"'    # 작은따옴표 안에 큰따옴표
sentence3 = "It's a \"quote\""  # 이스케이프 문자 사용

print(sentence1)
print(sentence2)
print(sentence3)

# 문자열 연산
first_name = "길동"
last_name = "홍"
full_name = last_name + first_name  # 문자열 합치기
print("전체 이름:", full_name)

greeting = "안녕" - 3  # 문자열 반복
print("반복 인사:", greeting)

# 문자열 길이와 인덱싱
text = "파이썬 프로그래밍"
print(f"문자열 길이: {len(text)}")
print(f"첫 번째 글자: {text[0]}")
print(f"마지막 글자: {text[-1]}")
print(f"3~5번째 글자: {text[2:5]}")

# f-string 활용
name = "김파이썬"
age = 25
height = 175.5

# 여러 방식의 문자열 포맷팅
old_style = "이름: %s, 나이: %d" % (name, age)
format_style = "이름: {}, 나이: {}".format(name, age)
f_string = f"이름: {name}, 나이: {age}, 키: {height:.1f}cm"

print("옛날 방식:", old_style)
print("format 방식:", format_style)
print("f-string:", f_string)  # 가장 권장되는 방식!
```

#### ✅ 불린형 (bool) 완전 정복

```python
# 기본 불린 값
is_sunny = True
is_raining = False

print("맑은 날씨:", is_sunny)
print("비 오는 날씨:", is_raining)

# 비교 연산의 결과는 불린
age = 20
is_adult = age >= 18
can_drink = age >= 21

print(f"나이 {age}세")
print(f"성인인가? {is_adult}")
print(f"음주 가능? {can_drink}")

# 다양한 값의 불린 변환
print("\n다양한 값의 불린 변환:")
values = [0, 1, -1, "", "hello", [], [1, 2], None]

for value in values:
    print(f"{str(value):>8} → {bool(value)}")

# 불린 연산 (논리 연산)
a = True
b = False

print(f"\n논리 연산:")
print(f"a = {a}, b = {b}")
print(f"a and b = {a and b}")  # 둘 다 True여야 True
print(f"a or b = {a or b}")    # 하나만 True여도 True  
print(f"not a = {not a}")      # 반대 값
print(f"not b = {not b}")

# 실용적인 예제
temperature = 25
humidity = 60
is_comfortable = (20 <= temperature <= 26) and (40 <= humidity <= 70)

print(f"\n날씨 쾌적도 판단:")
print(f"온도: {temperature}°C")
print(f"습도: {humidity}%")
print(f"쾌적한가? {is_comfortable}")
```

#### 🔍 type() 함수로 타입 확인

```python
# 다양한 데이터의 타입 확인
data_samples = [
    42,           # int
    3.14,         # float
    "Hello",      # str
    True,         # bool
    [1, 2, 3],    # list (나중에 배울 것)
    None          # NoneType
]

print("📋 데이터 타입 확인:")
print("-" - 30)

for i, data in enumerate(data_samples, 1):
    data_type = type(data)
    type_name = data_type.__name__  # 타입 이름만 추출
    
    print(f"{i}. {str(data):>10} → {type_name}")

# isinstance() 함수 - 타입 검사에 더 좋은 방법
number = 42
print(f"\nisinstance() 함수 사용:")
print(f"{number}은 정수인가? {isinstance(number, int)}")
print(f"{number}은 실수인가? {isinstance(number, float)}")
print(f"{number}은 문자열인가? {isinstance(number, str)}")

# 입력값의 타입을 확인하는 실용적인 예제
def check_input_type():
    user_input = input("아무 값이나 입력하세요: ")
    
    print(f"\n입력값: '{user_input}'")
    print(f"타입: {type(user_input).__name__}")  # 항상 str!
    
    # 숫자인지 확인
    if user_input.isdigit():
        print("→ 정수로 변환 가능")
    elif user_input.replace('.', '').isdigit():
        print("→ 실수로 변환 가능")
    else:
        print("→ 문자열입니다")

check_input_type()
```

---

### Part 3: 형변환과 응용 (50분)

#### 🔄 형변환 함수 완전 정복

```python
# 기본 형변환
print("📊 기본 형변환 예제")
print("=" - 30)

# 문자열 → 숫자
str_number = "123"
int_number = int(str_number)
float_number = float(str_number)

print(f"문자열 '{str_number}' → 정수: {int_number}")
print(f"문자열 '{str_number}' → 실수: {float_number}")

# 숫자 → 문자열
number = 456
str_from_int = str(number)
print(f"정수 {number} → 문자열: '{str_from_int}'")

# 실수 → 정수 (소수점 버림!)
float_num = 3.9
int_from_float = int(float_num)
print(f"실수 {float_num} → 정수: {int_from_float}")

# 불린 변환
print(f"\n불린 변환:")
print(f"int(True) = {int(True)}")    # 1
print(f"int(False) = {int(False)}")  # 0
print(f"bool(1) = {bool(1)}")        # True
print(f"bool(0) = {bool(0)}")        # False

# 형변환 오류 처리
print(f"\n⚠️ 형변환 오류 예제:")
try:
    result = int("hello")  # 오류 발생!
except ValueError as e:
    print(f"오류 발생: {e}")

# 안전한 형변환 함수
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}'는 정수로 변환할 수 없습니다.")
        return None

print(f"\n안전한 변환:")
print(f"safe_int_convert('123') = {safe_int_convert('123')}")
print(f"safe_int_convert('abc') = {safe_int_convert('abc')}")
```

#### 🎯 실습 1: 점수 입력받아 평균 계산

```python
# 파일명: grade_average.py
print("📊 학생 성적 평균 계산기")
print("=" - 30)

# 학생 정보 입력
student_name = input("학생 이름을 입력하세요: ")
student_id = input("학번을 입력하세요: ")

print(f"\n👤 {student_name} ({student_id}) 학생의 성적 입력")
print("-" - 40)

# 과목별 점수 입력 (문자열로 받아서 정수로 변환)
subjects = ["국어", "영어", "수학", "과학", "사회"]
scores = []
total_score = 0

for subject in subjects:
    while True:  # 올바른 점수를 입력할 때까지 반복
        try:
            score_input = input(f"{subject} 점수 (0-100): ")
            score = int(score_input)
            
            # 점수 유효성 검사
            if 0 <= score <= 100:
                scores.append(score)
                total_score += score
                break
            else:
                print("❌ 점수는 0-100 사이여야 합니다.")
        except ValueError:
            print("❌ 숫자만 입력해주세요.")

# 평균 계산
average = total_score / len(subjects)
average_float = float(total_score) / len(subjects)  # 명시적 형변환

# 등급 계산
if average >= 90:
    grade = "A"
    comment = "매우 우수"
elif average >= 80:
    grade = "B"
    comment = "우수"
elif average >= 70:
    grade = "C"
    comment = "보통"
elif average >= 60:
    grade = "D"
    comment = "노력 필요"
else:
    grade = "F"
    comment = "재수강 필요"

# 결과 출력
print("\n" + "🏆" - 40)
print(f"          📋 {student_name} 성적표")
print("🏆" - 40)

for i, subject in enumerate(subjects):
    print(f"{subject}: {scores[i]:>3}점")

print("-" - 30)
print(f"총점: {total_score}점")
print(f"평균: {average:.2f}점")
print(f"등급: {grade} ({comment})")

# 데이터 타입 정보 출력 (학습용)
print(f"\n🔍 데이터 타입 정보:")
print(f"총점의 타입: {type(total_score).__name__}")
print(f"평균의 타입: {type(average).__name__}")
print(f"등급의 타입: {type(grade).__name__}")

# 각 점수를 문자열로 변환하여 저장
scores_str = [str(score) for score in scores]
print(f"점수들을 문자열로: {scores_str}")
print(f"문자열 점수들의 타입: {type(scores_str[0]).__name__}")

print("🏆" - 40)
```

#### 🌡️ 실습 2: 온도 변환기 (섭씨 ↔ 화씨)

```python
# 파일명: temperature_converter.py
import math

print("🌡️ 고급 온도 변환기")
print("=" - 25)

def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환"""
    return (celsius - 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환"""
    return (fahrenheit - 32) - 5/9

def celsius_to_kelvin(celsius):
    """섭씨를 켈빈으로 변환"""
    return celsius + 273.15

def get_temperature_description(celsius):
    """온도에 따른 설명 반환"""
    if celsius <= -40:
        return "🥶 극한의 추위 (생존 위험)"
    elif celsius <= 0:
        return "🧊 어는점 이하 (얼음)"
    elif celsius <= 10:
        return "❄️ 매우 추움"
    elif celsius <= 20:
        return "😊 시원함"
    elif celsius <= 30:
        return "🌤️ 적당함"
    elif celsius <= 35:
        return "🌡️ 더움"
    elif celsius <= 40:
        return "🔥 매우 더움"
    else:
        return "☠️ 극한의 더위 (위험)"

# 메인 프로그램
while True:
    print("\n🌡️ 온도 변환 메뉴:")
    print("1. 섭씨 → 화씨")
    print("2. 화씨 → 섭씨")
    print("3. 섭씨 → 켈빈")
    print("4. 종합 변환")
    print("5. 종료")
    
    choice = input("\n선택하세요 (1-5): ")
    
    if choice == "5":
        print("👋 프로그램을 종료합니다!")
        break
    
    # 온도 입력 및 형변환
    try:
        if choice in ["1", "3", "4"]:
            temp_input = input("섭씨 온도를 입력하세요: ")
            temperature = float(temp_input)  # 문자열 → 실수 변환
            
            if choice == "1":
                fahrenheit = celsius_to_fahrenheit(temperature)
                print(f"\n📊 변환 결과:")
                print(f"{temperature}°C = {fahrenheit:.2f}°F")
                print(f"상태: {get_temperature_description(temperature)}")
                
            elif choice == "3":
                kelvin = celsius_to_kelvin(temperature)
                print(f"\n📊 변환 결과:")
                print(f"{temperature}°C = {kelvin:.2f}K")
                print(f"상태: {get_temperature_description(temperature)}")
                
            elif choice == "4":
                fahrenheit = celsius_to_fahrenheit(temperature)
                kelvin = celsius_to_kelvin(temperature)
                description = get_temperature_description(temperature)
                
                print(f"\n📊 종합 변환 결과:")
                print("=" - 35)
                print(f"입력 온도: {temperature}°C")
                print(f"화씨 온도: {fahrenheit:.2f}°F")
                print(f"켈빈 온도: {kelvin:.2f}K")
                print(f"온도 상태: {description}")
                
                # 추가 정보
                print(f"\n💡 추가 정보:")
                if temperature == 0:
                    print("🧊 물의 어는점입니다!")
                elif temperature == 100:
                    print("💨 물의 끓는점입니다!")
                elif temperature == 37:
                    print("🌡️ 사람의 체온입니다!")
                
                # 절댓값 온도 (켈빈 기준)
                if kelvin < 0:
                    print("❌ 절대영도보다 낮은 온도는 불가능합니다!")
                
        elif choice == "2":
            temp_input = input("화씨 온도를 입력하세요: ")
            fahrenheit_temp = float(temp_input)  # 문자열 → 실수 변환
            
            celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
            print(f"\n📊 변환 결과:")
            print(f"{fahrenheit_temp}°F = {celsius_temp:.2f}°C")
            print(f"상태: {get_temperature_description(celsius_temp)}")
            
        else:
            print("❌ 잘못된 선택입니다. 1-5 중에서 선택하세요.")
            
    except ValueError:
        print("❌ 올바른 숫자를 입력해주세요!")
    
    # 계속 여부 확인
    continue_choice = input("\n계속하시겠습니까? (y/n): ").lower()
    if continue_choice != 'y':
        print("👋 프로그램을 종료합니다!")
        break

print("\n🌡️ 온도 변환기를 이용해주셔서 감사합니다!")

# 형변환 데모
print("\n🔍 이 프로그램에서 사용된 형변환들:")
print("1. input() → str (사용자 입력)")
print("2. str → float (온도값 변환)")
print("3. float → str (출력을 위한 변환)")
print("4. int → str (메뉴 번호 비교)")
```

#### 🧮 고급 형변환 실습

```python
# 파일명: advanced_conversion.py
print("🧮 고급 데이터 변환 실습")
print("=" - 30)

# 1. 복잡한 문자열 파싱
data_string = "이름:김철수,나이:25,키:175.5,학생:True"
print(f"원본 데이터: {data_string}")

# 문자열을 파싱해서 딕셔너리로 만들기
data_dict = {}
items = data_string.split(',')

for item in items:
    key, value = item.split(':')
    
    # 값의 타입을 추론해서 변환
    if value.isdigit():
        data_dict[key] = int(value)
    elif value.replace('.', '').isdigit():
        data_dict[key] = float(value)
    elif value.lower() in ['true', 'false']:
        data_dict[key] = value.lower() == 'true'
    else:
        data_dict[key] = value

print("\n파싱된 결과:")
for key, value in data_dict.items():
    print(f"{key}: {value} ({type(value).__name__})")

# 2. 진법 변환
print(f"\n🔢 진법 변환:")
number = 42

# 10진수를 다른 진법으로
binary = bin(number)[2:]    # 2진수 (0b 제거)
octal = oct(number)[2:]     # 8진수 (0o 제거)
hexadecimal = hex(number)[2:]  # 16진수 (0x 제거)

print(f"10진수 {number}:")
print(f"2진수: {binary}")
print(f"8진수: {octal}")
print(f"16진수: {hexadecimal}")

# 다른 진법을 10진수로
print(f"\n역변환:")
print(f"2진수 '{binary}' → 10진수: {int(binary, 2)}")
print(f"8진수 '{octal}' → 10진수: {int(octal, 8)}")
print(f"16진수 '{hexadecimal}' → 10진수: {int(hexadecimal, 16)}")

# 3. 리스트와 문자열 간 변환
numbers = [1, 2, 3, 4, 5]
numbers_str = [str(num) for num in numbers]  # 각 요소를 문자열로
joined_str = ','.join(numbers_str)           # 쉼표로 연결

print(f"\n📋 리스트/문자열 변환:")
print(f"숫자 리스트: {numbers}")
print(f"문자 리스트: {numbers_str}")
print(f"연결된 문자열: '{joined_str}'")

# 역변환
split_list = joined_str.split(',')           # 쉼표로 분리
back_to_numbers = [int(s) for s in split_list]  # 다시 숫자로

print(f"분리된 문자열: {split_list}")
print(f"다시 숫자 리스트: {back_to_numbers}")

# 4. 타입 검증 함수
def validate_and_convert(value, target_type):
    """값을 검증하고 지정된 타입으로 변환"""
    try:
        if target_type == int:
            result = int(value)
        elif target_type == float:
            result = float(value)
        elif target_type == str:
            result = str(value)
        elif target_type == bool:
            if isinstance(value, str):
                result = value.lower() in ['true', '1', 'yes', 'on']
            else:
                result = bool(value)
        else:
            raise ValueError("지원하지 않는 타입입니다.")
        
        return True, result
    except ValueError as e:
        return False, str(e)

# 테스트
test_values = ["123", "45.67", "True", "hello", "0"]
target_types = [int, float, bool, str, bool]

print(f"\n🧪 타입 변환 테스트:")
for value, target in zip(test_values, target_types):
    success, result = validate_and_convert(value, target)
    status = "✅" if success else "❌"
    print(f"{status} '{value}' → {target.__name__}: {result}")
```

---

## 📝 연습 문제 (6개)

### 문제 1: 변수 교환
두 변수 a=10, b=20이 있을 때, 임시 변수를 사용하지 않고 두 변수의 값을 교환하세요.

--해답--:
```python
a = 10
b = 20
print(f"교환 전: a={a}, b={b}")

# 파이썬의 튜플 언패킹 활용
a, b = b, a

print(f"교환 후: a={a}, b={b}")
```

### 문제 2: 타입 변환 체인
문자열 "123.45"를 실수로 변환한 후, 정수로 변환하고, 다시 문자열로 변환하는 과정을 보여주세요. 각 단계에서 타입과 값을 출력하세요.

--해답--:
```python
original = "123.45"
print(f"1단계 - 원본: '{original}' ({type(original).__name__})")

step2 = float(original)
print(f"2단계 - 실수: {step2} ({type(step2).__name__})")

step3 = int(step2)
print(f"3단계 - 정수: {step3} ({type(step3).__name__})")

step4 = str(step3)
print(f"4단계 - 문자열: '{step4}' ({type(step4).__name__})")
```

### 문제 3: 불린 변환 테스트
다음 값들을 불린으로 변환했을 때 결과를 예측하고 검증하세요: 0, 1, -1, "", "False", [], [0]

--해답--:
```python
test_values = [0, 1, -1, "", "False", [], [0]]

print("불린 변환 결과:")
for value in test_values:
    bool_result = bool(value)
    print(f"{str(value):>8} → {bool_result}")
```

### 문제 4: 사용자 정보 입력 프로그램
사용자로부터 이름(문자열), 나이(정수), 키(실수), 결혼여부(불린)를 입력받아 저장하고 모든 정보를 출력하세요.

--해답--:
```python
print("📝 사용자 정보 입력")

name = input("이름: ")
age = int(input("나이: "))
height = float(input("키 (cm): "))
married_input = input("결혼 여부 (y/n): ").lower()
is_married = married_input == 'y'

print(f"\n👤 입력된 정보:")
print(f"이름: {name} ({type(name).__name__})")
print(f"나이: {age}세 ({type(age).__name__})")
print(f"키: {height}cm ({type(height).__name__})")
print(f"결혼 여부: {'기혼' if is_married else '미혼'} ({type(is_married).__name__})")
```

### 문제 5: 계산기
두 수와 연산자(+, -, -, /)를 입력받아 계산하는 프로그램을 작성하세요. 나눗셈시 0으로 나누는 경우를 처리하세요.

--해답--:
```python
print("🧮 간단 계산기")

num1 = float(input("첫 번째 수: "))
operator = input("연산자 (+, -, -, /): ")
num2 = float(input("두 번째 수: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '-':
    result = num1 - num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("❌ 0으로 나눌 수 없습니다!")
        exit()
else:
    print("❌ 잘못된 연산자입니다!")
    exit()

print(f"결과: {num1} {operator} {num2} = {result}")
```

### 문제 6: 데이터 검증기
사용자로부터 점수를 입력받되, 0-100 사이의 정수가 아닐 경우 다시 입력받도록 하는 프로그램을 작성하세요.

--해답--:
```python
print("📊 점수 입력 (0-100)")

while True:
    try:
        score_input = input("점수를 입력하세요: ")
        score = int(score_input)
        
        if 0 <= score <= 100:
            print(f"✅ 입력된 점수: {score}점")
            break
        else:
            print("❌ 점수는 0-100 사이여야 합니다.")
    except ValueError:
        print("❌ 정수만 입력해주세요.")
```

---

## 🚀 도전 과제 (2개)

### 도전 과제 1: 진법 변환기
사용자로부터 숫자와 진법을 입력받아 2진법, 8진법, 10진법, 16진법으로 모두 변환하여 보여주는 프로그램을 작성하세요.

--해답--:
```python
print("🔢 진법 변환기")

def convert_to_decimal(number_str, from_base):
    """주어진 진법의 숫자를 10진법으로 변환"""
    return int(number_str, from_base)

def display_all_bases(decimal_num):
    """10진수를 모든 진법으로 표시"""
    print(f"\n📊 변환 결과 (10진수 {decimal_num}):")
    print(f"2진법:  {bin(decimal_num)}")
    print(f"8진법:  {oct(decimal_num)}")
    print(f"10진법: {decimal_num}")
    print(f"16진법: {hex(decimal_num)}")

while True:
    try:
        number = input("\n숫자를 입력하세요: ")
        base = int(input("현재 진법 (2, 8, 10, 16): "))
        
        if base not in [2, 8, 10, 16]:
            print("❌ 2, 8, 10, 16 중에서 선택하세요.")
            continue
        
        decimal = convert_to_decimal(number, base)
        display_all_bases(decimal)
        
        if input("계속하시겠습니까? (y/n): ").lower() != 'y':
            break
            
    except ValueError:
        print("❌ 올바른 형식으로 입력해주세요.")

print("👋 프로그램을 종료합니다!")
```

### 도전 과제 2: 데이터 타입 분석기
문자열을 입력받아 그 안에 포함된 숫자, 문자, 특수문자의 개수를 세고, 숫자들만 추출하여 합계를 구하는 프로그램을 작성하세요.

--해답--:
```python
print("🔍 데이터 타입 분석기")

def analyze_string(text):
    """문자열을 분석하여 통계 정보 반환"""
    digits = []
    letters = []
    special_chars = []
    numbers = []
    
    i = 0
    while i < len(text):
        char = text[i]
        
        if char.isdigit():
            digits.append(char)
            # 연속된 숫자들을 하나의 수로 처리
            num_str = char
            i += 1
            while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                num_str += text[i]
                i += 1
            try:
                if '.' in num_str:
                    numbers.append(float(num_str))
                else:
                    numbers.append(int(num_str))
            except ValueError:
                pass
            i -= 1
        elif char.isalpha():
            letters.append(char)
        elif not char.isspace():
            special_chars.append(char)
        
        i += 1
    
    return {
        'digits': digits,
        'letters': letters,
        'special_chars': special_chars,
        'numbers': numbers
    }

while True:
    text = input("\n분석할 문자열을 입력하세요: ")
    
    if not text:
        print("👋 프로그램을 종료합니다!")
        break
    
    result = analyze_string(text)
    
    print(f"\n📊 분석 결과:")
    print(f"입력 문자열: '{text}'")
    print(f"전체 길이: {len(text)}자")
    print(f"숫자 개수: {len(result['digits'])}개")
    print(f"문자 개수: {len(result['letters'])}개") 
    print(f"특수문자 개수: {len(result['special_chars'])}개")
    
    if result['digits']:
        print(f"발견된 숫자들: {result['digits']}")
    
    if result['numbers']:
        print(f"추출된 수들: {result['numbers']}")
        print(f"수들의 합계: {sum(result['numbers'])}")
        print(f"수들의 평균: {sum(result['numbers'])/len(result['numbers']):.2f}")
    
    if result['letters']:
        print(f"문자들: {result['letters']}")
        
    if result['special_chars']:
        print(f"특수문자들: {result['special_chars']}")
```

---

## ❌ 흔한 실수와 해결법

### 1. 형변환 오류
--문제--:
```python
age = input("나이: ")
next_year = age + 1  # TypeError!
```

--해결--:
```python
age = int(input("나이: "))
next_year = age + 1  # 올바름
```

### 2. 변수명 규칙 위반
--문제--:
```python
1st_name = "김철수"    # SyntaxError!
user-name = "홍길동"   # SyntaxError!
```

--해결--:
```python
first_name = "김철수"   # 올바름
user_name = "홍길동"    # 올바름
```

### 3. 대소문자 구분
--문제--:
```python
Name = "김철수"
print(name)  # NameError!
```

--해결--:
```python
name = "김철수"
print(name)  # 올바름
```

### 4. 불린 변환 착각
--문제--:
```python
flag = "False"
if flag:  # 문자열 "False"는 True!
    print("실행됨")
```

--해결--:
```python
flag = False  # 또는
flag_str = "False"
flag = flag_str.lower() == "true"
```

### 5. 실수의 정밀도 문제
--문제--:
```python
result = 0.1 + 0.2
print(result == 0.3)  # False!
```

--해결--:
```python
result = 0.1 + 0.2
print(round(result, 1) == 0.3)  # True
```

---

## ✅ 학습 체크리스트

이번 주 학습을 완료했다면 다음 항목들을 체크해보세요:

- [ ] 변수의 개념과 메모리에서의 역할을 이해합니다
- [ ] 파이썬의 4가지 기본 데이터 타입을 구분할 수 있습니다
- [ ] 올바른 변수명 규칙을 준수하여 변수를 선언할 수 있습니다
- [ ] `type()` 함수로 데이터 타입을 확인할 수 있습니다
- [ ] `int()`, `float()`, `str()`, `bool()` 함수로 형변환을 할 수 있습니다
- [ ] 형변환 오류를 예상하고 적절히 처리할 수 있습니다
- [ ] 여러 변수를 동시에 할당하고 값을 교환할 수 있습니다
- [ ] 실수의 정밀도 문제를 인식하고 해결할 수 있습니다
- [ ] 불린 값의 변환 규칙을 이해합니다
- [ ] 복합적인 데이터 처리 프로그램을 작성할 수 있습니다

--완료율--: ___/10 항목

---

## 📖 다음 주 예습 내용

--Week 4: 연산자--에서는 다음 내용을 학습합니다:

### 🔍 미리 살펴보기
1. --산술 연산자--: +, -, -, /, //, %, --
2. --비교 연산자--: ==, !=, <, >, <=, >=
3. --논리 연산자--: and, or, not
4. --대입 연산자--: +=, -=, -=, /=
5. --연산자 우선순위--: 계산 순서 이해

### 📚 사전 준비
다음 코드들을 미리 실행해보세요:
```python
# 산술 연산
a, b = 17, 5
print(f"{a} / {b} = {a / b}")      # 나눗셈
print(f"{a} // {b} = {a // b}")    # 몫
print(f"{a} % {b} = {a % b}")      # 나머지

# 비교 연산
age = 20
print(f"성인인가? {age >= 18}")

# 논리 연산
is_sunny = True
is_warm = False
print(f"피크닉 가기 좋은가? {is_sunny and is_warm}")
```

---

## 🔗 참고 자료

### 📖 추가 학습
- [파이썬 데이터 타입 공식 문서](https://docs.python.org/ko/3/library/stdtypes.html)
- [변수와 객체 이해하기](https://docs.python.org/ko/3/reference/datamodel.html)
- [파이썬 네이밍 컨벤션 PEP 8](https://peps.python.org/pep-0008/#naming-conventions)

### 🛠️ 실습 도구
- [Python Tutor](http://pythontutor.com/) - 변수와 메모리 시각화
- [Repl.it](https://replit.com/languages/python3) - 온라인 파이썬 환경

### 💡 프로그래밍 팁

#### 🎯 좋은 변수명 만들기
```python
# 나쁜 예
a = 25
x = "김철수"
temp = 36.5

# 좋은 예  
student_age = 25
student_name = "김철수"
body_temperature = 36.5
```

#### 🔍 타입 체크 습관
```python
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "숫자만 입력해주세요"
    if b == 0:
        return "0으로 나눌 수 없습니다"
    return a / b
```

---

--🎉 세 번째 주 완료! 이제 파이썬의 데이터 타입을 자유자재로 다룰 수 있습니다! 🚀--

-"좋은 변수명과 적절한 데이터 타입 선택이 좋은 프로그램의 시작입니다!"-