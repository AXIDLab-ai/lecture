# Week 2: 미리 만드는 쓸 만한 프로그램

**[← Week 1](./week01.md) | [목차](lecture/04_PythonProgramming/2.%20lectureMap.md) | [다음: Week 3 →](./week03.md)**

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **실용적인 프로그램 작성**: 일상생활에서 사용할 수 있는 프로그램을 만들 수 있습니다
2. **사용자 입력 처리**: input() 함수를 활용하여 대화형 프로그램을 작성할 수 있습니다
3. **프로그램 구조 이해**: 입력 → 처리 → 출력의 기본 구조를 이해합니다
4. **데이터 타입 변환**: 문자열과 숫자 간 변환을 자유롭게 할 수 있습니다
5. **종합적인 문제 해결**: 복합적인 계산과 조건을 포함한 프로그램을 설계할 수 있습니다

---

## 📚 핵심 개념 요약

### 1. 프로그램의 기본 구조
```
📥 입력(Input) → 🔄 처리(Process) → 📤 출력(Output)
```

- **입력**: 사용자로부터 데이터 받기 (`input()`)
- **처리**: 받은 데이터를 계산하거나 가공하기
- **출력**: 결과를 사용자에게 보여주기 (`print()`)

### 2. input() 함수 완전 정복
```python
# 기본 사용법
user_input = input("메시지: ")

# 숫자로 변환
number = int(input("정수 입력: "))      # 정수
decimal = float(input("실수 입력: "))   # 실수
```

### 3. 데이터 타입 변환
| 함수 | 설명 | 예시 |
|------|------|------|
| `int()` | 정수로 변환 | `int("123")` → 123 |
| `float()` | 실수로 변환 | `float("3.14")` → 3.14 |
| `str()` | 문자열로 변환 | `str(123)` → "123" |

### 4. 프로그램 설계 패턴
1. **문제 정의**: 무엇을 만들 것인가?
2. **입력 설계**: 어떤 데이터가 필요한가?
3. **처리 설계**: 어떤 계산을 할 것인가?
4. **출력 설계**: 결과를 어떻게 보여줄 것인가?

---

## 💻 실습 세션 (2시간)

### Part 1: 사용자 입력 받기 (30분)

#### 🎤 input() 함수 기초

**기본 사용법**:
```python
# 간단한 입력받기
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님!")
```

**실행 결과**:
```
이름을 입력하세요: 홍길동
안녕하세요, 홍길동님!
```

#### 🔄 데이터 타입 변환 실습

```python
# 잘못된 예 - 문자열로 받아짐
age = input("나이를 입력하세요: ")
next_year = age + 1  # 오류 발생!

# 올바른 예
age = int(input("나이를 입력하세요: "))
next_year = age + 1
print(f"내년에는 {next_year}살이 되시는군요!")
```

#### 👋 인사 프로그램 만들기

```python
# 파일명: greeting_program.py
print("🤖 개인 맞춤형 인사 프로그램")
print("=" * 35)

# 사용자 정보 입력받기
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
hobby = input("취미를 입력하세요: ")
favorite_food = input("좋아하는 음식을 입력하세요: ")

# 개인화된 인사말 출력
print("\n" + "🌟" * 30)
print(f"안녕하세요, {name}님!")
print(f"나이가 {age}살이시군요!")

if age < 20:
    print("아직 어리시네요. 꿈을 향해 화이팅!")
elif age < 30:
    print("청춘이시네요! 많은 경험을 쌓아보세요!")
else:
    print("인생의 멘토가 되어주세요!")

print(f"취미가 {hobby}라니, 멋지네요! 🎯")
print(f"{favorite_food}는 정말 맛있죠! 🍽️")
print("🌟" * 30)
print("즐거운 하루 되세요! 😊")
```

#### 🎯 연습 미니 실습

**실습 1**: 좋아하는 색깔과 동물을 입력받아 "당신은 [색깔] 색을 좋아하고 [동물]를 좋아하는 분이시군요!"라고 출력하기

```python
color = input("좋아하는 색깔: ")
animal = input("좋아하는 동물: ")
print(f"당신은 {color} 색을 좋아하고 {animal}를 좋아하는 분이시군요!")
```

---

### Part 2: 실용 프로그램 예제 (40분)

#### 📅 Example 1: 나이 계산 프로그램

