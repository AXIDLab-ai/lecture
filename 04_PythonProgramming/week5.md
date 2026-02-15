# Week 5: 조건문

--[← Week 4](./week04.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 6 →](./week06.md)--

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. --조건문의 기본 구조 이해--: if문의 기본 문법과 들여쓰기 규칙을 완전히 익힙니다
2. --다중 조건 처리--: if-elif-else문을 사용하여 여러 조건을 효율적으로 처리합니다
3. --복합 조건문 작성--: 논리 연산자를 활용하여 복잡한 조건식을 만듭니다
4. --중첩 조건문 마스터--: 조건문 안에 조건문을 넣어 정교한 논리를 구현합니다
5. --삼항 연산자 활용--: 간단한 조건문을 한 줄로 표현하는 방법을 배웁니다
6. --실무 응용 프로그램 제작--: 성적 시스템, 로그인 시스템 등 실용적인 프로그램을 작성합니다

---

## 📚 핵심 개념 요약

### 1. 조건문이란?
```
🤔 조건문 = 특정 조건에 따라 다른 코드를 실행하는 제어 구조
⚡ 프로그램의 흐름을 제어하여 상황에 맞는 처리를 가능하게 함
🎯 현실의 "만약 ~라면 ~하고, 그렇지 않으면 ~해라" 논리를 코드로 구현
```

### 2. 파이썬 조건문 종류

| 종류 | 형태 | 용도 | 예시 |
|------|------|------|------|
| 단순 if문 | `if 조건:` | 조건이 참일 때만 실행 | `if age >= 18:` |
| if-else문 | `if 조건: ... else:` | 두 가지 경우 처리 | `if score >= 60: ... else:` |
| if-elif-else문 | `if ... elif ... else:` | 여러 조건 순차 검사 | 등급 판정 |
| 중첩 if문 | if문 안에 if문 | 복잡한 논리 구현 | 다단계 검증 |
| 삼항 연산자 | `값1 if 조건 else 값2` | 간단한 조건부 값 할당 | `result = "pass" if score >= 60 else "fail"` |

### 3. 조건식에 사용되는 연산자

| 분류 | 연산자 | 의미 | 예시 |
|------|--------|------|------|
| 비교 | `==`, `!=` | 같음, 다름 | `name == "admin"` |
| 크기 비교 | `>`, `<`, `>=`, `<=` | 크기 관계 | `age >= 18` |
| 논리 | `and`, `or`, `not` | 논리 연산 | `age >= 18 and has_license` |
| 멤버십 | `in`, `not in` | 포함 여부 | `"a" in "apple"` |
| 동일성 | `is`, `is not` | 객체 동일성 | `value is None` |

### 4. 들여쓰기 규칙
- --파이썬의 핵심--: 들여쓰기로 코드 블록을 구분
- --표준--: 공백 4개 또는 탭 1개 (공백 4개 권장)
- --일관성--: 같은 블록 내에서는 동일한 들여쓰기 사용
- --중첩--: 더 안쪽 블록은 더 많이 들여쓰기

---

## 💻 실습 세션 (2시간)

### Part 1: if문 기초 (30분)

#### 🚀 단순 if문

--기본 if문 구조--:
```python
print("🚀 단순 if문")
print("=" - 15)

# 기본 if문 문법
# if 조건:
#     실행할 코드

age = int(input("나이를 입력하세요: "))

if age >= 18:
    print("🎉 성인입니다!")
    print("투표할 수 있습니다.")
    print("운전면허를 취득할 수 있습니다.")

print("프로그램이 계속 실행됩니다.")

# 여러 개의 독립적인 if문
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("🏆 우수한 성적입니다!")

if score >= 60:
    print("✅ 합격입니다!")

if score < 60:
    print("❌ 불합격입니다. 다시 도전하세요!")

print(f"입력한 점수: {score}점")
```

--실행 예시--:
```
🚀 단순 if문
===============
나이를 입력하세요: 20
🎉 성인입니다!
투표할 수 있습니다.
운전면허를 취득할 수 있습니다.
프로그램이 계속 실행됩니다.
점수를 입력하세요: 85
✅ 합격입니다!
입력한 점수: 85점
```

#### ⚖️ if-else문

```python
print("⚖️ if-else문")
print("=" - 15)

# if-else 기본 구조
password = input("비밀번호를 입력하세요: ")

if password == "python123":
    print("🔓 로그인 성공!")
    print("메인 화면으로 이동합니다.")
else:
    print("🔒 비밀번호가 틀렸습니다.")
    print("다시 시도해주세요.")

print("=" - 30)

# 숫자 홀짝 판별
number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print(f"🔢 {number}는 짝수입니다.")
else:
    print(f"🔢 {number}는 홀수입니다.")

print("=" - 30)

# 온도에 따른 옷차림 추천
temperature = int(input("오늘 기온을 입력하세요(°C): "))

if temperature >= 25:
    print("🌞 더운 날씨입니다.")
    print("👕 반팔, 반바지를 입으세요.")
    print("🧴 선크림을 바르는 것을 잊지 마세요!")
else:
    print("🌤️ 시원한 날씨입니다.")
    print("👔 긴팔 옷을 입으세요.")
    print("🧥 외투를 준비하는 것도 좋겠어요.")

print(f"현재 기온: {temperature}°C")
```

#### 🎯 if-elif-else문

