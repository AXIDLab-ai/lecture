
**[← Week 10](./week10.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 12 →](./week12.md)**

Week 11: 파일 입출력

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **파일 기본 조작**: 파일을 열고, 읽고, 쓰고, 닫는 기본 작업을 자유자재로 다룹니다
2. **다양한 파일 모드**: 읽기, 쓰기, 추가 모드를 상황에 맞게 선택하여 사용합니다
3. **with문 활용**: 안전한 파일 처리를 위해 with문을 사용합니다
4. **예외 처리**: 파일 처리 과정에서 발생할 수 있는 오류를 적절히 처리합니다
5. **구조화된 데이터**: CSV와 JSON 형식의 파일을 읽고 쓸 수 있습니다
6. **실용적 프로그램**: 일기장, 학생 관리 시스템 등 실생활에서 사용할 수 있는 프로그램을 제작합니다

---

## 📚 핵심 개념 요약

### 1. 파일 입출력 기초

| 개념 | 설명 | 예시 |
|------|------|------|
| **파일 열기** | open() 함수로 파일 접근 | `open('file.txt', 'r')` |
| **파일 닫기** | close() 메서드로 리소스 해제 | `file.close()` |
| **with문** | 자동으로 파일을 닫아주는 구문 | `with open('file.txt') as f:` |
| **파일 경로** | 절대경로 vs 상대경로 | `C:\data\file.txt` vs `./data/file.txt` |

### 2. 파일 모드

| 모드 | 설명 | 기능 | 파일 없을 때 |
|------|------|------|-------------|
| **'r'** | 읽기 전용 | 파일 내용 읽기 | 오류 발생 |
| **'w'** | 쓰기 전용 | 새로 쓰기 (덮어쓰기) | 새 파일 생성 |
| **'a'** | 추가 모드 | 파일 끝에 내용 추가 | 새 파일 생성 |
| **'x'** | 배타 생성 | 새 파일만 생성 | 새 파일 생성 |
| **'r+'** | 읽기+쓰기 | 읽고 쓰기 모두 | 오류 발생 |
| **'w+'** | 쓰기+읽기 | 덮어쓰고 읽기 | 새 파일 생성 |
| **'a+'** | 추가+읽기 | 추가하고 읽기 | 새 파일 생성 |

### 3. 파일 읽기 메서드

| 메서드 | 반환값 | 특징 | 사용 시기 |
|--------|--------|------|---------|
| **read()** | 전체 문자열 | 파일 전체를 한 번에 | 작은 파일 |
| **readline()** | 한 줄 문자열 | 한 줄씩 순차적으로 | 줄 단위 처리 |
| **readlines()** | 줄들의 리스트 | 모든 줄을 리스트로 | 줄별 작업 |

### 4. 파일 쓰기 메서드

| 메서드 | 매개변수 | 기능 | 줄바꿈 |
|--------|----------|------|--------|
| **write()** | 문자열 | 문자열 쓰기 | 자동 추가 안됨 |
| **writelines()** | 문자열 리스트 | 여러 줄 쓰기 | 자동 추가 안됨 |
| **print()** | 다양한 값 | 값 출력 | 자동 추가됨 |

### 5. 예외 처리

| 예외 | 발생 상황 | 해결 방법 |
|------|-----------|-----------|
| **FileNotFoundError** | 파일이 존재하지 않음 | 파일 존재 확인 |
| **PermissionError** | 접근 권한 없음 | 권한 확인 |
| **IsADirectoryError** | 디렉토리를 파일로 열려고 함 | 경로 확인 |
| **UnicodeDecodeError** | 인코딩 문제 | encoding 지정 |

---

## 💻 실습 세션 (2시간)

### Part 1: 텍스트 파일 기초 (30분)

#### 📝 파일 열기와 닫기