```python
# 파일명: age_calculator.py
print("📅 정확한 나이 계산 프로그램")
print("=" * 30)

# 현재 날짜 정보
current_year = 2024
current_month = 12
current_day = 15

print(f"오늘 날짜: {current_year}년 {current_month}월 {current_day}일")
print()

# 사용자 생년월일 입력
birth_year = int(input("태어난 년도를 입력하세요 (예: 2000): "))
birth_month = int(input("태어난 월을 입력하세요 (예: 3): "))
birth_day = int(input("태어난 일을 입력하세요 (예: 15): "))

# 나이 계산
age = current_year - birth_year

# 생일이 지났는지 확인
if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    age -= 1

# 다음 생일까지 남은 일수 계산 (간단 버전)
if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    days_to_birthday = (birth_month - current_month) * 30 + (birth_day - current_day)
else:
    days_to_birthday = (12 - current_month + birth_month) * 30 + (birth_day - current_day)

# 결과 출력
print("\n" + "🎂" * 25)
print(f"당신의 정확한 나이: {age}세")
print(f"생년월일: {birth_year}년 {birth_month}월 {birth_day}일")
print(f"다음 생일까지 약 {days_to_birthday}일 남았습니다!")

# 나이대별 메시지
if age < 10:
    message = "어린이시군요! 꿈을 크게 키우세요! 🌟"
elif age < 20:
    message = "청소년이시군요! 열심히 공부하세요! 📚"
elif age < 30:
    message = "청년이시군요! 많은 도전을 해보세요! 🚀"
elif age < 65:
    message = "어른이시군요! 경험을 나눠주세요! 🎯"
else:
    message = "어르신이시군요! 건강하세요! 🌸"

print(message)
print("🎂" * 25)
```

#### 💱 Example 2: 환율 계산기

```python
# 파일명: exchange_calculator.py
print("💱 실시간 환율 계산기")
print("=" * 25)

# 환율 정보 (2024년 12월 기준 예시)
exchange_rates = {
    "USD": 1320,    # 달러
    "EUR": 1380,    # 유로
    "JPY": 8.9,     # 엔 (100엔당)
    "CNY": 182,     # 위안
    "GBP": 1580     # 파운드
}

print("📊 현재 환율 정보:")
print("1 USD = 1,320원")
print("1 EUR = 1,380원") 
print("100 JPY = 890원")
print("1 CNY = 182원")
print("1 GBP = 1,580원")
print()

# 사용자 입력
print("💰 환전할 금액과 통화를 선택하세요:")
amount = float(input("금액을 입력하세요: "))

print("\n통화 선택:")
print("1. USD (달러)")
print("2. EUR (유로)")
print("3. JPY (엔)")
print("4. CNY (위안)")
print("5. GBP (파운드)")

choice = input("\n번호를 선택하세요 (1-5): ")

# 환율 계산
if choice == "1":
    won = amount * exchange_rates["USD"]
    currency = "USD"
elif choice == "2":
    won = amount * exchange_rates["EUR"]
    currency = "EUR"
elif choice == "3":
    won = amount * exchange_rates["JPY"]
    currency = "JPY"
elif choice == "4":
    won = amount * exchange_rates["CNY"]
    currency = "CNY"
elif choice == "5":
    won = amount * exchange_rates["GBP"]
    currency = "GBP"
else:
    print("❌ 잘못된 선택입니다.")
    exit()

# 결과 출력
print("\n" + "💸" * 30)
print("🧮 환전 결과")
if currency == "JPY":
    print(f"{amount} {currency} = {won:,.0f}원")
else:
    print(f"{amount} {currency} = {won:,.0f}원")

# 수수료 계산 (1.5% 가정)
fee = won * 0.015
total_with_fee = won + fee

print(f"수수료 (1.5%): {fee:,.0f}원")
print(f"총 필요 금액: {total_with_fee:,.0f}원")
print("💸" * 30)

print("\n💡 TIP: 환율은 실시간으로 변동됩니다!")
```

#### ⚖️ Example 3: BMI 계산기