```python
print("🎯 if-elif-else문")
print("=" - 20)

# 성적 등급 판정
score = int(input("점수를 입력하세요 (0-100): "))

print(f"입력한 점수: {score}점")

if score >= 90:
    grade = "A"
    comment = "🏆 최우수 성적입니다!"
elif score >= 80:
    grade = "B"  
    comment = "👍 우수한 성적입니다!"
elif score >= 70:
    grade = "C"
    comment = "😊 좋은 성적입니다!"
elif score >= 60:
    grade = "D"
    comment = "😐 아쉬운 성적이네요."
else:
    grade = "F"
    comment = "😢 더 노력이 필요합니다."

print(f"등급: {grade}")
print(comment)

print("=" - 30)

# 계절 판정
month = int(input("월을 입력하세요 (1-12): "))

if month in [12, 1, 2]:
    season = "겨울"
    emoji = "❄️"
    activity = "스키, 스케이트"
elif month in [3, 4, 5]:
    season = "봄"
    emoji = "🌸"
    activity = "꽃구경, 피크닉"
elif month in [6, 7, 8]:
    season = "여름"
    emoji = "☀️"
    activity = "수영, 여행"
elif month in [9, 10, 11]:
    season = "가을"
    emoji = "🍂"
    activity = "단풍구경, 등산"
else:
    season = "잘못된 월"
    emoji = "❓"
    activity = "1-12 사이의 숫자를 입력해주세요"

print(f"{month}월은 {emoji} {season}입니다!")
print(f"추천 활동: {activity}")

print("=" - 30)

# BMI 계산 및 판정
height = float(input("키를 입력하세요 (cm): ")) / 100  # m 단위로 변환
weight = float(input("몸무게를 입력하세요 (kg): "))

bmi = weight / (height -- 2)

print(f"BMI 지수: {bmi:.1f}")

if bmi < 18.5:
    status = "저체중"
    color = "🔵"
    advice = "영양 섭취를 늘리세요."
elif bmi < 23:
    status = "정상"
    color = "🟢"
    advice = "현재 상태를 유지하세요!"
elif bmi < 25:
    status = "과체중"
    color = "🟡"
    advice = "가벼운 운동을 시작하세요."
elif bmi < 30:
    status = "비만"
    color = "🟠"
    advice = "규칙적인 운동과 식단 조절이 필요합니다."
else:
    status = "고도비만"
    color = "🔴"
    advice = "전문의와 상담을 받으시길 권합니다."

print(f"{color} 판정: {status}")
print(f"조언: {advice}")
```

#### 🎮 실습: 간단한 메뉴 시스템

```python
# 파일명: menu_system.py
print("🎮 간단한 메뉴 시스템")
print("=" - 25)

def show_menu():
    """메뉴를 보여주는 함수"""
    print("\n" + "="-30)
    print("🍔 햄버거 주문 시스템")
    print("="-30)
    print("1. 🍟 햄버거 세트 - 8,000원")
    print("2. 🌭 핫도그 세트 - 6,000원") 
    print("3. 🍕 피자 세트 - 12,000원")
    print("4. 🥤 음료수만 - 2,000원")
    print("5. 🚪 종료")
    print("="-30)

def process_order():
    """주문 처리 함수"""
    while True:
        show_menu()
        
        try:
            choice = int(input("메뉴를 선택하세요 (1-5): "))
            
            if choice == 1:
                print("🍟 햔버거 세트를 선택하셨습니다.")
                print("가격: 8,000원")
                print("구성: 햄버거 + 감자튀김 + 음료")
                
                confirm = input("주문하시겠습니까? (y/n): ")
                if confirm.lower() == 'y':
                    print("✅ 주문이 완료되었습니다!")
                    print("⏰ 약 10분 후 준비됩니다.")
                else:
                    print("❌ 주문이 취소되었습니다.")
                    
            elif choice == 2:
                print("🌭 핫도그 세트를 선택하셨습니다.")
                print("가격: 6,000원")
                print("구성: 핫도그 + 감자튀김 + 음료")
                
                confirm = input("주문하시겠습니까? (y/n): ")
                if confirm.lower() == 'y':
                    print("✅ 주문이 완료되었습니다!")
                    print("⏰ 약 8분 후 준비됩니다.")
                else:
                    print("❌ 주문이 취소되었습니다.")
                    
            elif choice == 3:
                print("🍕 피자 세트를 선택하셨습니다.")
                print("가격: 12,000원")
                print("구성: 개인용 피자 + 샐러드 + 음료")
                
                confirm = input("주문하시겠습니까? (y/n): ")
                if confirm.lower() == 'y':
                    print("✅ 주문이 완료되었습니다!")
                    print("⏰ 약 15분 후 준비됩니다.")
                else:
                    print("❌ 주문이 취소되었습니다.")
                    
            elif choice == 4:
                print("🥤 음료수를 선택하셨습니다.")
                print("가격: 2,000원")
                
                # 음료 종류 선택
                print("\n음료 종류:")
                print("1. 콜라")
                print("2. 사이다") 
                print("3. 오렌지 주스")
                print("4. 커피")
                
                drink_choice = int(input("음료를 선택하세요 (1-4): "))
                
                if drink_choice == 1:
                    drink_name = "콜라"
                elif drink_choice == 2:
                    drink_name = "사이다"
                elif drink_choice == 3:
                    drink_name = "오렌지 주스"
                elif drink_choice == 4:
                    drink_name = "커피"
                else:
                    print("❌ 잘못된 선택입니다.")
                    continue
                
                confirm = input(f"{drink_name}를 주문하시겠습니까? (y/n): ")
                if confirm.lower() == 'y':
                    print(f"✅ {drink_name} 주문이 완료되었습니다!")
                    print("⏰ 약 3분 후 준비됩니다.")
                else:
                    print("❌ 주문이 취소되었습니다.")
                    
            elif choice == 5:
                print("👋 이용해 주셔서 감사합니다!")
                break
                
            else:
                print("❌ 1-5 사이의 번호를 선택해주세요.")
                
        except ValueError:
            print("❌ 숫자만 입력해주세요.")
        
        # 계속하기
        if choice != 5:
            continue_order = input("\n다른 메뉴도 주문하시겠습니까? (y/n): ")
            if continue_order.lower() != 'y':
                print("👋 이용해 주셔서 감사합니다!")
                break

# 프로그램 실행
if __name__ == "__main__":
    process_order()
```

