
**[← Week 6](./week6.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 8 →](./week8.md)**

Week 7: 리스트와 튜플

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **리스트 완전 정복**: 생성, 접근, 수정, 삭제 등 리스트의 모든 기능을 마스터합니다
2. **인덱싱과 슬라이싱**: 음수 인덱스, 다양한 슬라이싱 기법을 자유자재로 사용합니다
3. **리스트 메서드 활용**: append, insert, remove, pop 등 핵심 메서드를 완벽히 구사합니다
4. **고급 리스트 기법**: 리스트 컴프리헨션으로 효율적인 코드를 작성합니다
5. **튜플 이해와 활용**: 불변 자료형인 튜플의 특성과 활용법을 익힙니다
6. **실용 프로그램 개발**: 성적 관리, 할일 목록 등 실생활 응용 프로그램을 제작합니다

---

## 📚 핵심 개념 요약

### 1. 리스트(List)란?
```
📦 리스트 = 여러 개의 데이터를 순서대로 저장하는 가변(mutable) 자료형
🔄 생성 후 내용 변경 가능 (추가, 삭제, 수정)
📍 인덱스로 각 원소에 접근 (0부터 시작)
🎯 대괄호 []로 생성: [1, 2, 3, "hello", True]
```

### 2. 튜플(Tuple)란?
```
📋 튜플 = 여러 개의 데이터를 순서대로 저장하는 불변(immutable) 자료형
🚫 생성 후 내용 변경 불가 (추가, 삭제, 수정 안됨)
📍 인덱스로 각 원소에 접근 (0부터 시작)
🎯 소괄호 ()로 생성: (1, 2, 3, "hello", True)
```

### 3. 리스트 vs 튜플 비교

| 특성 | 리스트 (List) | 튜플 (Tuple) |
|------|---------------|---------------|
| **표기법** | `[1, 2, 3]` | `(1, 2, 3)` |
| **가변성** | 가변 (Mutable) | 불변 (Immutable) |
| **수정** | 가능 | 불가능 |
| **속도** | 상대적으로 느림 | 상대적으로 빠름 |
| **메모리** | 많이 사용 | 적게 사용 |
| **사용 목적** | 데이터 변경이 필요한 경우 | 데이터 보호가 필요한 경우 |

### 4. 인덱싱과 슬라이싱

| 방법 | 문법 | 예시 | 결과 |
|------|------|------|------|
| **양수 인덱스** | `list[n]` | `[1,2,3,4][1]` | `2` |
| **음수 인덱스** | `list[-n]` | `[1,2,3,4][-1]` | `4` |
| **기본 슬라이싱** | `list[start:end]` | `[1,2,3,4][1:3]` | `[2,3]` |
| **단계 슬라이싱** | `list[start:end:step]` | `[1,2,3,4,5][::2]` | `[1,3,5]` |
| **역순 슬라이싱** | `list[::-1]` | `[1,2,3,4][::-1]` | `[4,3,2,1]` |

### 5. 주요 리스트 메서드

| 메서드 | 기능 | 예시 | 설명 |
|--------|------|------|------|
| **append()** | 끝에 추가 | `list.append(5)` | 맨 뒤에 하나 추가 |
| **insert()** | 지정 위치에 추가 | `list.insert(1, 'x')` | 인덱스 1에 'x' 삽입 |
| **remove()** | 값으로 삭제 | `list.remove(3)` | 값 3을 찾아서 삭제 |
| **pop()** | 인덱스로 삭제 후 반환 | `list.pop(0)` | 인덱스 0 삭제 후 반환 |
| **sort()** | 정렬 (원본 변경) | `list.sort()` | 오름차순 정렬 |
| **reverse()** | 뒤집기 (원본 변경) | `list.reverse()` | 순서 뒤집기 |

---

## 💻 실습 세션 (2시간)

### Part 1: 리스트 기초 (30분)

#### 🚀 리스트 생성과 접근

