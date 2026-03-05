
**[← Week 11](./week11.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 13 →](./week13.md)**

Week 12: 객체지향 프로그래밍 (OOP)

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **클래스와 객체**: 클래스를 설계하고 객체를 생성하여 활용할 수 있습니다
2. **생성자와 소멸자**: __init__ 메서드를 활용한 객체 초기화를 이해합니다
3. **인스턴스 변수와 메서드**: 객체의 속성과 행동을 정의하고 조작할 수 있습니다
4. **상속과 다형성**: 클래스 상속을 통한 코드 재사용과 확장을 구현합니다
5. **캡슐화**: 데이터 은닉과 접근 제어를 통한 안전한 프로그래밍을 실습합니다
6. **실전 시스템 설계**: 학생 관리, 은행 계좌, 게임 캐릭터 등 실용적인 시스템을 설계합니다

---

## 📚 핵심 개념 요약

### 1. 객체지향 프로그래밍 기초

| 개념 | 설명 | 예시 |
|------|------|------|
| **클래스(Class)** | 객체를 만들기 위한 틀/설계도 | `class Car:` |
| **객체(Object)** | 클래스로부터 생성된 실체 | `my_car = Car()` |
| **인스턴스(Instance)** | 생성된 객체의 다른 이름 | my_car는 Car의 인스턴스 |
| **속성(Attribute)** | 객체가 가진 데이터 | `self.name`, `self.age` |
| **메서드(Method)** | 객체가 수행하는 동작 | `def drive(self):` |

### 2. OOP 4대 특성

| 특성 | 설명 | 장점 | 구현 방법 |
|------|------|------|-----------|
| **캡슐화** | 데이터와 메서드를 하나로 묶음 | 데이터 보호, 유지보수 용이 | `_private`, `__private` |
| **상속** | 기존 클래스를 확장하여 새 클래스 생성 | 코드 재사용, 계층 구조 | `class Child(Parent):` |
| **다형성** | 같은 메서드가 다른 동작 수행 | 유연성, 확장성 | 메서드 오버라이딩 |
| **추상화** | 복잡한 구현을 숨기고 간단한 인터페이스 제공 | 복잡성 감소, 사용 편의성 | 추상 클래스, 인터페이스 |

### 3. 메서드 종류

| 메서드 타입 | 정의 | 첫 번째 매개변수 | 호출 방법 | 용도 |
|-------------|------|------------------|-----------|------|
| **인스턴스 메서드** | `def method(self):` | `self` | `obj.method()` | 객체 상태 조작 |
| **클래스 메서드** | `@classmethod def method(cls):` | `cls` | `Class.method()` | 클래스 차원 작업 |
| **정적 메서드** | `@staticmethod def method():` | 없음 | `Class.method()` | 유틸리티 함수 |

### 4. 특별한 메서드 (매직 메서드)

| 메서드 | 용도 | 호출 시기 | 예시 |
|--------|------|-----------|------|
| `__init__` | 생성자 | 객체 생성 시 | `obj = Class()` |
| `__del__` | 소멸자 | 객체 삭제 시 | `del obj` |
| `__str__` | 문자열 표현 | `print(obj)` | 사용자 친화적 출력 |
| `__repr__` | 공식 문자열 표현 | `repr(obj)` | 개발자용 출력 |
| `__len__` | 길이 | `len(obj)` | 컨테이너 크기 |

---

## 💻 실습 세션 (2시간)

### Part 1: 클래스 기초 (30분)

#### 📝 클래스 정의와 객체 생성

