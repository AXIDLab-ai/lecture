
**[← Week 12](./week12.md) | [목차](./lectureMap.md) | [다음: Week 14 →](./week14.md)**

Week 13: 데이터베이스 (SQLite)

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **SQLite 기초**: SQLite 데이터베이스의 개념과 sqlite3 모듈 활용법을 익힙니다
2. **SQL 문법**: CREATE, INSERT, SELECT, UPDATE, DELETE 등 기본 SQL 문법을 마스터합니다
3. **Python DB API**: 파이썬에서 데이터베이스에 연결하고 조작하는 방법을 학습합니다
4. **CRUD 연산**: 데이터 생성, 조회, 수정, 삭제의 전체 과정을 실습합니다
5. **실전 DB 시스템**: 주소록, 재고관리, 성적관리 등 실용적인 시스템을 구축합니다
6. **데이터 관리**: 트랜잭션, 인덱스, 백업 등 데이터 관리 기법을 이해합니다

---

## 📚 핵심 개념 요약

### 1. 데이터베이스 기본 개념

| 용어 | 설명 | 예시 |
|------|------|------|
| **Database** | 관련된 정보들의 집합 | `school.db` |
| **Table** | 데이터를 저장하는 구조 | `students` 테이블 |
| **Row(Record)** | 테이블의 한 행 | 한 명의 학생 정보 |
| **Column(Field)** | 테이블의 열 | `name`, `age`, `grade` |
| **Primary Key** | 각 행을 구분하는 고유 키 | `student_id` |
| **Foreign Key** | 다른 테이블을 참조하는 키 | `class_id` |

### 2. SQLite 데이터 타입

| SQLite 타입 | 설명 | Python 타입 | 예시 |
|-------------|------|--------------|------|
| **INTEGER** | 정수 | `int` | `123`, `-456` |
| **REAL** | 실수 | `float` | `3.14`, `-2.5` |
| **TEXT** | 문자열 | `str` | `'Hello'`, `'안녕하세요'` |
| **BLOB** | 바이너리 데이터 | `bytes` | 이미지, 파일 |
| **NULL** | 빈 값 | `None` | `NULL` |

### 3. 기본 SQL 명령어

| 명령어 | 용도 | 기본 문법 | 예시 |
|--------|------|-----------|------|
| **CREATE TABLE** | 테이블 생성 | `CREATE TABLE name (columns)` | 학생 테이블 생성 |
| **INSERT** | 데이터 추가 | `INSERT INTO table VALUES (...)` | 새 학생 추가 |
| **SELECT** | 데이터 조회 | `SELECT * FROM table WHERE ...` | 학생 목록 조회 |
| **UPDATE** | 데이터 수정 | `UPDATE table SET col=val WHERE ...` | 학생 정보 수정 |
| **DELETE** | 데이터 삭제 | `DELETE FROM table WHERE ...` | 학생 정보 삭제 |
| **DROP TABLE** | 테이블 삭제 | `DROP TABLE name` | 테이블 완전 삭제 |

### 4. sqlite3 모듈 주요 함수

| 함수 | 설명 | 반환값 | 예시 |
|------|------|--------|------|
| `sqlite3.connect()` | DB 연결 | Connection 객체 | `conn = sqlite3.connect('db.db')` |
| `conn.cursor()` | 커서 생성 | Cursor 객체 | `cur = conn.cursor()` |
| `cur.execute()` | SQL 실행 | None | `cur.execute("SELECT * FROM table")` |
| `cur.fetchone()` | 한 행 가져오기 | 튜플 또는 None | `row = cur.fetchone()` |
| `cur.fetchall()` | 모든 행 가져오기 | 튜플 리스트 | `rows = cur.fetchall()` |
| `conn.commit()` | 변경사항 저장 | None | `conn.commit()` |

---

## 💻 실습 세션 (2시간)

### Part 1: SQLite 기초 (30분)

#### 📝 SQLite와 sqlite3 모듈 기초