```python
print("🚀 리스트 생성과 접근")
print("=" * 20)

# 1. 다양한 방법으로 리스트 생성
print("📦 리스트 생성 방법들")

# 빈 리스트 생성
empty_list1 = []
empty_list2 = list()
print(f"빈 리스트1: {empty_list1}")
print(f"빈 리스트2: {empty_list2}")

# 초기값이 있는 리스트
numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "오렌지", "포도"]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]

print(f"숫자 리스트: {numbers}")
print(f"과일 리스트: {fruits}")
print(f"혼합 리스트: {mixed}")

# range()를 이용한 리스트 생성
range_list = list(range(10))
even_numbers = list(range(0, 21, 2))
print(f"범위 리스트: {range_list}")
print(f"짝수 리스트: {even_numbers}")

# 반복을 이용한 리스트 생성
repeated_list = ["안녕"] * 5
zeros = [0] * 10
print(f"반복 리스트: {repeated_list}")
print(f"0으로 채운 리스트: {zeros}")

print("=" * 30)

# 2. 리스트 길이와 타입
print("📏 리스트 정보 확인")

sample_list = [10, 20, 30, 40, 50]
print(f"리스트: {sample_list}")
print(f"길이: {len(sample_list)}")
print(f"타입: {type(sample_list)}")
print(f"최댓값: {max(sample_list)}")
print(f"최솟값: {min(sample_list)}")
print(f"합계: {sum(sample_list)}")

print("=" * 30)

# 3. 기본 인덱싱
print("📍 기본 인덱싱")

colors = ["빨강", "파랑", "노랑", "초록", "보라"]
print(f"색상 리스트: {colors}")
print(f"리스트 길이: {len(colors)}")

print("\n양수 인덱스로 접근:")
for i in range(len(colors)):
    print(f"  colors[{i}] = {colors[i]}")

print("\n음수 인덱스로 접근:")
for i in range(-len(colors), 0):
    print(f"  colors[{i}] = {colors[i]}")

# 특정 위치 접근
print(f"\n첫 번째 색상: {colors[0]}")
print(f"마지막 색상: {colors[-1]}")
print(f"두 번째 색상: {colors[1]}")
print(f"끝에서 두 번째: {colors[-2]}")

print("=" * 30)

# 4. 리스트 원소 존재 확인
print("🔍 원소 존재 확인")

pets = ["강아지", "고양이", "햄스터", "앵무새", "금붕어"]
print(f"애완동물 리스트: {pets}")

# in 연산자 사용
search_pets = ["강아지", "토끼", "고양이", "거북이"]

for pet in search_pets:
    if pet in pets:
        print(f"✅ {pet}는 리스트에 있습니다!")
    else:
        print(f"❌ {pet}는 리스트에 없습니다.")

# count() 메서드로 개수 확인
numbers_with_duplicates = [1, 2, 3, 2, 4, 2, 5]
print(f"\n숫자 리스트: {numbers_with_duplicates}")
print(f"숫자 2의 개수: {numbers_with_duplicates.count(2)}")
print(f"숫자 6의 개수: {numbers_with_duplicates.count(6)}")

print("=" * 30)

# 5. 리스트 연산
print("🧮 리스트 연산")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

# 연결 (concatenation)
combined = list1 + list2
print(f"연결: {list1} + {list2} = {combined}")

# 반복 (repetition)
repeated = list1 * 3
print(f"반복: {list1} * 3 = {repeated}")

# 확장 (extend)
list3 = [1, 2, 3]
list3.extend([4, 5, 6])
print(f"확장 후: {list3}")

# 리스트 비교
print(f"\n리스트 비교:")
print(f"[1, 2, 3] == [1, 2, 3]: {[1, 2, 3] == [1, 2, 3]}")
print(f"[1, 2, 3] == [3, 2, 1]: {[1, 2, 3] == [3, 2, 1]}")
print(f"[1, 2] < [1, 3]: {[1, 2] < [1, 3]}")
```

#### 🔪 슬라이싱 마스터