---

### Part 2: 복합 조건문 (40분)

#### 🔗 논리 연산자와 조건문

```python
print("🔗 논리 연산자와 조건문")
print("=" - 25)

# AND 연산자 활용
print("💳 대출 심사 시스템")
age = int(input("나이를 입력하세요: "))
income = int(input("연소득을 입력하세요 (만원): "))
credit_score = int(input("신용점수를 입력하세요: "))

print(f"\n📋 신청자 정보:")
print(f"나이: {age}세")
print(f"연소득: {income:,}만원") 
print(f"신용점수: {credit_score}점")

# 복합 조건으로 대출 심사
if age >= 20 and age <= 65 and income >= 3000 and credit_score >= 700:
    print("✅ 대출 승인!")
    print("🎉 최우대 금리 적용 가능합니다.")
    loan_limit = min(income - 5, 50000)  # 연소득의 5배 또는 5억 중 작은 값
    print(f"💰 대출 한도: {loan_limit:,}만원")
    
elif age >= 20 and age <= 65 and income >= 2000 and credit_score >= 600:
    print("⚠️ 조건부 대출 승인")
    print("📄 추가 서류가 필요할 수 있습니다.")
    loan_limit = min(income - 3, 30000)
    print(f"💰 대출 한도: {loan_limit:,}만원")
    
else:
    print("❌ 대출 승인 불가")
    print("📋 승인 조건:")
    print("   - 나이: 20-65세")
    print("   - 연소득: 2,000만원 이상")
    print("   - 신용점수: 600점 이상")

print("=" - 40)

# OR 연산자 활용
print("🎫 할인 혜택 확인")
is_student = input("학생이신가요? (y/n): ").lower() == 'y'
is_senior = input("65세 이상 어르신인가요? (y/n): ").lower() == 'y'
is_member = input("멤버십 회원인가요? (y/n): ").lower() == 'y'
is_birthday = input("오늘 생일이신가요? (y/n): ").lower() == 'y'

print(f"\n🎯 혜택 적용 결과:")

# 기본 요금
base_price = 15000
final_price = base_price
discount_reasons = []

if is_student or is_senior:
    student_senior_discount = 0.3  # 30% 할인
    final_price -= (1 - student_senior_discount)
    discount_reasons.append("학생/경로 할인 30%")

if is_member:
    member_discount = 0.1  # 10% 추가 할인
    final_price -= (1 - member_discount)
    discount_reasons.append("멤버십 할인 10%")

if is_birthday:
    birthday_discount = 0.2  # 20% 추가 할인
    final_price -= (1 - birthday_discount)
    discount_reasons.append("생일 할인 20%")

# 결과 출력
print(f"기본 요금: {base_price:,}원")
if discount_reasons:
    print("적용된 할인:")
    for reason in discount_reasons:
        print(f"   • {reason}")
    print(f"최종 요금: {final_price:,.0f}원")
    saved_amount = base_price - final_price
    print(f"💰 절약 금액: {saved_amount:,.0f}원")
else:
    print("적용된 할인: 없음")
    print(f"최종 요금: {final_price:,}원")

print("=" - 40)

# NOT 연산자 활용
print("🚫 접근 제한 확인")
user_id = input("사용자 ID를 입력하세요: ")
is_banned = input("정지된 계정인가요? (y/n): ").lower() == 'y'
is_admin = input("관리자 계정인가요? (y/n): ").lower() == 'y'
maintenance_mode = input("시스템 점검 중인가요? (y/n): ").lower() == 'y'

print(f"\n🔍 접근 권한 확인:")
print(f"사용자: {user_id}")
print(f"정지 상태: {'예' if is_banned else '아니오'}")
print(f"관리자: {'예' if is_admin else '아니오'}")
print(f"점검 모드: {'예' if maintenance_mode else '아니오'}")

# 복잡한 접근 권한 로직
if not is_banned and not maintenance_mode:
    print("✅ 접근 허용")
    print("🎮 서비스를 이용하실 수 있습니다.")
elif not is_banned and maintenance_mode and is_admin:
    print("⚠️ 관리자 특별 접근 허용")
    print("🔧 점검 모드이지만 관리자로 접근 가능합니다.")
elif is_banned and not is_admin:
    print("❌ 접근 거부 - 계정 정지")
    print("📞 고객센터에 문의해주세요.")
elif not is_banned and maintenance_mode and not is_admin:
    print("❌ 접근 거부 - 시스템 점검중")
    print("⏰ 점검 완료 후 다시 이용해주세요.")
else:
    print("❌ 접근 거부")
    print("🔍 관리자에게 문의하세요.")
```

#### 🏗️ 중첩 if문