```python
print("📝 SQLite와 sqlite3 모듈 기초")
print("=" * 20)

import sqlite3
import os
from datetime import datetime, date

# 1. 데이터베이스 연결과 기본 조작
print("1️⃣ 데이터베이스 연결")

# 데이터베이스 파일이 있으면 삭제 (깨끗한 시작)
if os.path.exists('tutorial.db'):
    os.remove('tutorial.db')
    print("🗑️ 기존 데이터베이스 파일 삭제")

# 데이터베이스 연결 (파일이 없으면 자동 생성)
try:
    conn = sqlite3.connect('tutorial.db')
    print("✅ 데이터베이스 'tutorial.db' 연결 성공")
    
    # 커서 생성
    cursor = conn.cursor()
    print("✅ 커서 생성 완료")
    
    # SQLite 버전 확인
    cursor.execute("SELECT sqlite_version()")
    version = cursor.fetchone()[0]
    print(f"📊 SQLite 버전: {version}")
    
except sqlite3.Error as e:
    print(f"❌ 데이터베이스 연결 실패: {e}")

print("=" * 30)

# 2. 테이블 생성
print("2️⃣ 테이블 생성")

try:
    # 학생 테이블 생성
    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT,
        email TEXT UNIQUE,
        created_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """
    
    cursor.execute(create_students_table)
    print("✅ 'students' 테이블 생성 완료")
    
    # 과목 테이블 생성
    create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        credits INTEGER DEFAULT 3,
        professor TEXT
    )
    """
    
    cursor.execute(create_subjects_table)
    print("✅ 'subjects' 테이블 생성 완료")
    
    # 성적 테이블 생성 (학생과 과목을 연결)
    create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        score INTEGER CHECK (score >= 0 AND score <= 100),
        semester TEXT,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )
    """
    
    cursor.execute(create_grades_table)
    print("✅ 'grades' 테이블 생성 완료")
    
    # 변경사항 저장
    conn.commit()
    print("💾 테이블 생성 변경사항 저장")
    
except sqlite3.Error as e:
    print(f"❌ 테이블 생성 실패: {e}")

print("=" * 30)

# 3. 테이블 정보 확인
print("3️⃣ 테이블 정보 확인")

try:
    # 데이터베이스의 모든 테이블 목록
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print("📋 생성된 테이블 목록:")
    for table in tables:
        print(f"  📁 {table[0]}")
    
    print()
    
    # 각 테이블의 구조 확인
    for table in tables:
        table_name = table[0]
        print(f"🔍 '{table_name}' 테이블 구조:")
        
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        print("   컬럼명        | 타입     | NULL허용 | 기본값 | 기본키")
        print("   " + "-" * 50)
        
        for column in columns:
            col_id, name, data_type, not_null, default_val, pk = column
            null_ok = "NO" if not_null else "YES"
            default_str = str(default_val) if default_val else ""
            pk_str = "YES" if pk else ""
            
            print(f"   {name:12s} | {data_type:8s} | {null_ok:8s} | {default_str:6s} | {pk_str}")
        
        print()

except sqlite3.Error as e:
    print(f"❌ 테이블 정보 조회 실패: {e}")

print("=" * 30)

# 4. 기본 SQL 문법 실습
print("4️⃣ 기본 SQL 문법 실습")

def execute_and_print(sql, description, fetch_results=False):
    """SQL 실행 및 결과 출력 헬퍼 함수"""
    try:
        print(f"📝 {description}")
        print(f"   SQL: {sql}")
        
        cursor.execute(sql)
        
        if fetch_results:
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(f"   결과: {row}")
            else:
                print("   결과: (데이터 없음)")
        else:
            print(f"   실행됨: {cursor.rowcount}개 행 영향받음")
        
        print()
        
    except sqlite3.Error as e:
        print(f"   ❌ 실행 실패: {e}")
        print()

# INSERT 예제들
execute_and_print(
    "INSERT INTO students (name, age, grade, email) VALUES ('김철수', 20, 'A', 'kim@school.com')",
    "학생 데이터 삽입 #1"
)

execute_and_print(
    "INSERT INTO students (name, age, grade, email) VALUES ('이영희', 19, 'B+', 'lee@school.com')",
    "학생 데이터 삽입 #2"
)

execute_and_print(
    "INSERT INTO students (name, age, grade, email) VALUES ('박민수', 21, 'A+', 'park@school.com')",
    "학생 데이터 삽입 #3"
)

# 과목 데이터 삽입
execute_and_print(
    "INSERT INTO subjects (subject_name, credits, professor) VALUES ('파이썬프로그래밍', 3, '김교수')",
    "과목 데이터 삽입 #1"
)

execute_and_print(
    "INSERT INTO subjects (subject_name, credits, professor) VALUES ('데이터베이스', 3, '이교수')",
    "과목 데이터 삽입 #2"
)

# 변경사항 저장
conn.commit()

# SELECT 예제들
execute_and_print(
    "SELECT * FROM students",
    "모든 학생 조회",
    fetch_results=True
)

execute_and_print(
    "SELECT name, age FROM students WHERE age >= 20",
    "20세 이상 학생의 이름과 나이 조회",
    fetch_results=True
)

execute_and_print(
    "SELECT COUNT(*) FROM students",
    "총 학생 수 조회",
    fetch_results=True
)

print("🎯 Part 1 요약:")
print("✅ SQLite 데이터베이스 연결")
print("✅ 테이블 생성 (CREATE TABLE)")
print("✅ 데이터 삽입 (INSERT)")
print("✅ 데이터 조회 (SELECT)")
print("✅ 테이블 구조 확인")
```

---

### Part 2: CRUD 연산 (40분)

#### 🔧 Create, Read, Update, Delete 완전 정복

