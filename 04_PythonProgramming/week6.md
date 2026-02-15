# Week 6: 반복문

**[← Week 5](./week05.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 7 →](./week07.md)**

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **for문 마스터**: range() 함수와 다양한 자료형을 순회하는 for문을 완벽히 구사합니다
2. **while문 활용**: 조건 기반 반복과 무한 루프를 안전하게 다룰 수 있습니다
3. **반복 제어문**: break, continue, else절을 적재적소에 사용합니다
4. **중첩 반복문**: 이중, 삼중 반복문을 사용하여 복잡한 패턴을 구현합니다
5. **실용 프로그램 작성**: 게임, 메뉴 시스템 등 인터랙티브한 프로그램을 제작합니다
6. **효율적인 알고리즘**: 반복문을 이용한 계산과 데이터 처리를 최적화합니다

---

## 📚 핵심 개념 요약

### 1. 반복문이란?
```
🔄 반복문 = 같은 코드를 여러 번 실행하는 제어 구조
⚡ 반복적인 작업을 자동화하여 코드의 효율성을 극대화
🎯 "이 작업을 N번 해라" 또는 "조건이 맞는 동안 계속 해라"
```

### 2. 파이썬 반복문 종류

| 종류 | 형태 | 특징 | 사용 시기 |
|------|------|------|-----------|
| **for문** | `for 변수 in 시퀀스:` | 정해진 횟수나 시퀀스 순회 | 횟수가 정해져 있을 때 |
| **while문** | `while 조건:` | 조건이 참인 동안 반복 | 조건에 따라 반복할 때 |
| **중첩 반복문** | 반복문 안에 반복문 | 2차원 데이터나 복잡한 패턴 | 표, 패턴, 조합 처리 |

### 3. 반복 제어문

| 제어문 | 기능 | 사용법 | 예시 |
|--------|------|--------|------|
| **break** | 반복문 완전 탈출 | `if 조건: break` | 특정 값 찾으면 종료 |
| **continue** | 현재 반복 건너뛰기 | `if 조건: continue` | 짝수만 처리하고 홀수 건너뛰기 |
| **else** | 반복문 정상 완료시 실행 | `for/while: ... else:` | break 없이 끝났을 때만 실행 |

### 4. range() 함수

| 형태 | 의미 | 예시 | 결과 |
|------|------|------|------|
| `range(n)` | 0부터 n-1까지 | `range(5)` | 0, 1, 2, 3, 4 |
| `range(시작, 끝)` | 시작부터 끝-1까지 | `range(2, 7)` | 2, 3, 4, 5, 6 |
| `range(시작, 끝, 단계)` | 단계별로 증가 | `range(0, 10, 2)` | 0, 2, 4, 6, 8 |

### 5. 반복문 성능 팁
- **리스트 컴프리헨션**: `[x*2 for x in range(10)]`
- **enumerate()**: 인덱스와 값 동시 접근
- **zip()**: 여러 시퀀스 동시 순회
- **break 적극 활용**: 불필요한 반복 방지

---

## 💻 실습 세션 (2시간)

### Part 1: for문 기초 (30분)

#### 🚀 range() 함수 완전 정복

```python
print("🚀 range() 함수 마스터하기")
print("=" * 25)

# 1. 기본 range(n) - 0부터 n-1까지
print("📊 기본 range() 사용법")
print("range(5):")
for i in range(5):
    print(f"  {i}번째 반복")

print("\nrange(3)으로 카운트다운:")
for i in range(3):
    print(f"  {3-i}초 남음...")
print("  발사! 🚀")

print("=" * 30)

# 2. range(시작, 끝)
print("📈 range(시작, 끝)")
print("range(3, 8):")
for num in range(3, 8):
    print(f"  숫자: {num}")

print("\n구구단 2단:")
for i in range(1, 10):
    result = 2 * i
    print(f"  2 × {i} = {result}")

print("=" * 30)

# 3. range(시작, 끝, 단계)
print("🎯 range(시작, 끝, 단계)")

print("짝수만 출력 range(0, 11, 2):")
for even in range(0, 11, 2):
    print(f"  짝수: {even}")

print("\n홀수만 출력 range(1, 11, 2):")
for odd in range(1, 11, 2):
    print(f"  홀수: {odd}")

print("\n역순으로 출력 range(10, 0, -1):")
for countdown in range(10, 0, -1):
    print(f"  카운트다운: {countdown}")

print("\n5의 배수 range(5, 51, 5):")
for multiple in range(5, 51, 5):
    print(f"  5의 배수: {multiple}")

print("=" * 30)

# 4. 실용적인 range() 활용
print("💡 실용적인 range() 활용")

# 별찍기
print("별찍기 패턴:")
for i in range(1, 6):
    stars = "★" * i
    print(f"  {stars}")

print()
for i in range(5, 0, -1):
    stars = "☆" * i
    print(f"  {stars}")

print("\n숫자 피라미드:")
for i in range(1, 6):
    spaces = " " * (5 - i)
    numbers = " ".join(str(j) for j in range(1, i + 1))
    print(f"  {spaces}{numbers}")

print("=" * 30)

# 5. range()를 이용한 계산
print("🧮 range()로 계산하기")

# 1부터 100까지의 합
total = 0
for num in range(1, 101):
    total += num
print(f"1부터 100까지의 합: {total}")

# 팩토리얼 계산
factorial = 1
n = 5
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# 제곱의 합
square_sum = 0
for i in range(1, 11):
    square_sum += i ** 2
print(f"1²+2²+...+10² = {square_sum}")

# 피보나치 수열
print("피보나치 수열 처음 10개:")
a, b = 0, 1
fib_sequence = [a, b]
for _ in range(8):  # 처음 2개는 이미 있으므로 8번 더
    next_fib = a + b
    fib_sequence.append(next_fib)
    a, b = b, next_fib

print(f"  {fib_sequence}")
```

