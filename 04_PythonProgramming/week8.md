# Week 8: 딕셔너리와 집합

**[← Week 7](./week07.md) | [목차](lecture/04_PythonProgramming/2.%20lectureMap.md) | [다음: Week 9 →](./week09.md)**

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **딕셔너리 완전 정복**: 키-값 구조를 이해하고 CRUD 연산을 자유자재로 수행합니다
2. **딕셔너리 메서드 마스터**: keys(), values(), items(), get() 등 핵심 메서드를 완벽히 구사합니다
3. **중첩 딕셔너리 다루기**: 복잡한 데이터 구조를 설계하고 효율적으로 관리합니다
4. **딕셔너리 컴프리헨션**: 간결하고 효율적인 딕셔너리 생성 기법을 익힙니다
5. **집합 연산 활용**: 수학적 집합 개념을 프로그래밍에 적용하여 데이터를 분석합니다
6. **실용 프로그램 개발**: 연락처 관리, 단어 빈도수, 투표 시스템 등을 제작합니다

---

## 📚 핵심 개념 요약

### 1. 딕셔너리(Dictionary)란?
```
🗂️ 딕셔너리 = 키(Key)와 값(Value)의 쌍으로 데이터를 저장하는 가변 자료형
🔑 키로 값에 빠르게 접근 가능 (해시 테이블 기반)
📝 순서가 유지됨 (Python 3.7+)
🎯 중괄호 {}로 생성: {"name": "김철수", "age": 25}
```

### 2. 집합(Set)란?
```
🎲 집합 = 중복을 허용하지 않는 순서 없는 자료형
🚫 중복 값 자동 제거
⚡ 매우 빠른 멤버십 테스트 (in 연산)
🧮 수학적 집합 연산 지원 (합집합, 교집합, 차집합)
🎯 중괄호 {}로 생성: {1, 2, 3, 4, 5}
```

### 3. 딕셔너리 vs 리스트 비교

| 특성 | 딕셔너리 (Dictionary) | 리스트 (List) |
|------|----------------------|---------------|
| **접근 방법** | `dict[key]` | `list[index]` |
| **검색 속도** | O(1) 매우 빠름 | O(n) 느림 |
| **순서** | 유지됨 (3.7+) | 유지됨 |
| **중복** | 키는 중복 불가, 값은 가능 | 중복 가능 |
| **용도** | 연관 데이터, 빠른 검색 | 순서 있는 데이터 |

### 4. 주요 딕셔너리 메서드

| 메서드 | 기능 | 예시 | 설명 |
|--------|------|------|------|
| **keys()** | 모든 키 반환 | `dict.keys()` | 키들의 뷰 객체 |
| **values()** | 모든 값 반환 | `dict.values()` | 값들의 뷰 객체 |
| **items()** | 키-값 쌍 반환 | `dict.items()` | (키, 값) 튜플들 |
| **get()** | 안전한 값 접근 | `dict.get('key', 기본값)` | 키가 없어도 오류 없음 |
| **setdefault()** | 키가 없으면 설정 | `dict.setdefault('key', 값)` | 기존 값은 변경 안함 |
| **update()** | 딕셔너리 병합 | `dict.update(other)` | 다른 딕셔너리와 합침 |

### 5. 집합 연산

| 연산 | 기호 | 메서드 | 설명 | 예시 |
|------|------|--------|------|------|
| **합집합** | `\|` | `union()` | 두 집합의 모든 원소 | `{1,2} \| {2,3}` → `{1,2,3}` |
| **교집합** | `&` | `intersection()` | 공통 원소만 | `{1,2} & {2,3}` → `{2}` |
| **차집합** | `-` | `difference()` | 첫 번째에만 있는 원소 | `{1,2} - {2,3}` → `{1}` |
| **대칭차집합** | `^` | `symmetric_difference()` | 공통이 아닌 원소 | `{1,2} ^ {2,3}` → `{1,3}` |

---

## 💻 실습 세션 (2시간)

### Part 1: 딕셔너리 기초 (30분)

#### 🗂️ 딕셔너리 생성과 접근