```python
print("🔧 CRUD 연산 완전 정복")
print("=" * 15)

# 1. CREATE - 데이터 생성
print("1️⃣ CREATE - 데이터 생성")

def insert_student(name, age, grade, email):
    """학생 데이터 삽입 함수"""
    try:
        sql = "INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (name, age, grade, email))
        conn.commit()
        
        # 방금 삽입된 행의 ID 가져오기
        student_id = cursor.lastrowid
        print(f"✅ 학생 추가 완료: {name} (ID: {student_id})")
        return student_id
        
    except sqlite3.IntegrityError as e:
        print(f"❌ 삽입 실패 (중복 또는 제약조건): {e}")
        return None
    except sqlite3.Error as e:
        print(f"❌ 삽입 실패: {e}")
        return None

def insert_subject(subject_name, credits, professor):
    """과목 데이터 삽입 함수"""
    try:
        sql = "INSERT INTO subjects (subject_name, credits, professor) VALUES (?, ?, ?)"
        cursor.execute(sql, (subject_name, credits, professor))
        conn.commit()
        
        subject_id = cursor.lastrowid
        print(f"✅ 과목 추가 완료: {subject_name} (ID: {subject_id})")
        return subject_id
        
    except sqlite3.Error as e:
        print(f"❌ 과목 추가 실패: {e}")
        return None

def insert_grade(student_id, subject_id, score, semester):
    """성적 데이터 삽입 함수"""
    try:
        sql = "INSERT INTO grades (student_id, subject_id, score, semester) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (student_id, subject_id, score, semester))
        conn.commit()
        
        grade_id = cursor.lastrowid
        print(f"✅ 성적 추가 완료: 학생ID {student_id}, 과목ID {subject_id}, 점수 {score} (ID: {grade_id})")
        return grade_id
        
    except sqlite3.Error as e:
        print(f"❌ 성적 추가 실패: {e}")
        return None

# 더 많은 데이터 삽입
print("👥 더 많은 학생 데이터 삽입:")
students_data = [
    ("정다영", 22, "A+", "jung@school.com"),
    ("최민호", 20, "B", "choi@school.com"),
    ("한지수", 19, "A", "han@school.com"),
    ("오성민", 21, "C+", "oh@school.com"),
    ("윤서영", 20, "A+", "yoon@school.com")
]

student_ids = []
for name, age, grade, email in students_data:
    student_id = insert_student(name, age, grade, email)
    if student_id:
        student_ids.append(student_id)

print(f"📊 총 {len(student_ids)}명의 새 학생 추가됨")

print("\n📚 더 많은 과목 추가:")
subjects_data = [
    ("자료구조", 3, "박교수"),
    ("알고리즘", 3, "최교수"),
    ("운영체제", 3, "김교수"),
    ("네트워크", 2, "이교수")
]

subject_ids = []
for subject_name, credits, professor in subjects_data:
    subject_id = insert_subject(subject_name, credits, professor)
    if subject_id:
        subject_ids.append(subject_id)

print(f"📊 총 {len(subject_ids)}개의 새 과목 추가됨")

# 성적 데이터 추가
print("\n📝 성적 데이터 추가:")
import random

# 랜덤 성적 생성
for student_id in range(1, 9):  # 학생 ID 1-8
    for subject_id in range(1, 7):  # 과목 ID 1-6
        if random.choice([True, True, False]):  # 70% 확률로 성적 있음
            score = random.randint(60, 100)
            semester = random.choice(["2023-1", "2023-2"])
            insert_grade(student_id, subject_id, score, semester)

print("=" * 30)

# 2. READ - 데이터 조회
print("2️⃣ READ - 데이터 조회")

def print_query_results(sql, description):
    """쿼리 결과를 예쁘게 출력하는 함수"""
    try:
        print(f"🔍 {description}")
        print(f"   SQL: {sql}")
        
        cursor.execute(sql)
        results = cursor.fetchall()
        
        if results:
            # 컬럼 이름 가져오기
            column_names = [description[0] for description in cursor.description]
            
            # 헤더 출력
            header = " | ".join(f"{name:12s}" for name in column_names)
            print(f"   {header}")
            print(f"   {'-' * len(header)}")
            
            # 데이터 출력
            for row in results:
                row_str = " | ".join(f"{str(item):12s}" for item in row)
                print(f"   {row_str}")
            
            print(f"   📊 총 {len(results)}개 행 조회됨\n")
        else:
            print("   결과: 데이터 없음\n")
            
    except sqlite3.Error as e:
        print(f"   ❌ 조회 실패: {e}\n")

# 기본 조회 쿼리들
print_query_results(
    "SELECT * FROM students",
    "모든 학생 정보 조회"
)

print_query_results(
    "SELECT name, age, grade FROM students WHERE grade LIKE 'A%'",
    "A 등급 학생들 조회"
)

print_query_results(
    "SELECT * FROM subjects ORDER BY credits DESC",
    "과목들을 학점 순으로 정렬"
)

print_query_results(
    "SELECT COUNT(*) as student_count FROM students",
    "전체 학생 수"
)

print_query_results(
    """
    SELECT AVG(age) as average_age, MIN(age) as min_age, MAX(age) as max_age 
    FROM students
    """,
    "학생 나이 통계"
)

# JOIN 쿼리 - 학생과 성적 정보 함께 조회
print_query_results(
    """
    SELECT s.name, sub.subject_name, g.score, g.semester
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects sub ON g.subject_id = sub.id
    WHERE g.score >= 90
    ORDER BY g.score DESC
    """,
    "90점 이상 고득점자 목록 (과목별)"
)

# 그룹화 쿼리
print_query_results(
    """
    SELECT s.name, AVG(g.score) as avg_score, COUNT(g.score) as subject_count
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.name
    HAVING AVG(g.score) >= 80
    ORDER BY avg_score DESC
    """,
    "평균 80점 이상 학생들의 성적 현황"
)

print("=" * 30)

# 3. UPDATE - 데이터 수정
print("3️⃣ UPDATE - 데이터 수정")

def update_student_info(student_id, **kwargs):
    """학생 정보 수정 함수"""
    try:
        # 수정할 필드들 구성
        set_clauses = []
        values = []
        
        for field, value in kwargs.items():
            if field in ['name', 'age', 'grade', 'email']:
                set_clauses.append(f"{field} = ?")
                values.append(value)
        
        if not set_clauses:
            print("❌ 수정할 필드가 없습니다.")
            return False
        
        # SQL 쿼리 구성
        sql = f"UPDATE students SET {', '.join(set_clauses)} WHERE id = ?"
        values.append(student_id)
        
        cursor.execute(sql, values)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ 학생 ID {student_id} 정보 수정 완료 ({cursor.rowcount}개 행 수정)")
            return True
        else:
            print(f"❌ 학생 ID {student_id}를 찾을 수 없습니다.")
            return False
            
    except sqlite3.Error as e:
        print(f"❌ 수정 실패: {e}")
        return False

def update_grade(student_id, subject_id, new_score, semester=None):
    """성적 수정 함수"""
    try:
        if semester:
            sql = """
            UPDATE grades 
            SET score = ? 
            WHERE student_id = ? AND subject_id = ? AND semester = ?
            """
            cursor.execute(sql, (new_score, student_id, subject_id, semester))
        else:
            sql = """
            UPDATE grades 
            SET score = ? 
            WHERE student_id = ? AND subject_id = ?
            """
            cursor.execute(sql, (new_score, student_id, subject_id))
        
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ 성적 수정 완료: 학생ID {student_id}, 과목ID {subject_id} → {new_score}점")
            return True
        else:
            print(f"❌ 해당 성적 레코드를 찾을 수 없습니다.")
            return False
            
    except sqlite3.Error as e:
        print(f"❌ 성적 수정 실패: {e}")
        return False

# 수정 작업 실습
print("📝 학생 정보 수정 실습:")

# 특정 학생의 나이와 등급 수정
update_student_info(1, age=21, grade="A+")
update_student_info(2, email="lee_new@school.com")

# 존재하지 않는 학생 수정 시도
update_student_info(999, name="존재안함")

print("\n📊 성적 수정 실습:")

# 특정 성적 수정
update_grade(1, 1, 95, "2023-1")
update_grade(2, 2, 88)

# 대량 수정 - 모든 F등급을 D등급으로 변경
print("\n📈 대량 수정 - 낮은 점수 보정:")
try:
    sql = "UPDATE grades SET score = score + 5 WHERE score < 70"
    cursor.execute(sql)
    conn.commit()
    print(f"✅ {cursor.rowcount}개의 성적이 5점씩 상향 조정되었습니다.")
except sqlite3.Error as e:
    print(f"❌ 대량 수정 실패: {e}")

print("=" * 30)

# 4. DELETE - 데이터 삭제
print("4️⃣ DELETE - 데이터 삭제")

def delete_student(student_id):
    """학생 데이터 삭제 (성적도 함께 삭제)"""
    try:
        # 먼저 해당 학생의 성적 삭제
        cursor.execute("DELETE FROM grades WHERE student_id = ?", (student_id,))
        grades_deleted = cursor.rowcount
        
        # 학생 정보 삭제
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        student_deleted = cursor.rowcount
        
        conn.commit()
        
        if student_deleted > 0:
            print(f"✅ 학생 ID {student_id} 삭제 완료 (성적 {grades_deleted}개도 함께 삭제)")
            return True
        else:
            print(f"❌ 학생 ID {student_id}를 찾을 수 없습니다.")
            return False
            
    except sqlite3.Error as e:
        print(f"❌ 삭제 실패: {e}")
        return False

def delete_low_scores(min_score):
    """특정 점수 미만의 성적 데이터 삭제"""
    try:
        sql = "DELETE FROM grades WHERE score < ?"
        cursor.execute(sql, (min_score,))
        conn.commit()
        
        print(f"✅ {min_score}점 미만 성적 {cursor.rowcount}개 삭제 완료")
        return cursor.rowcount
        
    except sqlite3.Error as e:
        print(f"❌ 성적 삭제 실패: {e}")
        return 0

# 삭제 작업 실습
print("🗑️ 데이터 삭제 실습:")

# 현재 데이터 상태 확인
print_query_results("SELECT COUNT(*) FROM students", "삭제 전 학생 수")
print_query_results("SELECT COUNT(*) FROM grades", "삭제 전 성적 레코드 수")

# 특정 학생 삭제
delete_student(8)  # 마지막 학생 삭제

# 낮은 점수 삭제
delete_low_scores(65)

# 삭제 후 상태 확인
print_query_results("SELECT COUNT(*) FROM students", "삭제 후 학생 수")
print_query_results("SELECT COUNT(*) FROM grades", "삭제 후 성적 레코드 수")

# 조건부 삭제 - 성적이 없는 학생 찾기
print_query_results(
    """
    SELECT s.id, s.name 
    FROM students s 
    LEFT JOIN grades g ON s.id = g.student_id 
    WHERE g.student_id IS NULL
    """,
    "성적이 없는 학생 찾기"
)

print("=" * 30)

# 5. 고급 쿼리와 트랜잭션
print("5️⃣ 고급 쿼리와 트랜잭션")

def safe_transfer_student(old_email, new_email):
    """트랜잭션을 사용한 안전한 이메일 변경"""
    try:
        # 트랜잭션 시작
        cursor.execute("BEGIN TRANSACTION")
        
        # 기존 이메일 확인
        cursor.execute("SELECT id, name FROM students WHERE email = ?", (old_email,))
        student = cursor.fetchone()
        
        if not student:
            raise Exception(f"이메일 '{old_email}'을 가진 학생이 없습니다.")
        
        student_id, name = student
        
        # 새 이메일이 이미 사용중인지 확인
        cursor.execute("SELECT id FROM students WHERE email = ?", (new_email,))
        if cursor.fetchone():
            raise Exception(f"이메일 '{new_email}'은 이미 사용중입니다.")
        
        # 이메일 변경
        cursor.execute("UPDATE students SET email = ? WHERE id = ?", (new_email, student_id))
        
        # 트랜잭션 커밋
        conn.commit()
        print(f"✅ {name}님의 이메일이 {old_email} → {new_email}로 변경되었습니다.")
        
    except Exception as e:
        # 오류 발생 시 롤백
        conn.rollback()
        print(f"❌ 이메일 변경 실패: {e}")

# 트랜잭션 실습
print("🔐 트랜잭션 실습:")
safe_transfer_student("kim@school.com", "kim_new@school.com")
safe_transfer_student("nonexistent@school.com", "new@school.com")  # 실패 케이스

print("🎯 Part 2 요약:")
print("✅ INSERT로 데이터 생성")
print("✅ SELECT로 다양한 조건 조회")
print("✅ UPDATE로 데이터 수정")
print("✅ DELETE로 데이터 삭제")
print("✅ JOIN과 GROUP BY 활용")
print("✅ 트랜잭션을 통한 안전한 데이터 처리")
```