#### 📝 리스트와 문자열 순회

```python
print("📝 리스트와 문자열 순회")
print("=" * 25)

# 1. 리스트 순회 기본
fruits = ["🍎", "🍌", "🍇", "🍊", "🥝"]

print("과일 리스트 순회:")
for fruit in fruits:
    print(f"  좋아하는 과일: {fruit}")

print("\n인덱스와 함께 순회 (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"  {index + 1}번째 과일: {fruit}")

print("\n인덱스를 직접 사용:")
for i in range(len(fruits)):
    print(f"  fruits[{i}] = {fruits[i]}")

print("=" * 30)

# 2. 숫자 리스트 처리
numbers = [10, 25, 3, 47, 8, 91, 34, 15]

print(f"원본 리스트: {numbers}")

# 각 숫자를 2배로
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(f"2배로: {doubled}")

# 짝수만 필터링
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"짝수만: {even_numbers}")

# 최댓값과 최솟값 찾기
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"최댓값: {max_num}, 최솟값: {min_num}")

# 평균 계산
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"평균: {average:.2f}")

print("=" * 30)

# 3. 문자열 순회
message = "Python Programming"

print(f"문자열: '{message}'")

print("한 글자씩 출력:")
for char in message:
    if char == ' ':
        print("  [공백]")
    else:
        print(f"  '{char}'")

print("\n문자별 분석:")
vowels = "aeiouAEIOU"
consonants = 0
vowel_count = 0
spaces = 0

for char in message:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonants += 1
    elif char == ' ':
        spaces += 1

print(f"  모음: {vowel_count}개")
print(f"  자음: {consonants}개") 
print(f"  공백: {spaces}개")

print("\n각 문자의 위치:")
for i, char in enumerate(message):
    print(f"  위치 {i:2d}: '{char}'")

print("=" * 30)

# 4. 여러 리스트 동시 순회 (zip)
names = ["김철수", "이영희", "박민수", "최지원"]
scores = [85, 92, 78, 96]
subjects = ["수학", "영어", "과학", "국어"]

print("성적표:")
for name, score, subject in zip(names, scores, subjects):
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"  {name}: {subject} {score}점 ({grade})")

print("\n학생별 평균 점수 (가정):")
all_scores = [
    [85, 90, 78],  # 김철수
    [92, 88, 95],  # 이영희  
    [78, 82, 75],  # 박민수
    [96, 94, 98]   # 최지원
]

for name, student_scores in zip(names, all_scores):
    average = sum(student_scores) / len(student_scores)
    print(f"  {name}: {average:.1f}점")

print("=" * 30)

# 5. 리스트 컴프리헨션 맛보기
original = [1, 2, 3, 4, 5]

print("리스트 컴프리헨션 vs 일반 for문:")

# 일반 for문으로 제곱 만들기
squares_normal = []
for x in original:
    squares_normal.append(x ** 2)

# 리스트 컴프리헨션으로 제곱 만들기
squares_comp = [x ** 2 for x in original]

print(f"원본: {original}")
print(f"일반 방법: {squares_normal}")
print(f"컴프리헨션: {squares_comp}")

# 조건부 리스트 컴프리헨션
even_squares = [x ** 2 for x in original if x % 2 == 0]
print(f"짝수의 제곱만: {even_squares}")
```

#### 🎮 실습: 간단한 for문 게임