```python
print("🔪 슬라이싱 마스터")
print("=" * 18)

# 테스트용 리스트
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"알파벳: {alphabet}")
print(f"숫자: {numbers}")
print(f"인덱스: {list(range(len(alphabet)))}")

print("=" * 30)

# 1. 기본 슬라이싱 [start:end]
print("📋 기본 슬라이싱 [start:end]")

examples = [
    (alphabet[1:4], "alphabet[1:4]", "인덱스 1부터 3까지"),
    (alphabet[0:5], "alphabet[0:5]", "처음부터 4까지"),
    (alphabet[5:], "alphabet[5:]", "5부터 끝까지"),
    (alphabet[:3], "alphabet[:3]", "처음부터 2까지"),
    (alphabet[:], "alphabet[:]", "전체 복사")
]

for result, code, description in examples:
    print(f"  {code:15} = {result} ({description})")

print("=" * 30)

# 2. 음수 인덱스 슬라이싱
print("➖ 음수 인덱스 슬라이싱")

examples = [
    (alphabet[-3:], "alphabet[-3:]", "끝에서 3개부터 끝까지"),
    (alphabet[:-2], "alphabet[:-2]", "처음부터 끝에서 2개 전까지"),
    (alphabet[-5:-2], "alphabet[-5:-2]", "끝에서 5번째부터 3번째까지"),
    (alphabet[-1:], "alphabet[-1:]", "마지막 원소만"),
    (numbers[-6:-1], "numbers[-6:-1]", "끝에서 6번째부터 2번째까지")
]

for result, code, description in examples:
    print(f"  {code:18} = {result} ({description})")

print("=" * 30)

# 3. 단계(step) 슬라이싱 [start:end:step]
print("👣 단계(step) 슬라이싱")

examples = [
    (alphabet[::2], "alphabet[::2]", "2개씩 건너뛰며 전체"),
    (alphabet[1::2], "alphabet[1::2]", "1부터 시작해서 2개씩 건너뛰기"),
    (alphabet[::3], "alphabet[::3]", "3개씩 건너뛰며 전체"),
    (numbers[2:8:2], "numbers[2:8:2]", "2부터 7까지 2개씩 건너뛰기"),
    (alphabet[::-1], "alphabet[::-1]", "전체를 역순으로"),
    (alphabet[8:2:-2], "alphabet[8:2:-2]", "8부터 3까지 역순으로 2개씩")
]

for result, code, description in examples:
    print(f"  {code:19} = {result}")
    print(f"  {' ' * 19}   ({description})")

print("=" * 30)

# 4. 실용적인 슬라이싱 활용
print("💡 실용적인 슬라이싱")

# 문자열도 슬라이싱 가능
message = "Python Programming"
print(f"문자열: '{message}'")
print(f"  처음 6글자: '{message[:6]}'")
print(f"  마지막 11글자: '{message[-11:]}'")
print(f"  가운데 부분: '{message[7:-4]}'")
print(f"  역순: '{message[::-1]}'")

# 리스트에서 패턴 찾기
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(f"\n데이터: {data}")
print(f"  앞의 5개 (홀수): {data[:5]}")
print(f"  뒤의 5개 (짝수): {data[5:]}")
print(f"  홀수 위치만: {data[::2]}")
print(f"  짝수 위치만: {data[1::2]}")

# 데이터 나누기
scores = [85, 92, 78, 96, 88, 74, 91, 83, 87, 95]
print(f"\n점수: {scores}")

# 상위 5개, 하위 5개 나누기
sorted_scores = sorted(scores, reverse=True)
top_5 = sorted_scores[:5]
bottom_5 = sorted_scores[-5:]
print(f"  상위 5개: {top_5}")
print(f"  하위 5개: {bottom_5}")

print("=" * 30)

# 5. 슬라이싱을 이용한 리스트 수정
print("✂️ 슬라이싱으로 수정")

# 원본 리스트
fruits = ["사과", "바나나", "오렌지", "포도", "키위"]
print(f"원본: {fruits}")

# 슬라이싱으로 일부분 교체
fruits_copy = fruits.copy()
fruits_copy[1:3] = ["딸기", "블루베리"]
print(f"1:3 교체: {fruits_copy}")

# 슬라이싱으로 삽입
fruits_copy = fruits.copy()
fruits_copy[2:2] = ["망고", "파인애플"]  # 2번 인덱스에 삽입
print(f"2번에 삽입: {fruits_copy}")

# 슬라이싱으로 삭제
fruits_copy = fruits.copy()
fruits_copy[1:4] = []  # 1부터 3까지 삭제
print(f"1:4 삭제: {fruits_copy}")

# 단계 슬라이싱으로 교체
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\n숫자 원본: {numbers}")

numbers_copy = numbers.copy()
numbers_copy[::2] = [10, 30, 50, 70, 90]  # 짝수 인덱스 위치 교체
print(f"짝수 인덱스 교체: {numbers_copy}")

print("=" * 30)

# 6. 슬라이싱 연습 문제
print("📝 슬라이싱 연습")

# 문제용 데이터
test_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"연습용 리스트: {test_list}")

print("\n연습 문제:")
print("1. 처음 3개 원소:", test_list[:3])
print("2. 마지막 3개 원소:", test_list[-3:])
print("3. 가운데 4개 원소:", test_list[3:7])
print("4. 홀수 번째 위치 원소:", test_list[::2])
print("5. 역순으로 전체:", test_list[::-1])
print("6. 역순으로 처음 5개:", test_list[::-1][:5])
print("7. 30부터 70까지:", test_list[2:7])
print("8. 끝에서부터 2개씩 건너뛰며 5개:", test_list[::-2][:5])

# 복잡한 슬라이싱
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\n2차원 리스트: {matrix}")
print("첫 번째 행:", matrix[0])
print("각 행의 첫 번째 열:", [row[0] for row in matrix])
print("각 행의 마지막 열:", [row[-1] for row in matrix])
```

#### 🔧 리스트 수정과 연산