```python
print("🗂️ 딕셔너리 생성과 접근")
print("=" * 24)

# 1. 다양한 방법으로 딕셔너리 생성
print("📝 딕셔너리 생성 방법들")

# 빈 딕셔너리 생성
empty_dict1 = {}
empty_dict2 = dict()
print(f"빈 딕셔너리1: {empty_dict1}")
print(f"빈 딕셔너리2: {empty_dict2}")

# 초기값이 있는 딕셔너리
student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학",
    "grade": 3,
    "gpa": 3.8
}
print(f"학생 정보: {student}")

# 다양한 데이터 타입
mixed_dict = {
    "string": "안녕하세요",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "nested_dict": {"x": 10, "y": 20}
}
print(f"혼합 딕셔너리: {mixed_dict}")

# dict() 생성자 사용
person = dict(name="이영희", age=25, city="서울")
print(f"dict() 생성: {person}")

# 키-값 쌍 리스트로 생성
pairs = [("apple", "사과"), ("banana", "바나나"), ("orange", "오렌지")]
fruit_dict = dict(pairs)
print(f"쌍 리스트로 생성: {fruit_dict}")

print("=" * 30)

# 2. 딕셔너리 정보 확인
print("📊 딕셔너리 정보")

sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"딕셔너리: {sample_dict}")
print(f"길이: {len(sample_dict)}")
print(f"타입: {type(sample_dict)}")
print(f"비어있나?: {len(sample_dict) == 0}")

# 키 존재 확인
print(f"\n키 존재 확인:")
print(f"'a' in sample_dict: {'a' in sample_dict}")
print(f"'e' in sample_dict: {'e' in sample_dict}")
print(f"'z' not in sample_dict: {'z' not in sample_dict}")

print("=" * 30)

# 3. 값 접근 방법
print("🔑 값 접근 방법")

book = {
    "title": "파이썬 프로그래밍",
    "author": "김개발",
    "price": 25000,
    "pages": 400,
    "publisher": "프로그래밍 출판사"
}

print(f"책 정보: {book}")

# 대괄호 표기법
print(f"\n대괄호 접근:")
print(f"제목: {book['title']}")
print(f"저자: {book['author']}")
print(f"가격: {book['price']}원")

# 존재하지 않는 키에 접근하면 오류
try:
    print(book['isbn'])
except KeyError as e:
    print(f"키 오류: {e}")

# get() 메서드 - 안전한 접근
print(f"\nget() 메서드:")
print(f"제목: {book.get('title')}")
print(f"ISBN: {book.get('isbn')}")  # None 반환
print(f"ISBN: {book.get('isbn', '정보 없음')}")  # 기본값 설정

# 여러 값을 한번에 접근
print(f"\n여러 값 접근:")
title, author, price = book['title'], book['author'], book['price']
print(f"{title} - {author} ({price:,}원)")

print("=" * 30)

# 4. 딕셔너리와 반복문
print("🔄 딕셔너리와 반복문")

colors = {"red": "빨강", "green": "초록", "blue": "파랑", "yellow": "노랑"}
print(f"색상 딕셔너리: {colors}")

# 키만 순회
print("\n키 순회:")
for key in colors:
    print(f"  {key} -> {colors[key]}")

# 키 명시적으로 순회
print("\n키 명시적 순회:")
for key in colors.keys():
    print(f"  {key}: {colors[key]}")

# 값만 순회
print("\n값 순회:")
for value in colors.values():
    print(f"  {value}")

# 키-값 쌍 순회
print("\n키-값 쌍 순회:")
for key, value in colors.items():
    print(f"  {key} = {value}")

# 인덱스와 함께 순회
print("\n인덱스와 함께:")
for i, (key, value) in enumerate(colors.items(), 1):
    print(f"  {i}. {key}: {value}")

print("=" * 30)

# 5. 딕셔너리 복사
print("📋 딕셔너리 복사")

original = {"a": 1, "b": 2, "c": [3, 4, 5]}
print(f"원본: {original}")

# 얕은 복사 (주소 복사) - 위험!
shallow = original
shallow["a"] = 999
print(f"얕은 복사 후 원본: {original}")  # 원본도 변경됨

# 깊은 복사 방법들
original = {"a": 1, "b": 2, "c": [3, 4, 5]}

# copy() 메서드
deep_copy1 = original.copy()
deep_copy1["a"] = 777
print(f"copy() 후 원본: {original}")  # 원본 안전
print(f"copy() 복사본: {deep_copy1}")

# dict() 생성자
deep_copy2 = dict(original)
deep_copy2["b"] = 888
print(f"dict() 복사본: {deep_copy2}")

# 중첩 객체의 경우 주의!
original["c"][0] = 999  # 리스트는 공유됨
print(f"중첩 수정 후:")
print(f"원본: {original}")
print(f"copy() 복사본: {deep_copy1}")  # 리스트도 변경됨!

# 완전한 깊은 복사는 copy 모듈 사용
import copy
original = {"a": 1, "b": [2, 3, 4]}
deep_copy3 = copy.deepcopy(original)
original["b"][0] = 999
print(f"\ndeepcopy() 후:")
print(f"원본: {original}")
print(f"deepcopy(): {deep_copy3}")  # 완전히 독립적

print("=" * 30)

# 6. 실생활 예제 - 학생 성적 관리
print("🎓 학생 성적 관리 시스템")

# 학생 데이터
students_scores = {
    "김철수": {"국어": 85, "영어": 90, "수학": 92},
    "이영희": {"국어": 88, "영어": 95, "수학": 87},
    "박민수": {"국어": 75, "영어": 82, "수학": 90},
    "최지원": {"국어": 92, "영어": 88, "수학": 94}
}

print("📊 학생별 성적표:")
subjects = ["국어", "영어", "수학"]

for student_name, scores in students_scores.items():
    print(f"\n{student_name}:")
    total = 0
    for subject in subjects:
        score = scores[subject]
        print(f"  {subject}: {score:3d}점")
        total += score
    
    average = total / len(subjects)
    grade = 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'F'
    print(f"  평균: {average:5.1f}점 ({grade}등급)")

# 과목별 통계
print(f"\n📈 과목별 통계:")
for subject in subjects:
    subject_scores = [scores[subject] for scores in students_scores.values()]
    avg_score = sum(subject_scores) / len(subject_scores)
    max_score = max(subject_scores)
    min_score = min(subject_scores)
    
    print(f"{subject}:")
    print(f"  평균: {avg_score:5.1f}점")
    print(f"  최고: {max_score:3d}점")
    print(f"  최저: {min_score:3d}점")

# 우수 학생 찾기
print(f"\n🏆 우수 학생 (평균 90점 이상):")
excellent_students = []

for student, scores in students_scores.items():
    average = sum(scores.values()) / len(scores)
    if average >= 90:
        excellent_students.append((student, average))

# 평균순으로 정렬
excellent_students.sort(key=lambda x: x[1], reverse=True)

for rank, (student, avg) in enumerate(excellent_students, 1):
    print(f"  {rank}위: {student} ({avg:.1f}점)")

if not excellent_students:
    print("  해당 없음")
```