---

### Part 3: 실전 데이터베이스 프로그램 (50분)

#### 📱 실습 1: 주소록 관리 시스템

```python
print("📱 실습 1: 주소록 관리 시스템")
print("=" * 20)

import sqlite3
import re
from datetime import datetime

class ContactManager:
    """주소록 관리 클래스"""
    
    def __init__(self, db_name="contacts.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.init_database()
    
    def init_database(self):
        """데이터베이스 초기화"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            # 연락처 테이블 생성
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT,
                address TEXT,
                company TEXT,
                birthday TEXT,
                notes TEXT,
                created_date TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_date TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
            
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("✅ 주소록 데이터베이스 초기화 완료")
            
        except sqlite3.Error as e:
            print(f"❌ 데이터베이스 초기화 실패: {e}")
    
    def validate_phone(self, phone):
        """전화번호 유효성 검사"""
        # 숫자, 하이픈, 공백만 허용
        pattern = r'^[\d\s\-]+$'
        return re.match(pattern, phone) is not None
    
    def validate_email(self, email):
        """이메일 유효성 검사"""
        if not email:  # 이메일은 선택사항
            return True
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def add_contact(self, name, phone, email="", address="", company="", birthday="", notes=""):
        """연락처 추가"""
        try:
            # 입력 유효성 검사
            if not name.strip():
                print("❌ 이름은 필수 항목입니다.")
                return False
            
            if not self.validate_phone(phone):
                print("❌ 올바른 전화번호 형식이 아닙니다.")
                return False
            
            if not self.validate_email(email):
                print("❌ 올바른 이메일 형식이 아닙니다.")
                return False
            
            # 중복 전화번호 검사
            self.cursor.execute("SELECT id FROM contacts WHERE phone = ?", (phone,))
            if self.cursor.fetchone():
                print("❌ 이미 존재하는 전화번호입니다.")
                return False
            
            # 연락처 추가
            sql = """
            INSERT INTO contacts (name, phone, email, address, company, birthday, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            
            self.cursor.execute(sql, (name, phone, email, address, company, birthday, notes))
            self.conn.commit()
            
            contact_id = self.cursor.lastrowid
            print(f"✅ 연락처 추가 완료: {name} (ID: {contact_id})")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 연락처 추가 실패: {e}")
            return False
    
    def search_contacts(self, keyword):
        """연락처 검색"""
        try:
            sql = """
            SELECT * FROM contacts 
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR company LIKE ?
            ORDER BY name
            """
            
            pattern = f"%{keyword}%"
            self.cursor.execute(sql, (pattern, pattern, pattern, pattern))
            results = self.cursor.fetchall()
            
            if results:
                print(f"🔍 '{keyword}' 검색 결과: {len(results)}건")
                self.print_contacts(results)
            else:
                print(f"🔍 '{keyword}'로 검색된 연락처가 없습니다.")
            
            return results
            
        except sqlite3.Error as e:
            print(f"❌ 검색 실패: {e}")
            return []
    
    def get_all_contacts(self):
        """모든 연락처 조회"""
        try:
            self.cursor.execute("SELECT * FROM contacts ORDER BY name")
            results = self.cursor.fetchall()
            
            print(f"📋 전체 연락처: {len(results)}건")
            self.print_contacts(results)
            
            return results
            
        except sqlite3.Error as e:
            print(f"❌ 연락처 조회 실패: {e}")
            return []
    
    def print_contacts(self, contacts):
        """연락처 목록 출력"""
        if not contacts:
            print("표시할 연락처가 없습니다.")
            return
        
        print("-" * 80)
        print(f"{'ID':>3} | {'이름':10s} | {'전화번호':15s} | {'이메일':20s} | {'회사':10s}")
        print("-" * 80)
        
        for contact in contacts:
            id, name, phone, email, address, company, birthday, notes, created, updated = contact
            email_str = email[:18] + ".." if len(email) > 20 else email
            company_str = company[:8] + ".." if len(company) > 10 else company
            
            print(f"{id:>3} | {name:10s} | {phone:15s} | {email_str:20s} | {company_str:10s}")
        
        print("-" * 80)
    
    def get_contact_by_id(self, contact_id):
        """ID로 연락처 상세 조회"""
        try:
            self.cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
            result = self.cursor.fetchone()
            
            if result:
                print(f"📄 연락처 상세 정보 (ID: {contact_id})")
                print("-" * 40)
                
                fields = ['ID', '이름', '전화번호', '이메일', '주소', '회사', '생일', '메모', '생성일', '수정일']
                for i, field in enumerate(fields):
                    value = result[i] if result[i] else "(없음)"
                    print(f"{field:8s}: {value}")
                
                print("-" * 40)
            else:
                print(f"❌ ID {contact_id}에 해당하는 연락처가 없습니다.")
            
            return result
            
        except sqlite3.Error as e:
            print(f"❌ 연락처 조회 실패: {e}")
            return None
    
    def update_contact(self, contact_id, **kwargs):
        """연락처 수정"""
        try:
            # 연락처 존재 확인
            if not self.get_contact_by_id(contact_id):
                return False
            
            # 수정할 필드 구성
            set_clauses = []
            values = []
            
            valid_fields = ['name', 'phone', 'email', 'address', 'company', 'birthday', 'notes']
            
            for field, value in kwargs.items():
                if field in valid_fields:
                    if field == 'phone' and not self.validate_phone(value):
                        print(f"❌ 올바른 전화번호 형식이 아닙니다: {value}")
                        return False
                    
                    if field == 'email' and not self.validate_email(value):
                        print(f"❌ 올바른 이메일 형식이 아닙니다: {value}")
                        return False
                    
                    set_clauses.append(f"{field} = ?")
                    values.append(value)
            
            if not set_clauses:
                print("❌ 수정할 필드가 없습니다.")
                return False
            
            # 수정일 추가
            set_clauses.append("updated_date = CURRENT_TIMESTAMP")
            
            sql = f"UPDATE contacts SET {', '.join(set_clauses)} WHERE id = ?"
            values.append(contact_id)
            
            self.cursor.execute(sql, values)
            self.conn.commit()
            
            print(f"✅ 연락처 ID {contact_id} 수정 완료")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 연락처 수정 실패: {e}")
            return False
    
    def delete_contact(self, contact_id):
        """연락처 삭제"""
        try:
            # 연락처 존재 확인
            contact = self.get_contact_by_id(contact_id)
            if not contact:
                return False
            
            name = contact[1]
            
            # 삭제 확인
            confirm = input(f"정말로 '{name}'님의 연락처를 삭제하시겠습니까? (y/N): ").strip().lower()
            
            if confirm == 'y':
                self.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
                self.conn.commit()
                
                if self.cursor.rowcount > 0:
                    print(f"✅ '{name}'님의 연락처가 삭제되었습니다.")
                    return True
                else:
                    print("❌ 삭제 처리 중 오류가 발생했습니다.")
                    return False
            else:
                print("삭제가 취소되었습니다.")
                return False
                
        except sqlite3.Error as e:
            print(f"❌ 연락처 삭제 실패: {e}")
            return False
    
    def get_birthday_contacts(self, month=None):
        """생일인 연락처 조회"""
        try:
            if month:
                # 특정 달의 생일자
                pattern = f"%-{month:02d}-%"  # YYYY-MM-DD 형식에서 월만 매칭
                sql = "SELECT * FROM contacts WHERE birthday LIKE ? ORDER BY birthday"
                self.cursor.execute(sql, (pattern,))
            else:
                # 모든 생일 정보가 있는 연락처
                sql = "SELECT * FROM contacts WHERE birthday != '' ORDER BY birthday"
                self.cursor.execute(sql)
            
            results = self.cursor.fetchall()
            
            if results:
                month_str = f"{month}월" if month else "전체"
                print(f"🎂 {month_str} 생일인 연락처: {len(results)}건")
                self.print_contacts(results)
            else:
                print("🎂 해당하는 생일 연락처가 없습니다.")
            
            return results
            
        except sqlite3.Error as e:
            print(f"❌ 생일 연락처 조회 실패: {e}")
            return []
    
    def export_to_csv(self, filename="contacts_export.csv"):
        """CSV로 연락처 내보내기"""
        try:
            import csv
            
            self.cursor.execute("SELECT * FROM contacts ORDER BY name")
            contacts = self.cursor.fetchall()
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # 헤더 작성
                headers = ['ID', '이름', '전화번호', '이메일', '주소', '회사', '생일', '메모', '생성일', '수정일']
                writer.writerow(headers)
                
                # 데이터 작성
                for contact in contacts:
                    writer.writerow(contact)
            
            print(f"✅ 연락처 {len(contacts)}건이 '{filename}'으로 내보내기 완료")
            return True
            
        except Exception as e:
            print(f"❌ CSV 내보내기 실패: {e}")
            return False
    
    def close(self):
        """데이터베이스 연결 종료"""
        if self.conn:
            self.conn.close()
            print("✅ 주소록 데이터베이스 연결 종료")

# 주소록 시스템 실습
print("📱 주소록 관리 시스템 실습:")

# 기존 파일 삭제 (새로운 시작)
import os
if os.path.exists("contacts.db"):
    os.remove("contacts.db")
    print("🗑️ 기존 주소록 삭제")

# 주소록 관리자 생성
contacts = ContactManager()

print("\n👥 연락처 추가:")

# 샘플 연락처 추가
sample_contacts = [
    ("김철수", "010-1234-5678", "kim@email.com", "서울시 강남구", "ABC회사", "1990-03-15", "대학 동기"),
    ("이영희", "010-2345-6789", "lee@email.com", "서울시 서초구", "XYZ회사", "1992-07-22", "직장 동료"),
    ("박민수", "010-3456-7890", "park@email.com", "부산시 해운대구", "DEF회사", "1988-12-08", "고등학교 친구"),
    ("최지원", "010-4567-8901", "choi@email.com", "대구시 중구", "GHI회사", "1995-01-30", "동호회 회원"),
    ("정다영", "010-5678-9012", "jung@email.com", "인천시 연수구", "JKL회사", "1991-09-12", "사촌")
]

for name, phone, email, address, company, birthday, notes in sample_contacts:
    contacts.add_contact(name, phone, email, address, company, birthday, notes)

print("\n📋 전체 연락처 목록:")
contacts.get_all_contacts()

print("\n🔍 검색 테스트:")
contacts.search_contacts("김")
contacts.search_contacts("010-1234")
contacts.search_contacts("ABC")

print("\n📄 상세 정보 조회:")
contacts.get_contact_by_id(1)

print("\n✏️ 연락처 수정:")
contacts.update_contact(1, company="새로운 회사", notes="정보 업데이트됨")
contacts.get_contact_by_id(1)

print("\n🎂 생일 조회:")
contacts.get_birthday_contacts(3)  # 3월 생일자

print("\n💾 CSV 내보내기:")
contacts.export_to_csv("my_contacts.csv")

# 연결 종료
contacts.close()

print("=" * 30)
```