```python
# 파일명: for_loop_games.py
import random

print("🎮 for문으로 만드는 간단한 게임들")
print("=" * 35)

def number_guessing_game():
    """숫자 맞추기 게임 (제한된 기회)"""
    print("\n🎯 숫자 맞추기 게임")
    print("-" * 20)
    
    secret_number = random.randint(1, 100)
    max_attempts = 7
    
    print("1부터 100 사이의 숫자를 생각했습니다!")
    print(f"총 {max_attempts}번의 기회가 있습니다.")
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n🎲 {attempt}번째 시도:")
        
        try:
            guess = int(input("숫자를 입력하세요: "))
            
            if guess < 1 or guess > 100:
                print("❌ 1부터 100 사이의 숫자를 입력하세요!")
                continue
            
            if guess == secret_number:
                print(f"🎉 정답입니다! {attempt}번 만에 맞췄습니다!")
                print(f"숨겨진 숫자: {secret_number}")
                return True
            elif guess < secret_number:
                remaining = max_attempts - attempt
                print(f"⬆️ 더 큰 숫자입니다! (남은 기회: {remaining}번)")
            else:
                remaining = max_attempts - attempt
                print(f"⬇️ 더 작은 숫자입니다! (남은 기회: {remaining}번)")
                
        except ValueError:
            print("❌ 올바른 숫자를 입력하세요!")
    
    print(f"\n💥 게임 오버! 정답은 {secret_number}였습니다.")
    return False

def multiplication_quiz():
    """구구단 퀴즈"""
    print("\n📚 구구단 퀴즈")
    print("-" * 15)
    
    correct_count = 0
    total_questions = 10
    
    print(f"구구단 문제 {total_questions}개를 풀어보세요!")
    
    for question_num in range(1, total_questions + 1):
        # 랜덤한 곱셈 문제 생성
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct_answer = a * b
        
        print(f"\n📝 문제 {question_num}: {a} × {b} = ?")
        
        try:
            user_answer = int(input("답: "))
            
            if user_answer == correct_answer:
                print("✅ 정답!")
                correct_count += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {correct_answer}입니다.")
                
        except ValueError:
            print(f"❌ 올바른 숫자를 입력하세요! 정답은 {correct_answer}였습니다.")
    
    # 결과 발표
    score = (correct_count / total_questions) * 100
    print(f"\n🎯 퀴즈 결과:")
    print(f"총 {total_questions}문제 중 {correct_count}문제 정답!")
    print(f"점수: {score:.0f}점")
    
    if score >= 90:
        print("🏆 구구단 마스터!")
    elif score >= 70:
        print("👍 잘했습니다!")
    elif score >= 50:
        print("😊 더 연습해보세요!")
    else:
        print("💪 구구단을 더 공부해야겠어요!")

def lottery_simulator():
    """복권 시뮬레이터"""
    print("\n🎰 복권 시뮬레이터")
    print("-" * 18)
    
    # 당첨 번호 생성 (1-45 중 6개)
    winning_numbers = random.sample(range(1, 46), 6)
    winning_numbers.sort()
    
    print("복권을 몇 장 살지 정하세요!")
    
    try:
        num_tickets = int(input("복권 매수 (1-100): "))
        if num_tickets < 1 or num_tickets > 100:
            print("❌ 1-100 사이의 숫자를 입력하세요!")
            return
    except ValueError:
        print("❌ 올바른 숫자를 입력하세요!")
        return
    
    print(f"\n🎫 {num_tickets}장의 복권을 구매합니다...")
    
    # 결과 집계
    results = {6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    
    for ticket_num in range(1, num_tickets + 1):
        # 복권 번호 생성
        my_numbers = random.sample(range(1, 46), 6)
        my_numbers.sort()
        
        # 맞춘 개수 계산
        matches = len(set(my_numbers) & set(winning_numbers))
        results[matches] += 1
        
        # 처음 10장은 상세히 표시
        if ticket_num <= 10:
            print(f"  {ticket_num:2d}번째 복권: {my_numbers} -> {matches}개 맞음")
        elif ticket_num == 11:
            print("  ...")
    
    # 결과 발표
    print(f"\n🏆 당첨 번호: {winning_numbers}")
    print(f"📊 결과 (총 {num_tickets}장):")
    
    prize_info = {
        6: ("1등", "20억원", "🏆"),
        5: ("2등", "5천만원", "🥈"), 
        4: ("3등", "150만원", "🥉"),
        3: ("4등", "5만원", "🎫"),
        2: ("5등", "5천원", "🎟️")
    }
    
    total_prize = 0
    total_cost = num_tickets * 1000  # 복권 1장당 1000원
    
    for matches in range(6, 1, -1):
        if results[matches] > 0:
            rank, prize, emoji = prize_info[matches]
            print(f"  {emoji} {rank} ({matches}개 맞음): {results[matches]}장")
            
            # 상금 계산 (가상)
            if matches == 6:
                prize_money = results[matches] * 2000000000
            elif matches == 5:
                prize_money = results[matches] * 50000000
            elif matches == 4:
                prize_money = results[matches] * 1500000
            elif matches == 3:
                prize_money = results[matches] * 50000
            elif matches == 2:
                prize_money = results[matches] * 5000
            
            total_prize += prize_money
    
    # 꽝
    if results[0] + results[1] > 0:
        print(f"  💸 꽝: {results[0] + results[1]}장")
    
    print(f"\n💰 수지 계산:")
    print(f"구입 비용: {total_cost:,}원")
    print(f"총 상금: {total_prize:,}원")
    profit = total_prize - total_cost
    print(f"손익: {profit:,}원 ({'💸 손실' if profit < 0 else '💰 이익'})")

def rock_paper_scissors_tournament():
    """가위바위보 토너먼트"""
    print("\n✂️ 가위바위보 토너먼트")
    print("-" * 20)
    
    choices = ["가위", "바위", "보"]
    choice_emoji = {"가위": "✂️", "바위": "👊", "보": "🖐️"}
    
    wins = 0
    losses = 0
    draws = 0
    
    rounds = int(input("몇 라운드 진행할까요? (1-20): "))
    
    for round_num in range(1, rounds + 1):
        print(f"\n🥊 라운드 {round_num}")
        
        # 사용자 선택
        print("선택하세요:")
        print("1. ✂️ 가위")
        print("2. 👊 바위") 
        print("3. 🖐️ 보")
        
        try:
            user_choice_num = int(input("번호 입력 (1-3): "))
            if user_choice_num not in [1, 2, 3]:
                print("❌ 1, 2, 3 중에서 선택하세요!")
                continue
                
            user_choice = choices[user_choice_num - 1]
        except ValueError:
            print("❌ 올바른 번호를 입력하세요!")
            continue
        
        # 컴퓨터 선택
        computer_choice = random.choice(choices)
        
        print(f"당신: {choice_emoji[user_choice]} {user_choice}")
        print(f"컴퓨터: {choice_emoji[computer_choice]} {computer_choice}")
        
        # 승부 판정
        if user_choice == computer_choice:
            print("🤝 무승부!")
            draws += 1
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            print("🎉 승리!")
            wins += 1
        else:
            print("😢 패배!")
            losses += 1
        
        # 현재 전적 표시
        print(f"현재 전적: {wins}승 {losses}패 {draws}무")
    
    # 최종 결과
    print(f"\n🏁 토너먼트 결과:")
    print(f"최종 전적: {wins}승 {losses}패 {draws}무")
    
    total_games = wins + losses + draws
    if total_games > 0:
        win_rate = (wins / total_games) * 100
        print(f"승률: {win_rate:.1f}%")
        
        if win_rate >= 70:
            print("🏆 가위바위보 챔피언!")
        elif win_rate >= 50:
            print("👍 좋은 실력!")
        else:
            print("💪 더 연습해보세요!")

# 게임 메뉴 시스템
def main():
    """메인 게임 선택"""
    games = {
        1: ("🎯 숫자 맞추기", number_guessing_game),
        2: ("📚 구구단 퀴즈", multiplication_quiz), 
        3: ("🎰 복권 시뮬레이터", lottery_simulator),
        4: ("✂️ 가위바위보 토너먼트", rock_paper_scissors_tournament)
    }
    
    while True:
        print(f"\n" + "="*40)
        print("🎮 For문 게임 센터")
        print("="*40)
        
        for num, (name, _) in games.items():
            print(f"{num}. {name}")
        print("5. 🚪 종료")
        
        try:
            choice = int(input("\n게임을 선택하세요 (1-5): "))
            
            if choice in games:
                name, game_func = games[choice]
                print(f"\n{name}을(를) 시작합니다!")
                game_func()
                
                # 게임 후 계속할지 묻기
                play_again = input("\n다른 게임을 하시겠습니까? (y/n): ")
                if play_again.lower() != 'y':
                    break
                    
            elif choice == 5:
                print("👋 게임을 종료합니다!")
                break
            else:
                print("❌ 1-5 사이의 번호를 선택하세요!")
                
        except ValueError:
            print("❌ 올바른 번호를 입력하세요!")

# 프로그램 실행
if __name__ == "__main__":
    main()
```