#### 🔧 키-값 추가/수정/삭제

```python
print("🔧 키-값 추가/수정/삭제")
print("=" * 22)

# 1. 값 추가와 수정
print("➕ 값 추가와 수정")

# 빈 딕셔너리에서 시작
person = {}
print(f"초기 상태: {person}")

# 새 키-값 추가
person["name"] = "김철수"
print(f"이름 추가: {person}")

person["age"] = 25
print(f"나이 추가: {person}")

person["city"] = "서울"
print(f"도시 추가: {person}")

person["job"] = "개발자"
print(f"직업 추가: {person}")

# 기존 값 수정
print(f"\n값 수정:")
print(f"수정 전: {person}")

person["age"] = 26  # 나이 수정
print(f"나이 수정: {person}")

person["city"] = "부산"  # 도시 수정
print(f"도시 수정: {person}")

# 여러 값 동시 수정
person.update({"age": 27, "job": "시니어 개발자", "salary": 50000000})
print(f"여러 값 수정: {person}")

print("=" * 30)

# 2. 값 삭제
print("🗑️ 값 삭제")

# 테스트용 딕셔너리
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "grape": 15,
    "kiwi": 25
}

print(f"초기 재고: {inventory}")

# del 키워드로 삭제
del inventory["kiwi"]
print(f"del로 kiwi 삭제: {inventory}")

# pop() 메서드로 삭제 후 값 반환
removed_value = inventory.pop("banana")
print(f"pop()으로 banana 삭제: {removed_value}개")
print(f"삭제 후 재고: {inventory}")

# pop()에 기본값 설정
removed_value2 = inventory.pop("mango", 0)  # 없어도 오류 안남
print(f"없는 항목 pop: {removed_value2}")

# popitem() - 마지막 항목 삭제 (LIFO)
last_item = inventory.popitem()
print(f"popitem() 결과: {last_item}")
print(f"마지막 삭제 후: {inventory}")

# clear() - 전체 삭제
temp_dict = {"a": 1, "b": 2}
print(f"clear() 전: {temp_dict}")
temp_dict.clear()
print(f"clear() 후: {temp_dict}")

print("=" * 30)

# 3. 안전한 딕셔너리 조작
print("🛡️ 안전한 딕셔너리 조작")

# 안전한 삭제 함수
def safe_delete(dictionary, key):
    if key in dictionary:
        value = dictionary.pop(key)
        print(f"'{key}' 삭제 완료: {value}")
        return value
    else:
        print(f"'{key}'를 찾을 수 없습니다")
        return None

# 테스트
test_dict = {"a": 1, "b": 2, "c": 3}
print(f"테스트 딕셔너리: {test_dict}")

safe_delete(test_dict, "b")  # 존재하는 키
safe_delete(test_dict, "x")  # 존재하지 않는 키
print(f"최종 상태: {test_dict}")

# 조건부 삭제
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(f"\n숫자 딕셔너리: {numbers}")

# 값이 3보다 큰 항목들 삭제
to_delete = []
for key, value in numbers.items():
    if value > 3:
        to_delete.append(key)

for key in to_delete:
    deleted_value = numbers.pop(key)
    print(f"값 {deleted_value} > 3인 '{key}' 삭제")

print(f"조건부 삭제 후: {numbers}")

print("=" * 30)

# 4. 동적 딕셔너리 구성
print("⚡ 동적 딕셔너리 구성")

# 사용자 입력 시뮬레이션
print("📝 연락처 관리 시스템")

contacts = {}
# 실제로는 input()으로 입력받음
contact_data = [
    ("김철수", "010-1234-5678"),
    ("이영희", "010-2345-6789"),
    ("박민수", "010-3456-7890"),
    ("최지원", "010-4567-8901")
]

for name, phone in contact_data:
    contacts[name] = phone
    print(f"'{name}' 연락처 추가: {contacts}")

# 연락처 검색
print(f"\n📞 연락처 검색:")
search_names = ["김철수", "홍길동", "이영희"]

for name in search_names:
    phone = contacts.get(name, "연락처 없음")
    print(f"{name}: {phone}")

# 연락처 수정
print(f"\n✏️ 연락처 수정:")
contacts["김철수"] = "010-1111-2222"
print(f"김철수 번호 변경: {contacts['김철수']}")

# 연락처 삭제
print(f"\n🗑️ 연락처 삭제:")
if "박민수" in contacts:
    old_phone = contacts.pop("박민수")
    print(f"박민수 ({old_phone}) 삭제 완료")

print(f"최종 연락처: {contacts}")

print("=" * 30)

# 5. 딕셔너리를 이용한 카운팅
print("📊 딕셔너리 카운팅")

# 문자 빈도수 계산
text = "hello world python programming"
print(f"텍스트: '{text}'")

char_count = {}
for char in text:
    if char != ' ':  # 공백 제외
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print(f"문자 빈도수: {char_count}")

# 더 간단한 방법 (get 사용)
text = "programming"
char_count2 = {}
for char in text:
    char_count2[char] = char_count2.get(char, 0) + 1

print(f"'programming' 문자 빈도: {char_count2}")

# 가장 많이 나온 문자 찾기
if char_count2:
    most_frequent = max(char_count2, key=char_count2.get)
    print(f"가장 빈번한 문자: '{most_frequent}' ({char_count2[most_frequent]}회)")

# 단어 빈도수
sentence = "python is great python is powerful python is easy"
words = sentence.split()
print(f"\n단어들: {words}")

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"단어 빈도수: {word_count}")

# 빈도수별로 정렬
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(f"빈도수 순 정렬: {sorted_words}")

print("=" * 30)

# 6. 실용적인 예제 - 온라인 쇼핑몰
print("🛒 온라인 쇼핑몰 장바구니")

# 상품 정보
products = {
    "P001": {"name": "노트북", "price": 1200000, "stock": 5},
    "P002": {"name": "마우스", "price": 25000, "stock": 20},
    "P003": {"name": "키보드", "price": 80000, "stock": 15},
    "P004": {"name": "모니터", "price": 300000, "stock": 8}
}

# 장바구니
cart = {}

print("🏪 상품 목록:")
for code, info in products.items():
    print(f"  {code}: {info['name']} - {info['price']:,}원 (재고: {info['stock']}개)")

# 장바구니에 상품 추가
def add_to_cart(product_code, quantity):
    if product_code in products:
        product = products[product_code]
        if product["stock"] >= quantity:
            if product_code in cart:
                cart[product_code] += quantity
            else:
                cart[product_code] = quantity
            
            products[product_code]["stock"] -= quantity
            print(f"✅ {product['name']} {quantity}개 추가됨")
        else:
            print(f"❌ 재고 부족 (재고: {product['stock']}개)")
    else:
        print(f"❌ 상품을 찾을 수 없음: {product_code}")

# 쇼핑 시뮬레이션
print(f"\n🛒 쇼핑 시뮬레이션:")
shopping_list = [
    ("P001", 2),  # 노트북 2개
    ("P002", 5),  # 마우스 5개
    ("P003", 1),  # 키보드 1개
    ("P001", 4),  # 노트북 4개 더 (재고 부족 상황)
]

for product_code, qty in shopping_list:
    add_to_cart(product_code, qty)

# 장바구니 확인
print(f"\n📋 장바구니 내역:")
total_price = 0

for product_code, quantity in cart.items():
    product = products[product_code]
    item_total = product["price"] * quantity
    total_price += item_total
    print(f"  {product['name']}: {quantity}개 × {product['price']:,}원 = {item_total:,}원")

print(f"\n💰 총 결제 금액: {total_price:,}원")

# 남은 재고 확인
print(f"\n📦 남은 재고:")
for code, info in products.items():
    print(f"  {info['name']}: {info['stock']}개")
```