```python
# 파일명: bmi_calculator.py
print("⚖️ 체질량지수(BMI) 계산기")
print("=" * 30)

# 사용자 정보 입력
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
gender = input("성별을 입력하세요 (남/여): ")
height = float(input("키를 입력하세요 (cm): "))
weight = float(input("몸무게를 입력하세요 (kg): "))

# BMI 계산
height_m = height / 100  # cm를 m로 변환
bmi = weight / (height_m * height_m)

# BMI 평가
if bmi < 18.5:
    status = "저체중"
    emoji = "⬇️"
    advice = "적정 체중을 위해 건강한 체중 증가가 필요합니다."
elif bmi < 23:
    status = "정상체중"
    emoji = "✅"
    advice = "현재 체중을 잘 유지하세요!"
elif bmi < 25:
    status = "과체중"
    emoji = "⚠️"
    advice = "규칙적인 운동과 식단 관리를 추천합니다."
else:
    status = "비만"
    emoji = "🔴"
    advice = "전문의와 상담하여 체중 관리 계획을 세우세요."

# 표준 체중 계산 (간단 공식)
if gender == "남":
    standard_weight = (height - 100) * 0.9
else:
    standard_weight = (height - 100) * 0.85

weight_diff = weight - standard_weight

# 결과 출력
print("\n" + "📊" * 35)
print(f"🏥 {name}님의 건강 진단 결과")
print("📊" * 35)
print(f"👤 나이: {age}세 ({gender})")
print(f"📏 키: {height}cm")
print(f"⚖️ 몸무게: {weight}kg")
print(f"📈 BMI: {bmi:.1f}")
print(f"{emoji} 상태: {status}")
print(f"🎯 표준 체중: {standard_weight:.1f}kg")

if weight_diff > 0:
    print(f"📉 표준 체중보다 {weight_diff:.1f}kg 무거워요")
else:
    print(f"📈 표준 체중보다 {abs(weight_diff):.1f}kg 가벼워요")

print(f"\n💡 건강 조언: {advice}")

# 칼로리 소모 계산 (예시)
walking_cal = int(weight * 3.5)  # 1시간 걷기
running_cal = int(weight * 8.5)  # 1시간 달리기

print(f"\n🔥 1시간 운동 시 예상 칼로리 소모:")
print(f"🚶‍♀️ 걷기: 약 {walking_cal}kcal")
print(f"🏃‍♀️ 달리기: 약 {running_cal}kcal")
print("📊" * 35)
```

---

### Part 3: 종합 실습 (50분)

#### 🛒 쇼핑 계산기 만들기

```python
# 파일명: shopping_calculator.py
print("🛒 스마트 쇼핑 계산기")
print("=" * 25)

# 상품 정보 입력
print("📝 구매할 상품 정보를 입력하세요:")
product1 = input("첫 번째 상품명: ")
price1 = float(input("가격: "))
quantity1 = int(input("수량: "))

product2 = input("\n두 번째 상품명: ")
price2 = float(input("가격: "))
quantity2 = int(input("수량: "))

product3 = input("\n세 번째 상품명: ")
price3 = float(input("가격: "))
quantity3 = int(input("수량: "))

# 할인 정보 입력
print("\n💳 할인 혜택:")
member_discount = input("멤버십 할인이 있나요? (y/n): ").lower()
coupon_discount = float(input("쿠폰 할인율을 입력하세요 (예: 10 → 10%): "))

# 계산
subtotal1 = price1 * quantity1
subtotal2 = price2 * quantity2
subtotal3 = price3 * quantity3
total_before_discount = subtotal1 + subtotal2 + subtotal3

# 할인 적용
discount_amount = 0

# 멤버십 할인 (5%)
if member_discount == 'y':
    membership_discount = total_before_discount * 0.05
    discount_amount += membership_discount
else:
    membership_discount = 0

# 쿠폰 할인
coupon_amount = total_before_discount * (coupon_discount / 100)
discount_amount += coupon_amount

# 최종 금액
final_total = total_before_discount - discount_amount

# 배송비 계산
shipping_fee = 0 if final_total >= 30000 else 3000

# 최종 결제 금액
final_payment = final_total + shipping_fee

# 영수증 출력
print("\n" + "🧾" * 40)
print("           📋 쇼핑 영수증")
print("🧾" * 40)
print(f"🛍️  {product1:<10} {price1:>8,.0f}원 x {quantity1} = {subtotal1:>10,.0f}원")
print(f"🛍️  {product2:<10} {price2:>8,.0f}원 x {quantity2} = {subtotal2:>10,.0f}원")
print(f"🛍️  {product3:<10} {price3:>8,.0f}원 x {quantity3} = {subtotal3:>10,.0f}원")
print("-" * 50)
print(f"💰 소계:                    {total_before_discount:>15,.0f}원")

if membership_discount > 0:
    print(f"🏷️  멤버십 할인 (5%):         -{membership_discount:>10,.0f}원")
if coupon_amount > 0:
    print(f"🎫 쿠폰 할인 ({coupon_discount}%):          -{coupon_amount:>10,.0f}원")

print(f"🎯 할인 후 금액:              {final_total:>15,.0f}원")

if shipping_fee > 0:
    print(f"🚚 배송비:                   +{shipping_fee:>10,.0f}원")
    print("   (30,000원 이상 구매 시 무료배송)")
else:
    print("🚚 배송비:                        무료")

print("=" * 50)
print(f"💳 최종 결제 금액:           {final_payment:>15,.0f}원")
print("=" * 50)

# 절약 정보
savings = total_before_discount - final_total
if savings > 0:
    print(f"🎉 총 {savings:,.0f}원 절약하셨습니다!")
    
# 포인트 적립
points = int(final_payment * 0.01)  # 1% 적립
print(f"⭐ {points}포인트가 적립됩니다!")

print("\n🛒 이용해 주셔서 감사합니다!")
print("🧾" * 40)
```