```python
print("📝 클래스 정의와 객체 생성")
print("=" * 18)

# 1. 가장 간단한 클래스
print("1️⃣ 가장 간단한 클래스")

class SimpleClass:
    """가장 간단한 클래스 예제"""
    pass  # 아무것도 하지 않는 클래스

# 객체 생성
obj1 = SimpleClass()
obj2 = SimpleClass()

print(f"obj1: {obj1}")
print(f"obj2: {obj2}")
print(f"obj1과 obj2는 같은 객체인가? {obj1 is obj2}")
print(f"obj1의 타입: {type(obj1)}")

print("=" * 30)

# 2. 속성을 가진 클래스
print("2️⃣ 속성을 가진 클래스")

class Person:
    """사람을 나타내는 클래스"""
    
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age):
        """생성자 - 객체 초기화"""
        print(f"👶 새로운 Person 객체 생성: {name}")
        
        # 인스턴스 변수 (각 객체마다 고유)
        self.name = name
        self.age = age
        self.is_alive = True
        
        # 클래스 변수 증가
        Person.population += 1
    
    def introduce(self):
        """자기소개 메서드"""
        return f"안녕하세요! 저는 {self.name}이고, {self.age}살입니다."
    
    def have_birthday(self):
        """생일을 맞는 메서드"""
        self.age += 1
        print(f"🎂 {self.name}님의 생일! 이제 {self.age}살입니다.")
    
    def __str__(self):
        """객체의 문자열 표현"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """객체의 공식 문자열 표현"""
        return f"Person('{self.name}', {self.age})"

# Person 객체들 생성
print("👥 Person 객체들 생성:")

person1 = Person("김철수", 25)
person2 = Person("이영희", 30)
person3 = Person("박민수", 22)

print(f"현재 인구: {Person.population}명")

# 객체 정보 출력
print("\n📋 생성된 사람들:")
people = [person1, person2, person3]

for person in people:
    print(f"  {person} - {person.introduce()}")

# 메서드 호출
print("\n🎉 생일 파티:")
person1.have_birthday()
person2.have_birthday()

print(f"\n업데이트된 정보:")
for person in people:
    print(f"  {person}")

print("=" * 30)

# 3. self의 이해
print("3️⃣ self의 이해")

class Calculator:
    """계산기 클래스로 self 이해하기"""
    
    def __init__(self, name):
        self.name = name
        self.result = 0
        self.history = []
    
    def add(self, number):
        """덧셈"""
        self.result += number
        self.history.append(f"+{number} = {self.result}")
        return self  # 메서드 체이닝을 위해 self 반환
    
    def subtract(self, number):
        """뺄셈"""
        self.result -= number
        self.history.append(f"-{number} = {self.result}")
        return self
    
    def multiply(self, number):
        """곱셈"""
        self.result *= number
        self.history.append(f"×{number} = {self.result}")
        return self
    
    def divide(self, number):
        """나눗셈"""
        if number != 0:
            self.result /= number
            self.history.append(f"÷{number} = {self.result}")
        else:
            print("❌ 0으로 나눌 수 없습니다!")
        return self
    
    def clear(self):
        """초기화"""
        self.result = 0
        self.history.clear()
        print(f"🔄 {self.name} 계산기가 초기화되었습니다.")
        return self
    
    def show_result(self):
        """결과 표시"""
        print(f"📊 {self.name} 계산 결과: {self.result}")
        return self
    
    def show_history(self):
        """계산 과정 표시"""
        print(f"📜 {self.name} 계산 과정:")
        if self.history:
            for step in self.history:
                print(f"  {step}")
        else:
            print("  (계산 기록이 없습니다)")
        return self

# Calculator 사용 예제
print("🧮 계산기 사용 예제:")

calc1 = Calculator("계산기1")
calc2 = Calculator("계산기2")

# calc1 사용
print("\n계산기1 작업:")
calc1.add(10).multiply(2).subtract(5).show_result().show_history()

print("\n계산기2 작업:")
calc2.add(100).divide(4).add(25).show_result().show_history()

# 각 계산기는 독립적인 상태를 유지
print(f"\ncalc1 최종 결과: {calc1.result}")
print(f"calc2 최종 결과: {calc2.result}")

print("=" * 30)

# 4. 클래스와 인스턴스 변수 구분
print("4️⃣ 클래스 변수 vs 인스턴스 변수")

class BankAccount:
    """은행 계좌 클래스"""
    
    # 클래스 변수들
    bank_name = "파이썬 은행"
    interest_rate = 0.03  # 3% 이자율
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, owner, initial_balance=0):
        """계좌 생성"""
        # 인스턴스 변수들
        self.owner = owner
        self.balance = initial_balance
        self.account_number = f"ACC-{BankAccount.total_accounts + 1:04d}"
        self.transaction_history = []
        
        # 클래스 변수 업데이트
        BankAccount.total_accounts += 1
        BankAccount.total_balance += initial_balance
        
        self.transaction_history.append(f"계좌 개설: {initial_balance}원")
        print(f"✅ {self.owner}님의 계좌({self.account_number})가 개설되었습니다.")
    
    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            BankAccount.total_balance += amount
            self.transaction_history.append(f"입금: +{amount:,}원")
            print(f"💰 {amount:,}원 입금 완료. 잔액: {self.balance:,}원")
        else:
            print("❌ 0보다 큰 금액을 입금해주세요.")
    
    def withdraw(self, amount):
        """출금"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                BankAccount.total_balance -= amount
                self.transaction_history.append(f"출금: -{amount:,}원")
                print(f"💸 {amount:,}원 출금 완료. 잔액: {self.balance:,}원")
            else:
                print("❌ 잔액이 부족합니다.")
        else:
            print("❌ 0보다 큰 금액을 출금해주세요.")
    
    def check_balance(self):
        """잔액 조회"""
        print(f"💳 {self.owner}님({self.account_number}) 잔액: {self.balance:,}원")
        return self.balance
    
    @classmethod
    def get_bank_info(cls):
        """은행 전체 정보 조회 (클래스 메서드)"""
        print(f"🏦 {cls.bank_name}")
        print(f"   총 계좌 수: {cls.total_accounts}개")
        print(f"   총 예치금: {cls.total_balance:,}원")
        print(f"   이자율: {cls.interest_rate*100}%")
    
    @staticmethod
    def calculate_interest(principal, rate, time):
        """이자 계산 (정적 메서드)"""
        interest = principal * rate * time
        return interest
    
    def show_transaction_history(self):
        """거래 내역 조회"""
        print(f"📊 {self.owner}님({self.account_number}) 거래 내역:")
        for transaction in self.transaction_history:
            print(f"   {transaction}")

# BankAccount 사용 예제
print("🏦 은행 계좌 시스템:")

# 초기 은행 정보
BankAccount.get_bank_info()

print("\n👥 계좌 개설:")
account1 = BankAccount("김철수", 100000)
account2 = BankAccount("이영희", 50000)
account3 = BankAccount("박민수")

print("\n🏦 계좌 개설 후 은행 정보:")
BankAccount.get_bank_info()

print("\n💰 거래 실습:")
# 김철수 계좌 거래
account1.deposit(50000)
account1.withdraw(20000)
account1.check_balance()

print()
# 이영희 계좌 거래
account2.deposit(100000)
account2.withdraw(200000)  # 잔액 부족
account2.check_balance()

print("\n📊 거래 내역:")
account1.show_transaction_history()
print()
account2.show_transaction_history()

print("\n💹 이자 계산 (정적 메서드):")
interest = BankAccount.calculate_interest(1000000, 0.03, 1)
print(f"원금 100만원, 연 3%, 1년 → 이자: {interest:,}원")

print("\n🏦 최종 은행 정보:")
BankAccount.get_bank_info()

print("=" * 30)

print("🎯 Part 1 요약:")
print("✅ 클래스 정의 및 객체 생성")
print("✅ __init__ 생성자 활용")
print("✅ self 개념과 활용")
print("✅ 인스턴스 변수와 메서드")
print("✅ 클래스 변수와 인스턴스 변수 구분")
print("✅ 클래스 메서드와 정적 메서드")
```