```python
print("📝 파일 열기와 닫기")
print("=" * 15)

import os

# 1. 기본적인 파일 열기/닫기
print("📄 기본 파일 열기/닫기")

def basic_file_operations():
    """기본적인 파일 조작"""
    
    # 파일 생성 및 쓰기
    print("1. 파일 쓰기 (기본 방법)")
    
    # 방법 1: 전통적인 방법
    file = open('example.txt', 'w', encoding='utf-8')
    file.write("안녕하세요! 첫 번째 파일입니다.\n")
    file.write("파이썬으로 파일을 만들었어요.\n")
    file.close()  # 반드시 닫아야 함!
    
    print("✅ example.txt 파일 생성 완료")
    
    # 파일 읽기
    print("\n2. 파일 읽기 (기본 방법)")
    
    file = open('example.txt', 'r', encoding='utf-8')
    content = file.read()
    print("파일 내용:")
    print(content)
    file.close()  # 반드시 닫아야 함!
    
    # 방법 2: with문 사용 (권장!)
    print("\n3. with문을 사용한 안전한 파일 처리")
    
    with open('example_with.txt', 'w', encoding='utf-8') as file:
        file.write("with문을 사용하면 자동으로 파일이 닫힙니다.\n")
        file.write("더 안전하고 깔끔한 코드를 만들 수 있어요.\n")
        file.write("예외가 발생해도 자동으로 파일이 닫힙니다.\n")
    
    print("✅ example_with.txt 파일 생성 완료 (with문 사용)")
    
    # with문으로 읽기
    with open('example_with.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("파일 내용:")
        print(content)
    
    print("💡 with문의 장점:")
    print("   - 자동으로 파일을 닫아줌")
    print("   - 예외 발생시에도 안전하게 파일 닫기")
    print("   - 코드가 더 깔끔함")

# 기본 파일 조작 실행
basic_file_operations()

print("=" * 30)

# 2. 다양한 파일 읽기 방법
print("📖 다양한 파일 읽기 방법")

def file_reading_methods():
    """파일 읽기의 다양한 방법들"""
    
    # 샘플 파일 생성
    sample_content = """첫 번째 줄입니다.
두 번째 줄입니다.
세 번째 줄입니다.
네 번째 줄입니다.
다섯 번째 줄입니다."""
    
    with open('sample_lines.txt', 'w', encoding='utf-8') as file:
        file.write(sample_content)
    
    print("📝 샘플 파일 내용:")
    print(sample_content)
    print()
    
    # 방법 1: read() - 전체 내용 읽기
    print("1️⃣ read() - 전체 내용을 한 번에")
    with open('sample_lines.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"read() 결과: '{content}'")
        print(f"타입: {type(content)}")
    
    print()
    
    # 방법 2: readline() - 한 줄씩 읽기
    print("2️⃣ readline() - 한 줄씩 읽기")
    with open('sample_lines.txt', 'r', encoding='utf-8') as file:
        line_count = 0
        while True:
            line = file.readline()
            if not line:  # 파일 끝에 도달
                break
            line_count += 1
            print(f"줄 {line_count}: '{line.strip()}'")  # strip()으로 줄바꿈 제거
    
    print()
    
    # 방법 3: readlines() - 모든 줄을 리스트로
    print("3️⃣ readlines() - 모든 줄을 리스트로")
    with open('sample_lines.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"readlines() 결과: {lines}")
        print(f"타입: {type(lines)}")
        print(f"줄 수: {len(lines)}")
        
        print("각 줄 처리:")
        for i, line in enumerate(lines, 1):
            print(f"  줄 {i}: '{line.strip()}'")
    
    print()
    
    # 방법 4: for문으로 직접 순회 (메모리 효율적)
    print("4️⃣ for문으로 파일 직접 순회 (권장)")
    with open('sample_lines.txt', 'r', encoding='utf-8') as file:
        print("for문 순회 결과:")
        for line_num, line in enumerate(file, 1):
            print(f"  줄 {line_num}: '{line.strip()}'")
    
    print()
    print("📊 각 방법의 특징:")
    print("read()      : 작은 파일, 전체 내용 필요시")
    print("readline()  : 큰 파일, 조건부 읽기")
    print("readlines() : 중간 크기, 줄별 처리")
    print("for 순회    : 큰 파일, 메모리 효율적 (가장 권장)")

# 파일 읽기 방법들 실행
file_reading_methods()

print("=" * 30)

# 3. 다양한 파일 쓰기 방법
print("✏️ 다양한 파일 쓰기 방법")

def file_writing_methods():
    """파일 쓰기의 다양한 방법들"""
    
    # 방법 1: write() - 문자열 쓰기
    print("1️⃣ write() - 문자열 쓰기")
    with open('write_example.txt', 'w', encoding='utf-8') as file:
        file.write("첫 번째 문장입니다.")
        file.write("두 번째 문장입니다.")  # 자동으로 줄바꿈이 되지 않음!
        file.write("\n세 번째 문장입니다.\n")  # 명시적으로 \n 추가
    
    # 결과 확인
    with open('write_example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"write() 결과:\n{repr(content)}")  # repr로 특수문자 확인
    
    print()
    
    # 방법 2: writelines() - 문자열 리스트 쓰기
    print("2️⃣ writelines() - 문자열 리스트 쓰기")
    
    lines_to_write = [
        "첫 번째 줄\n",
        "두 번째 줄\n",
        "세 번째 줄\n"
    ]
    
    with open('writelines_example.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines_to_write)
    
    # 결과 확인
    with open('writelines_example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"writelines() 결과:\n{content}")
    
    print()
    
    # 방법 3: print() 함수로 파일에 쓰기
    print("3️⃣ print() 함수로 파일에 쓰기")
    
    with open('print_example.txt', 'w', encoding='utf-8') as file:
        print("print 함수로 쓰는 첫 번째 줄", file=file)
        print("print 함수로 쓰는 두 번째 줄", file=file)
        print("숫자도 쓸 수 있어요:", 12345, file=file)
        print("여러", "값을", "한번에", file=file)
        print()  # 일반 출력 (화면)
        print("파일에는 안 들어감")
    
    # 결과 확인
    with open('print_example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"print() 결과:\n{content}")
    
    # 방법 4: 포맷팅과 함께 쓰기
    print("4️⃣ 포맷팅과 함께 쓰기")
    
    students = [
        {"name": "김철수", "score": 85},
        {"name": "이영희", "score": 92},
        {"name": "박민수", "score": 78}
    ]
    
    with open('formatted_example.txt', 'w', encoding='utf-8') as file:
        file.write("=== 학생 성적 리스트 ===\n")
        for student in students:
            # 문자열 포맷팅 사용
            line = f"이름: {student['name']:6s} | 점수: {student['score']:3d}점\n"
            file.write(line)
        
        file.write("-" * 25 + "\n")
        
        # 평균 계산
        avg_score = sum(s['score'] for s in students) / len(students)
        file.write(f"평균 점수: {avg_score:.1f}점\n")
    
    # 결과 확인
    with open('formatted_example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("포맷팅 결과:")
        print(content)
    
    print("💡 쓰기 방법 선택 가이드:")
    print("write()      : 정확한 제어가 필요할 때")
    print("writelines() : 미리 준비된 줄들을 쓸 때")
    print("print()      : 간단하고 편리하게")
    print("포맷팅       : 구조화된 데이터를 쓸 때")

# 파일 쓰기 방법들 실행
file_writing_methods()

print("=" * 30)

# 4. 파일 모드 실습
print("🔧 파일 모드 실습")

def file_modes_practice():
    """다양한 파일 모드 실습"""
    
    print("📝 파일 모드별 동작 확인")
    
    # 기본 파일 생성
    original_content = "원본 내용 첫 번째 줄\n원본 내용 두 번째 줄\n원본 내용 세 번째 줄\n"
    
    with open('mode_test.txt', 'w', encoding='utf-8') as file:
        file.write(original_content)
    
    print("📄 원본 파일 생성:")
    print(original_content)
    
    # 모드별 테스트
    modes_to_test = [
        ('r', '읽기 전용'),
        ('w', '쓰기 전용 (덮어쓰기)'),
        ('a', '추가 모드'),
        ('r+', '읽기+쓰기'),
        ('w+', '쓰기+읽기 (덮어쓰기)'),
        ('a+', '추가+읽기')
    ]
    
    for mode, description in modes_to_test:
        print(f"\n🔧 모드 '{mode}' ({description}) 테스트:")
        
        try:
            if mode == 'r':
                # 읽기 전용
                with open('mode_test.txt', mode, encoding='utf-8') as file:
                    content = file.read()
                    print(f"   읽은 내용 (처음 50자): {content[:50]}")
            
            elif mode == 'w':
                # 덮어쓰기 (원본 파일 백업)
                with open('mode_test_backup.txt', 'w', encoding='utf-8') as backup:
                    backup.write(original_content)
                
                with open('mode_test.txt', mode, encoding='utf-8') as file:
                    file.write("새로운 내용으로 덮어썼습니다!\n")
                
                # 결과 확인
                with open('mode_test.txt', 'r', encoding='utf-8') as file:
                    new_content = file.read()
                    print(f"   새 내용: {new_content.strip()}")
                
                # 원본 복구
                with open('mode_test_backup.txt', 'r', encoding='utf-8') as backup:
                    backup_content = backup.read()
                with open('mode_test.txt', 'w', encoding='utf-8') as file:
                    file.write(backup_content)
            
            elif mode == 'a':
                # 추가 모드
                with open('mode_test.txt', mode, encoding='utf-8') as file:
                    file.write("추가된 내용입니다.\n")
                
                # 결과 확인
                with open('mode_test.txt', 'r', encoding='utf-8') as file:
                    content = file.read()
                    lines = content.strip().split('\n')
                    print(f"   총 줄 수: {len(lines)}")
                    print(f"   마지막 줄: {lines[-1]}")
                
                # 추가된 내용 제거 (원본 복구)
                with open('mode_test.txt', 'w', encoding='utf-8') as file:
                    file.write(original_content)
            
            elif mode in ['r+', 'w+', 'a+']:
                # 복합 모드
                if mode == 'w+':
                    # w+ 모드는 파일을 비우므로 주의
                    with open('mode_test.txt', mode, encoding='utf-8') as file:
                        file.write("w+ 모드 테스트\n")
                        file.seek(0)  # 파일 처음으로 이동
                        content = file.read()
                        print(f"   {mode} 모드 내용: {content.strip()}")
                    
                    # 원본 복구
                    with open('mode_test.txt', 'w', encoding='utf-8') as file:
                        file.write(original_content)
                
                else:
                    with open('mode_test.txt', mode, encoding='utf-8') as file:
                        if mode == 'r+':
                            # 처음부터 읽기
                            content = file.read()
                            print(f"   읽은 내용 (처음 30자): {content[:30]}")
                            
                            # 파일 끝에 내용 추가
                            file.write("r+ 모드로 추가한 내용\n")
                        
                        elif mode == 'a+':
                            # 끝에 내용 추가
                            file.write("a+ 모드로 추가한 내용\n")
                            
                            # 처음으로 돌아가서 읽기
                            file.seek(0)
                            content = file.read()
                            lines = content.strip().split('\n')
                            print(f"   총 줄 수: {len(lines)}")
                    
                    # 원본 복구
                    with open('mode_test.txt', 'w', encoding='utf-8') as file:
                        file.write(original_content)
        
        except Exception as e:
            print(f"   ❌ 오류 발생: {e}")
    
    # 정리
    for filename in ['mode_test.txt', 'mode_test_backup.txt']:
        try:
            os.remove(filename)
        except:
            pass
    
    print("\n📋 파일 모드 정리:")
    print("r   : 읽기만, 파일 없으면 오류")
    print("w   : 쓰기만, 기존 내용 삭제")
    print("a   : 추가만, 파일 끝에 내용 추가")
    print("r+  : 읽기+쓰기, 파일 없으면 오류")
    print("w+  : 쓰기+읽기, 기존 내용 삭제")
    print("a+  : 추가+읽기, 파일 끝에 내용 추가")

# 파일 모드 실습 실행
file_modes_practice()

print("=" * 30)

# 5. 실습 종합 - 간단한 메모장
print("📝 실습 종합 - 간단한 메모장")

def simple_notepad():
    """간단한 메모장 프로그램"""
    
    memo_file = "my_memo.txt"
    
    def show_menu():
        print("\n" + "="*30)
        print("📝 간단한 메모장 프로그램")
        print("="*30)
        print("1. 메모 작성")
        print("2. 메모 읽기")
        print("3. 메모 목록 보기")
        print("4. 메모 추가")
        print("5. 메모 지우기")
        print("6. 종료")
        print("-"*30)
    
    def write_memo():
        """새 메모 작성"""
        print("\n📝 새 메모 작성")
        memo = input("메모 내용을 입력하세요 (여러 줄은 Enter로 구분): ")
        
        with open(memo_file, 'w', encoding='utf-8') as file:
            file.write(memo + "\n")
        
        print("✅ 메모가 저장되었습니다!")
    
    def read_memo():
        """메모 읽기"""
        print("\n📖 메모 읽기")
        try:
            with open(memo_file, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if content:
                    print("📄 저장된 메모:")
                    print("-" * 20)
                    print(content)
                    print("-" * 20)
                else:
                    print("📭 저장된 메모가 없습니다.")
        except FileNotFoundError:
            print("📭 아직 작성된 메모가 없습니다.")
    
    def list_memos():
        """메모 줄별 목록"""
        print("\n📋 메모 목록")
        try:
            with open(memo_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    print("📄 메모 줄 목록:")
                    for i, line in enumerate(lines, 1):
                        print(f"{i:2d}. {line.strip()}")
                else:
                    print("📭 저장된 메모가 없습니다.")
        except FileNotFoundError:
            print("📭 아직 작성된 메모가 없습니다.")
    
    def append_memo():
        """메모 추가"""
        print("\n➕ 메모 추가")
        
        # 기존 메모 확인
        try:
            with open(memo_file, 'r', encoding='utf-8') as file:
                existing = file.read().strip()
                if existing:
                    print("📄 기존 메모:")
                    print(existing)
                    print("-" * 20)
        except FileNotFoundError:
            print("📭 기존 메모가 없습니다. 새로 작성합니다.")
        
        new_memo = input("추가할 메모 내용: ")
        
        with open(memo_file, 'a', encoding='utf-8') as file:
            file.write(new_memo + "\n")
        
        print("✅ 메모가 추가되었습니다!")
    
    def clear_memo():
        """메모 지우기"""
        print("\n🗑️ 메모 지우기")
        
        try:
            with open(memo_file, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if content:
                    print("📄 현재 메모:")
                    print(content)
                    print("-" * 20)
                    
                    confirm = input("정말로 모든 메모를 지우시겠습니까? (y/n): ")
                    if confirm.lower() in ['y', 'yes', '예']:
                        os.remove(memo_file)
                        print("🗑️ 모든 메모가 삭제되었습니다.")
                    else:
                        print("❌ 취소되었습니다.")
                else:
                    print("📭 지울 메모가 없습니다.")
        except FileNotFoundError:
            print("📭 지울 메모가 없습니다.")
    
    # 메인 루프
    print("🎉 간단한 메모장 프로그램에 오신 것을 환영합니다!")
    
    while True:
        show_menu()
        
        try:
            choice = input("선택하세요 (1-6): ").strip()
            
            if choice == '1':
                write_memo()
            elif choice == '2':
                read_memo()
            elif choice == '3':
                list_memos()
            elif choice == '4':
                append_memo()
            elif choice == '5':
                clear_memo()
            elif choice == '6':
                print("👋 메모장 프로그램을 종료합니다.")
                break
            else:
                print("❌ 잘못된 선택입니다. 1-6 사이의 숫자를 입력하세요.")
        
        except KeyboardInterrupt:
            print("\n👋 프로그램이 중단되었습니다.")
            break
        except Exception as e:
            print(f"❌ 오류가 발생했습니다: {e}")

# 메모장 프로그램 실행 (주석 해제하여 테스트)
# simple_notepad()

print("=" * 30)

print("🎯 Part 1 요약:")
print("✅ 파일 열기/닫기 (open, close, with)")
print("✅ 파일 읽기 (read, readline, readlines)")
print("✅ 파일 쓰기 (write, writelines, print)")
print("✅ 파일 모드 (r, w, a, r+, w+, a+)")
print("✅ 간단한 메모장 프로그램 완성")
```