#### 📊 성적 계산 프로그램

```python
# 파일명: grade_calculator.py
print("📊 종합 성적 관리 시스템")
print("=" * 30)

# 학생 정보 입력
student_name = input("학생 이름: ")
student_id = input("학번: ")
grade_level = input("학년: ")
semester = input("학기 (1 or 2): ")

print(f"\n👤 {student_name}({student_id}) - {grade_level}학년 {semester}학기")
print("=" * 40)

# 과목별 성적 입력
print("📚 과목별 성적을 입력하세요 (0-100점):")
subjects = []
scores = []
credits = []

for i in range(5):
    print(f"\n📖 {i+1}번째 과목:")
    subject = input("과목명: ")
    score = float(input("점수 (0-100): "))
    credit = int(input("학점 (1-4): "))
    
    subjects.append(subject)
    scores.append(score)
    credits.append(credit)

# 성적 계산 함수들
def score_to_grade(score):
    if score >= 95:
        return "A+", 4.5
    elif score >= 90:
        return "A", 4.0
    elif score >= 85:
        return "B+", 3.5
    elif score >= 80:
        return "B", 3.0
    elif score >= 75:
        return "C+", 2.5
    elif score >= 70:
        return "C", 2.0
    elif score >= 65:
        return "D+", 1.5
    elif score >= 60:
        return "D", 1.0
    else:
        return "F", 0.0

def calculate_gpa(scores, credits):
    total_grade_points = 0
    total_credits = sum(credits)
    
    for score, credit in zip(scores, credits):
        _, grade_point = score_to_grade(score)
        total_grade_points += grade_point * credit
    
    return total_grade_points / total_credits if total_credits > 0 else 0

# 성적표 생성
print("\n" + "📋" * 50)
print(f"           🎓 {student_name} 성적표")
print("📋" * 50)
print("과목명      점수    등급   학점   평점   성취도")
print("-" * 60)

total_score = 0
grade_points = 0
total_credits_sum = sum(credits)

for i in range(5):
    letter_grade, grade_point = score_to_grade(scores[i])
    
    # 성취도 계산
    if scores[i] >= 90:
        achievement = "우수"
    elif scores[i] >= 80:
        achievement = "양호"
    elif scores[i] >= 70:
        achievement = "보통"
    elif scores[i] >= 60:
        achievement = "노력필요"
    else:
        achievement = "재수강"
    
    print(f"{subjects[i]:<8} {scores[i]:>5.1f}   {letter_grade:>3}   {credits[i]:>2}    {grade_point:.1f}   {achievement}")
    total_score += scores[i]
    grade_points += grade_point * credits[i]

# 통계 계산
average_score = total_score / 5
gpa = grade_points / total_credits_sum

print("-" * 60)
print(f"📊 종합 통계:")
print(f"평균 점수: {average_score:.2f}점")
print(f"총 학점: {total_credits_sum}학점")
print(f"평점 평균 (GPA): {gpa:.3f}")

# 학사 경고 여부
if gpa < 1.75:
    warning = "⚠️ 학사 경고"
elif gpa < 2.0:
    warning = "📢 주의 필요"
elif gpa >= 3.5:
    warning = "🏆 우등생"
else:
    warning = "✅ 정상"

print(f"학사 상태: {warning}")

# 순위 예측 (가정)
if gpa >= 4.0:
    rank_estimate = "상위 10% 예상"
elif gpa >= 3.5:
    rank_estimate = "상위 20% 예상"
elif gpa >= 3.0:
    rank_estimate = "상위 40% 예상"
elif gpa >= 2.5:
    rank_estimate = "중위권 예상"
else:
    rank_estimate = "하위권 예상"

print(f"성적 순위: {rank_estimate}")

# 개선 조언
print(f"\n💡 학습 조언:")
low_scores = [subjects[i] for i, score in enumerate(scores) if score < 80]
if low_scores:
    print(f"📚 보완이 필요한 과목: {', '.join(low_scores)}")
    print("🎯 해당 과목의 학습 시간을 늘려보세요!")
else:
    print("🌟 모든 과목에서 우수한 성적을 거두었습니다!")

if gpa < 3.0:
    print("📖 스터디 그룹 참여나 튜터링을 고려해보세요.")
    print("🕐 계획적인 시간 관리로 성적 향상을 노려보세요.")

print("📋" * 50)
```