#### 📦 실습 2: 간단한 쇼핑몰 재고 관리

```python
print("📦 실습 2: 간단한 쇼핑몰 재고 관리")
print("=" * 22)

class InventoryManager:
    """재고 관리 시스템 클래스"""
    
    def __init__(self, db_name="inventory.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.init_database()
    
    def init_database(self):
        """데이터베이스 초기화"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            # 카테고리 테이블
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT
                )
            """)
            
            # 상품 테이블
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category_id INTEGER,
                    price REAL NOT NULL,
                    cost REAL NOT NULL,
                    stock_quantity INTEGER DEFAULT 0,
                    min_stock INTEGER DEFAULT 10,
                    description TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (category_id) REFERENCES categories (id)
                )
            """)
            
            # 재고 이동 히스토리 테이블
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS stock_movements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    movement_type TEXT CHECK (movement_type IN ('입고', '출고', '조정')),
                    quantity INTEGER,
                    reason TEXT,
                    movement_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            """)
            
            self.conn.commit()
            print("✅ 재고 관리 데이터베이스 초기화 완료")
            
        except sqlite3.Error as e:
            print(f"❌ 데이터베이스 초기화 실패: {e}")
    
    def add_category(self, name, description=""):
        """카테고리 추가"""
        try:
            sql = "INSERT INTO categories (name, description) VALUES (?, ?)"
            self.cursor.execute(sql, (name, description))
            self.conn.commit()
            
            category_id = self.cursor.lastrowid
            print(f"✅ 카테고리 추가 완료: {name} (ID: {category_id})")
            return category_id
            
        except sqlite3.IntegrityError:
            print(f"❌ 카테고리 '{name}'은 이미 존재합니다.")
            return None
        except sqlite3.Error as e:
            print(f"❌ 카테고리 추가 실패: {e}")
            return None
    
    def add_product(self, name, category_id, price, cost, stock_quantity=0, min_stock=10, description=""):
        """상품 추가"""
        try:
            # 카테고리 존재 확인
            self.cursor.execute("SELECT name FROM categories WHERE id = ?", (category_id,))
            category = self.cursor.fetchone()
            
            if not category:
                print(f"❌ 카테고리 ID {category_id}가 존재하지 않습니다.")
                return None
            
            sql = """
            INSERT INTO products (name, category_id, price, cost, stock_quantity, min_stock, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            
            self.cursor.execute(sql, (name, category_id, price, cost, stock_quantity, min_stock, description))
            self.conn.commit()
            
            product_id = self.cursor.lastrowid
            
            # 초기 재고가 0이 아니면 입고 기록 추가
            if stock_quantity > 0:
                self.record_stock_movement(product_id, "입고", stock_quantity, "초기 재고")
            
            print(f"✅ 상품 추가 완료: {name} (ID: {product_id})")
            return product_id
            
        except sqlite3.Error as e:
            print(f"❌ 상품 추가 실패: {e}")
            return None
    
    def record_stock_movement(self, product_id, movement_type, quantity, reason=""):
        """재고 이동 기록"""
        try:
            sql = """
            INSERT INTO stock_movements (product_id, movement_type, quantity, reason)
            VALUES (?, ?, ?, ?)
            """
            
            self.cursor.execute(sql, (product_id, movement_type, quantity, reason))
            self.conn.commit()
            
            return self.cursor.lastrowid
            
        except sqlite3.Error as e:
            print(f"❌ 재고 이동 기록 실패: {e}")
            return None
    
    def stock_in(self, product_id, quantity, reason="입고"):
        """재고 입고"""
        try:
            # 현재 재고 확인
            self.cursor.execute("SELECT name, stock_quantity FROM products WHERE id = ?", (product_id,))
            product = self.cursor.fetchone()
            
            if not product:
                print(f"❌ 상품 ID {product_id}가 존재하지 않습니다.")
                return False
            
            name, current_stock = product
            new_stock = current_stock + quantity
            
            # 재고 업데이트
            self.cursor.execute(
                "UPDATE products SET stock_quantity = ?, updated_date = CURRENT_TIMESTAMP WHERE id = ?",
                (new_stock, product_id)
            )
            
            # 재고 이동 기록
            self.record_stock_movement(product_id, "입고", quantity, reason)
            
            self.conn.commit()
            
            print(f"✅ 입고 완료: {name} ({current_stock} → {new_stock})")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 입고 처리 실패: {e}")
            return False
    
    def stock_out(self, product_id, quantity, reason="출고"):
        """재고 출고"""
        try:
            # 현재 재고 확인
            self.cursor.execute("SELECT name, stock_quantity FROM products WHERE id = ?", (product_id,))
            product = self.cursor.fetchone()
            
            if not product:
                print(f"❌ 상품 ID {product_id}가 존재하지 않습니다.")
                return False
            
            name, current_stock = product
            
            if current_stock < quantity:
                print(f"❌ 재고 부족: {name} (현재: {current_stock}, 요청: {quantity})")
                return False
            
            new_stock = current_stock - quantity
            
            # 재고 업데이트
            self.cursor.execute(
                "UPDATE products SET stock_quantity = ?, updated_date = CURRENT_TIMESTAMP WHERE id = ?",
                (new_stock, product_id)
            )
            
            # 재고 이동 기록
            self.record_stock_movement(product_id, "출고", quantity, reason)
            
            self.conn.commit()
            
            print(f"✅ 출고 완료: {name} ({current_stock} → {new_stock})")
            
            # 최소 재고 경고
            self.cursor.execute("SELECT min_stock FROM products WHERE id = ?", (product_id,))
            min_stock = self.cursor.fetchone()[0]
            
            if new_stock <= min_stock:
                print(f"⚠️ 재고 부족 경고: {name} (현재: {new_stock}, 최소: {min_stock})")
            
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 출고 처리 실패: {e}")
            return False
    
    def get_all_products(self):
        """모든 상품 조회"""
        try:
            sql = """
            SELECT p.id, p.name, c.name as category, p.price, p.cost, 
                   p.stock_quantity, p.min_stock, p.description
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            ORDER BY p.name
            """
            
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            
            if products:
                print(f"📦 전체 상품 목록: {len(products)}개")
                print("-" * 100)
                print(f"{'ID':>3} | {'상품명':15s} | {'카테고리':10s} | {'판매가':>8s} | {'원가':>8s} | {'재고':>6s} | {'최소':>6s}")
                print("-" * 100)
                
                for product in products:
                    pid, name, category, price, cost, stock, min_stock, desc = product
                    category = category if category else "미분류"
                    
                    # 재고 상태에 따른 표시
                    stock_status = ""
                    if stock <= min_stock:
                        stock_status = " ⚠️"
                    elif stock == 0:
                        stock_status = " ❌"
                    
                    print(f"{pid:>3} | {name:15s} | {category:10s} | {price:>8,.0f} | {cost:>8,.0f} | {stock:>6d} | {min_stock:>6d}{stock_status}")
                
                print("-" * 100)
            else:
                print("상품이 없습니다.")
            
            return products
            
        except sqlite3.Error as e:
            print(f"❌ 상품 조회 실패: {e}")
            return []
    
    def get_low_stock_products(self):
        """재고 부족 상품 조회"""
        try:
            sql = """
            SELECT p.id, p.name, c.name as category, p.stock_quantity, p.min_stock
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.stock_quantity <= p.min_stock
            ORDER BY (p.stock_quantity - p.min_stock), p.name
            """
            
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            
            if products:
                print(f"⚠️ 재고 부족 상품: {len(products)}개")
                print("-" * 60)
                print(f"{'ID':>3} | {'상품명':20s} | {'카테고리':10s} | {'현재':>6s} | {'최소':>6s}")
                print("-" * 60)
                
                for product in products:
                    pid, name, category, stock, min_stock = product
                    category = category if category else "미분류"
                    
                    status = "품절" if stock == 0 else "부족"
                    print(f"{pid:>3} | {name:20s} | {category:10s} | {stock:>6d} | {min_stock:>6d} ({status})")
                
                print("-" * 60)
            else:
                print("✅ 재고가 충분한 상태입니다.")
            
            return products
            
        except sqlite3.Error as e:
            print(f"❌ 재고 부족 상품 조회 실패: {e}")
            return []
    
    def get_stock_movements(self, product_id=None, limit=20):
        """재고 이동 히스토리 조회"""
        try:
            if product_id:
                sql = """
                SELECT sm.id, p.name, sm.movement_type, sm.quantity, sm.reason, sm.movement_date
                FROM stock_movements sm
                JOIN products p ON sm.product_id = p.id
                WHERE sm.product_id = ?
                ORDER BY sm.movement_date DESC
                LIMIT ?
                """
                self.cursor.execute(sql, (product_id, limit))
            else:
                sql = """
                SELECT sm.id, p.name, sm.movement_type, sm.quantity, sm.reason, sm.movement_date
                FROM stock_movements sm
                JOIN products p ON sm.product_id = p.id
                ORDER BY sm.movement_date DESC
                LIMIT ?
                """
                self.cursor.execute(sql, (limit,))
            
            movements = self.cursor.fetchall()
            
            if movements:
                title = f"특정 상품 재고 이동" if product_id else f"전체 재고 이동"
                print(f"📊 {title} 히스토리: {len(movements)}건")
                print("-" * 80)
                print(f"{'ID':>3} | {'상품명':15s} | {'구분':6s} | {'수량':>6s} | {'사유':15s} | {'일시':16s}")
                print("-" * 80)
                
                for movement in movements:
                    mid, name, mtype, quantity, reason, mdate = movement
                    mdate_short = mdate[:16] if mdate else ""
                    reason = reason[:13] + ".." if len(reason) > 15 else reason
                    
                    print(f"{mid:>3} | {name:15s} | {mtype:6s} | {quantity:>6d} | {reason:15s} | {mdate_short}")
                
                print("-" * 80)
            else:
                print("재고 이동 기록이 없습니다.")
            
            return movements
            
        except sqlite3.Error as e:
            print(f"❌ 재고 이동 히스토리 조회 실패: {e}")
            return []
    
    def get_inventory_report(self):
        """재고 현황 리포트"""
        try:
            # 전체 통계
            self.cursor.execute("SELECT COUNT(*), SUM(stock_quantity * cost) FROM products")
            total_products, total_value = self.cursor.fetchone()
            total_value = total_value if total_value else 0
            
            # 카테고리별 통계
            self.cursor.execute("""
                SELECT c.name, COUNT(p.id), SUM(p.stock_quantity