```python
print("🔧 리스트 수정과 연산")
print("=" * 20)

# 1. 개별 원소 수정
print("✏️ 개별 원소 수정")

colors = ["빨강", "파랑", "노랑", "초록"]
print(f"원본: {colors}")

# 인덱스로 수정
colors[1] = "보라"
print(f"1번 수정: {colors}")

colors[-1] = "주황"
print(f"마지막 수정: {colors}")

print("=" * 30)

# 2. 리스트 복사의 주의사항
print("⚠️ 리스트 복사 주의사항")

# 얕은 복사 (주소 복사)
original = [1, 2, 3, 4, 5]
shallow_copy = original  # 같은 리스트를 가리킴
print(f"원본: {original}")
print(f"얕은 복사: {shallow_copy}")

shallow_copy[0] = 999
print(f"얕은 복사 수정 후:")
print(f"원본: {original}")  # 원본도 변경됨!
print(f"얕은 복사: {shallow_copy}")

print("\n깊은 복사 방법들:")
original = [1, 2, 3, 4, 5]

# 방법 1: copy() 메서드
deep_copy1 = original.copy()
print(f"원본: {original}")
print(f"copy() 복사: {deep_copy1}")

deep_copy1[0] = 888
print(f"copy() 수정 후:")
print(f"원본: {original}")  # 원본은 변경 안됨
print(f"copy() 복사: {deep_copy1}")

# 방법 2: 슬라이싱
original = [1, 2, 3, 4, 5]
deep_copy2 = original[:]
deep_copy2[1] = 777
print(f"\n슬라이싱 복사:")
print(f"원본: {original}")
print(f"슬라이싱 복사: {deep_copy2}")

# 방법 3: list() 생성자
original = [1, 2, 3, 4, 5]
deep_copy3 = list(original)
deep_copy3[2] = 666
print(f"\nlist() 복사:")
print(f"원본: {original}")
print(f"list() 복사: {deep_copy3}")

print("=" * 30)

# 3. 리스트 산술 연산
print("➕ 리스트 산술 연산")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

# 덧셈 (연결)
result = list1 + list2
print(f"덧셈: {list1} + {list2} = {result}")

# 곱셈 (반복)
result = list1 * 3
print(f"곱셈: {list1} * 3 = {result}")

# 복합 연산
result = ([1, 2] * 2) + ([3, 4] * 2)
print(f"복합: ([1, 2] * 2) + ([3, 4] * 2) = {result}")

print("=" * 30)

# 4. 리스트 비교 연산
print("🆚 리스트 비교 연산")

lists_to_compare = [
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 4]),
    ([1, 2], [1, 2, 3]),
    (["a", "b"], ["A", "B"]),
    ([1, "2"], [1, 2])
]

for list_a, list_b in lists_to_compare:
    print(f"{list_a} == {list_b}: {list_a == list_b}")
    print(f"{list_a} != {list_b}: {list_a != list_b}")
    
    try:
        print(f"{list_a} < {list_b}: {list_a < list_b}")
    except TypeError:
        print(f"{list_a} < {list_b}: 비교 불가 (타입 다름)")
    print()

print("=" * 30)

# 5. 다차원 리스트 기초
print("📊 다차원 리스트")

# 2차원 리스트 생성
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2차원 리스트:")
for i, row in enumerate(matrix):
    print(f"  행 {i}: {row}")

# 개별 원소 접근
print(f"\nmatrix[0][0] = {matrix[0][0]}")
print(f"matrix[1][2] = {matrix[1][2]}")
print(f"matrix[2][1] = {matrix[2][1]}")

# 행과 열 접근
print(f"\n첫 번째 행: {matrix[0]}")
print(f"첫 번째 열: {[row[0] for row in matrix]}")
print(f"대각선: {[matrix[i][i] for i in range(3)]}")

# 2차원 리스트 수정
matrix[1][1] = 99
print(f"\n수정 후: {matrix}")

print("=" * 30)

# 6. 실용적인 예제
print("💼 실용적인 예제")

# 학생 점수 관리
students = ["김철수", "이영희", "박민수", "최지원"]
scores = [
    [90, 85, 92],  # 김철수: 국어, 영어, 수학
    [88, 92, 89],  # 이영희
    [75, 80, 85],  # 박민수
    [95, 88, 94]   # 최지원
]

print("📊 학생별 점수:")
subjects = ["국어", "영어", "수학"]

for i, student in enumerate(students):
    print(f"{student}: ", end="")
    for j, subject in enumerate(subjects):
        print(f"{subject} {scores[i][j]}점", end=" ")
    
    # 평균 계산
    average = sum(scores[i]) / len(subjects)
    print(f"(평균: {average:.1f}점)")

# 과목별 평균
print(f"\n📈 과목별 평균:")
for j, subject in enumerate(subjects):
    subject_scores = [scores[i][j] for i in range(len(students))]
    subject_average = sum(subject_scores) / len(students)
    print(f"{subject}: {subject_average:.1f}점")

# 할일 목록 관리
print(f"\n✅ 할일 목록 관리:")
todo_list = [
    ["파이썬 공부", False],
    ["장보기", True],
    ["운동하기", False],
    ["친구 만나기", False],
    ["책 읽기", True]
]

print("현재 할일 목록:")
for i, (task, done) in enumerate(todo_list):
    status = "✅ 완료" if done else "⏳ 대기"
    print(f"  {i+1}. {task} - {status}")

# 완료되지 않은 할일만 추출
pending_tasks = [task for task, done in todo_list if not done]
completed_tasks = [task for task, done in todo_list if done]

print(f"\n미완료 작업 ({len(pending_tasks)}개): {pending_tasks}")
print(f"완료 작업 ({len(completed_tasks)}개): {completed_tasks}")
```

---

### Part 2: 리스트 메서드 (40분)

#### 📝 추가와 삽입 메서드