#### 🎯 keys(), values(), items() 메서드

```python
print("🎯 keys(), values(), items() 메서드")
print("=" * 34)

# 1. 뷰 객체의 특성
print("👁️ 뷰 객체의 특성")

sample_dict = {"a": 1, "b": 2, "c": 3}
print(f"원본 딕셔너리: {sample_dict}")

# 뷰 객체 생성
keys_view = sample_dict.keys()
values_view = sample_dict.values()
items_view = sample_dict.items()

print(f"keys() 결과: {keys_view}")
print(f"values() 결과: {values_view}")
print(f"items() 결과: {items_view}")
print(f"각각의 타입: {type(keys_view)}, {type(values_view)}, {type(items_view)}")

# 원본 딕셔너리가 변경되면 뷰도 같이 변경됨
sample_dict["d"] = 4
print(f"\n딕셔너리 변경 후:")
print(f"원본: {sample_dict}")
print(f"keys_view: {keys_view}")
print(f"values_view: {values_view}")
print(f"items_view: {items_view}")

# 뷰를 리스트로 변환
keys_list = list(keys_view)
values_list = list(values_view)
items_list = list(items_view)

print(f"\n리스트 변환:")
print(f"키 리스트: {keys_list}")
print(f"값 리스트: {values_list}")
print(f"아이템 리스트: {items_list}")

print("=" * 30)

# 2. keys() 메서드 활용
print("🔑 keys() 메서드 활용")

student_info = {
    "name": "김철수",
    "student_id": "2023001",
    "major": "컴퓨터공학",
    "year": 3,
    "gpa": 3.8,
    "credits": 120
}

print(f"학생 정보: {student_info}")
print(f"모든 키: {list(student_info.keys())}")

# 키 존재 확인
required_fields = ["name", "student_id", "major", "email"]
print(f"\n필수 필드 확인:")
for field in required_fields:
    if field in student_info.keys():
        print(f"  ✅ {field}: 있음")
    else:
        print(f"  ❌ {field}: 없음")

# 키를 이용한 반복문
print(f"\n모든 필드 출력:")
for key in student_info.keys():
    print(f"  {key}: {student_info[key]}")

# 키 개수 확인
print(f"\n총 필드 개수: {len(student_info.keys())}")

# 키를 정렬해서 사용
print(f"정렬된 키로 출력:")
for key in sorted(student_info.keys()):
    print(f"  {key}: {student_info[key]}")

print("=" * 30)

# 3. values() 메서드 활용
print("💎 values() 메서드 활용")

scores = {"국어": 85, "영어": 92, "수학": 88, "과학": 90, "사회": 87}
print(f"과목별 점수: {scores}")

# 모든 값 확인
all_scores = list(scores.values())
print(f"모든 점수: {all_scores}")

# 통계 계산
print(f"통계:")
print(f"  총점: {sum(scores.values())}")
print(f"  평균: {sum(scores.values()) / len(scores.values()):.1f}")
print(f"  최고점: {max(scores.values())}")
print(f"  최저점: {min(scores.values())}")

# 특정 조건의 값 찾기
high_scores = [score for score in scores.values() if score >= 90]
print(f"90점 이상 점수: {high_scores}")

# 값의 빈도수 계산
grade_counts = {}
for score in scores.values():
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
    grade_counts[grade] = grade_counts.get(grade, 0) + 1

print(f"등급별 분포: {grade_counts}")

print("=" * 30)

# 4. items() 메서드 활용
print("👫 items() 메서드 활용")

products = {
    "apple": 1500,
    "banana": 2000,
    "orange": 3000,
    "grape": 5000,
    "kiwi": 4000
}

print(f"상품 가격표: {products}")

# 키-값 쌍으로 반복
print(f"\n가격표 출력:")
for product, price in products.items():
    print(f"  {product}: {price:,}원")

# 조건에 맞는 아이템 필터링
print(f"\n3000원 이상 상품:")
expensive_items = [(name, price) for name, price in products.items() if price >= 3000]
for name, price in expensive_items:
    print(f"  {name}: {price:,}원")

# 할인 가격 계산
print(f"\n10% 할인가:")
for product, price in products.items():
    discounted = int(price * 0.9)
    print(f"  {product}: {price:,}원 → {discounted:,}원")

# 가격순 정렬
print(f"\n가격순 정렬 (낮은 → 높은):")
sorted_items = sorted(products.items(), key=lambda x: x[1])
for product, price in sorted_items:
    print(f"  {product}: {price:,}원")

print("=" * 30)

# 5. 딕셔너리 변환과 조작
print("🔄 딕셔너리 변환과 조작")

# 영한 사전
en_ko_dict = {
    "apple": "사과",
    "banana": "바나나", 
    "cherry": "체리",
    "date": "대추",
    "elderberry": "엘더베리"
}

print(f"영한 사전: {en_ko_dict}")

# 한영 사전 만들기 (키-값 뒤바꾸기)
ko_en_dict = {korean: english for english, korean in en_ko_dict.items()}
print(f"한영 사전: {ko_en_dict}")

# 단어 길이와 함께 저장
word_length_dict = {word: len(word) for word in en_ko_dict.keys()}
print(f"단어 길이: {word_length_dict}")

# 조건부 딕셔너리 생성
short_words = {word: meaning for word, meaning in en_ko_dict.items() if len(word) <= 5}
print(f"5글자 이하 단어: {short_words}")

# 두 딕셔너리 합치기
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # 중복 키 있음

print(f"\n딕셔너리 합치기:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"dict3: {dict3}")

# update() 사용
combined1 = dict1.copy()
combined1.update(dict2)
print(f"dict1 + dict2: {combined1}")

# ** 연산자 사용 (Python 3.5+)
combined2 = {**dict1, **dict2, **dict3}
print(f"모든 딕셔너리 합치기: {combined2}")  # 중복 키는 마지막 값이 유지됨

print("=" * 30)

# 6. 실용적인 예제 - 설문조사 분석
print("📊 설문조사 분석 시스템")

# 설문 응답 데이터
survey_responses = {
    "respondent_1": {"age": 25, "gender": "male", "satisfaction": 4, "recommend": "yes"},
    "respondent_2": {"age": 32, "gender": "female", "satisfaction": 5, "recommend": "yes"},
    "respondent_3": {"age": 28, "gender": "male", "satisfaction": 3, "recommend": "no"},
    "respondent_4": {"age": 45, "gender": "female", "satisfaction": 5, "recommend": "yes"},
    "respondent_5": {"age": 38, "gender": "male", "satisfaction": 4, "recommend": "yes"},
    "respondent_6": {"age": 29, "gender": "female", "satisfaction": 2, "recommend": "no"}
}

print("📝 설문 응답 데이터 분석:")
print(f"총 응답자 수: {len(survey_responses)}명")

# 성별 분포 분석
gender_count = {}
for response in survey_responses.values():
    gender = response["gender"]
    gender_count[gender] = gender_count.get(gender, 0) + 1

print(f"\n성별 분포:")
for gender, count in gender_count.items():
    percentage = (count / len(survey_responses)) * 100
    print(f"  {gender}: {count}명 ({percentage:.1f}%)")

# 만족도 분석
satisfaction_scores = [response["satisfaction"] for response in survey_responses.values()]
avg_satisfaction = sum(satisfaction_scores) / len(satisfaction_scores)

print(f"\n만족도 분석:")
print(f"  평균 만족도: {avg_satisfaction:.2f}/5")
print(f"  최고 만족도: {max(satisfaction_scores)}")
print(f"  최저 만족도: {min(satisfaction_scores)}")

# 만족도 분포
satisfaction_dist = {}
for score in satisfaction_scores:
    satisfaction_dist[score] = satisfaction_dist.get(score, 0) + 1

print(f"  만족도 분포:")
for score in sorted(satisfaction_dist.keys()):
    count = satisfaction_dist[score]
    print(f"    {score}점: {count}명")

# 추천 의향 분석
recommend_count = {}
for response in survey_responses.values():
    recommend = response["recommend"]
    recommend_count[recommend] = recommend_count.get(recommend, 0) + 1

print(f"\n추천 의향:")
for recommend, count in recommend_count.items():
    percentage = (count / len(survey_responses)) * 100
    print(f"  {recommend}: {count}명 ({percentage:.1f}%)")

# 연령대별 만족도
age_groups = {"20대": [], "30대": [], "40대": []}
for response in survey_responses.values():
    age = response["age"]
    satisfaction = response["satisfaction"]
    
    if 20 <= age < 30:
        age_groups["20대"].append(satisfaction)
    elif 30 <= age < 40:
        age_groups["30대"].append(satisfaction)
    elif 40 <= age < 50:
        age_groups["40대"].append(satisfaction)

print(f"\n연령대별 평균 만족도:")
for age_group, scores in age_groups.items():
    if scores:  # 빈 리스트가 아닌 경우만
        avg = sum(scores) / len(scores)
        print(f"  {age_group}: {avg:.2f}/5 ({len(scores)}명)")
```