---

### Part 2: while문과 제어문 (40분)

#### ⭕ while문 기본

```python
print("⭕ while문 기본")
print("=" * 15)

# 1. 기본 while문
print("📊 while문 기본 구조")

count = 1
print("1부터 5까지 출력:")
while count <= 5:
    print(f"  count = {count}")
    count += 1  # 이 부분이 없으면 무한루프!

print(f"while문 종료 후 count = {count}")

print("=" * 30)

# 2. 사용자 입력을 받는 while문
print("🎯 올바른 입력 받기")

while True:
    try:
        age = int(input("나이를 입력하세요 (1-120): "))
        if 1 <= age <= 120:
            print(f"✅ 입력된 나이: {age}세")
            break
        else:
            print("❌ 1세부터 120세 사이의 나이를 입력하세요!")
    except ValueError:
        print("❌ 숫자만 입력하세요!")

print("=" * 30)

# 3. 누적 계산
print("🧮 누적 계산")

# 팩토리얼 계산
n = 5
factorial = 1
i = 1

print(f"{n}! 계산:")
while i <= n:
    print(f"  {factorial} × {i} = {factorial * i}")
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")

# 제곱근 추정 (뉴턴-랩슨 방법 간단 버전)
print("\n제곱근 근사값 계산:")
number = 25
guess = number / 2  # 초기 추정값
precision = 0.0001

iteration = 0
print(f"{number}의 제곱근 계산:")
while abs(guess * guess - number) > precision:
    iteration += 1
    new_guess = (guess + number / guess) / 2
    print(f"  {iteration}번째: {guess:.6f} -> {new_guess:.6f}")
    guess = new_guess
    
    if iteration > 10:  # 무한루프 방지
        break

print(f"근사값: {guess:.6f}")
print(f"실제값: {number**0.5:.6f}")

print("=" * 30)

# 4. 조건 기반 반복
print("💰 목표 달성 시뮬레이션")

# 저축 목표 달성
target_amount = 1000000  # 100만원
current_amount = 0
monthly_saving = 50000   # 월 5만원
month = 0

print(f"목표: {target_amount:,}원")
print(f"월 저축액: {monthly_saving:,}원")
print()

while current_amount < target_amount:
    month += 1
    current_amount += monthly_saving
    
    # 이자 계산 (연 3% 가정, 월복리)
    monthly_interest = current_amount * 0.03 / 12
    current_amount += monthly_interest
    
    print(f"{month:2d}개월 후: {current_amount:,.0f}원 (이자: {monthly_interest:,.0f}원)")

print(f"\n🎉 목표 달성! {month}개월 만에 {current_amount:,.0f}원 모았습니다!")

print("=" * 30)

# 5. 리스트와 while문
print("📋 리스트 처리")

numbers = [10, 25, 3, 47, 8, 91, 34, 15, 62, 7]
print(f"숫자 리스트: {numbers}")

# 최댓값 찾기
index = 0
max_value = numbers[0]
max_index = 0

while index < len(numbers):
    if numbers[index] > max_value:
        max_value = numbers[index]
        max_index = index
    index += 1

print(f"최댓값: {max_value} (인덱스 {max_index})")

# 조건에 맞는 원소 찾기
target = 47
index = 0
found = False

while index < len(numbers) and not found:
    if numbers[index] == target:
        print(f"값 {target}을 인덱스 {index}에서 찾았습니다!")
        found = True
    index += 1

if not found:
    print(f"값 {target}을 찾을 수 없습니다.")
```