```python
print("📝 추가와 삽입 메서드")
print("=" * 22)

# 1. append() - 끝에 하나씩 추가
print("➕ append() - 끝에 하나씩 추가")

fruits = ["사과", "바나나"]
print(f"초기 리스트: {fruits}")

fruits.append("오렌지")
print(f"append('오렌지') 후: {fruits}")

fruits.append("포도")
print(f"append('포도') 후: {fruits}")

# 리스트를 append하면?
fruits.append(["키위", "망고"])
print(f"append(['키위', '망고']) 후: {fruits}")
print(f"마지막 원소 타입: {type(fruits[-1])}")

print("=" * 30)

# 2. insert() - 지정 위치에 삽입
print("📍 insert() - 지정 위치에 삽입")

colors = ["빨강", "파랑", "노랑"]
print(f"초기 리스트: {colors}")

colors.insert(1, "초록")  # 1번 인덱스에 삽입
print(f"insert(1, '초록') 후: {colors}")

colors.insert(0, "보라")  # 맨 앞에 삽입
print(f"insert(0, '보라') 후: {colors}")

colors.insert(100, "주황")  # 범위를 벗어나면 맨 끝에 삽입
print(f"insert(100, '주황') 후: {colors}")

colors.insert(-1, "분홍")  # 음수 인덱스도 가능
print(f"insert(-1, '분홍') 후: {colors}")

print("=" * 30)

# 3. extend() - 리스트 확장
print("🔗 extend() - 리스트 확장")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print(f"리스트1: {numbers1}")
print(f"리스트2: {numbers2}")

# extend()는 각 원소를 하나씩 추가
numbers1.extend(numbers2)
print(f"extend() 후 리스트1: {numbers1}")

# append()와 extend() 비교
list_a = [1, 2, 3]
list_b = [1, 2, 3]

list_a.append([4, 5, 6])
list_b.extend([4, 5, 6])

print(f"\nappend([4, 5, 6]) 결과: {list_a}")
print(f"extend([4, 5, 6]) 결과: {list_b}")

# extend()는 문자열도 가능
letters = ["A", "B"]
letters.extend("CDE")  # 문자열을 문자 단위로 확장
print(f"extend('CDE') 결과: {letters}")

print("=" * 30)

# 4. 실용적인 추가 예제
print("💡 실용적인 추가 예제")

# 쇼핑 카트 시뮬레이션
shopping_cart = []
print("🛒 쇼핑 카트 시뮬레이션")
print(f"빈 카트: {shopping_cart}")

# 상품 하나씩 추가
items_to_add = ["우유", "계란", "빵", "사과"]
for item in items_to_add:
    shopping_cart.append(item)
    print(f"'{item}' 추가: {shopping_cart}")

# 대량 상품 추가 (extend 사용)
bulk_items = ["바나나", "오렌지", "요거트"]
shopping_cart.extend(bulk_items)
print(f"대량 추가 후: {shopping_cart}")

# 급하게 필요한 상품을 맨 앞에 추가
shopping_cart.insert(0, "마스크")
print(f"긴급 상품 추가: {shopping_cart}")

print("=" * 30)

# 5. 성적 입력 시스템
print("📊 성적 입력 시스템")

students = []
scores = []

# 학생 정보 입력 시뮬레이션
student_data = [
    ("김철수", [90, 85, 92]),
    ("이영희", [88, 92, 89]),
    ("박민수", [75, 80, 85])
]

for name, student_scores in student_data:
    students.append(name)
    scores.append(student_scores)
    
    # 평균 계산
    average = sum(student_scores) / len(student_scores)
    print(f"{name} 추가: 점수 {student_scores}, 평균 {average:.1f}점")

print(f"\n전체 학생: {students}")
print(f"전체 점수: {scores}")

# 새 학생 중간에 삽입
students.insert(1, "최지원")
scores.insert(1, [95, 88, 94])
print(f"\n중간 삽입 후:")
print(f"학생: {students}")
print(f"점수: {scores}")

print("=" * 30)

# 6. 동적 리스트 생성
print("🔄 동적 리스트 생성")

# 피보나치 수열 생성
fibonacci = [0, 1]
print(f"초기값: {fibonacci}")

# 10개까지 생성
for i in range(8):  # 이미 2개 있으므로 8개 더
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)
    print(f"{i+3}번째 수 추가: {fibonacci}")

print(f"\n완성된 피보나치 수열: {fibonacci}")

# 소수 찾기
primes = []
print(f"\n소수 찾기 (2~50):")

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        primes.append(num)
        if len(primes) <= 10:  # 처음 10개만 출력
            print(f"소수 {num} 추가: {primes}")

print(f"\n모든 소수 ({len(primes)}개): {primes}")
```

#### 🗑️ 삭제 메서드