---

### Part 2: 딕셔너리 활용 (40분)

#### 🏢 중첩 딕셔너리

```python
print("🏢 중첩 딕셔너리")
print("=" * 16)

# 1. 기본 중첩 구조
print("📊 기본 중첩 구조")

# 회사 조직도
company = {
    "개발팀": {
        "팀장": "김개발",
        "멤버": ["이코딩", "박프로그래밍", "최알고리즘"],
        "프로젝트": {
            "프로젝트A": {"진행률": 80, "마감일": "2024-03-15"},
            "프로젝트B": {"진행률": 45, "마감일": "2024-04-20"}
        }
    },
    "디자인팀": {
        "팀장": "김디자인",
        "멤버": ["이UI", "박UX"],
        "프로젝트": {
            "디자인시스템": {"진행률": 90, "마감일": "2024-02-28"},
            "브랜딩": {"진행률": 60, "마감일": "2024-05-10"}
        }
    },
    "마케팅팀": {
        "팀장": "김마케팅",
        "멤버": ["이광고", "박SNS", "최분석"],
        "프로젝트": {
            "봄시즌캠페인": {"진행률": 70, "마감일": "2024-03-30"}
        }
    }
}

print("🏢 회사 조직도:")
for team_name, team_info in company.items():
    print(f"\n{team_name}:")
    print(f"  팀장: {team_info['팀장']}")
    print(f"  멤버: {', '.join(team_info['멤버'])}")
    print(f"  진행 중인 프로젝트:")
    
    for project_name, project_info in team_info["프로젝트"].items():
        progress = project_info["진행률"]
        deadline = project_info["마감일"]
        print(f"    - {project_name}: {progress}% (마감: {deadline})")

print("=" * 30)

# 2. 학교 데이터 구조
print("🎓 학교 데이터 구조")

school = {
    "1학년": {
        "A반": {
            "담임": "김선생",
            "학생수": 25,
            "학생들": {
                "김철수": {"국어": 85, "영어": 90, "수학": 92},
                "이영희": {"국어": 88, "영어": 95, "수학": 87},
                "박민수": {"국어": 75, "영어": 82, "수학": 90}
            }
        },
        "B반": {
            "담임": "이선생",
            "학생수": 28,
            "학생들": {
                "최지원": {"국어": 92, "영어": 88, "수학": 94},
                "정수진": {"국어": 89, "영어": 93, "수학": 85}
            }
        }
    },
    "2학년": {
        "A반": {
            "담임": "박선생",
            "학생수": 27,
            "학생들": {
                "홍길동": {"국어": 78, "영어": 85, "수학": 80},
                "강감찬": {"국어": 95, "영어": 92, "수학": 97}
            }
        }
    }
}

print("📚 학교 전체 현황:")
total_students = 0
all_scores = []

for grade, classes in school.items():
    print(f"\n{grade}:")
    grade_students = 0
    
    for class_name, class_info in classes.items():
        print(f"  {class_name} (담임: {class_info['담임']}):")
        print(f"    학생수: {class_info['학생수']}명")
        
        grade_students += class_info["학생수"]
        
        # 학생별 성적
        for student_name, scores in class_info["학생들"].items():
            avg_score = sum(scores.values()) / len(scores)
            all_scores.append(avg_score)
            print(f"      {student_name}: 평균 {avg_score:.1f}점")
    
    print(f"  {grade} 총 학생수: {grade_students}명")
    total_students += grade_students

print(f"\n🎯 전체 통계:")
print(f"전교 학생수: {total_students}명")
if all_scores:
    print(f"전교 평균: {sum(all_scores) / len(all_scores):.1f}점")

print("=" * 30)

# 3. 중첩 딕셔너리 접근과 수정
print("🔧 중첩 딕셔너리 접근과 수정")

# 깊은 접근
print("📍 깊은 접근:")
dev_team_leader = company["개발팀"]["팀장"]
print(f"개발팀 팀장: {dev_team_leader}")

project_a_progress = company["개발팀"]["프로젝트"]["프로젝트A"]["진행률"]
print(f"프로젝트A 진행률: {project_a_progress}%")

# 안전한 접근 (get 메서드 체이닝)
def safe_get_nested(dictionary, *keys):
    """중첩 딕셔너리에서 안전하게 값을 가져오는 함수"""
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary

# 안전한 접근 테스트
result1 = safe_get_nested(company, "개발팀", "팀장")
result2 = safe_get_nested(company, "개발팀", "예산")  # 없는 키
result3 = safe_get_nested(company, "HR팀", "팀장")   # 없는 팀

print(f"안전한 접근 결과:")
print(f"  개발팀 팀장: {result1}")
print(f"  개발팀 예산: {result2}")
print(f"  HR팀 팀장: {result3}")

# 값 수정
print(f"\n✏️ 값 수정:")
print(f"수정 전 프로젝트A 진행률: {company['개발팀']['프로젝트']['프로젝트A']['진행률']}%")

company["개발팀"]["프로젝트"]["프로젝트A"]["진행률"] = 95
print(f"수정 후 프로젝트A 진행률: {company['개발팀']['프로젝트']['프로젝트A']['진행률']}%")

# 새로운 중첩 구조 추가
company["개발팀"]["프로젝트"]["프로젝트C"] = {
    "진행률": 10,
    "마감일": "2024-06-15"
}
print(f"프로젝트C 추가: {company['개발팀']['프로젝트']['프로젝트C']}")

print("=" * 30)

# 4. 동적 중첩 딕셔너리 구성
print("⚡ 동적 중첩 딕셔너리 구성")

# 판매 데이터 집계
sales_data = [
    {"날짜": "2024-01-15", "지역": "서울", "제품": "노트북", "수량": 3, "단가": 1200000},
    {"날짜": "2024-01-15", "지역": "서울", "제품": "마우스", "수량": 10, "단가": 25000},
    {"날짜": "2024-01-16", "지역": "부산", "제품": "노트북", "수량": 2, "단가": 1200000},
    {"날짜": "2024-01-16", "지역": "서울", "제품": "키보드", "수량": 5, "단가": 80000},
    {"날짜": "2024-01-17", "지역": "대구", "제품": "마우스", "수량": 8, "단가": 25000},
]

# 지역별 -> 제품별 -> 매출 집계
regional_sales = {}

for sale in sales_data:
    region = sale["지역"]
    product = sale["제품"]
    revenue = sale["수량"] * sale["단가"]
    
    # 지역이 없으면 새로 생성
    if region not in regional_sales:
        regional_sales[region] = {}
    
    # 제품이 없으면 새로 생성
    if product not in regional_sales[region]:
        regional_sales[region][product] = {"수량": 0, "매출": 0}
    
    # 값 누적
    regional_sales[region][product]["수량"] += sale["수량"]
    regional_sales[region][product]["매출"] += revenue

print("📊 지역별 제품별 매출 현황:")
for region, products in regional_sales.items():
    print(f"\n{region}:")
    region_total = 0
    
    for product, stats in products.items():
        quantity = stats["수량"]
        revenue = stats["매출"]
        region_total += revenue
        print(f"  {product}: {quantity}개, {revenue:,}원")
    
    print(f"  {region} 총 매출: {region_total:,}원")

print("=" * 30)

# 5. 중첩 딕셔너리 순회와 검색
print("🔍 중첩 딕셔너리 순회와 검색")

def find_in_nested_dict(data, search_key, search_value):
    """중첩 딕셔너리에서 특정 키-값 쌍을 찾는 함수"""
    results = []
    
    def recursive_search(current_dict, path=""):
        if isinstance(current_dict, dict):
            for key, value in current_dict.items():
                current_path = f"{path}.{key}" if path else key
                
                if key == search_key and value == search_value:
                    results.append(current_path)
                
                recursive_search(value, current_path)
    
    recursive_search(data)
    return results

# 검색 테스트
print("🔍 검색 테스트:")
search_results = find_in_nested_dict(company, "팀장", "김개발")
print(f"'팀장'이 '김개발'인 경로: {search_results}")

search_results2 = find_in_nested_dict(company, "진행률", 80)
print(f"'진행률'이 80인 경로: {search_results2}")

# 모든 팀장 찾기
def find_all_team_leaders(data):
    """모든 팀장을 찾는 함수"""
    leaders = []
    
    def recursive_find(current_dict, path=""):
        if isinstance(current_dict, dict):
            for key, value in current_dict.items():
                current_path = f"{path}.{key}" if path else key
                
                if key == "팀장":
                    leaders.append((current_path, value))
                
                recursive_find(value, current_path)
    
    recursive_find(data)
    return leaders

all_leaders = find_all_team_leaders(company)
print(f"\n👥 모든 팀장 목록:")
for path, leader in all_leaders:
    print(f"  {path}: {leader}")

print("=" * 30)

# 6. 실용적인 중첩 딕셔너리 - 설정 관리 시스템
print("⚙️ 설정 관리 시스템")

# 애플리케이션 설정
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "user": "admin",
        "password": "secret123",
        "pool_size": 10,
        "timeout": 30
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True,
        "cors": {
            "enabled": True,
            "origins": ["http://localhost:3000", "https://myapp.com"],
            "methods": ["GET", "POST", "PUT", "DELETE"]
        },
        "rate_limit": {
            "requests": 100,
            "window": 60,  # seconds
            "enabled": True
        }
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "handlers": {
            "file": {
                "enabled": True,
                "path": "logs/app.log",
                "max_size": "10MB",
                "backup_count": 5
            },
            "console": {
                "enabled": True,
                "colored": True
            }
        }
    },
    "features": {
        "user_registration": True,
        "email_verification": True,
        "social_login": {
            "google": True,
            "facebook": False,
            "github": True
        },
        "payment": {
            "stripe": True,
            "paypal": False,
            "bank_transfer": True
        }
    }
}

def print_config(config, indent=0):
    """설정을 보기 좋게 출력하는 함수"""
    for key, value in config.items():
        print("  " * indent + f"{key}:", end="")
        
        if isinstance(value, dict):
            print()
            print_config(value, indent + 1)
        else:
            print(f" {value}")

print("⚙️ 애플리케이션 설정:")
print_config(app_config)

# 특정 설정값 가져오기
def get_config_value(config, *path):
    """점 표기법으로 설정값 가져오기"""
    current = config
    try:
        for key in path:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return None

print(f"\n🔍 설정값 조회:")
print(f"데이터베이스 호스트: {get_config_value(app_config, 'database', 'host')}")
print(f"API 포트: {get_config_value(app_config, 'api', 'port')}")
print(f"CORS 활성화: {get_config_value(app_config, 'api', 'cors', 'enabled')}")
print(f"Google 로그인: {get_config_value(app_config, 'features', 'social_login', 'google')}")
print(f"존재하지 않는 설정: {get_config_value(app_config, 'cache', 'redis', 'host')}")

# 설정 업데이트
def update_config_value(config, value, *path):
    """설정값 업데이트"""
    current = config
    for key in path[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    current[path[-1]] = value

print(f"\n✏️ 설정 업데이트:")
print(f"업데이트 전 디버그 모드: {get_config_value(app_config, 'api', 'debug')}")

update_config_value(app_config, False, 'api', 'debug')
print(f"업데이트 후 디버그 모드: {get_config_value(app_config, 'api', 'debug')}")

# 환경별 설정 병합
production_overrides = {
    "api": {
        "debug": False,
        "host": "0.0.0.0"
    },
    "database": {
        "host": "prod-db.company.com",
        "password": "super_secret_prod_password"
    },
    "logging": {
        "level": "WARNING"
    }
}

def merge_configs(base_config, override_config):
    """설정 딕셔너리 깊은 병합"""
    result = base_config.copy()
    
    for key, value in override_config.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    
    return result

production_config = merge_configs(app_config, production_overrides)

print(f"\n🚀 프로덕션 설정 적용:")
print(f"개발 환경 디버그: {get_config_value(app_config, 'api', 'debug')}")
print(f"프로덕션 디버그: {get_config_value(production_config, 'api', 'debug')}")
print(f"개발 환경 DB 호스트: {get_config_value(app_config, 'database', 'host')}")
print(f"프로덕션 DB 호스트: {get_config_value(production_config, 'database', 'host')}")
```