#### 🔄 break와 continue

```python
print("🔄 break와 continue")
print("=" * 20)

# 1. break 문
print("🚫 break문 - 반복문 완전 탈출")

print("1부터 10까지 숫자 중 5가 나오면 중단:")
for i in range(1, 11):
    if i == 5:
        print(f"  {i}에서 break 실행!")
        break
    print(f"  {i}")

print("for문 종료")

print("\nwhile문에서 break:")
count = 0
while True:  # 무한 루프
    count += 1
    print(f"  카운트: {count}")
    
    if count == 3:
        print("  3에 도달했으므로 break!")
        break

print("=" * 30)

# 2. continue문
print("⏭️ continue문 - 현재 반복 건너뛰기")

print("1부터 10까지, 짝수는 건너뛰기:")
for i in range(1, 11):
    if i % 2 == 0:  # 짝수면
        continue    # 아래 코드 건너뛰고 다음 반복으로
    print(f"  홀수: {i}")

print("\nwhile문에서 continue:")
count = 0
while count < 10:
    count += 1
    
    if count % 3 == 0:  # 3의 배수는 건너뛰기
        continue
    
    print(f"  {count} (3의 배수 아님)")

print("=" * 30)

# 3. 실용적인 break/continue 활용
print("💡 실용적인 활용 예제")

# 비밀번호 입력 (최대 3번 시도)
print("🔐 비밀번호 입력 시스템")
correct_password = "python123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input(f"비밀번호 입력 ({attempt}/{max_attempts}): ")
    
    if password == correct_password:
        print("✅ 로그인 성공!")
        break
    else:
        if attempt == max_attempts:
            print("❌ 로그인 실패! 계정이 잠겼습니다.")
        else:
            remaining = max_attempts - attempt
            print(f"❌ 틀렸습니다. {remaining}번 더 시도할 수 있습니다.")

print("=" * 30)

# 4. 숫자 처리에서 continue 활용
print("🔢 숫자 리스트 처리")

numbers = [10, -5, 0, 25, -3, 8, 0, 15, -7]
print(f"원본 리스트: {numbers}")

print("양수만 처리 (continue 사용):")
positive_sum = 0
positive_count = 0

for num in numbers:
    if num <= 0:  # 0이나 음수는 건너뛰기
        continue
    
    positive_sum += num
    positive_count += 1
    print(f"  양수 {num} 처리")

if positive_count > 0:
    average = positive_sum / positive_count
    print(f"양수의 합: {positive_sum}, 평균: {average:.2f}")

print("=" * 30)

# 5. 중첩 반복문에서 break
print("🔄 중첩 반복문에서 break")

print("구구단에서 곱이 30 이상인 첫 번째 경우 찾기:")
found = False

for i in range(2, 10):  # 2단부터 9단까지
    if found:
        break
        
    for j in range(1, 10):  # 1부터 9까지
        product = i * j
        print(f"  {i} × {j} = {product}")
        
        if product >= 30:
            print(f"  ✅ 30 이상 발견! ({i} × {j} = {product})")
            found = True
            break  # 안쪽 for문만 빠져나감

print("검색 완료")

print("=" * 30)

# 6. 사용자 메뉴 시스템
print("📋 메뉴 시스템 예제")

def calculator_menu():
    """계산기 메뉴 시스템"""
    while True:
        print("\n🧮 간단한 계산기")
        print("1. ➕ 더하기")
        print("2. ➖ 빼기")
        print("3. ✖️ 곱하기")
        print("4. ➗ 나누기")
        print("5. 🚪 종료")
        
        choice = input("선택하세요 (1-5): ")
        
        if choice == '5':
            print("👋 계산기를 종료합니다!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("❌ 1-5 사이의 번호를 선택하세요!")
            continue
        
        # 숫자 입력
        try:
            a = float(input("첫 번째 숫자: "))
            b = float(input("두 번째 숫자: "))
        except ValueError:
            print("❌ 올바른 숫자를 입력하세요!")
            continue
        
        # 계산 수행
        if choice == '1':
            result = a + b
            operation = "+"
        elif choice == '2':
            result = a - b
            operation = "-"
        elif choice == '3':
            result = a * b
            operation = "×"
        elif choice == '4':
            if b == 0:
                print("❌ 0으로 나눌 수 없습니다!")
                continue
            result = a / b
            operation = "÷"
        
        print(f"📊 결과: {a} {operation} {b} = {result}")

# 메뉴 실행 (주석 해제하여 실행)
# calculator_menu()
```