```python
print("🗑️ 삭제 메서드")
print("=" * 15)

# 1. remove() - 값으로 삭제
print("❌ remove() - 값으로 삭제")

animals = ["강아지", "고양이", "토끼", "강아지", "햄스터"]
print(f"초기 리스트: {animals}")

animals.remove("고양이")  # 첫 번째 "고양이"만 삭제
print(f"remove('고양이') 후: {animals}")

animals.remove("강아지")  # 첫 번째 "강아지"만 삭제
print(f"remove('강아지') 후: {animals}")

# 없는 값을 삭제하려 하면 오류
try:
    animals.remove("거북이")
except ValueError as e:
    print(f"오류: {e}")

# 안전한 삭제
def safe_remove(lst, item):
    if item in lst:
        lst.remove(item)
        print(f"'{item}' 삭제 완료")
    else:
        print(f"'{item}'를 찾을 수 없습니다")

safe_remove(animals, "거북이")
safe_remove(animals, "토끼")
print(f"안전 삭제 후: {animals}")

print("=" * 30)

# 2. pop() - 인덱스로 삭제 후 반환
print("📤 pop() - 인덱스로 삭제 후 반환")

numbers = [10, 20, 30, 40, 50]
print(f"초기 리스트: {numbers}")

# pop() - 마지막 원소 삭제 후 반환
last_item = numbers.pop()
print(f"pop() 결과: {last_item}")
print(f"리스트: {numbers}")

# pop(index) - 특정 인덱스 삭제 후 반환
first_item = numbers.pop(0)
print(f"pop(0) 결과: {first_item}")
print(f"리스트: {numbers}")

middle_item = numbers.pop(1)  # 현재 1번 인덱스 (30) 삭제
print(f"pop(1) 결과: {middle_item}")
print(f"리스트: {numbers}")

# 스택(Stack) 시뮬레이션 - LIFO (Last In, First Out)
stack = []
print(f"\n📚 스택 시뮬레이션:")
print(f"빈 스택: {stack}")

# push 연산 (append 사용)
items_to_push = ["책1", "책2", "책3"]
for item in items_to_push:
    stack.append(item)
    print(f"PUSH '{item}': {stack}")

# pop 연산
while stack:
    item = stack.pop()
    print(f"POP '{item}': {stack}")

print("=" * 30)

# 3. clear() - 전체 삭제
print("🧹 clear() - 전체 삭제")

temp_list = [1, 2, 3, 4, 5]
print(f"삭제 전: {temp_list}")
temp_list.clear()
print(f"clear() 후: {temp_list}")

print("=" * 30)

# 4. del 키워드 - 다양한 삭제
print("🔥 del 키워드 - 다양한 삭제")

sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"원본: {sample}")

# 인덱스로 삭제
del sample[0]  # 첫 번째 원소 삭제
print(f"del sample[0]: {sample}")

# 슬라이싱으로 삭제
del sample[2:5]  # 인덱스 2~4 삭제
print(f"del sample[2:5]: {sample}")

# 단계 슬라이싱으로 삭제
del sample[::2]  # 짝수 인덱스 삭제
print(f"del sample[::2]: {sample}")

print("=" * 30)

# 5. 실용적인 삭제 예제
print("💼 실용적인 삭제 예제")

# 할일 목록 관리
todo_list = [
    "파이썬 공부",
    "장보기", 
    "운동하기",
    "친구 만나기",
    "책 읽기",
    "영화 보기"
]

print("📝 할일 목록 관리")
print(f"초기 목록: {todo_list}")

# 완료된 할일 제거
completed_tasks = ["장보기", "책 읽기"]
for task in completed_tasks:
    if task in todo_list:
        todo_list.remove(task)
        print(f"'{task}' 완료 처리: {todo_list}")

# 급한 일이 생겨서 마지막 일정 취소
cancelled = todo_list.pop()
print(f"'{cancelled}' 취소: {todo_list}")

# 특정 위치의 일정 변경 (삭제 후 추가)
old_task = todo_list.pop(1)  # 1번 인덱스 삭제
new_task = "병원 가기"
todo_list.insert(1, new_task)  # 같은 위치에 새 할일 추가
print(f"'{old_task}' → '{new_task}' 변경: {todo_list}")

print("=" * 30)

# 6. 중복 제거
print("🎯 중복 제거")

# 중복이 있는 리스트
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"중복 있는 리스트: {numbers_with_duplicates}")

# 방법 1: 직접 제거 (순서 유지)
unique_numbers = []
for num in numbers_with_duplicates:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"중복 제거 (방법1): {unique_numbers}")

# 방법 2: set 사용 후 다시 list로 변환 (순서 변경될 수 있음)
unique_numbers2 = list(set(numbers_with_duplicates))
print(f"중복 제거 (방법2): {unique_numbers2}")

# 특정 값 모두 제거
words = ["사과", "바나나", "사과", "오렌지", "사과", "포도"]
print(f"\n단어 리스트: {words}")

word_to_remove = "사과"
while word_to_remove in words:
    words.remove(word_to_remove)

print(f"'{word_to_remove}' 모두 제거: {words}")

# 조건에 맞는 항목들 제거
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
print(f"\n숫자 리스트: {numbers}")

# 음수 모두 제거 (역순으로 순회하면서 삭제)
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < 0:
        removed = numbers.pop(i)
        print(f"음수 {removed} 제거: {numbers}")

print(f"최종 결과: {numbers}")
```

#### 🔧 정렬과 검색 메서드