---

### Part 2: 파일 처리 실습 (40분)

#### 🛠️ 고급 파일 처리 기법

```python
print("🛠️ 고급 파일 처리 기법")
print("=" * 18)

import os
import shutil
from datetime import datetime
import glob

# 1. 파일 존재 확인 및 경로 처리
print("📁 파일 존재 확인 및 경로 처리")

def file_path_operations():
    """파일 경로와 존재 확인 실습"""
    
    print("1️⃣ 파일 및 디렉토리 존재 확인")
    
    # 테스트할 경로들
    test_paths = [
        "existing_file.txt",
        "nonexistent_file.txt",
        "test_directory",
        "C:\\Windows\\System32",  # 윈도우 시스템 디렉토리
        "."  # 현재 디렉토리
    ]
    
    # 테스트 파일과 디렉토리 생성
    with open("existing_file.txt", "w") as f:
        f.write("이 파일은 존재합니다.")
    
    os.makedirs("test_directory", exist_ok=True)
    
    print("📋 경로 존재 확인 결과:")
    for path in test_paths:
        exists = os.path.exists(path)
        is_file = os.path.isfile(path)
        is_dir = os.path.isdir(path)
        
        print(f"  {path:25s} | 존재: {exists} | 파일: {is_file} | 디렉토리: {is_dir}")
    
    print("\n2️⃣ 파일 정보 조회")
    
    def get_file_info(filepath):
        """파일 정보를 자세히 조회"""
        if not os.path.exists(filepath):
            return f"❌ {filepath} 파일이 존재하지 않습니다."
        
        stat = os.stat(filepath)
        size = stat.st_size
        created = datetime.fromtimestamp(stat.st_ctime)
        modified = datetime.fromtimestamp(stat.st_mtime)
        
        return f"""📄 {filepath} 정보:
    - 크기: {size} bytes
    - 생성일: {created.strftime('%Y-%m-%d %H:%M:%S')}
    - 수정일: {modified.strftime('%Y-%m-%d %H:%M:%S')}"""
    
    print(get_file_info("existing_file.txt"))
    
    print("\n3️⃣ 절대경로와 상대경로")
    
    current_dir = os.getcwd()
    abs_path = os.path.abspath("existing_file.txt")
    rel_path = os.path.relpath(abs_path)
    
    print(f"현재 디렉토리: {current_dir}")
    print(f"절대 경로: {abs_path}")
    print(f"상대 경로: {rel_path}")
    
    print("\n4️⃣ 경로 분리 및 조합")
    
    sample_path = r"C:\Users\Username\Documents\myfile.txt"
    
    dirname = os.path.dirname(sample_path)  # 디렉토리 부분
    basename = os.path.basename(sample_path)  # 파일명 부분
    name, ext = os.path.splitext(basename)  # 파일명과 확장자 분리
    
    print(f"전체 경로: {sample_path}")
    print(f"디렉토리: {dirname}")
    print(f"파일명: {basename}")
    print(f"이름: {name}")
    print(f"확장자: {ext}")
    
    # 경로 조합
    new_path = os.path.join("data", "files", "output.txt")
    print(f"조합된 경로: {new_path}")
    
    print("\n5️⃣ 파일 패턴 매칭")
    
    # 테스트 파일들 생성
    test_files = ["data1.txt", "data2.txt", "info.csv", "backup.bak", "image.jpg"]
    for filename in test_files:
        with open(filename, "w") as f:
            f.write("test")
    
    print("생성된 테스트 파일들:")
    for file in test_files:
        print(f"  {file}")
    
    # glob을 사용한 패턴 매칭
    patterns = ["*.txt", "data*.txt", "*.csv", "*.*"]
    
    print("\n패턴 매칭 결과:")
    for pattern in patterns:
        matches = glob.glob(pattern)
        print(f"  패턴 '{pattern}': {matches}")
    
    # 정리
    for file in test_files + ["existing_file.txt"]:
        try:
            os.remove(file)
        except:
            pass
    
    try:
        os.rmdir("test_directory")
    except:
        pass

# 파일 경로 조작 실행
file_path_operations()

print("=" * 30)

# 2. 예외 처리 실습
print("🚨 예외 처리 실습")

def exception_handling_practice():
    """파일 처리 시 예외 처리 실습"""
    
    print("1️⃣ 다양한 파일 예외 상황 처리")
    
    test_cases = [
        ("nonexistent.txt", "r"),  # 파일 없음
        (".", "r"),                # 디렉토리를 파일로 열기
        ("test_readonly.txt", "w") # 읽기 전용 파일에 쓰기
    ]
    
    # 읽기 전용 테스트 파일 생성 (윈도우에서)
    try:
        with open("test_readonly.txt", "w") as f:
            f.write("읽기 전용 파일")
        os.chmod("test_readonly.txt", 0o444)  # 읽기 전용으로 설정
    except:
        pass
    
    for filepath, mode in test_cases:
        print(f"\n📝 테스트: {filepath} 파일을 '{mode}' 모드로 열기")
        
        try:
            with open(filepath, mode, encoding='utf-8') as file:
                if mode == 'r':
                    content = file.read()
                    print(f"✅ 성공: 내용 길이 {len(content)}")
                else:
                    file.write("테스트")
                    print("✅ 성공: 쓰기 완료")
        
        except FileNotFoundError:
            print("❌ FileNotFoundError: 파일을 찾을 수 없습니다.")
            
            # 자동 복구: 파일 생성
            if mode == 'r':
                print("🔧 자동 복구: 빈 파일을 생성합니다.")
                with open(filepath, 'w') as f:
                    f.write("자동 생성된 파일입니다.")
        
        except IsADirectoryError:
            print("❌ IsADirectoryError: 디렉토리를 파일로 열려고 했습니다.")
        
        except PermissionError:
            print("❌ PermissionError: 파일에 대한 권한이 없습니다.")
            print("🔧 해결책: 파일 권한을 확인하거나 관리자 권한으로 실행하세요.")
        
        except UnicodeDecodeError as e:
            print(f"❌ UnicodeDecodeError: 인코딩 문제 - {e}")
            print("🔧 해결책: encoding 매개변수를 지정하세요.")
        
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {type(e).__name__}: {e}")
    
    print("\n2️⃣ 안전한 파일 처리 함수")
    
    def safe_read_file(filepath, default_content="파일이 존재하지 않습니다."):
        """안전하게 파일을 읽는 함수"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"⚠️ 파일 '{filepath}'을 찾을 수 없습니다. 기본값을 반환합니다.")
            return default_content
        except PermissionError:
            print(f"⚠️ 파일 '{filepath}'에 대한 읽기 권한이 없습니다.")
            return "권한 오류로 파일을 읽을 수 없습니다."
        except UnicodeDecodeError:
            print(f"⚠️ 파일 '{filepath}'의 인코딩에 문제가 있습니다.")
            try:
                with open(filepath, 'r', encoding='cp949') as file:  # 다른 인코딩 시도
                    return file.read()
            except:
                return "인코딩 오류로 파일을 읽을 수 없습니다."
        except Exception as e:
            print(f"⚠️ 예상치 못한 오류: {e}")
            return f"오류 발생: {e}"
    
    def safe_write_file(filepath, content):
        """안전하게 파일에 쓰는 함수"""
        try:
            # 디렉토리가 없으면 생성
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            return True, "파일 쓰기 성공"
        
        except PermissionError:
            return False, "권한 오류: 파일에 쓸 권한이 없습니다."
        except OSError as e:
            return False, f"시스템 오류: {e}"
        except Exception as e:
            return False, f"예상치 못한 오류: {e}"
    
    # 안전한 함수들 테스트
    print("\n📝 안전한 파일 처리 함수 테스트:")
    
    test_files = [
        "existing_test.txt",
        "nonexistent_test.txt",
        "subdir/new_file.txt"
    ]
    
    # 테스트 파일 생성
    with open("existing_test.txt", "w", encoding="utf-8") as f:
        f.write("이 파일은 존재합니다!")
    
    for test_file in test_files:
        print(f"\n파일: {test_file}")
        
        # 읽기 테스트
        content = safe_read_file(test_file)
        print(f"읽기 결과: {content[:50]}{'...' if len(content) > 50 else ''}")
        
        # 쓰기 테스트
        success, message = safe_write_file(test_file, f"테스트 내용 - {datetime.now()}")
        print(f"쓰기 결과: {message}")
    
    print("\n3️⃣ try-except-else-finally 완전 활용")
    
    def complete_exception_handling(filepath, content):
        """완전한 예외 처리 예제"""
        file = None
        try:
            print(f"📝 파일 '{filepath}' 작업 시작")
            file = open(filepath, 'w', encoding='utf-8')
            file.write(content)
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            return False
        
        else:
            # try 블록이 성공했을 때만 실행
            print("✅ 파일 쓰기 성공")
            return True
        
        finally:
            # 항상 실행되는 블록
            if file:
                file.close()
                print("📁 파일이 안전하게 닫혔습니다.")
            print("🔄 작업 완료\n")
    
    # 완전한 예외 처리 테스트
    test_contents = [
        ("success_test.txt", "성공적인 쓰기 테스트"),
        (".", "디렉토리에 쓰기 시도 (실패)")
    ]
    
    for filepath, content in test_contents:
        result = complete_exception_handling(filepath, content)
        print(f"결과: {'성공' if result else '실패'}")
    
    # 정리
    cleanup_files = ["nonexistent.txt", "existing_test.txt", "success_test.txt", "test_readonly.txt"]
    for file in cleanup_files:
        try:
            if os.path.exists(file):
                os.chmod(file, 0o666)  # 쓰기 권한 복구
                os.remove(file)
        except:
            pass
    
    try:
        shutil.rmtree("subdir")
    except:
        pass

# 예외 처리 실습 실행
exception_handling_practice()

print("=" * 30)

# 3. 파일 복사 및 이동
print("📁 파일 복사 및 이동")

def file_operations():
    """파일 복사, 이동, 삭제 실습"""
    
    print("1️⃣ 파일 복사 및 이동")
    
    # 원본 파일들 생성
    original_files = {
        "source1.txt": "첫 번째 원본 파일의 내용입니다.",
        "source2.txt": "두 번째 원본 파일의 내용입니다.",
        "data.csv": "이름,나이,점수\n김철수,20,85\n이영희,22,92"
    }
    
    for filename, content in original_files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # 대상 디렉토리 생성
    os.makedirs("backup", exist_ok=True)
    os.makedirs("archive", exist_ok=True)
    
    print("📁 원본 파일들 생성 완료")
    
    # 파일 복사
    print("\n📋 파일 복사:")
    
    files_to_copy = [
        ("source1.txt", "backup/source1_backup.txt"),
        ("source2.txt", "backup/source2_copy.txt"),
        ("data.csv", "archive/data_archive.csv")
    ]
    
    for src, dst in files_to_copy:
        try:
            shutil.copy2(src, dst)  # copy2는 메타데이터도 복사
            print(f"✅ {src} → {dst} 복사 완료")
            
            # 파일 크기 비교
            src_size = os.path.getsize(src)
            dst_size = os.path.getsize(dst)
            print(f"   크기 비교: 원본 {src_size}bytes, 복사본 {dst_size}bytes")
            
        except Exception as e:
            print(f"❌ {src} → {dst} 복사 실패: {e}")
    
    # 디렉토리 전체 복사
    print("\n📂 디렉토리 복사:")
    try:
        shutil.copytree("backup", "backup_copy")
        print("✅ backup 디렉토리를 backup_copy로 복사 완료")
        
        # 복사된 파일 목록 확인
        copied_files = os.listdir("backup_copy")
        print(f"   복사된 파일들: {copied_files}")
        
    except Exception as e:
        print(f"❌ 디렉토리 복사 실패: {e}")
    
    # 파일 이동
    print("\n🚚 파일 이동:")
    
    # 이동할 파일 생성
    with open("temp_file.txt", 'w') as f:
        f.write("임시 파일입니다.")
    
    try:
        shutil.move("temp_file.txt", "archive/moved_file.txt")
        print("✅ temp_file.txt → archive/moved_file.txt 이동 완료")
        
        # 원본 파일이 삭제되었는지 확인
        if not os.path.exists("temp_file.txt"):
            print("   ✓ 원본 파일이 삭제되었습니다.")
        
        if os.path.exists("archive/moved_file.txt"):
            print("   ✓ 대상 위치에 파일이 생성되었습니다.")
            
    except Exception as e:
        print(f"❌ 파일 이동 실패: {e}")
    
    print("\n2️⃣ 파일 및 디렉토리 목록 조회")
    
    def list_directory_contents(directory):
        """디렉토리 내용을 자세히 조회"""
        if not os.path.exists(directory):
            return f"❌ 디렉토리 '{directory}'가 존재하지 않습니다."
        
        print(f"\n📂 {directory} 디렉토리 내용:")
        try:
            items = os.listdir(directory)
            if not items:
                print("   📭 빈 디렉토리입니다.")
                return
            
            for item in sorted(items):
                item_path = os.path.join(directory, item)
                
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    modified = datetime.fromtimestamp(os.path.getmtime(item_path))
                    print(f"   📄 {item:20s} | {size:6d}bytes | {modified.strftime('%Y-%m-%d %H:%M')}")
                
                elif os.path.isdir(item_path):
                    try:
                        sub_count = len(os.listdir(item_path))
                        print(f"   📁 {item:20s} | {sub_count:6d}items | 디렉토리")
                    except PermissionError:
                        print(f"   📁 {item:20s} | ?????? items | 디렉토리 (권한 없음)")
        
        except PermissionError:
            print("   ❌ 디렉토리에 대한 접근 권한이 없습니다.")
        except Exception as e:
            print(f"   ❌ 오류 발생: {e}")
    
    # 현재 디렉토리와 생성된 디렉토리들 조회
    directories_to_check = [".", "backup", "archive", "backup_copy"]
    
    for directory in directories_to_check:
        list_directory_contents(directory)
    
    print("\n3️⃣ 파일 삭제 및 정리")
    
    def safe_delete_file(filepath):
        """안전하게 파일 삭제"""
        try:
            if os.path.exists(filepath):
                if os.path.isfile(filepath):
                    os.remove(filepath)
                    print(f"✅ 파일 '{filepath}' 삭제 완료")
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)
                    print(f"✅ 디렉토리 '{filepath}' 삭제 완료")
            else:
                print(f"⚠️ '{filepath}'가 존재하지 않습니다.")
        except PermissionError:
            print(f"❌ '{filepath}' 삭제 권한이 없습니다.")
        except Exception as e:
            print(f"❌ '{filepath}' 삭제 실패: {e}")
    
    # 정리할 파일 및 디렉토리 목록
    cleanup_items = [
        "source1.txt", "source2.txt", "data.csv",
        "backup", "archive", "backup_copy"
    ]
    
    print("🗑️ 생성된 파일들 정리 중...")
    for item in cleanup_items:
        safe_delete_file(item)
    
    print("\n4️⃣ 파일 시스템 모니터링")
    
    def monitor_file_changes():
        """파일 변경 사항 모니터링 시뮬레이션"""
        monitor_file = "monitor_test.txt"
        
        print(f"👁️ '{monitor_file}' 파일 모니터링 시작")
        
        # 초기 상태
        if os.path.exists(monitor_file):
            initial_mtime = os.path.getmtime(monitor_file)
            initial_size = os.path.getsize(monitor_file)
            print(f"   초기 상태: 크기 {initial_size}bytes, 수정시간 {datetime.fromtimestamp(initial_mtime)}")
        else:
            print("   파일이 존재하지 않음")
            initial_mtime = None
            initial_size = 0
        
        # 파일 생성/수정
        actions = [
            ("생성", "첫 번째 내용입니다."),
            ("수정1", "첫 번째 내용입니다.\n두 번째 줄이 추가되었습니다."),
            ("수정2", "내용이 완전히 바뀌었습니다!"),
            ("추가", "내용이 완전히 바뀌었습니다!\n추가된 내용입니다.")
        ]
        
        for action_name, content in actions:
            if action_name == "추가":
                with open(monitor_file, 'a', encoding='utf-8') as f:
                    f.write("\n추가된 내용입니다.")
            else:
                with open(monitor_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # 변경 사항 확인
            new_mtime = os.path.getmtime(monitor_file)
            new_size = os.path.getsize(monitor_file)
            
            print(f"   {action_name:4s}: 크기 {new_size:3d}bytes, 수정시간 {datetime.fromtimestamp(new_mtime).strftime('%H:%M:%S')}")
            
            import time
            time.sleep(0.1)  # 시간 차이를 위한 대기
        
        # 파일 삭제
        os.remove(monitor_file)
        print(f"   삭제: 파일이 삭제되었습니다.")
    
    monitor_file_changes()

# 파일 조작 실습 실행
file_operations()

print("=" * 30)

print("🎯 Part 2 요약:")
print("✅ 파일 존재 확인 및 경로 처리")
print("✅ 종합적인 예외 처리 전략")
print("✅ 파일 복사, 이동, 삭제")
print("✅ 디렉토리 조작 및 모니터링")
print("✅ 안전한 파일 처리 함수 작성")
```