---

### Part 2: OOP 핵심 개념 (40분)

#### 🏗️ 상속과 다형성

```python
print("🏗️ 상속과 다형성")
print("=" * 12)

# 1. 기본 상속
print("1️⃣ 기본 상속")

class Animal:
    """동물 기본 클래스 (부모 클래스)"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
        print(f"🐾 동물 '{name}' ({species}) 생성")
    
    def eat(self, food):
        """먹기"""
        print(f"🍽️ {self.name}이(가) {food}을(를) 먹습니다.")
    
    def sleep(self):
        """자기"""
        print(f"😴 {self.name}이(가) 잠을 잡니다.")
    
    def make_sound(self):
        """소리내기 - 추상적 메서드 (하위 클래스에서 구현)"""
        print(f"🔊 {self.name}이(가) 소리를 냅니다.")
    
    def introduce(self):
        """자기소개"""
        return f"저는 {self.species} {self.name}입니다."
    
    def __str__(self):
        return f"{self.species} {self.name}"

class Dog(Animal):
    """개 클래스 (자식 클래스)"""
    
    def __init__(self, name, breed):
        # 부모 클래스의 __init__ 호출
        super().__init__(name, "개")
        self.breed = breed  # 개만의 고유 속성
        self.loyalty = 100
        print(f"🐕 {breed} 품종의 개가 추가로 초기화됨")
    
    def make_sound(self):
        """개의 소리 (메서드 오버라이딩)"""
        print(f"🐕 {self.name}: 멍멍!")
    
    def fetch(self, item):
        """물어오기 - 개만의 특별한 메서드"""
        print(f"🎾 {self.name}이(가) {item}을(를) 물어옵니다!")
    
    def wag_tail(self):
        """꼬리 흔들기"""
        print(f"🐕 {self.name}이(가) 꼬리를 신나게 흔듭니다!")
    
    def introduce(self):
        """자기소개 (메서드 오버라이딩)"""
        return f"멍멍! 저는 {self.breed} 품종의 {self.name}입니다!"

class Cat(Animal):
    """고양이 클래스 (자식 클래스)"""
    
    def __init__(self, name, color):
        super().__init__(name, "고양이")
        self.color = color
        self.independence = 80
        print(f"🐱 {color} 색깔의 고양이가 추가로 초기화됨")
    
    def make_sound(self):
        """고양이의 소리 (메서드 오버라이딩)"""
        print(f"🐱 {self.name}: 야옹~")
    
    def scratch(self, target):
        """할퀴기 - 고양이만의 특별한 메서드"""
        print(f"🐱 {self.name}이(가) {target}을(를) 할큅니다!")
    
    def purr(self):
        """골골거리기"""
        print(f"🐱 {self.name}이(가) 만족하며 골골거립니다~")
    
    def introduce(self):
        """자기소개 (메서드 오버라이딩)"""
        return f"냐옹~ 저는 {self.color} {self.name}이에요~"

class Bird(Animal):
    """새 클래스 (자식 클래스)"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name, "새")
        self.can_fly = can_fly
        self.altitude = 0
        print(f"🐦 {'날 수 있는' if can_fly else '날 수 없는'} 새가 추가로 초기화됨")
    
    def make_sound(self):
        """새의 소리 (메서드 오버라이딩)"""
        print(f"🐦 {self.name}: 짹짹!")
    
    def fly(self, height):
        """날기 - 새만의 특별한 메서드"""
        if self.can_fly:
            self.altitude = height
            print(f"🐦 {self.name}이(가) {height}미터 높이로 날아갑니다!")
        else:
            print(f"🐦 {self.name}은(는) 날 수 없습니다.")
    
    def land(self):
        """착륙"""
        if self.altitude > 0:
            print(f"🐦 {self.name}이(가) 착륙합니다.")
            self.altitude = 0
        else:
            print(f"🐦 {self.name}은(는) 이미 땅에 있습니다.")

# 상속 실습
print("🐾 동물원 만들기:")

animals = [
    Dog("바둑이", "진돗개"),
    Cat("나비", "삼색이"),
    Bird("피요", True),
    Dog("멍멍이", "골든 리트리버"),
    Cat("까망이", "검은색"),
    Bird("펭귄이", False)  # 날 수 없는 새
]

print(f"\n🏠 동물원에 {len(animals)}마리 동물들이 있습니다:")
for animal in animals:
    print(f"  {animal} - {animal.introduce()}")

print("\n🔊 동물들의 소리:")
for animal in animals:
    animal.make_sound()

print("\n🍽️ 급식 시간:")
foods = ["사료", "생선", "씨앗", "뼈다귀", "참치캔", "벌레"]
for i, animal in enumerate(animals):
    animal.eat(foods[i])

print("\n🎪 동물들의 특별한 능력:")
for animal in animals:
    if isinstance(animal, Dog):
        animal.fetch("공")
        animal.wag_tail()
    elif isinstance(animal, Cat):
        animal.scratch("스크래치 포스트")
        animal.purr()
    elif isinstance(animal, Bird):
        animal.fly(50)
        animal.land()

print("=" * 30)

# 2. 다중 상속과 super() 활용
print("2️⃣ 다중 상속과 super() 활용")

class Swimmer:
    """수영할 수 있는 능력을 제공하는 믹스인 클래스"""
    
    def __init__(self):
        self.swimming_speed = 0
        print("🏊 수영 능력 초기화")
    
    def swim(self, distance):
        """수영하기"""
        print(f"🏊 {distance}미터 수영합니다!")
        self.swimming_speed = distance / 10  # 속도 계산

class Flyer:
    """날 수 있는 능력을 제공하는 믹스인 클래스"""
    
    def __init__(self):
        self.flying_speed = 0
        print("✈️ 비행 능력 초기화")
    
    def fly_to(self, destination):
        """목적지로 비행"""
        print(f"✈️ {destination}으로 날아갑니다!")
        self.flying_speed = 100  # 기본 비행 속도

class Duck(Animal, Swimmer, Flyer):
    """오리 클래스 - 다중 상속 활용"""
    
    def __init__(self, name):
        # 모든 부모 클래스 초기화 (MRO 순서대로)
        Animal.__init__(self, name, "오리")
        Swimmer.__init__(self)
        Flyer.__init__(self)
        print("🦆 오리의 모든 능력이 초기화됨")
    
    def make_sound(self):
        """오리의 소리"""
        print(f"🦆 {self.name}: 꽥꽥!")
    
    def dive(self):
        """잠수하기"""
        print(f"🦆 {self.name}이(가) 물 속으로 잠수합니다!")

# 다중 상속 실습
print("🦆 특별한 오리 생성:")
donald = Duck("도날드")

print(f"\n🦆 {donald.name}의 능력 시연:")
donald.make_sound()
donald.swim(100)
donald.fly_to("남쪽 연못")
donald.dive()
donald.eat("물풀")

# MRO (Method Resolution Order) 확인
print(f"\n🔍 Duck 클래스의 MRO:")
for i, cls in enumerate(Duck.__mro__):
    print(f"  {i+1}. {cls.__name__}")

print("=" * 30)

# 3. 추상 클래스와 다형성
print("3️⃣ 추상 클래스와 다형성")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """교통수단 추상 클래스"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False
        print(f"🚗 {brand} {model} 차량 기본 정보 설정")
    
    def start_engine(self):
        """엔진 시작 (공통 메서드)"""
        if not self.is_running:
            self.is_running = True
            print(f"🔑 {self.brand} {self.model} 시동 켜짐")
        else:
            print(f"⚠️ {self.brand} {self.model}은 이미 시동이 걸려있습니다")
    
    def stop_engine(self):
        """엔진 정지 (공통 메서드)"""
        if self.is_running:
            self.is_running = False
            print(f"🔑 {self.brand} {self.model} 시동 꺼짐")
        else:
            print(f"⚠️ {self.brand} {self.model}은 이미 시동이 꺼져있습니다")
    
    @abstractmethod
    def move(self):
        """이동 (추상 메서드 - 반드시 구현해야 함)"""
        pass
    
    @abstractmethod
    def get_max_speed(self):
        """최대 속도 반환 (추상 메서드)"""
        pass
    
    def __str__(self):
        status = "운행중" if self.is_running else "정지"
        return f"{self.brand} {self.model} ({status})"

class Car(Vehicle):
    """자동차 클래스"""
    
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.fuel_level = 100
        print(f"🚗 {fuel_type} 자동차 추가 설정 완료")
    
    def move(self):
        """자동차 이동"""
        if self.is_running:
            if self.fuel_level > 0:
                self.fuel_level -= 10
                print(f"🚗 {self.brand} {self.model}이(가) 도로를 달립니다! (연료: {self.fuel_level}%)")
            else:
                print(f"⛽ {self.brand} {self.model}의 연료가 부족합니다!")
        else:
            print(f"🔑 먼저 {self.brand} {self.model}의 시동을 켜세요!")
    
    def get_max_speed(self):
        """최대 속도"""
        return 180
    
    def refuel(self):
        """연료 보충"""
        self.fuel_level = 100
        print(f"⛽ {self.brand} {self.model} 연료 보충 완료!")

class Airplane(Vehicle):
    """비행기 클래스"""
    
    def __init__(self, brand, model, passenger_capacity):
        super().__init__(brand, model)
        self.passenger_capacity = passenger_capacity
        self.altitude = 0
        print(f"✈️ {passenger_capacity}인승 비행기 추가 설정 완료")
    
    def move(self):
        """비행기 이동"""
        if self.is_running:
            self.altitude = 10000
            print(f"✈️ {self.brand} {self.model}이(가) 고도 {self.altitude}m에서 비행합니다!")
        else:
            print(f"🔑 먼저 {self.brand} {self.model}의 엔진을 가동시키세요!")
    
    def get_max_speed(self):
        """최대 속도"""
        return 900
    
    def land(self):
        """착륙"""
        if self.altitude > 0:
            self.altitude = 0
            print(f"✈️ {self.brand} {self.model}이(가) 착륙했습니다.")
        else:
            print(f"✈️ {self.brand} {self.model}은 이미 지상에 있습니다.")

class Boat(Vehicle):
    """배 클래스"""
    
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type
        self.anchor_down = True
        print(f"⛵ {boat_type} 타입 배 추가 설정 완료")
    
    def move(self):
        """배 이동"""
        if self.is_running:
            if not self.anchor_down:
                print(f"⛵ {self.brand} {self.model}이(가) 바다를 항해합니다!")
            else:
                print(f"⚓ {self.brand} {self.model}의 닻을 먼저 올리세요!")
        else:
            print(f"🔑 먼저 {self.brand} {self.model}의 엔진을 가동시키세요!")
    
    def get_max_speed(self):
        """최대 속도"""
        return 50
    
    def drop_anchor(self):
        """닻 내리기"""
        if not self.anchor_down:
            self.anchor_down = True
            print(f"⚓ {self.brand} {self.model}의 닻을 내렸습니다.")
    
    def raise_anchor(self):
        """닻 올리기"""
        if self.anchor_down:
            self.anchor_down = False
            print(f"⚓ {self.brand} {self.model}의 닻을 올렸습니다.")

# 다형성 실습
print("🚗 교통수단 시뮬레이션:")

vehicles = [
    Car("현대", "소나타", "가솔린"),
    Airplane("보잉", "747", 400),
    Boat("삼성", "크루저", "요트"),
    Car("테슬라", "Model S", "전기"),
    Airplane("에어버스", "A380", 850)
]

print(f"\n🏭 {len(vehicles)}대의 교통수단이 준비되었습니다:")
for vehicle in vehicles:
    print(f"  {vehicle} - 최대속도: {vehicle.get_max_speed()}km/h")

print("\n🔑 모든 교통수단 시동 켜기:")
for vehicle in vehicles:
    vehicle.start_engine()

print("\n🚀 모든 교통수단 이동:")
for vehicle in vehicles:
    # 다형성 - 같은 메서드 호출이지만 각기 다른 동작
    vehicle.move()
    
    # 특별한 기능들
    if isinstance(vehicle, Car):
        if vehicle.fuel_level <= 10:
            vehicle.refuel()
    elif isinstance(vehicle, Airplane):
        vehicle.land()
    elif isinstance(vehicle, Boat):
        vehicle.raise_anchor()
        vehicle.move()  # 닻을 올린 후 다시 이동

print("\n📊 교통수단별 최대 속도 비교:")
for vehicle in vehicles:
    print(f"  {vehicle.brand} {vehicle.model}: {vehicle.get_max_speed():3d}km/h")

print("=" * 30)

print("🎯 Part 2 요약:")
print("✅ 클래스 상속의 기본 개념")
print("✅ 메서드 오버라이딩")
print("✅ super() 함수 활용")
print("✅ 다중 상속과 MRO")
print("✅ 추상 클래스와 추상 메서드")
print("✅ 다형성의 실제 활용")
```