#### 🔚 else절과 고급 활용

```python
print("🔚 else절과 고급 활용")
print("=" * 22)

# 1. for-else문
print("🔍 for-else문")

# 소수 판별
print("소수 찾기:")
numbers_to_check = [17, 18, 19, 20, 21, 22, 23]

for num in numbers_to_check:
    print(f"\n{num} 검사:")
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"  {i}로 나누어 떨어짐 -> 합성수")
            break
    else:
        # break가 실행되지 않았을 때만 실행
        print(f"  어떤 수로도 나누어떨어지지 않음 -> 소수!")

print("=" * 30)

# 2. while-else문
print("🎯 while-else문")

# 완벽한 수 찾기 (자기 자신을 제외한 약수의 합이 자기 자신과 같은 수)
print("1부터 30까지 완벽한 수 찾기:")

for num in range(1, 31):
    divisor_sum = 0
    divisor = 1
    
    # 약수의 합 계산 (자기 자신 제외)
    while divisor < num:
        if num % divisor == 0:
            divisor_sum += divisor
        divisor += 1
    else:
        # while문이 정상 종료되었을 때
        if divisor_sum == num:
            print(f"  완벽한 수 발견: {num}")
            # 약수들 보여주기
            divisors = []
            for d in range(1, num):
                if num % d == 0:
                    divisors.append(d)
            print(f"    약수: {divisors}, 합: {sum(divisors)}")

print("=" * 30)

# 3. 실용적인 검색 예제
print("📚 도서 검색 시스템")

books = [
    {"title": "파이썬 프로그래밍", "author": "김파이", "year": 2023},
    {"title": "웹 개발 입문", "author": "이웹", "year": 2022},
    {"title": "데이터 사이언스", "author": "박데이", "year": 2023},
    {"title": "머신러닝 기초", "author": "최머신", "year": 2021},
    {"title": "알고리즘 정복", "author": "정알고", "year": 2024}
]

search_keyword = "머신러닝"
print(f"'{search_keyword}' 검색 결과:")

for book in books:
    if search_keyword in book["title"]:
        print(f"✅ 찾았습니다!")
        print(f"   제목: {book['title']}")
        print(f"   저자: {book['author']}")
        print(f"   출판년도: {book['year']}")
        break
else:
    print("❌ 해당 키워드의 책을 찾을 수 없습니다.")

print("=" * 30)

# 4. 다중 조건 검색
print("🔍 고급 검색")

# 연도별 책 찾기
target_year = 2023
print(f"{target_year}년 출간 도서:")

found_books = []
for book in books:
    if book["year"] == target_year:
        found_books.append(book)

if found_books:
    print(f"📚 {len(found_books)}권 발견:")
    for i, book in enumerate(found_books, 1):
        print(f"  {i}. {book['title']} - {book['author']}")
else:
    print("❌ 해당 년도의 책이 없습니다.")

print("=" * 30)

# 5. 패턴 매칭 예제
print("🎨 패턴 매칭")

# 피보나치 수열에서 특정 조건 찾기
print("피보나치 수열에서 1000 이하인 3의 배수 찾기:")

a, b = 0, 1
fibonacci_numbers = [0, 1]

while b <= 1000:
    next_fib = a + b
    fibonacci_numbers.append(next_fib)
    a, b = b, next_fib

print("피보나치 수열:", fibonacci_numbers)

print("3의 배수인 피보나치 수:")
multiples_of_3 = []
for fib in fibonacci_numbers:
    if fib % 3 == 0 and fib > 0:
        multiples_of_3.append(fib)

print(f"  {multiples_of_3}")

print("=" * 30)

# 6. 실시간 입력 처리
print("💬 실시간 채팅 시뮬레이션")

def chat_simulator():
    """간단한 채팅 시뮬레이션"""
    print("채팅을 시작합니다! ('quit'을 입력하면 종료)")
    print("명령어: '/help' - 도움말, '/users' - 사용자 목록")
    
    users_online = ["Alice", "Bob", "Charlie"]
    message_count = 0
    
    while True:
        message = input("💬 ")
        
        if message.lower() == 'quit':
            print("👋 채팅을 종료합니다.")
            break
        
        if message == '/help':
            print("📋 사용 가능한 명령어:")
            print("  /help - 이 도움말")
            print("  /users - 온라인 사용자 목록")
            print("  quit - 채팅 종료")
            continue
        
        if message == '/users':
            print(f"👥 온라인 사용자 ({len(users_online)}명):")
            for user in users_online:
                print(f"  🟢 {user}")
            continue
        
        if message.strip() == '':
            print("❌ 빈 메시지는 보낼 수 없습니다!")
            continue
        
        # 일반 메시지 처리
        message_count += 1
        print(f"📨 [{message_count:03d}] You: {message}")
        
        # 간단한 자동 응답
        if "안녕" in message:
            print("🤖 Bot: 안녕하세요! 좋은 하루 되세요!")
        elif "날씨" in message:
            print("🤖 Bot: 오늘 날씨가 정말 좋네요! ☀️")
        elif "?" in message:
            print("🤖 Bot: 흥미로운 질문이네요! 🤔")

# 채팅 시뮬레이션 (주석 해제하여 실행)
# chat_simulator()
```