```python
print("🏗️ 중첩 if문")
print("=" - 15)

# 온라인 쇼핑몰 배송비 계산
print("📦 배송비 계산 시스템")
order_amount = int(input("주문 금액을 입력하세요: "))
is_member = input("VIP 회원인가요? (y/n): ").lower() == 'y'
region = input("지역을 선택하세요 (서울/경기/지방/제주): ")
is_express = input("당일배송을 원하시나요? (y/n): ").lower() == 'y'

shipping_fee = 0

print(f"\n📋 주문 정보:")
print(f"주문 금액: {order_amount:,}원")
print(f"VIP 회원: {'예' if is_member else '아니오'}")
print(f"배송 지역: {region}")
print(f"당일배송: {'예' if is_express else '아니오'}")

# 중첩된 조건으로 배송비 계산
if order_amount >= 50000:  # 5만원 이상 주문
    if is_member:
        shipping_fee = 0  # VIP 회원은 무료배송
        shipping_type = "VIP 무료배송"
    else:
        if region in ["서울", "경기"]:
            shipping_fee = 0  # 수도권은 무료배송
            shipping_type = "수도권 무료배송"
        else:
            shipping_fee = 2000  # 지방은 2천원
            shipping_type = "지방배송"
else:  # 5만원 미만 주문
    if is_member:
        if region in ["서울", "경기"]:
            shipping_fee = 2000  # VIP도 5만원 미만시 수도권 2천원
            shipping_type = "VIP 우대배송"
        elif region == "제주":
            shipping_fee = 5000  # 제주는 5천원
            shipping_type = "제주 특별배송"
        else:
            shipping_fee = 3000  # 지방은 3천원
            shipping_type = "VIP 지방배송"
    else:
        if region in ["서울", "경기"]:
            shipping_fee = 3000  # 일반회원 수도권 3천원
            shipping_type = "수도권 일반배송"
        elif region == "제주":
            shipping_fee = 7000  # 제주는 7천원
            shipping_type = "제주 일반배송"
        else:
            shipping_fee = 4000  # 지방은 4천원
            shipping_type = "지방 일반배송"

# 당일배송 추가 요금
if is_express:
    if region == "제주":
        print("❌ 제주 지역은 당일배송이 불가능합니다.")
        is_express = False
    else:
        express_fee = 5000
        shipping_fee += express_fee
        shipping_type += " (당일배송)"

# 최종 결과
print(f"\n💰 배송비 계산 결과:")
print(f"배송 유형: {shipping_type}")
print(f"기본 배송비: {shipping_fee - (5000 if is_express else 0):,}원")

if is_express:
    print(f"당일배송 추가: 5,000원")

print(f"최종 배송비: {shipping_fee:,}원")
print(f"총 결제금액: {order_amount + shipping_fee:,}원")

# 절약 팁 제공
if not is_member and order_amount < 50000:
    needed_amount = 50000 - order_amount
    print(f"\n💡 절약 팁:")
    print(f"   {needed_amount:,}원 더 주문하시면 배송비를 절약할 수 있습니다!")

if not is_member:
    print(f"   VIP 회원 가입시 배송비 할인 혜택을 받으실 수 있습니다!")

print("=" - 50)

# 학교 성적 처리 시스템 (더 복잡한 중첩)
print("📚 종합 성적 처리 시스템")
student_name = input("학생 이름: ")
korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))
attendance = int(input("출석 일수 (전체 20일): "))

total_score = korean + english + math
average = total_score / 3

print(f"\n📊 {student_name} 학생 성적 분석:")
print(f"국어: {korean}점, 영어: {english}점, 수학: {math}점")
print(f"총점: {total_score}점, 평균: {average:.1f}점")
print(f"출석: {attendance}일 / 20일 ({attendance/20-100:.0f}%)")

# 복잡한 중첩 조건으로 최종 판정
if attendance >= 16:  # 출석률 80% 이상
    if average >= 90:
        if korean >= 80 and english >= 80 and math >= 80:
            final_grade = "A+"
            comment = "🏆 전 과목 우수, 완벽한 성적!"
            scholarship = True
        else:
            final_grade = "A"
            comment = "🎯 평균은 우수하나 일부 과목 보완 필요"
            scholarship = True
    elif average >= 80:
        if korean >= 70 and english >= 70 and math >= 70:
            final_grade = "B+"
            comment = "👍 전반적으로 양호한 성적"
            scholarship = False
        else:
            final_grade = "B"
            comment = "😊 평균 점수는 좋으나 편차가 큼"
            scholarship = False
    elif average >= 70:
        if all(score >= 60 for score in [korean, english, math]):
            final_grade = "C+"
            comment = "📈 모든 과목 통과, 노력 인정"
            scholarship = False
        else:
            final_grade = "C"
            comment = "⚠️ 일부 과목에 더 집중 필요"
            scholarship = False
    elif average >= 60:
        if all(score >= 50 for score in [korean, english, math]):
            final_grade = "D"
            comment = "😐 최소 기준 통과, 더 노력 필요"
            scholarship = False
        else:
            final_grade = "F"
            comment = "😢 재수강 권장"
            scholarship = False
    else:
        final_grade = "F"
        comment = "😢 전체적인 학습 계획 재검토 필요"
        scholarship = False
else:  # 출석률 80% 미만
    print("❌ 출석 부족으로 평가 불가")
    if attendance < 12:  # 60% 미만
        final_grade = "F"
        comment = "💀 출석 부족으로 자동 낙제"
        scholarship = False
    else:  # 60% 이상 80% 미만
        if average >= 85:  # 성적이 매우 우수한 경우만 구제
            final_grade = "D"
            comment = "⚠️ 성적 우수하나 출석 부족으로 등급 하향"
            scholarship = False
        else:
            final_grade = "F"
            comment = "📚 출석과 성적 모두 개선 필요"
            scholarship = False

# 최종 결과 출력
print(f"\n🎯 최종 결과:")
print(f"학점: {final_grade}")
print(f"평가: {comment}")

if scholarship:
    print("🎉 장학금 지급 대상입니다!")
else:
    print("💡 장학금 지급 대상이 아닙니다.")

# 개별 과목 분석
print(f"\n📈 과목별 분석:")
subjects = [("국어", korean), ("영어", english), ("수학", math)]

for subject, score in subjects:
    if score >= 90:
        level = "🏆 우수"
    elif score >= 80:
        level = "👍 양호" 
    elif score >= 70:
        level = "😊 보통"
    elif score >= 60:
        level = "😐 미흡"
    else:
        level = "😢 부족"
    
    print(f"   {subject}: {score}점 ({level})")
```