```python
print("🔧 정렬과 검색 메서드")
print("=" * 22)

# 1. sort() - 리스트 정렬 (원본 변경)
print("🔢 sort() - 원본 변경하는 정렬")

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"원본 숫자: {numbers}")

# 오름차순 정렬
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"오름차순 정렬: {numbers_copy}")

# 내림차순 정렬
numbers_copy = numbers.copy()
numbers_copy.sort(reverse=True)
print(f"내림차순 정렬: {numbers_copy}")

# 문자열 정렬
fruits = ["포도", "사과", "바나나", "오렌지", "키위"]
print(f"\n원본 과일: {fruits}")

fruits_copy = fruits.copy()
fruits_copy.sort()
print(f"가나다순 정렬: {fruits_copy}")

fruits_copy = fruits.copy()
fruits_copy.sort(reverse=True)
print(f"역순 정렬: {fruits_copy}")

# 길이순 정렬 (key 매개변수 사용)
words = ["python", "java", "c", "javascript", "go"]
print(f"\n원본 단어: {words}")

words_copy = words.copy()
words_copy.sort(key=len)
print(f"길이순 정렬: {words_copy}")

words_copy = words.copy()
words_copy.sort(key=len, reverse=True)
print(f"길이역순 정렬: {words_copy}")

print("=" * 30)

# 2. sorted() - 새 리스트 반환 (원본 유지)
print("📋 sorted() - 새 리스트 반환")

original = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {original}")

ascending = sorted(original)
print(f"오름차순 (새 리스트): {ascending}")

descending = sorted(original, reverse=True)
print(f"내림차순 (새 리스트): {descending}")

print(f"원본 확인: {original}")  # 원본은 변경되지 않음

# 복잡한 정렬
students = [
    ("김철수", 85),
    ("이영희", 92), 
    ("박민수", 78),
    ("최지원", 96),
    ("정수진", 88)
]

print(f"\n학생 점수: {students}")

# 이름순 정렬
by_name = sorted(students, key=lambda x: x[0])
print(f"이름순: {by_name}")

# 점수순 정렬
by_score = sorted(students, key=lambda x: x[1])
print(f"점수 오름차순: {by_score}")

by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"점수 내림차순: {by_score_desc}")

print("=" * 30)

# 3. reverse() - 리스트 뒤집기
print("🔄 reverse() - 리스트 뒤집기")

numbers = [1, 2, 3, 4, 5]
print(f"원본: {numbers}")

numbers.reverse()
print(f"reverse() 후: {numbers}")

# 문자열도 가능
chars = list("HELLO")
print(f"\n문자 리스트: {chars}")
chars.reverse()
print(f"reverse() 후: {chars}")
print(f"다시 문자열로: {''.join(chars)}")

print("=" * 30)

# 4. index() - 값의 위치 찾기
print("🔍 index() - 값의 위치 찾기")

animals = ["강아지", "고양이", "토끼", "강아지", "햄스터"]
print(f"동물 리스트: {animals}")

# 첫 번째로 나타나는 위치 반환
dog_index = animals.index("강아지")
print(f"'강아지'의 첫 위치: {dog_index}")

cat_index = animals.index("고양이")
print(f"'고양이'의 위치: {cat_index}")

# 없는 값을 찾으면 오류
try:
    bird_index = animals.index("새")
except ValueError as e:
    print(f"오류: {e}")

# 안전한 검색
def safe_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1  # 없으면 -1 반환

print(f"'햄스터' 위치: {safe_index(animals, '햄스터')}")
print(f"'거북이' 위치: {safe_index(animals, '거북이')}")

# 범위를 지정한 검색
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"\n숫자 리스트: {numbers}")

first_2 = numbers.index(2)
print(f"첫 번째 '2'의 위치: {first_2}")

# 3번 인덱스부터 검색
second_2 = numbers.index(2, first_2 + 1)
print(f"두 번째 '2'의 위치: {second_2}")

# 5번 인덱스부터 검색  
third_2 = numbers.index(2, second_2 + 1)
print(f"세 번째 '2'의 위치: {third_2}")

print("=" * 30)

# 5. count() - 값의 개수 세기
print("📊 count() - 값의 개수 세기")

letters = ['a', 'b', 'c', 'a', 'd', 'a', 'e', 'a']
print(f"문자 리스트: {letters}")

count_a = letters.count('a')
print(f"'a'의 개수: {count_a}")

count_x = letters.count('x')
print(f"'x'의 개수: {count_x}")

# 실용적인 예제 - 설문조사 결과
survey_results = ["좋음", "보통", "좋음", "나쁨", "좋음", "보통", "좋음", "보통", "좋음"]
print(f"\n설문 결과: {survey_results}")

good_count = survey_results.count("좋음")
normal_count = survey_results.count("보통")
bad_count = survey_results.count("나쁨")

total = len(survey_results)
print(f"좋음: {good_count}개 ({good_count/total*100:.1f}%)")
print(f"보통: {normal_count}개 ({normal_count/total*100:.1f}%)")
print(f"나쁨: {bad_count}개 ({bad_count/total*100:.1f}%)")

print("=" * 30)

# 6. 종합 활용 예제
print("🎯 종합 활용 예제")

# 학급 성적 분석 시스템
class_scores = [85, 92, 78, 96, 88, 74, 91, 83, 87, 95, 89, 93, 76, 84, 90]
print("📊 학급 성적 분석 시스템")
print(f"성적 리스트: {class_scores}")

# 기본 통계
print(f"\n📈 기본 통계:")
print(f"학생 수: {len(class_scores)}명")
print(f"최고점: {max(class_scores)}점")
print(f"최저점: {min(class_scores)}점")
print(f"평균: {sum(class_scores)/len(class_scores):.1f}점")

# 정렬된 성적
sorted_scores = sorted(class_scores, reverse=True)
print(f"정렬된 성적: {sorted_scores}")

# 등급별 분류
grade_a = [score for score in class_scores if score >= 90]
grade_b = [score for score in class_scores if 80 <= score < 90]  
grade_c = [score for score in class_scores if 70 <= score < 80]
grade_d = [score for score in class_scores if score < 70]

print(f"\n📋 등급별 분류:")
print(f"A등급 (90점 이상): {len(grade_a)}명 - {grade_a}")
print(f"B등급 (80-89점): {len(grade_b)}명 - {grade_b}")
print(f"C등급 (70-79점): {len(grade_c)}명 - {grade_c}")
print(f"D등급 (70점 미만): {len(grade_d)}명 - {grade_d}")

# 특정 점수 분석
target_score = 85
count_85 = class_scores.count(target_score)
if count_85 > 0:
    index_85 = class_scores.index(target_score)
    print(f"\n🎯 {target_score}점 분석:")
    print(f"{target_score}점 학생: {count_85}명")
    print(f"첫 번째 {target_score}점 학생 번호: {index_85 + 1}번")
```

#### 🧠 리스트 컴프리헨션

