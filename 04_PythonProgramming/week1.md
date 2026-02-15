# Week 1: 파이썬 들여다보기

--[목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 2 →](./week02.md)--

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. --파이썬 개발환경 구축--: 파이썬을 설치하고 IDLE을 사용할 수 있습니다
2. --첫 번째 프로그램 작성--: "Hello, Python!" 프로그램을 작성하고 실행할 수 있습니다
3. --대화형 셸 활용--: 파이썬을 계산기로 사용하고 간단한 변수를 다룰 수 있습니다
4. --기본 입출력 이해--: print() 함수와 input() 함수를 사용할 수 있습니다
5. --프로그래밍 개념 이해--: 프로그래밍 언어와 파이썬의 특징을 설명할 수 있습니다

---

## 📚 핵심 개념 요약

### 1. 프로그래밍 언어란?
- --정의--: 컴퓨터가 이해할 수 있는 명령어의 집합
- --종류--: 저수준 언어(기계어, 어셈블리어) vs 고수준 언어(Python, Java, C++)
- --컴파일러 vs 인터프리터--: 파이썬은 인터프리터 언어입니다

### 2. 파이썬의 특징
✅ --장점--:
- 배우기 쉽고 읽기 쉬운 문법
- 강력한 라이브러리와 프레임워크
- 다양한 분야 활용 (웹, 데이터 분석, AI, 자동화)
- 크로스 플랫폼 지원 (Windows, macOS, Linux)

❌ --단점--:
- 상대적으로 느린 실행 속도
- 모바일 개발 지원 부족

### 3. 파이썬 설치 및 환경
- --IDLE--: 파이썬 기본 제공 통합 개발 환경
- --대화형 모드--: >>> 프롬프트에서 즉시 실행
- --스크립트 모드--: .py 파일로 저장 후 실행

---

## 💻 실습 세션 (2시간)

### Part 1: 파이썬 설치 및 환경 설정 (30분)

#### 🔧 Step 1: 파이썬 다운로드 및 설치

1. --웹사이트 방문--
   - https://www.python.org 접속
   - [Downloads] → [Windows] 또는 해당 운영체제 선택

2. --설치 과정--
   ```
   ✅ Add Python to PATH 체크박스 반드시 선택!
   ✅ Install Now 클릭
   ✅ 설치 완료 후 Close 클릭
   ```

3. --설치 확인--
   - 명령 프롬프트(cmd) 실행
   - `python --version` 입력
   - Python 3.x.x 버전 정보 확인

#### 🖥️ Step 2: IDLE 실행하기

1. --IDLE 찾기--
   - 시작 메뉴 → 모든 앱 → Python 3.x → IDLE
   - 또는 검색창에 "IDLE" 입력

2. --IDLE 화면 구성--
   ```
   Python 3.x.x (...) on win32
   Type "help", "copyright", "credits" or "license()" for more information.
   >>> 
   ```

#### 🎉 Step 3: 첫 번째 코드 실행

```python
>>> print("Hello, Python!")
Hello, Python!

>>> print("안녕하세요, 파이썬!")
안녕하세요, 파이썬!

>>> print("Welcome to Programming World! 🐍")
Welcome to Programming World! 🐍
```

--💡 실습 포인트--:
- `>>>` 프롬프트 뒤에 코드 입력
- Enter 키로 즉시 실행
- 대소문자 구분 주의 (print, not Print)

---

### Part 2: 대화형 셸 사용하기 (40분)

#### 🧮 계산기로 사용하기

--기본 사칙연산--:
```python
>>> 10 + 5
15
>>> 20 - 7
13
>>> 6 - 8
48
>>> 15 / 3
5.0
>>> 17 // 5    # 몫
3
>>> 17 % 5     # 나머지
2
>>> 2 ** 3     # 거듭제곱
8
```

--복잡한 계산--:
```python
>>> (10 + 5) * 3
45
>>> 2 * 3 + 4 * 5
26
>>> (100 - 20) / 4
20.0

# 원의 넓이 구하기 (반지름 = 5)
>>> 3.14159 * 5 * 5
78.53975
```