#### 🎯 삼항 연산자 (조건부 표현식)

```python
print("🎯 삼항 연산자")
print("=" - 15)

# 기본 삼항 연산자
age = int(input("나이를 입력하세요: "))

# 일반적인 if-else문
if age >= 18:
    status = "성인"
else:
    status = "미성년자"

# 삼항 연산자로 간단하게
status_short = "성인" if age >= 18 else "미성년자"

print(f"일반 방식: {status}")
print(f"삼항 연산자: {status_short}")

print("=" - 30)

# 실용적인 삼항 연산자 예제들
score = int(input("시험 점수: "))

# 합격/불합격 판정
result = "합격" if score >= 60 else "불합격"
print(f"결과: {result}")

# 성적 등급 (중첩 삼항 연산자)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"등급: {grade}")

# 더 읽기 쉽게 여러 줄로 작성
grade_readable = ("A" if score >= 90 else
                 "B" if score >= 80 else  
                 "C" if score >= 70 else
                 "D" if score >= 60 else
                 "F")
print(f"등급 (읽기 쉬운 버전): {grade_readable}")

print("=" - 30)

# 다양한 삼항 연산자 활용
temperature = int(input("기온을 입력하세요: "))
weather = "덥다" if temperature >= 28 else "춥다" if temperature <= 10 else "적당하다"
print(f"날씨: {weather}")

# 절댓값 구하기 (abs 함수 대신)
number = int(input("숫자 입력: "))
absolute = number if number >= 0 else -number
print(f"{number}의 절댓값: {absolute}")

# 최대값 구하기 (max 함수 대신)
a = int(input("첫 번째 수: "))
b = int(input("두 번째 수: "))
maximum = a if a > b else b
print(f"최대값: {maximum}")

# 홀짝 판별
num = int(input("홀짝 판별할 수: "))
odd_even = "홀수" if num % 2 == 1 else "짝수"
print(f"{num}는 {odd_even}입니다.")

print("=" - 30)

# 복합적인 삼항 연산자 활용
print("🎮 게임 캐릭터 상태")
health = int(input("체력 (0-100): "))
mana = int(input("마나 (0-100): "))

# 캐릭터 상태 판정
health_status = ("위험" if health <= 20 else
                "주의" if health <= 50 else
                "양호" if health <= 80 else
                "완벽")

mana_status = ("고갈" if mana <= 10 else
              "부족" if mana <= 30 else
              "보통" if mana <= 70 else
              "충분")

# 행동 가능 여부
can_fight = "전투 가능" if health > 30 and mana > 20 else "휴식 필요"
can_cast_spell = "마법 사용 가능" if mana >= 50 else "마나 부족"

print(f"\n🎯 캐릭터 상태:")
print(f"체력 상태: {health_status} ({health}/100)")
print(f"마나 상태: {mana_status} ({mana}/100)")
print(f"전투 상태: {can_fight}")
print(f"마법 상태: {can_cast_spell}")

# 추천 행동
recommended_action = ("포션 사용" if health <= 30 else
                     "마나 회복" if mana <= 30 else
                     "전투 시작" if health >= 70 and mana >= 70 else
                     "조금 더 회복")

print(f"추천 행동: {recommended_action}")

print("=" - 30)

# 삼항 연산자 vs 일반 if문 비교
print("📊 코드 비교 예제")

# 세금 계산 예제
income = int(input("연봉을 입력하세요 (만원): "))

# 일반 if문 방식
if income <= 1200:
    tax_rate_normal = 0.06
elif income <= 4600:
    tax_rate_normal = 0.15  
elif income <= 8800:
    tax_rate_normal = 0.24
else:
    tax_rate_normal = 0.35

# 삼항 연산자 방식 (중첩)
tax_rate_short = (0.06 if income <= 1200 else
                 0.15 if income <= 4600 else
                 0.24 if income <= 8800 else
                 0.35)

tax_amount = income - tax_rate_short

print(f"연봉: {income:,}만원")
print(f"세율: {tax_rate_short-100}%")
print(f"세금: {tax_amount:,.0f}만원")
print(f"실수령액: {income - tax_amount:,.0f}만원")
```

---

### Part 3: 실용 프로그램 (50분)

#### 🏆 성적 등급 판정 시스템