---

### Part 3: 실전 OOP (50분)

#### 🏫 종합 실습 - 학생 관리 시스템

```python
print("🏫 종합 실습 - 학생 관리 시스템")
print("=" * 22)

from datetime import datetime, date
import json

# 1. 학생 관리 시스템
print("1️⃣ 학생 관리 시스템 구축")

class Subject:
    """과목 클래스"""
    
    def __init__(self, code, name, credits):
        self.code = code          # 과목 코드
        self.name = name          # 과목명
        self.credits = credits    # 학점
    
    def __str__(self):
        return f"{self.name}({self.code}, {self.credits}학점)"
    
    def __repr__(self):
        return f"Subject('{self.code}', '{self.name}', {self.credits})"

class Grade:
    """성적 클래스"""
    
    GRADE_POINTS = {
        'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0,
        'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0
    }
    
    def __init__(self, subject, grade, semester):
        self.subject = subject
        self.grade = grade
        self.semester = semester
        self.date_recorded = datetime.now()
    
    @property
    def grade_point(self):
        """학점 계산"""
        return self.GRADE_POINTS.get(self.grade, 0.0)
    
    @property
    def weighted_points(self):
        """가중 학점 (학점 × 평점)"""
        return self.subject.credits * self.grade_point
    
    def __str__(self):
        return f"{self.subject.name}: {self.grade} ({self.grade_point}점)"

class Person:
    """사람 기본 클래스"""
    
    def __init__(self, name, birth_date, phone=""):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.created_at = datetime.now()
    
    @property
    def age(self):
        """나이 계산"""
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
    
    def update_phone(self, phone):
        """전화번호 업데이트"""
        self.phone = phone
        print(f"📱 {self.name}님의 전화번호가 {phone}로 업데이트되었습니다.")
    
    def __str__(self):
        return f"{self.name} ({self.age}세)"

class Student(Person):
    """학생 클래스"""
    
    _student_count = 0  # 클래스 변수
    
    def __init__(self, name, birth_date, major, phone=""):
        super().__init__(name, birth_date, phone)
        self.major = major
        self.grades = []  # 성적 리스트
        self.enrollment_date = datetime.now()
        
        # 학번 자동 생성
        Student._student_count += 1
        year = self.enrollment_date.year
        self.student_id = f"{year}{Student._student_count:04d}"
        
        print(f"🎓 새 학생 등록: {self.name} (학번: {self.student_id})")
    
    def add_grade(self, subject, grade, semester):
        """성적 추가"""
        new_grade = Grade(subject, grade, semester)
        self.grades.append(new_grade)
        print(f"📝 {self.name}님의 {subject.name} 성적({grade}) 등록")
    
    def get_gpa(self, semester=None):
        """평점평균 계산"""
        if semester:
            semester_grades = [g for g in self.grades if g.semester == semester]
        else:
            semester_grades = self.grades
        
        if not semester_grades:
            return 0.0
        
        total_weighted_points = sum(g.weighted_points for g in semester_grades)
        total_credits = sum(g.subject.credits for g in semester_grades)
        
        if total_credits == 0:
            return 0.0
        
        return total_weighted_points / total_credits
    
    def get_total_credits(self):
        """총 이수 학점"""
        return sum(g.subject.credits for g in self.grades)
    
    def get_semester_report(self, semester):
        """학기별 성적표"""
        semester_grades = [g for g in self.grades if g.semester == semester]
        
        if not semester_grades:
            return f"{semester} 학기 성적이 없습니다."
        
        report = f"\n📋 {self.name}님의 {semester} 성적표\n"
        report += "=" * 40 + "\n"
        
        for grade in semester_grades:
            report += f"{grade.subject.name:12s} | {grade.grade:2s} | {grade.grade_point:3.1f}점 | {grade.subject.credits}학점\n"
        
        gpa = self.get_gpa(semester)
        total_credits = sum(g.subject.credits for g in semester_grades)
        
        report += "-" * 40 + "\n"
        report += f"학기 평점평균: {gpa:.2f}\n"
        report += f"이수 학점: {total_credits}학점\n"
        
        return report
    
    def get_transcript(self):
        """전체 성적 증명서"""
        if not self.grades:
            return "등록된 성적이 없습니다."
        
        transcript = f"\n📊 {self.name}님의 성적 증명서\n"
        transcript += "=" * 50 + "\n"
        transcript += f"학번: {self.student_id} | 전공: {self.major}\n"
        transcript += f"입학일: {self.enrollment_date.strftime('%Y-%m-%d')}\n"
        transcript += "=" * 50 + "\n"
        
        # 학기별로 정렬
        semesters = list(set(g.semester for g in self.grades))
        semesters.sort()
        
        for semester in semesters:
            semester_grades = [g for g in self.grades if g.semester == semester]
            
            transcript += f"\n📅 {semester}\n"
            transcript += "-" * 30 + "\n"
            
            for grade in semester_grades:
                transcript += f"{grade.subject.name:15s} | {grade.grade:2s} | {grade.subject.credits}학점\n"
            
            semester_gpa = self.get_gpa(semester)
            transcript += f"학기 평점평균: {semester_gpa:.2f}\n"
        
        total_gpa = self.get_gpa()
        total_credits = self.get_total_credits()
        
        transcript += "\n" + "=" * 30 + "\n"
        transcript += f"총 평점평균: {total_gpa:.2f}\n"
        transcript += f"총 이수학점: {total_credits}학점\n"
        
        return transcript
    
    @classmethod
    def get_student_count(cls):
        """총 학생 수 반환"""
        return cls._student_count
    
    def __str__(self):
        return f"학생 {self.name} ({self.student_id}, {self.major})"

class Professor(Person):
    """교수 클래스"""
    
    def __init__(self, name, birth_date, department, phone=""):
        super().__init__(name, birth_date, phone)
        self.department = department
        self.subjects_taught = []
        self.students = []
        
        print(f"👨‍🏫 새 교수 등록: {name} ({department}과)")
    
    def add_subject(self, subject):
        """담당 과목 추가"""
        if subject not in self.subjects_taught:
            self.subjects_taught.append(subject)
            print(f"📚 {self.name} 교수님이 {subject.name} 과목을 담당합니다.")
    
    def add_student(self, student):
        """담당 학생 추가"""
        if student not in self.students:
            self.students.append(student)
            print(f"👥 {self.name} 교수님이 {student.name} 학생을 지도합니다.")
    
    def give_grade(self, student, subject_code, grade, semester):
        """학생에게 성적 부여"""
        # 담당 과목 확인
        subject = next((s for s in self.subjects_taught if s.code == subject_code), None)
        if not subject:
            print(f"❌ {self.name} 교수님은 {subject_code} 과목을 담당하지 않습니다.")
            return
        
        # 담당 학생 확인
        if student not in self.students:
            print(f"❌ {student.name}님은 {self.name} 교수님의 담당 학생이 아닙니다.")
            return
        
        student.add_grade(subject, grade, semester)
        print(f"✅ {self.name} 교수님이 {student.name}님에게 {subject.name} {grade} 성적을 부여했습니다.")
    
    def get_student_list(self):
        """담당 학생 목록"""
        if not self.students:
            return f"{self.name} 교수님의 담당 학생이 없습니다."
        
        student_list = f"\n👥 {self.name} 교수님의 담당 학생 목록\n"
        student_list += "-" * 30 + "\n"
        
        for student in self.students:
            gpa = student.get_gpa()
            credits = student.get_total_credits()
            student_list += f"{student.name:8s} | {student.student_id} | GPA: {gpa:.2f} | {credits}학점\n"
        
        return student_list
    
    def __str__(self):
        return f"교수 {self.name} ({self.department}과)"

class University:
    """대학교 클래스"""
    
    def __init__(self, name):
        self.name = name
        self.students = []
        self.professors = []
        self.subjects = []
        self.founded_date = datetime.now()
        
        print(f"🏫 {name} 설립!")
    
    def add_student(self, student):
        """학생 등록"""
        if student not in self.students:
            self.students.append(student)
            print(f"📝 {student.name} 학생이 {self.name}에 등록되었습니다.")
    
    def add_professor(self, professor):
        """교수 등록"""
        if professor not in self.professors:
            self.professors.append(professor)
            print(f"📝 {professor.name} 교수님이 {self.name}에 등록되었습니다.")
    
    def add_subject(self, subject):
        """과목 등록"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"📚 {subject.name} 과목이 {self.name}에 등록되었습니다.")
    
    def find_student_by_id(self, student_id):
        """학번으로 학생 찾기"""
        return next((s for s in self.students if s.student_id == student_id), None)
    
    def find_student_by_name(self, name):
        """이름으로 학생 찾기"""
        return [s for s in self.students if s.name == name]
    
    def get_honor_students(self, min_gpa=3.5):
        """우등생 목록 (GPA 기준)"""
        honor_students = []
        
        for student in self.students:
            gpa = student.get_gpa()
            if gpa >= min_gpa:
                honor_students.append((student, gpa))
        
        # GPA 내림차순 정렬
        honor_students.sort(key=lambda x: x[1], reverse=True)
        
        if not honor_students:
            return f"GPA {min_gpa} 이상인 학생이 없습니다."
        
        result = f"\n🏆 우등생 목록 (GPA {min_gpa} 이상)\n"
        result += "=" * 40 + "\n"
        
        for rank, (student, gpa) in enumerate(honor_students, 1):
            credits = student.get_total_credits()
            result += f"{rank:2d}. {student.name:8s} | {student.student_id} | GPA: {gpa:.2f} | {credits}학점\n"
        
        return result
    
    def get_statistics(self):
        """대학 통계"""
        if not self.students:
            return "등록된 학생이 없습니다."
        
        stats = f"\n📊 {self.name} 통계\n"
        stats += "=" * 30 + "\n"
        
        # 기본 통계
        stats += f"총 학생 수: {len(self.students)}명\n"
        stats += f"총 교수 수: {len(self.professors)}명\n"
        stats += f"총 과목 수: {len(self.subjects)}명\n"
        
        # 학생 GPA 통계
        gpas = [s.get_gpa() for s in self.students if s.get_gpa() > 0]
        
        if gpas:
            avg_gpa = sum(gpas) / len(gpas)
            max_gpa = max(gpas)
            min_gpa = min(gpas)
            
            stats += f"\n📈 GPA 통계\n"
            stats += f"평균 GPA: {avg_gpa:.2f}\n"
            stats += f"최고 GPA: {max_gpa:.2f}\n"
            stats += f"최저 GPA: {min_gpa:.2f}\n"
        
        # 전공별 통계
        majors = {}
        for student in self.students:
            major = student.major
            if major not in majors:
                majors[major] = []
            majors[major].append(student)
        
        stats += f"\n🎓 전공별 학생 수\n"
        for major, students in majors.items():
            avg_major_gpa = sum(s.get_gpa() for s in students if s.get_gpa() > 0) / len([s for s in students if s.get_gpa() > 0]) if any(s.get_gpa() > 0 for s in students) else 0
            stats += f"{major:12s}: {len(students):2d}명 (평균 GPA: {avg_major_gpa:.2f})\n"
        
        return stats
    
    def save_data(self, filename):
        """대학 데이터 저장"""
        data = {
            'university_name': self.name,
            'founded_date': self.founded_date.isoformat(),
            'students': [],
            'professors': [],
            'subjects': []
        }
        
        # 학생 데이터
        for student in self.students:
            student_data = {
                'name': student.name,
                'birth_date': student.birth_date.isoformat(),
                'major': student.major,
                'phone': student.phone,
                'student_id': student.student_id,
                'grades': []
            }
            
            for grade in student.grades:
                grade_data = {
                    'subject_code': grade.subject.code,
                    'subject_name': grade.subject.name,
                    'credits': grade.subject.credits,
                    'grade': grade.grade,
                    'semester': grade.semester
                }
                student_data['grades'].append(grade_data)
            
            data['students'].append(student_data)
        
        # 과목 데이터
        for subject in self.subjects:
            subject_data = {
                'code': subject.code,
                'name': subject.name,
                'credits': subject.credits
            }
            data['subjects'].append(subject_data)
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"💾 대학 데이터가 '{filename}'에 저장되었습니다.")
        except Exception as e:
            print(f"❌ 데이터 저장 실패: {e}")

# 학생 관리 시스템 실습
print("🏫 파이썬 대학교 시스템 가동:")

# 대학교 생성
python_university = University("파이썬 대학교")

# 과목들 생성
subjects = [
    Subject("CS101", "프로그래밍 기초", 3),
    Subject("CS201", "자료구조", 3),
    Subject("CS301", "알고리즘", 3),
    Subject("MATH101", "미적분학", 3),
    Subject("MATH201", "선형대수", 3),
    Subject("ENG101", "영어회화", 2)
]

for subject in subjects:
    python_university.add_subject(subject)

print("\n👨‍🏫 교수진 등록:")

# 교수들 생성
prof_kim = Professor("김교수", date(1970, 5, 15), "컴퓨터공학", "010-1234-5678")
prof_lee = Professor("이교수", date(1975, 8, 20), "수학", "010-2345-6789")

python_university.add_professor(prof_kim)
python_university.add_professor(prof_lee)

# 교수 담당 과목 설정
prof_kim.add_subject(subjects[0])  # 프로그래밍 기초
prof_kim.add_subject(subjects[1])  # 자료구조
prof_kim.add_subject(subjects[2])  # 알고리즘

prof_lee.add_subject(subjects[3])  # 미적분학
prof_lee.add_subject(subjects[4])  # 선형대수

print("\n🎓 학생 등록:")

# 학생들 생성
students = [
    Student("김철수", date(2000, 3, 15), "컴퓨터공학", "010-1111-1111"),
    Student("이영희", date(2001, 7, 22), "컴퓨터공학", "010-2222-2222"),
    Student("박민수", date(2000, 12, 8), "수학", "010-3333-3333"),
    Student("최지원", date(2002, 1, 30), "컴퓨터공학", "010-4444-4444"),
    Student("정다영", date(2001, 9, 12), "수학", "010-5555-5555")
]

for student in students:
    python_university.add_student(student)

# 교수-학생 관계 설정
for student in students:
    if student.major == "컴퓨터공학":
        prof_kim.add_student(student)
    elif student.major == "수학":
        prof_lee.add_student(student)

print("\n📝 성적 입력:")

# 2023-1학기 성적 입력
semester = "2023-1"

# 김철수 성적
prof_kim.give_grade(students[0], "CS101", "A", semester)
prof_kim.give_grade(students[0], "CS201", "B+", semester)
prof_lee.give_grade(students[0], "MATH101", "A+", semester)

# 이영희 성적
prof_kim.give_grade(students[1], "CS101", "A+", semester)
prof_kim.give_grade(students[1], "CS201", "A", semester)
prof_lee.give_grade(students[1], "MATH101", "A", semester)

# 박민수 성적
prof_lee.give_grade(students[2], "MATH101", "A+", semester)
prof_lee.give_grade(students[2], "MATH201", "A", semester)
prof_kim.give_grade(students[2], "CS101", "B", semester)

# 2023-2학기 성적 입력
semester = "2023-2"

prof_kim.give_grade(students[0], "CS301", "B+", semester)
prof_kim.give_grade(students[1], "CS301", "A", semester)
prof_lee.give_grade(students[2], "MATH201", "A+", semester)

print("\n📊 성적표 출력:")

# 각 학생의 성적표 출력
for student in students[:3]:  # 처음 3명만
    print(student.get_transcript())

print("\n🏆 우등생 발표:")
print(python_university.get_honor_students(3.0))

print("\n👥 교수별 담당 학생:")
print(prof_kim.get_student_list())
print(prof_lee.get_student_list())

print("\n📊 대학 전체 통계:")
print(python_university.get_statistics())

# 데이터 저장
python_university.save_data("university_data.json")

print("=" * 30)

# 2. 은행 계좌 시스템 (간단 버전)
print("2️⃣ 은행 계좌 시스템")

class Account:
    """계좌 기본 클래스"""
    
    _account_number = 1000
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self._account_number = Account._account_number
        Account._account_number += 1
        self.transaction_history = []
        self.created_date = datetime.now()
        
        self._record_transaction("계좌개설", initial_balance)
    
    def _record_transaction(self, transaction_type, amount, balance_after=None):
        """거래 기록"""
        if balance_after is None:
            balance_after = self.balance
            
        record = {
            'date': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': balance_after
        }
        self.transaction_history.append(record)
    
    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            self._record_transaction("입금", amount)
            return True
        return False
    
    def withdraw(self, amount):
        """출금"""
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self._record_transaction("출금", -amount)
            return True
        return False
    
    def get_balance(self):
        """잔액 조회"""
        return self.balance
    
    def get_statement(self, num_transactions=10):
        """거래 내역서"""
        statement = f"\n💳 {self.owner}님의 계좌 ({self._account_number}) 거래내역\n"
        statement += "=" * 50 + "\n"
        
        recent_transactions = self.transaction_history[-num_transactions:]
        
        for transaction in recent_transactions:
            date_str = transaction['date'].strftime("%Y-%m-%d %H:%M")
            amount_str = f"{transaction['amount']:+,}"
            balance_str = f"{transaction['balance']:,}"
            
            statement += f"{date_str} | {transaction['type']:6s} | {amount_str:>10s} | 잔액: {balance_str:>10s}\n"
        
        return statement
    
    def __str__(self):
        return f"계좌({self._account_number}) - {self.owner}: {self.balance:,}원"

class SavingsAccount(Account):
    """저축 계좌"""
    
    def __init__(self, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate
        print(f"💰 저축계좌 개설: {owner} (이자율 {interest_rate*100}%)")
    
    def calculate_interest(self):
        """이자 계산 및 지급"""
        interest = self.balance * self.interest_rate
        if interest > 0:
            self.balance += interest
            self._record_transaction("이자지급", interest)
            print(f"💰 이자 지급: {interest:,.2f}원")
        return interest

class CheckingAccount(Account):
    """당좌 계좌 (마이너스 통장)"""
    
    def __init__(self, owner, initial_balance=0, overdraft_limit=100000):
        super().__init__(owner, initial_balance)
        self.overdraft_limit = overdraft_limit
        print(f"💳 당좌계좌 개설: {owner} (마이너스 한도 {overdraft_limit:,}원)")
    
    def withdraw(self, amount):
        """출금 (마이너스 허용)"""
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            self._record_transaction("출금", -amount)
            
            if self.balance < 0:
                print(f"⚠️ 마이너스 잔액: {self.balance