#### 📦 변수 사용해보기

--변수 생성과 사용--:
```python
>>> name = "홍길동"
>>> age = 25
>>> height = 175.5

>>> print(name)
홍길동
>>> print(age)
25
>>> print(height)
175.5

# 여러 변수 한 번에 출력
>>> print(name, age, height)
홍길동 25 175.5
```

--변수를 이용한 계산--:
```python
>>> a = 10
>>> b = 20
>>> result = a + b
>>> print("결과:", result)
결과: 30

# 변수 값 변경
>>> a = 100
>>> result = a + b
>>> print("새로운 결과:", result)
새로운 결과: 120
```

#### 🎯 간단한 프로그램 작성

--온도 변환기--:
```python
>>> celsius = 25
>>> fahrenheit = celsius * 9/5 + 32
>>> print(f"{celsius}도 = {fahrenheit}도")
25도 = 77.0도
```

--간단한 할인 계산--:
```python
>>> price = 10000
>>> discount_rate = 0.2  # 20% 할인
>>> discount_price = price * (1 - discount_rate)
>>> print(f"원가: {price}원, 할인가: {discount_price}원")
원가: 10000원, 할인가: 8000.0원
```

---

### Part 3: 실습 예제 (50분)

#### 📝 Example 1: 자기소개 프로그램

--IDLE에서 새 파일 만들기--:
1. IDLE 메뉴: File → New File
2. 다음 코드 입력:

```python
# 파일명: self_introduction.py
print("=" * 30)
print("     자기소개 프로그램")
print("=" * 30)

name = "김파이썬"
age = 22
hobby = "프로그래밍"
dream = "개발자"

print(f"안녕하세요! 제 이름은 {name}입니다.")
print(f"나이는 {age}살이고,")
print(f"취미는 {hobby}입니다.")
print(f"꿈은 {dream}가 되는 것입니다!")
print("=" * 30)
print("만나서 반가워요! 🐍")
```

--실행하기--:
- F5 키 또는 Run → Run Module
- 자신의 정보로 변수값 수정해보기

--실행 결과--:
```
==============================
     자기소개 프로그램
==============================
안녕하세요! 제 이름은 김파이썬입니다.
나이는 22살이고,
취미는 프로그래밍입니다.
꿈은 개발자가 되는 것입니다!
==============================
만나서 반가워요! 🐍
```

#### 🔢 Example 2: 간단한 계산기

```python
# 파일명: simple_calculator.py
print("🔢 간단한 계산기 프로그램")
print("-" * 25)

# 두 수 입력받기
num1 = float(input("첫 번째 수를 입력하세요: "))
num2 = float(input("두 번째 수를 입력하세요: "))

# 사칙연산 수행
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# 결과 출력
print("\n📊 계산 결과")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(f"{num1} ÷ {num2} = {division:.2f}")

print("\n계산이 완료되었습니다! ✨")
```

--실행 예시--:
```
🔢 간단한 계산기 프로그램
-------------------------
첫 번째 수를 입력하세요: 15
두 번째 수를 입력하세요: 4

📊 계산 결과
15.0 + 4.0 = 19.0
15.0 - 4.0 = 11.0
15.0 × 4.0 = 60.0
15.0 ÷ 4.0 = 3.75

계산이 완료되었습니다! ✨
```

#### 🎨 Example 3: 화면 출력 연습