```python
# 파일명: grade_system.py
print("🏆 종합 성적 관리 시스템")
print("=" - 25)

class GradeManager:
    def __init__(self):
        self.students = []
        self.subjects = ["국어", "영어", "수학", "과학", "사회"]
    
    def add_student(self):
        """학생 성적 입력"""
        print("\n📝 학생 정보 입력")
        print("-" - 20)
        
        name = input("학생 이름: ")
        student_id = input("학번: ")
        
        scores = {}
        total = 0
        
        print(f"\n{name} 학생의 과목별 점수를 입력하세요:")
        
        for subject in self.subjects:
            while True:
                try:
                    score = int(input(f"{subject} 점수 (0-100): "))
                    if 0 <= score <= 100:
                        scores[subject] = score
                        total += score
                        break
                    else:
                        print("❌ 0-100 사이의 점수를 입력하세요.")
                except ValueError:
                    print("❌ 숫자만 입력하세요.")
        
        # 출석 정보
        while True:
            try:
                attendance = int(input("출석 일수 (0-20): "))
                if 0 <= attendance <= 20:
                    break
                else:
                    print("❌ 0-20 사이의 값을 입력하세요.")
            except ValueError:
                print("❌ 숫자만 입력하세요.")
        
        # 성적 계산
        average = total / len(self.subjects)
        attendance_rate = (attendance / 20) - 100
        
        # 등급 산정
        grade_info = self.calculate_grade(scores, average, attendance)
        
        student = {
            'name': name,
            'student_id': student_id,
            'scores': scores,
            'total': total,
            'average': average,
            'attendance': attendance,
            'attendance_rate': attendance_rate,
            'grade': grade_info['grade'],
            'gpa': grade_info['gpa'],
            'comment': grade_info['comment'],
            'scholarship': grade_info['scholarship'],
            'warning': grade_info['warning']
        }
        
        self.students.append(student)
        
        print(f"\n✅ {name} 학생 정보가 등록되었습니다!")
        self.display_student_result(student)
    
    def calculate_grade(self, scores, average, attendance):
        """성적 등급 계산"""
        grade_info = {
            'grade': 'F',
            'gpa': 0.0,
            'comment': '',
            'scholarship': False,
            'warning': []
        }
        
        # 출석률 체크
        attendance_rate = (attendance / 20) - 100
        
        if attendance_rate < 60:
            grade_info['grade'] = 'F'
            grade_info['gpa'] = 0.0
            grade_info['comment'] = '출석 부족으로 평가 불가'
            grade_info['warning'].append('출석률 60% 미만')
            return grade_info
        
        # 낙제 과목 체크
        failing_subjects = [subject for subject, score in scores.items() if score < 40]
        
        if failing_subjects:
            grade_info['warning'].extend([f'{subject} 과목 40점 미만' for subject in failing_subjects])
        
        # 평균 기반 등급 산정
        if average >= 95:
            base_grade = 'A+'
            base_gpa = 4.5
        elif average >= 90:
            base_grade = 'A'
            base_gpa = 4.0
        elif average >= 85:
            base_grade = 'B+'
            base_gpa = 3.5
        elif average >= 80:
            base_grade = 'B'
            base_gpa = 3.0
        elif average >= 75:
            base_grade = 'C+'
            base_gpa = 2.5
        elif average >= 70:
            base_grade = 'C'
            base_gpa = 2.0
        elif average >= 65:
            base_grade = 'D+'
            base_gpa = 1.5
        elif average >= 60:
            base_grade = 'D'
            base_gpa = 1.0
        else:
            base_grade = 'F'
            base_gpa = 0.0
        
        # 세부 조건 검사
        excellent_subjects = sum(1 for score in scores.values() if score >= 95)
        good_subjects = sum(1 for score in scores.values() if score >= 85)
        failing_count = len(failing_subjects)
        
        # 최종 등급 조정
        if base_grade in ['A+', 'A'] and failing_count == 0 and attendance_rate >= 90:
            if excellent_subjects >= 3:
                grade_info['scholarship'] = True
                grade_info['comment'] = '최우수 성적 - 장학금 대상'
            else:
                grade_info['comment'] = '우수한 성적'
        elif base_grade in ['B+', 'B'] and failing_count <= 1:
            if attendance_rate >= 85:
                grade_info['comment'] = '양호한 성적'
            else:
                grade_info['comment'] = '양호한 성적이나 출석 개선 필요'
        elif base_grade in ['C+', 'C'] and failing_count <= 2:
            grade_info['comment'] = '보통 성적 - 더 노력 필요'
        elif base_grade in ['D+', 'D']:
            if failing_count > 2:
                base_grade = 'F'
                base_gpa = 0.0
                grade_info['comment'] = '다수 과목 낙제로 재수강 필요'
            else:
                grade_info['comment'] = '최소 기준 통과 - 집중 학습 필요'
        else:
            grade_info['comment'] = '학습 계획 전면 재검토 필요'
        
        # 출석률에 따른 등급 조정
        if attendance_rate < 75 and base_grade != 'F':
            # 한 단계 하향 조정
            grade_adjustments = {
                'A+': ('A', 4.0), 'A': ('B+', 3.5), 'B+': ('B', 3.0),
                'B': ('C+', 2.5), 'C+': ('C', 2.0), 'C': ('D+', 1.5),
                'D+': ('D', 1.0), 'D': ('F', 0.0)
            }
            if base_grade in grade_adjustments:
                base_grade, base_gpa = grade_adjustments[base_grade]
                grade_info['comment'] += ' (출석률로 인한 등급 하향)'
        
        grade_info['grade'] = base_grade
        grade_info['gpa'] = base_gpa
        
        return grade_info
    
    def display_student_result(self, student):
        """학생 결과 출력"""
        print(f"\n" + "="-50)
        print(f"🎓 {student['name']} 학생 성적표")
        print("="-50)
        
        print(f"👤 학번: {student['student_id']}")
        print(f"📅 출석: {student['attendance']}/20일 ({student['attendance_rate']:.1f}%)")
        
        print(f"\n📊 과목별 성적:")
        for subject, score in student['scores'].items():
            # 과목별 등급
            if score >= 90:
                subject_grade = "A"
                emoji = "🏆"
            elif score >= 80:
                subject_grade = "B"
                emoji = "👍"
            elif score >= 70:
                subject_grade = "C"
                emoji = "😊"
            elif score >= 60:
                subject_grade = "D"
                emoji = "😐"
            else:
                subject_grade = "F"
                emoji = "😢"
            
            print(f"   {subject}: {score:3d}점 ({subject_grade}) {emoji}")
        
        print(f"\n🎯 종합 성적:")
        print(f"총점: {student['total']}점")
        print(f"평균: {student['average']:.1f}점")
        print(f"학점: {student['grade']}")
        print(f"GPA: {student['gpa']:.1f}")
        
        print(f"\n💬 종합 평가:")
        print(f"   {student['comment']}")
        
        if student['scholarship']:
            print(f"🎉 장학금 지급 대상입니다!")
        
        if student['warning']:
            print(f"\n⚠️ 주의사항:")
            for warning in student['warning']:
                print(f"   • {warning}")
        
        # 개선 제안
        print(f"\n💡 개선 제안:")
        weak_subjects = [subject for subject, score in student['scores'].items() if score < 70]
        
        if weak_subjects:
            print(f"   📚 집중 학습 필요 과목: {', '.join(weak_subjects)}")
        
        if student['attendance_rate'] < 85:
            print(f"   🕐 출석률 개선이 필요합니다.")
        
        if student['average'] < 80:
            print(f"   📈 전체적인 성적 향상이 필요합니다.")
        
        if not weak_subjects and student['attendance_rate'] >= 90 and student['average'] >= 85:
            print(f"   ✨ 우수한 성적을 유지하고 있습니다!")
    
    def display_class_statistics(self):
        """학급 통계"""
        if not self.students:
            print("❌ 등록된 학생이 없습니다.")
            return
        
        print(f"\n📈 학급 통계 ({len(self.students)}명)")
        print("=" - 30)
        
        # 평균 점수 계산
        total_averages = [student['average'] for student in self.students]
        class_average = sum(total_averages) / len(total_averages)
        
        print(f"학급 평균: {class_average:.1f}점")
        
        # 등급별 분포
        grade_count = {}
        for student in self.students:
            grade = student['grade']
            grade_count[grade] = grade_count.get(grade, 0) + 1
        
        print(f"\n🎯 등급별 분포:")
        grade_order = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
        for grade in grade_order:
            count = grade_count.get(grade, 0)
            if count > 0:
                percentage = (count / len(self.students)) - 100
                print(f"   {grade}: {count}명 ({percentage:.1f}%)")
        
        # 과목별 평균
        print(f"\n📚 과목별 평균:")
        for subject in self.subjects:
            subject_scores = [student['scores'][subject] for student in self.students]
            subject_average = sum(subject_scores) / len(subject_scores)
            print(f"   {subject}: {subject_average:.1f}점")
        
        # 우수 학생
        top_students = sorted(self.students, key=lambda x: x['average'], reverse=True)[:3]
        print(f"\n🏆 상위 3명:")
        for i, student in enumerate(top_students, 1):
            print(f"   {i}등: {student['name']} ({student['average']:.1f}점, {student['grade']})")
        
        # 장학금 대상자
        scholarship_students = [s for s in self.students if s['scholarship']]
        if scholarship_students:
            print(f"\n🎓 장학금 대상자 ({len(scholarship_students)}명):")
            for student in scholarship_students:
                print(f"   • {student['name']} ({student['average']:.1f}점)")
    
    def find_student(self):
        """학생 검색"""
        if not self.students:
            print("❌ 등록된 학생이 없습니다.")
            return
        
        search_name = input("검색할 학생 이름: ")
        
        found_students = [s for s in self.students if search_name in s['name']]
        
        if found_students:
            print(f"\n🔍 검색 결과 ({len(found_students)}명):")
            for student in found_students:
                print(f"\n{student['name']} ({student['student_id']})")
                print(f"   평균: {student['average']:.1f}점")
                print(f"   학점: {student['grade']}")
                print(f"   출석률: {student['attendance_rate']:.1f}%")
                
                detail = input(f"{student['name']} 학생의 상세 정보를 보시겠습니까? (y/n): ")
                if detail.lower() == 'y':
                    self.display_student_result(student)
        else:
            print("❌ 해당하는 학생을 찾을 수 없습니다.")
    
    def run(self):
        """메인 실행 함수"""
        while True:
            print(f"\n" + "="-40)
            print("🏆 성적 관리 시스템")
            print("="-40)
            print("1. 학생 성적 입력")
            print("2. 학급 통계 보기")
            print("3. 학생 검색")
            print("4. 전체 학생 목록")
            print("5. 종료")
            
            try:
                choice = input("\n선택하세요 (1-5): ")
                
                if choice == "1":
                    self.add_student()
                
                elif choice == "2":
                    self.display_class_statistics()
                
                elif choice == "3":
                    self.find_student()
                
                elif choice == "4":
                    if self.students:
                        print(f"\n📋 전체 학생 목록 ({len(self.students)}명):")
                        for i, student in enumerate(self.students, 1):
                            print(f"{i:2d}. {student['name']} ({student['student_id']}) - "
                                  f"{student['average']:.1f}점 ({student['grade']})")
                    else:
                        print("❌ 등록된 학생이 없습니다.")
                
                elif choice == "5":
                    print("👋 성적 관리 시스템을 종료합니다!")
                    break
                
                else:
                    print("❌ 1-5 중에서 선택해주세요.")
                    
            except Exception as e:
                print(f"❌ 오류 발생: {e}")
            
            if choice != "5":
                input("\n⏸️ 엔터를 눌러 계속...")

# 프로그램 실행
if __name__ == "__main__":
    grade_manager = GradeManager()
    grade_manager.run()
```