#### 🛡️ get()과 setdefault() 메서드

```python
print("🛡️ get()과 setdefault() 메서드")
print("=" * 32)

# 1. get() 메서드 - 안전한 값 접근
print("🔍 get() 메서드 - 안전한 값 접근")

# 기본 사용법
person = {"name": "김철수", "age": 25, "city": "서울"}
print(f"사람 정보: {person}")

# 존재하는 키 접근
name = person.get("name")
print(f"이름: {name}")

# 존재하지 않는 키 접근
job = person.get("job")  # None 반환
print(f"직업: {job}")

# 기본값과 함께 사용
job_with_default = person.get("job", "무직")
salary = person.get("salary", 0)
print(f"직업 (기본값): {job_with_default}")
print(f"급여 (기본값): {salary}")

# 대괄호 접근법과 비교
print(f"\n📊 접근 방법 비교:")
print(f"person['name']: {person['name']}")
print(f"person.get('name'): {person.get('name')}")

try:
    print(f"person['job']: {person['job']}")  # 오류 발생
except KeyError as e:
    print(f"KeyError 발생: {e}")

print(f"person.get('job'): {person.get('job')}")  # None, 오류 없음

print("=" * 30)

# 2. get() 메서드 활용 사례
print("💼 get() 메서드 활용 사례")

# 사용자 입력 처리
user_inputs = [
    {"username": "user1", "email": "user1@email.com"},
    {"username": "user2", "password": "secret123"},
    {"email": "user3@email.com", "age": 30},
    {"username": "user4", "email": "user4@email.com", "age": 25, "city": "부산"}
]

print("👥 사용자 입력 처리:")
for i, user_data in enumerate(user_inputs, 1):
    username = user_data.get("username", f"익명{i}")
    email = user_data.get("email", "이메일 없음")
    age = user_data.get("age", "나이 정보 없음")
    city = user_data.get("city", "도시 정보 없음")
    
    print(f"사용자 {i}:")
    print(f"  이름: {username}")
    print(f"  이메일: {email}")
    print(f"  나이: {age}")
    print(f"  도시: {city}")

# 설정값 처리
app_settings = {
    "theme": "dark",
    "language": "ko",
    "notifications": True
}

print(f"\n⚙️ 애플리케이션 설정:")
theme = app_settings.get("theme", "light")
language = app_settings.get("language", "en")
notifications = app_settings.get("notifications", False)
auto_save = app_settings.get("auto_save", True)  # 기본값으로 활성화

print(f"테마: {theme}")
print(f"언어: {language}")
print(f"알림: {notifications}")
print(f"자동 저장: {auto_save}")

print("=" * 30)

# 3. setdefault() 메서드 - 키가 없으면 설정
print("🎯 setdefault() 메서드")

# 기본 사용법
inventory = {"apple": 10, "banana": 5}
print(f"초기 재고: {inventory}")

# 존재하는 키에 setdefault
apple_count = inventory.setdefault("apple", 0)
print(f"사과 재고: {apple_count}")
print(f"재