```python
# 파일명: output_practice.py
print("🎨 다양한 출력 연습")
print("=" * 30)

# 1. 기본 출력
print("1. 기본 출력:")
print("Hello, World!")
print("파이썬을 배워봅시다!")

print()  # 빈 줄 출력

# 2. 여러 값 출력
print("2. 여러 값 출력:")
name = "파이썬"
version = 3.9
print("언어:", name, "버전:", version)

print()

# 3. 구분자 변경
print("3. 구분자 변경:")
print("사과", "바나나", "오렌지", sep=" | ")
print("2024", "01", "15", sep="-")

print()

# 4. 줄바꿈 없이 출력
print("4. 줄바꿈 없이 출력:")
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Complete!")

print()

# 5. f-string 사용
print("5. f-string 사용:")
score = 95
grade = "A"
print(f"점수: {score}점, 등급: {grade}")

# 6. ASCII 아트
print("\n6. ASCII 아트:")
print("  🐍")
print(" /   \\")
print("(  o o )")
print(" \\  ^  /")
print("  ||||| ")
print("  ||||_")
```

--실행 결과--:
```
🎨 다양한 출력 연습
==============================
1. 기본 출력:
Hello, World!
파이썬을 배워봅시다!

2. 여러 값 출력:
언어: 파이썬 버전: 3.9

3. 구분자 변경:
사과 | 바나나 | 오렌지
2024-01-15

4. 줄바꿈 없이 출력:
Loading... Complete!

5. f-string 사용:
점수: 95점, 등급: A

6. ASCII 아트:
  🐍
 /   \
(  o o )
 \  ^  /
  ||||| 
  ||||_
```

---

## 📝 연습 문제 (5개)

### 문제 1: 기본 출력
다음과 같이 출력하는 프로그램을 작성하세요.
```
프로그래밍 첫걸음
파이썬과 함께하는 여행 시작!
```

--해답--:
```python
print("프로그래밍 첫걸음")
print("파이썬과 함께하는 여행 시작!")
```

### 문제 2: 변수 활용
나이, 이름, 좋아하는 색깔을 변수에 저장하고 다음과 같은 형식으로 출력하세요.
```
이름: 김철수, 나이: 20세, 좋아하는 색: 파란색
```

--해답--:
```python
name = "김철수"
age = 20
favorite_color = "파란색"
print(f"이름: {name}, 나이: {age}세, 좋아하는 색: {favorite_color}")
```

### 문제 3: 간단한 계산
반지름이 7인 원의 넓이와 둘레를 계산하여 출력하세요. (π = 3.14159 사용)

--해답--:
```python
radius = 7
pi = 3.14159
area = pi * radius * radius
circumference = 2 * pi * radius

print(f"반지름 {radius}인 원의 넓이: {area}")
print(f"반지름 {radius}인 원의 둘레: {circumference}")
```

### 문제 4: 입력받아서 계산
사용자로부터 두 수를 입력받아 평균을 계산하여 출력하세요.

--해답--:
```python
num1 = float(input("첫 번째 수: "))
num2 = float(input("두 번째 수: "))
average = (num1 + num2) / 2
print(f"두 수의 평균: {average}")
```

### 문제 5: 패턴 출력
다음과 같은 패턴을 출력하세요.
```
★
★★
★★★
```

--해답--:
```python
print("★")
print("★★")
print("★★★")
```

---

## 🚀 도전 과제 (2개)

### 도전 과제 1: 환전 계산기
사용자로부터 원화 금액을 입력받아 달러로 환전하는 프로그램을 작성하세요.
- 환율: 1달러 = 1300원
- 소수점 둘째 자리까지 표시

--힌트--:
```python
# 사용자 입력
won = int(input("원화 금액을 입력하세요: "))

# 환율 계산
exchange_rate = 1300
dollar = won / exchange_rate

# 결과 출력
print(f"{won}원 = ${dollar:.2f}")
```

### 도전 과제 2: BMI 계산기
사용자의 키와 몸무게를 입력받아 BMI를 계산하고 결과를 출력하세요.
- BMI = 몸무게(kg) ÷ 키(m)²
- 키는 cm 단위로 입력받아 m 단위로 변환

--힌트--:
```python
# 사용자 입력
height_cm = float(input("키를 입력하세요(cm): "))
weight = float(input("몸무게를 입력하세요(kg): "))

# BMI 계산
height_m = height_cm / 100
bmi = weight / (height_m * height_m)

# 결과 출력
print(f"당신의 BMI는 {bmi:.1f}입니다.")
```