#### 🔐 로그인 시스템

```python
# 파일명: login_system.py
import datetime
import hashlib

print("🔐 보안 로그인 시스템")
print("=" - 20)

class LoginSystem:
    def __init__(self):
        # 사용자 데이터베이스 (실제로는 데이터베이스에 저장)
        self.users = {
            "admin": {
                "password": self.hash_password("admin123"),
                "name": "관리자",
                "role": "admin",
                "created_date": "2024-01-01",
                "last_login": None,
                "failed_attempts": 0,
                "locked": False
            },
            "user1": {
                "password": self.hash_password("user123"),
                "name": "사용자1",
                "role": "user",
                "created_date": "2024-01-15",
                "last_login": None,
                "failed_attempts": 0,
                "locked": False
            },
            "guest": {
                "password": self.hash_password("guest123"),
                "name": "게스트",
                "role": "guest",
                "created_date": "2024-02-01",
                "last_login": None,
                "failed_attempts": 0,
                "locked": False
            }
        }
        
        self.current_user = None
        self.login_attempts = {}  # IP별 로그인 시도 횟수 (시뮬레이션)
        self.session_timeout = 1800  # 30분 (초 단위)
        self.max_failed_attempts = 3
    
    def hash_password(self, password):
        """비밀번호 해시화"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_password_strength(self, password):
        """비밀번호 강도 검증"""
        if len(password) < 8:
            return False, "비밀번호는 최소 8자 이상이어야 합니다."
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&-()_+-=[]{}|;:,.<>?" for c in password)
        
        if not (has_upper and has_lower and has_digit):
            return False, "대문자, 소문자, 숫자가 모두 포함되어야 합니다."
        
        if password.lower() in ["password", "123456", "qwerty"]:
            return False, "일반적인 패턴의 비밀번호는 사용할 수 없습니다."
        
        return True, "안전한 비밀번호입니다."
    
    def register_user(self):
        """사용자 등록"""
        print("\n👤 새 계정 등록")
        print("-" - 20)
        
        # 아이디 입력 및 중복 확인
        while True:
            username = input("사용자 ID: ").strip()
            
            if not username:
                print("❌ 아이디를 입력해주세요.")
                continue
            
            if len(username) < 4:
                print("❌ 아이디는 최소 4자 이상이어야 합니다.")
                continue
            
            if username in self.users:
                print("❌ 이미 존재하는 아이디입니다.")
                continue
            
            if not username.isalnum():
                print("❌ 아이디는 영문자와 숫자만 사용할 수 있습니다.")
                continue
            
            break
        
        # 비밀번호 입력 및 검증
        while True:
            password = input("비밀번호: ")
            is_valid, message = self.validate_password_strength(password)
            
            if is_valid:
                print(f"✅ {message}")
                break
            else:
                print(f"❌ {message}")
        
        # 비밀번호 확인
        while True:
            confirm_password = input("비밀번호 확인: ")
            if password == confirm_password:
                break
            else:
                print("❌ 비밀번호가 일치하지 않습니다.")
        
        # 추가 정보
        name = input("이름: ").strip()
        if not name:
            name = username
        
        # 계정 생성
        self.users[username] = {
            "password": self.hash_password(password),
            "name": name,
            "role": "user",
            "created_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "last_login": None,
            "failed_attempts": 0,
            "locked": False
        }
        
        print(f"✅ 계정이 성공적으로 생성되었습니다!")
        print(f"   사용자명: {username}")
        print(f"   이름: {name}")
        print(f"   가입일: {self.users[username]['created_date']}")
    
    def login(self):
        """로그인 처리"""
        print("\n🔐 로그인")
        print("-" - 15)
        
        if self.current_user:
            print(f"❌ 이미 {self.current_user['name']}님이 로그인되어 있습니다.")
            logout_choice = input("로그아웃하고 다른 계정으로 로그인하시겠습니까? (y/n): ")
            if logout_choice.lower() == 'y':
                self.logout()
            else:
                return False
        
        max_attempts = 3
        
        for attempt in range(max_attempts):
            username = input("사용자 ID: ").strip()
            password = input("비밀번호: ")
            
            # 계정 존재 확인
            if username not in self.users:
                print(f"❌ 존재하지 않는 아이디입니다. ({max_attempts - attempt - 1}번 남음)")
                continue
            
            user = self.users[username]
            
            # 계정 잠금 확인
            if user['locked']:
                print("❌ 계정이 잠겨있습니다. 관리자에게 문의하세요.")
                return False
            
            # 비밀번호 확인
            if user['password'] == self.hash_password(password):
                # 로그인 성공
                user['failed_attempts'] = 0
                user['last_login'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                self.current_user