---

## 📝 연습 문제 (5개)

### 문제 1: 단위 변환기
사용자로부터 미터(m) 단위의 거리를 입력받아 킬로미터(km), 센티미터(cm), 밀리미터(mm)로 변환하여 출력하세요.

**해답**:
```python
meters = float(input("미터를 입력하세요: "))
kilometers = meters / 1000
centimeters = meters * 100
millimeters = meters * 1000

print(f"{meters}m = {kilometers}km")
print(f"{meters}m = {centimeters}cm") 
print(f"{meters}m = {millimeters}mm")
```

### 문제 2: 온도 변환기
섭씨 온도를 입력받아 화씨 온도로 변환하고, 날씨 상태도 출력하세요.
- 화씨 = 섭씨 × 9/5 + 32
- 0도 이하: "얼어요!", 0-10도: "춥네요", 11-25도: "시원해요", 26도 이상: "더워요!"

**해답**:
```python
celsius = float(input("섭씨 온도를 입력하세요: "))
fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C = {fahrenheit}°F")

if celsius <= 0:
    print("얼어요!")
elif celsius <= 10:
    print("춥네요")
elif celsius <= 25:
    print("시원해요")
else:
    print("더워요!")
```

### 문제 3: 할인 계산기
상품 가격과 할인율을 입력받아 할인된 가격과 절약 금액을 계산하세요.

**해답**:
```python
price = float(input("상품 가격을 입력하세요: "))
discount_rate = float(input("할인율을 입력하세요 (%): "))

discount_amount = price * (discount_rate / 100)
final_price = price - discount_amount

print(f"원가: {price:,.0f}원")
print(f"할인 금액: {discount_amount:,.0f}원")
print(f"할인된 가격: {final_price:,.0f}원")
```

### 문제 4: 시간 계산기
초(second) 단위의 시간을 입력받아 시, 분, 초로 변환하여 출력하세요.

**해답**:
```python
total_seconds = int(input("초를 입력하세요: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds}초 = {hours}시간 {minutes}분 {seconds}초")
```

### 문제 5: 팁 계산기
식사 금액과 서비스 만족도를 입력받아 적절한 팁을 계산하세요.
- 우수: 20%, 양호: 15%, 보통: 10%

**해답**:
```python
bill = float(input("식사 금액을 입력하세요: "))
service = input("서비스 만족도 (우수/양호/보통): ")

if service == "우수":
    tip_rate = 0.20
elif service == "양호":
    tip_rate = 0.15
else:
    tip_rate = 0.10

tip = bill * tip_rate
total = bill + tip

print(f"팁 ({tip_rate*100}%): {tip:,.0f}원")
print(f"총 금액: {total:,.0f}원")
```

---

## 🚀 도전 과제 (2개)

### 도전 과제 1: 종합 건강 관리 프로그램
사용자의 신체 정보와 운동량을 입력받아 다음을 계산하는 프로그램을 작성하세요:
1. BMI 계산 및 평가
2. 하루 권장 칼로리 계산 (기초대사율 + 활동대사율)
3. 목표 체중까지 몇 개월이 걸릴지 예상