```python
print("🧠 리스트 컴프리헨션")
print("=" * 20)

# 1. 기본 리스트 컴프리헨션
print("⚡ 기본 문법")

# 일반적인 방법
squares_normal = []
for i in range(5):
    squares_normal.append(i ** 2)
print(f"일반적인 방법: {squares_normal}")

# 리스트 컴프리헨션
squares_comp = [i ** 2 for i in range(5)]
print(f"컴프리헨션: {squares_comp}")

# 문자열 처리
words = ["hello", "world", "python", "programming"]
print(f"\n원본 단어: {words}")

# 대문자로 변환
upper_normal = []
for word in words:
    upper_normal.append(word.upper())
print(f"일반적인 방법: {upper_normal}")

upper_comp = [word.upper() for word in words]
print(f"컴프리헨션: {upper_comp}")

print("=" * 30)

# 2. 조건부 리스트 컴프리헨션
print("🎯 조건부 컴프리헨션")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 숫자: {numbers}")

# 짝수만 필터링
evens_normal = []
for num in numbers:
    if num % 2 == 0:
        evens_normal.append(num)
print(f"짝수 (일반): {evens_normal}")

evens_comp = [num for num in numbers if num % 2 == 0]
print(f"짝수 (컴프리헨션): {evens_comp}")

# 5보다 큰 수의 제곱
big_squares = [num ** 2 for num in numbers if num > 5]
print(f"5보다 큰 수의 제곱: {big_squares}")

# 문자열 길이 조건
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
print(f"\n단어: {words}")

# 길이가 4 이상인 단어만
long_words = [word for word in words if len(word) >= 4]
print(f"긴 단어들: {long_words}")

# 길이가 4 이상인 단어를 대문자로
long_upper = [word.upper() for word in words if len(word) >= 4]
print(f"긴 단어들 (대문자): {long_upper}")

print("=" * 30)

# 3. 조건부 표현식이 있는 컴프리헨션
print("🔀 조건부 표현식")

numbers = [-3, -1, 0, 2, 5, -2, 8]
print(f"원본 숫자: {numbers}")

# 음수는 0으로, 양수는 그대로
processed = [num if num > 0 else 0 for num in numbers]
print(f"음수→0 변환: {processed}")

# 짝수는 제곱, 홀수는 세제곱
power_processed = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
print(f"짝수²홀수³: {power_processed}")

# 절댓값 처리
abs_values = [num if num >= 0 else -num for num in numbers]
print(f"절댓값: {abs_values}")

# 학점 처리
scores = [95, 87, 92, 76, 84, 98, 73, 89]
print(f"\n점수: {scores}")

grades = ['A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F' 
          for score in scores]
print(f"학점: {grades}")

print("=" * 30)

# 4. 중첩 반복문 컴프리헨션
print("🔄 중첩 반복문")

# 구구단
multiplication_table = [[i * j for j in range(1, 10)] for i in range(2, 10)]
print("구구단 (2~9단):")
for i, row in enumerate(multiplication_table, 2):
    print(f"{i}단: {row}")

# 좌표 생성
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"\n3×3 좌표: {coordinates}")

# 조건이 있는 중첩
even_coords = [(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0]
print(f"좌표합이 짝수인 경우: {even_coords}")

print("=" * 30)

# 5. 실용적인 컴프리헨션 예제
print("💼 실용적인 예제")

# 파일 필터링 시뮬레이션
files = ["report.txt", "image.jpg", "data.csv", "photo.png", "backup.txt", "script.py"]
print(f"파일 목록: {files}")

# 특정 확장자 파일만
txt_files = [file for file in files if file.endswith('.txt')]
print(f"텍스트 파일: {txt_files}")

# 파일명만 (확장자 제거)
names_only = [file.split('.')[0] for file in files]
print(f"파일명만: {names_only}")

# 이메일 필터링
emails = ["user1@gmail.com", "admin@company.co.kr", "user2@naver.com", "spam@ads.com"]
print(f"\n이메일 목록: {emails}")

# gmail과 naver만
personal_emails = [email for email in emails if 'gmail.com' in email or 'naver.com' in email]
print(f"개인 이메일: {personal_emails}")

# 도메인만 추출
domains = [email.split('@')[1] for email in emails]
print(f"도메인 목록: {domains}")

# 온도 변환 (섭씨 → 화씨)
celsius_temps = [0, 10, 20, 30, 37, 100]
print(f"\n섭씨 온도: {celsius_temps}")

fahrenheit_temps = [c * 9/5 + 32 for c in celsius_temps]
print(f"화씨 온도: {fahrenheit_temps}")

# 온도별 설명
temp_descriptions = [
    f"{c}°C ({c*9/5+32:.1f}°F): {'매우춥다' if c < 0 else '춥다' if c < 15 else '따뜻하다' if c < 25 else '덥다'}"
    for c in celsius_temps
]

print("온도별 설명:")
for desc in temp_descriptions:
    print(f"  {desc}")

print("=" * 30)

# 6. 성능 비교 및 고급 활용
print("⚡ 성능과 고급 활용")

# 매우 큰 리스트 생성 (메모리 효율성 테스트)
import time

# 일반적인 방법
start_time = time.time()
normal_list = []
for i in range(100000):
    if i % 2 == 0:
        normal_list.append(i ** 2)
normal_time = time.time() - start_time

# 리스트 컴프리헨션
start_time = time.time()
comp_list = [i ** 2 for i in range(100000) if i % 2 == 0]
comp_time = time.time() - start_time

print(f"일반 방법 시간: {normal_time:.4f}초")
print(f"컴프리헨션 시간: {comp_