---

### Part 3: 구조화된 데이터 (50분)

#### 📊 CSV와 JSON 파일 처리

```python
print("📊 CSV와 JSON 파일 처리")
print("=" * 19)

import csv
import json
from datetime import datetime, date
import os

# 1. CSV 파일 처리
print("📈 CSV 파일 처리")

def csv_file_operations():
    """CSV 파일 읽기/쓰기 실습"""
    
    print("1️⃣ CSV 파일 기본 읽기/쓰기")
    
    # 샘플 데이터 준비
    student_data = [
        ["이름", "나이", "학과", "성적", "등록일"],
        ["김철수", 20, "컴퓨터공학", 85.5, "2023-03-01"],
        ["이영희", 22, "경영학", 92.3, "2023-03-01"],
        ["박민수", 21, "전자공학", 78.9, "2023-03-02"],
        ["최지원", 23, "디자인", 88.7, "2023-03-02"],
        ["정다영", 19, "수학", 95.2, "2023-03-03"]
    ]
    
    # CSV 파일 쓰기
    csv_filename = "students.csv"
    
    print("📝 CSV 파일 쓰기:")
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(student_data)
    
    print(f"✅ '{csv_filename}' 파일 생성 완료")
    
    # 파일 내용 확인
    with open(csv_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("📄 생성된 CSV 내용:")
        print(content)
    
    # CSV 파일 읽기 - 기본 방법
    print("\n📖 CSV 파일 읽기 (기본 방법):")
    
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"헤더: {row}")
            else:
                print(f"데이터 {row_num}: {row}")
    
    # CSV 파일 읽기 - 딕셔너리 방법
    print("\n📖 CSV 파일 읽기 (딕셔너리 방법):")
    
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        print("📋 학생 정보:")
        for row in reader:
            print(f"  이름: {row['이름']:6s} | 나이: {row['나이']:2s} | 학과: {row['학과']:8s} | 성적: {row['성적']:5s}")
    
    print("\n2️⃣ CSV 파일 고급 처리")
    
    # 조건부 데이터 필터링
    print("🔍 성적이 85점 이상인 학생 필터링:")
    
    high_performers = []
    
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if float(row['성적']) >= 85.0:
                high_performers.append(row)
                print(f"  {row['이름']:6s} | {row['학과']:8s} | {row['성적']}점")
    
    # 필터링된 데이터를 새 CSV 파일로 저장
    high_performers_file = "high_performers.csv"
    
    with open(high_performers_file, 'w', newline='', encoding='utf-8') as csvfile:
        if high_performers:
            fieldnames = high_performers[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(high_performers)
    
    print(f"✅ 우수학생 데이터를 '{high_performers_file}'에 저장")
    
    # 통계 계산
    print("\n📊 학생 성적 통계:")
    
    scores = []
    subjects = {}
    
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            score = float(row['성적'])
            subject = row['학과']
            
            scores.append(score)
            
            if subject not in subjects:
                subjects[subject] = []
            subjects[subject].append(score)
    
    # 전체 통계
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    print(f"  전체 평균: {avg_score:.1f}점")
    print(f"  최고 점수: {max_score}점")
    print(f"  최저 점수: {min_score}점")
    
    # 학과별 통계
    print("\n  학과별 평균:")
    for subject, subject_scores in subjects.items():
        subject_avg = sum(subject_scores) / len(subject_scores)
        print(f"    {subject:8s}: {subject_avg:.1f}점 ({len(subject_scores)}명)")
    
    # 통계를 CSV로 저장
    stats_file = "statistics.csv"
    
    with open(stats_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["구분", "값"])
        writer.writerow(["전체 평균", f"{avg_score:.1f}"])
        writer.writerow(["최고 점수", max_score])
        writer.writerow(["최저 점수", min_score])
        writer.writerow(["학생 수", len(scores)])
    
    print(f"✅ 통계 데이터를 '{stats_file}'에 저장")
    
    print("\n3️⃣ CSV 다양한 옵션")
    
    # 다양한 구분자 및 옵션 테스트
    custom_data = [
        ["제품명", "가격", "재고", "설명"],
        ["노트북", "1200000", "15", "고성능 게이밍 노트북"],
        ["마우스", "35000", "120", "무선 게이밍 마우스"],
        ["키보