---

### Part 3: 고급 반복문 (50분)

#### 🔄 중첩 반복문

```python
print("🔄 중첩 반복문")
print("=" * 15)

# 1. 기본 중첩 for문
print("📊 기본 중첩 for문")

print("간단한 표 만들기:")
for i in range(1, 4):
    for j in range(1, 5):
        product = i * j
        print(f"{product:3d}", end=" ")
    print()  # 줄바꿈

print("=" * 30)

# 2. 구구단 완전판
print("📚 구구단 완전판")

print("구구단 2단~9단:")
print("    ", end="")
for i in range(1, 10):
    print(f" {i}단 ", end="")
print()

print("    " + "─" * 54)

for i in range(1, 10):  # 1~9 (곱하는 수)
    print(f" ×{i} ", end="")
    
    for dan in range(2, 10):  # 2단~9단
        result = dan * i
        print(f"{result:4d}", end="")
    print()

print("=" * 30)

# 3. 다양한 별 패턴
print("⭐ 별 패턴 모음")

# 직각삼각형
print("1. 직각삼각형:")
for i in range(1, 6):
    for j in range(i):
        print("★", end="")
    print()

print()

# 역직각삼각형
print("2. 역직각삼각형:")
for i in range(5, 0, -1):
    for j in range(i):
        print("☆", end="")
    print()

print()

# 정삼각형
print("3. 정삼각형:")
for i in range(1, 6):
    # 공백 출력
    for j in range(5 - i):
        print(" ", end="")
    # 별 출력
    for j in range(2 * i - 1):
        print("★", end="")
    print()

print()

# 다이아몬드
print("4. 다이아몬드:")
# 위쪽 삼각형
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("♦", end="")
    print()

# 아래쪽 역삼각형
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("♦", end="")
    print()

print()

# 속이 빈 사각형
print("5. 속이 빈 사각형:")
width, height = 8, 5

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("■", end="")
        else:
            print(" ", end="")
    print()

print("=" * 30)

# 4. 숫자 패턴
print("🔢 숫자 패턴")

# 숫자 피라미드
print("1. 숫자 피라미드:")
for i in range(1, 6):
    # 앞쪽 공백
    for j in range(5 - i):
        print(" ", end="")
    
    # 증가하는 숫자
    for j in range(1, i + 1):
        print(j, end="")
    
    # 감소하는 숫자
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

print()

# 곱셈표 형태
print("2. 곱셈표:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:2d}", end=" ")
    print()

print()

# 파스칼의 삼각형
print("3. 파스칼의 삼각형:")
n = 6

# 파스칼 계수 계산을 위한 함수
def pascal_coefficient(row, col):
    if col == 0 or col == row:
        return 1
    
    result = 1
    for i in range(col):
        result = result * (row - i) // (i + 1)
    return result

for i in range(n):
    # 앞쪽 공백
    for j in range(n - i - 1):
        print("  ", end="")
    
    # 파스칼 계수 출력
    for j in range(i + 1):
        coef = pascal_coefficient(i, j)
        print(f"{coef:3d}", end=" ")
    
    print()

print("=" * 30)

# 5. 2차원 리스트 처리
print("📋 2차원 리스트 처리")

# 성적표 만들기
students = ["김철수", "이영희", "박민수", "최지원"]
subjects = ["국어", "영어", "수학", "과학"]

# 랜덤 점수 생성 (실제로는 입력받을 수 있음)
import random
scores = []
for i in range(len(students)):
    student_scores = []
    for j in range(len(subjects)):
        score = random.randint(70, 100)
        student_scores.append(score)
    scores.append(student_scores)

# 성적표 출력
print("📊 학생 성적표:")
print("     ", end="")
for subject in subjects:
    print(f"{subject:>6}", end="")
print("  평균")

print("─" * 40)

for i in range(len(students)):
    print(f"{students[i]:4s}", end="")
    
    total = 0
    for j in range(len(subjects)):
        score = scores[i][j]
        print(f"{score:6d}", end="")
        total += score
    
    average = total / len(subjects)
    print(f"{average:6.1f}")

# 과목별 평균
print("─" * 40)
print("평균  ", end="")
for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(students)):
        subject_total += scores[i][j]
    subject_average = subject_total / len(students)
    print(f"{subject_average:6.1f}", end="")
print()

print("=" * 30)

# 6. 좌표계와 그래프
print("📈 좌표계 표시")

# 간단한 그래프 그리기
print("좌표평면 (0,0 ~ 9,9):")

# y축 (위에서 아래로)
for y in range(9, -1, -1):
    print(f"{y}", end=" ")
    
    # x축 (왼쪽에서 오른쪽으로)  
    for x in range(10):
        # 특정 좌표에 표시
        if x == 0 and y == 0:
            print("O", end=" ")  # 원점
        elif x == 0:
            print("│", end=" ")  # y축
        elif y == 0:
            print("─", end=" ")  # x축
        elif x == 3 and y == 7:
            print("A", end=" ")  # 점 A
        elif x == 7 and y == 2:
            print("B", end=" ")  # 점 B
        elif x == 5 and y == 5:
            print("C", end=" ")  # 점 C
        else:
            print("·", end=" ")
    print()

print("  " + " ".join(str(i) for i in range(10)))

print("=" * 30)

# 7. 복잡한 패턴 만들기
print("🎨 복잡한 패턴")

# 체스판 패턴
print("체스판 패턴 (8×8):")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("□", end="")
        else:
            print("■", end="")
    print()

print()

# 나선 모양 숫자
print("나선 숫자 패턴 (5×5):")
n = 5
matrix = [[0] * n for _ in range(n)]

# 방향: 오른쪽 → 아래 → 왼쪽 → 위
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_idx = 0

row, col = 0, 0
for num in range(1, n * n + 1):
    matrix[row][col] = num
    
    # 다음 위치 계산
    next_row = row + directions[direction_idx][0]
    next_col = col + directions[direction_idx][1]
    
    # 경계 체크 또는 이미 채워진 곳 체크
    if (next_row < 0 or next_row >= n or 
        next_col < 0 or next_col >= n or 
        matrix[next_row][next_col] != 0):
        # 방향 전환
        direction_idx = (direction_idx + 1) % 4
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]
    
    row, col = next_row, next_col

# 출력
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2d}", end=" ")
    print()
```