---

## ✅ 학습 체크리스트

이번 주 학습을 완료했다면 다음 항목들을 체크해보세요:

- [ ] 파이썬을 성공적으로 설치했습니다
- [ ] IDLE를 실행하고 사용할 수 있습니다
- [ ] `print()` 함수를 사용하여 다양한 출력을 할 수 있습니다
- [ ] 변수를 선언하고 값을 저장할 수 있습니다
- [ ] 기본적인 사칙연산을 수행할 수 있습니다
- [ ] `input()` 함수로 사용자 입력을 받을 수 있습니다
- [ ] f-string을 사용하여 변수를 포함한 문자열을 출력할 수 있습니다
- [ ] .py 파일로 프로그램을 저장하고 실행할 수 있습니다
- [ ] 주석(#)을 사용하여 코드에 설명을 추가할 수 있습니다
- [ ] 모든 연습문제를 완료했습니다

--완료율--: ___/10 항목

---

## 📖 다음 주 예습 내용

--Week 2: 미리 만드는 쓸 만한 프로그램--에서는 다음 내용을 학습합니다:

### 🔍 미리 살펴보기
1. --터틀 그래픽--: 거북이를 움직여 그림 그리기
2. --계산기 프로그램--: 더 고급진 계산기 만들기
3. --프로그램 저장--: 작성한 프로그램을 파일로 저장
4. --모듈 사용--: `turtle`, `random` 모듈 활용

### 📚 사전 준비
다음 코드를 미리 실행해보세요:
```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
turtle.done()
```

---

## 🔗 참고 자료

### 📖 공식 문서
- [파이썬 공식 사이트](https://www.python.org/)
- [파이썬 한국어 문서](https://docs.python.org/ko/3/)
- [파이썬 튜토리얼](https://docs.python.org/ko/3/tutorial/)

### 🛠️ 도구 및 환경
- [Python 다운로드](https://www.python.org/downloads/)
- [IDLE 사용법](https://docs.python.org/ko/3/library/idle.html)
- [Visual Studio Code](https://code.visualstudio.com/) (추가 에디터)

### 📚 추가 학습 자료
- [점프 투 파이썬](https://wikidocs.net/book/1)
- [Python Tutor - 코드 시각화](http://pythontutor.com/)
- [W3Schools Python](https://www.w3schools.com/python/)

### 🎥 동영상 강의
- [생활코딩 파이썬](https://opentutorials.org/course/4769)
- [나도코딩 파이썬](https://www.youtube.com/watch?v=kWiCuklohdY&list=PLMsa_0kAjjrdiwQykI8eb3H4IRxLTqCnP)

---

## 💡 실습 꿀팁

### 🐛 자주 발생하는 오류
1. --NameError--: 변수명을 잘못 입력했을 때
   ```python
   >>> name = "홍길동"
   >>> print(Name)  # N이 대문자!
   NameError: name 'Name' is not defined
   ```

2. --SyntaxError--: 문법이 잘못되었을 때
   ```python
   >>> print("Hello"  # ) 빠짐!
   SyntaxError: unexpected EOF while parsing
   ```

3. --IndentationError--: 들여쓰기가 잘못되었을 때 (다음 주에 자세히)

### 🎯 효과적인 학습 방법
- --타이핑 연습--: 복사-붙여넣기 대신 직접 타이핑
- --변형 실습--: 예제 코드의 값을 바꿔가며 실험
- --오류 경험--: 일부러 오류를 발생시켜 오류 메시지 익히기
- --메모 습관--: 새로 배운 개념을 정리하며 학습

---

--🎉 첫 번째 주 수고하셨습니다! 파이썬의 세계에 오신 것을 환영합니다! 🐍--

-"모든 전문가도 처음에는 초보자였다. 꾸준히 연습하면 반드시 실력이 향상됩니다!"-