**힌트**:
```python
# 기초대사율 계산 (해리스-베네딕트 공식)
# 남성: 66 + (13.7 × 체중) + (5 × 키) - (6.8 × 나이)
# 여성: 655 + (9.6 × 체중) + (1.8 × 키) - (4.7 × 나이)

# 활동대사율 (기초대사율 × 활동계수)
# 거의 운동 안함: 1.2, 가벼운 운동: 1.375, 보통 운동: 1.55, 심한 운동: 1.725
```

### 도전 과제 2: 개인 가계부 프로그램
한 달 가계부를 작성하는 프로그램을 만드세요:
1. 월급, 용돈 등 수입 입력
2. 식비, 교통비, 통신비 등 지출 입력
3. 카테고리별 지출 비율 계산
4. 저축 가능 금액 계산
5. 가계 건전성 평가 및 조언

**힌트**:
```python
# 수입 카테고리
income_categories = ["월급", "용돈", "아르바이트", "기타"]

# 지출 카테고리
expense_categories = ["식비", "교통비", "통신비", "문화생활", "의료비", "기타"]

# 건전성 평가 기준
# 저축률 20% 이상: 매우 양호
# 저축률 10-19%: 양호  
# 저축률 0-9%: 보통
# 적자: 위험
```

---

## ✅ 학습 체크리스트

이번 주 학습을 완료했다면 다음 항목들을 체크해보세요:

- [ ] `input()` 함수로 다양한 타입의 데이터를 입력받을 수 있습니다
- [ ] `int()`, `float()`, `str()` 함수로 데이터 타입을 변환할 수 있습니다  
- [ ] 사용자와 상호작용하는 대화형 프로그램을 만들 수 있습니다
- [ ] 입력 → 처리 → 출력 구조의 프로그램을 설계할 수 있습니다
- [ ] 조건문을 사용하여 상황에 맞는 메시지를 출력할 수 있습니다
- [ ] 복잡한 계산을 포함한 실용적인 프로그램을 작성할 수 있습니다
- [ ] f-string과 문자열 포맷팅을 자유롭게 사용할 수 있습니다
- [ ] 프로그램에 주석을 달아 코드를 설명할 수 있습니다
- [ ] 사용자 친화적인 인터페이스를 설계할 수 있습니다
- [ ] 모든 연습문제와 예제를 완료했습니다

**완료율**: ___/10 항목

---

## 📖 다음 주 예습 내용

**Week 3: 변수와 데이터형**에서는 다음 내용을 학습합니다:

### 🔍 미리 살펴보기
1. **변수의 종류**: 전역변수, 지역변수의 개념
2. **데이터 타입**: int, float, str, bool의 특성
3. **타입 체크**: type() 함수 사용법
4. **변수 명명 규칙**: 파이썬 스타일 가이드

### 📚 사전 준비
다음 코드들을 미리 실행해보세요:
```python
# 다양한 데이터 타입
number = 42
decimal = 3.14
text = "Hello"
flag = True

print(type(number))
print(type(decimal))
print(type(text))
print(type(flag))
```

---

## 🔗 참고 자료

### 📖 추가 학습
- [파이썬 input() 함수 공식 문서](https://docs.python.org/ko/3/library/functions.html#input)
- [문자열 포맷팅 가이드](https://docs.python.org/ko/3/library/string.html#format-string-syntax)
- [파이썬 스타일 가이드 PEP 8](https://peps.python.org/pep-0008/)

### 🛠️ 실습 도구
- [Online Python](https://www.online-python.com/) - 온라인 파이썬 실행기
- [Repl.it Python](https://replit.com/languages/python3) - 브라우저 기반 IDE

### 💡 프로그래밍 팁

#### 🐛 자주 발생하는 오류
1. **ValueError**: 잘못된 타입 변환
   ```python
   age = int(input("나이: "))  # "abc" 입력 시 오류
   ```

2. **들여쓰기 주의**: if문 사용 시 들여쓰기 필수
   ```python
   if age > 20:
       print("성인입니다")  # 4칸 들여쓰기
   ```

#### 🎯 효과적인 디버깅
- **print() 활용**: 중간 결과 확인
- **단계별 테스트**: 작은 단위로 나누어 테스트
- **오류 메시지 읽기**: 에러 메시지를 자세히 읽어보기

---

**🎉 두 번째 주 완료! 실용적인 프로그램을 만들 수 있게 되셨네요! 🚀**

*"프로그래밍은 문제를 해결하는 도구입니다. 일상의 불편함을 코드로 해결해보세요!"*