#### 🎮 실습: 고급 게임 만들기

```python
# 파일명: advanced_loop_games.py
import random
import time

print("🎮 고급 반복문 게임")
print("=" * 20)

class NumberGuessingAdvanced:
    """고급 숫자 맞추기 게임"""
    
    def __init__(self):
        self.min_range = 1
        self.max_range = 100
        self.secret_number = random.randint(self.min_range, self.max_range)
        self.attempts = 0
        self.max_attempts = 7
        self.hints_used = 0
        self.max_hints = 2
        
    def give_hint(self):
        """힌트 제공"""
        if self.hints_used >= self.max_hints:
            print("❌ 더 이상 힌트를 사용할 수 없습니다!")
            return
        
        self.hints_used += 1
        
        if self.hints_used == 1:
            # 홀짝 힌트
            parity = "홀수" if self.secret_number % 2 == 1 else "짝수"
            print(f"💡 힌트 1: 숫자는 {parity}입니다!")
        
        elif self.hints_used == 2:
            # 범위 힌트
            if self.secret_number <= 25:
                print("💡 힌트 2: 숫자는 25 이하입니다!")
            elif self.secret_number <= 50:
                print("💡 힌트 2: 숫자는 26~50 사이입니다!")
            elif self.secret_number <= 75:
                print("💡 힌트 2: 숫자는 51~75 사이입니다!")
            else:
                print("💡 힌트 2: 숫자는 76 이상입니다!")
    
    def analyze_guess(self, guess):
        """추측 분석"""
        difference = abs(guess - self.secret_number)
        
        if difference == 0:
            return "correct"
        elif difference <= 5:
            return "very_close"
        elif difference <= 15:
            return "close"
        elif difference <= 30:
            return "warm"
        else:
            return "cold"
    
    def play(self):
        """게임 실행"""
        print(f"\n🎯 고급 숫자 맞추기 게임")
        print(f"📊 범위: {self.min_range}~{self.max_range}")
        print(f"🎫 기회: {self.max_attempts}번")
        print(f"💡 힌트: {self.max_hints}개 사용 가능")
        print("💬 명령어: 'hint' - 힌트, 'quit' - 포기")
        
        guesses = []
        
        while self.attempts < self.max_attempts:
            self.attempts += 1
            print(f"\n🎲 {self.attempts}번째 시도:")
            
            user_input = input("숫자를 입력하세요: ").strip().lower()
            
            if user_input == 'quit':
                print(f"😢 포기하셨습니다. 정답은 {self.secret_number}였습니다.")
                return False
            
            if user_input == 'hint':
                self.give_hint()
                self.attempts -= 1  # 힌트는 시도 횟수에서 제외
                continue
            
            try:
                guess = int(user_input)
                
                if guess < self.min_range or guess > self.max_range:
                    print(f"❌ {self.min_range}~{self.max_range} 사이의 숫자를 입력하세요!")
                    self.attempts -= 1
                    continue
                
                if guess in guesses:
                    print(f"❌ {guess}는 이미 시도한 숫자입니다!")
                    print(f"이전 시도: {guesses}")
                    self.attempts -= 1
                    continue
                
                guesses.append(guess)
                analysis = self.analyze_guess(guess)
                
                if analysis == "correct":
                    print(f"🎉 정답입니다! {self.attempts}번 만에 맞췄습니다!")
                    
                    # 성과 분석
                    if self.attempts <= 3:
                        print("🏆 천재! 완벽한 실력입니다!")
                    elif self.attempts <= 5:
                        print("👍 훌륭합니다! 좋은 실력이네요!")
                    else:
                        print("😊 성공! 포기하지 않는 정신이 훌륭합니다!")
                    
                    return True
                
                # 피드백 제공
                if guess < self.secret_number:
                    direction = "⬆️ 더 큰 수"
                else:
                    direction = "⬇️ 더 작은 수"
                
                feedback = {
                    "very_close": "🔥 매우 가까워요!",
                    "close": "🌡️ 가까워요!",
                    "warm": "😊 따뜻해요~",