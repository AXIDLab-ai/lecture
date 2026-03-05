
**[← Week 9](./week9.md) | [목차](lecture/04_PythonProgramming/lectureMap.md) | [다음: Week 11 →](./week11.md)**

Week 10: 윈도 프로그래밍 (tkinter GUI)

---

## 🎯 학습 목표

이번 주 실습을 완료하면 다음과 같은 능력을 갖추게 됩니다:

1. **tkinter 기초**: 윈도우 창을 생성하고 기본 설정을 할 수 있습니다
2. **위젯 활용**: Label, Button, Entry, Text 등 핵심 위젯을 자유자재로 다룹니다
3. **이벤트 처리**: 버튼 클릭, 키보드 입력 등의 사용자 이벤트를 처리합니다
4. **레이아웃 관리**: pack(), grid(), place() 레이아웃 매니저를 적재적소에 활용합니다
5. **GUI 프로그램 설계**: 계산기, 텍스트 에디터 등 실용적인 GUI 애플리케이션을 제작합니다
6. **사용자 경험**: 직관적이고 사용하기 편한 인터페이스를 설계합니다

---

## 📚 핵심 개념 요약

### 1. tkinter란?
```
🖼️ tkinter = Python의 표준 GUI 툴킷
🏠 Tk 인터페이스의 파이썬 바인딩
📦 별도 설치 없이 Python과 함께 제공
🎨 크로스 플랫폼 지원 (Windows, Mac, Linux)
```

### 2. GUI 구성 요소

| 구성 요소 | 설명 | 예시 |
|----------|------|------|
| **윈도우(Window)** | GUI의 최상위 컨테이너 | 메인 창, 대화상자 |
| **위젯(Widget)** | GUI의 구성 요소들 | 버튼, 레이블, 입력창 |
| **이벤트(Event)** | 사용자 행동 | 클릭, 키 입력, 창 닫기 |
| **레이아웃(Layout)** | 위젯 배치 방법 | pack, grid, place |

### 3. 주요 위젯

| 위젯 | 기능 | 주요 옵션 | 예시 |
|------|------|----------|------|
| **Tk()** | 메인 윈도우 | title, geometry | `root = tk.Tk()` |
| **Label** | 텍스트/이미지 표시 | text, fg, bg, font | `Label(root, text="안녕")` |
| **Button** | 클릭 가능한 버튼 | text, command, bg | `Button(root, text="클릭")` |
| **Entry** | 한 줄 텍스트 입력 | width, font | `Entry(root, width=20)` |
| **Text** | 여러 줄 텍스트 입력 | width, height | `Text(root, width=30)` |
| **Frame** | 위젯 그룹화 | relief, bd | `Frame(root, relief="solid")` |
| **Canvas** | 그리기 영역 | width, height, bg | `Canvas(root, width=300)` |

### 4. 레이아웃 매니저

| 매니저 | 특징 | 적합한 상황 | 예시 |
|--------|------|-------------|------|
| **pack()** | 순차적 배치 | 간단한 레이아웃 | `widget.pack(side="left")` |
| **grid()** | 격자 배치 | 복잡한 폼 | `widget.grid(row=0, column=1)` |
| **place()** | 절대 위치 | 정밀한 위치 조정 | `widget.place(x=10, y=20)` |

### 5. 이벤트 처리 방식

| 방식 | 설명 | 예시 |
|------|------|------|
| **command 옵션** | 버튼 클릭 처리 | `Button(command=함수명)` |
| **bind() 메서드** | 다양한 이벤트 바인딩 | `widget.bind("<Key>", 함수)` |
| **이벤트 객체** | 이벤트 정보 접근 | `def handler(event):` |

---

## 💻 실습 세션 (2시간)

### Part 1: tkinter 기초 (30분)

#### 🖼️ 첫 번째 윈도우 만들기

```python
print("🖼️ 첫 번째 윈도우 만들기")
print("=" * 20)

import tkinter as tk
from tkinter import messagebox
import random

# 1. 가장 기본적인 윈도우
print("📝 기본 윈도우 생성")

def create_basic_window():
    """가장 간단한 윈도우"""
    root = tk.Tk()
    root.title("내 첫 번째 GUI")
    root.geometry("300x200")  # 너비x높이
    
    # 윈도우를 화면에 표시하고 이벤트 루프 시작
    root.mainloop()

# 기본 윈도우 실행 (주석 해제하여 테스트)
# create_basic_window()

print("=" * 30)

# 2. 윈도우 설정 옵션들
print("⚙️ 윈도우 설정 옵션")

def create_configured_window():
    """다양한 설정이 적용된 윈도우"""
    root = tk.Tk()
    
    # 기본 설정
    root.title("설정된 윈도우")
    root.geometry("400x300")
    
    # 추가 설정
    root.resizable(True, True)  # 크기 조절 가능 (width, height)
    root.configure(bg="lightblue")  # 배경색
    
    # 윈도우 위치 설정 (x, y 좌표)
    root.geometry("400x300+100+50")  # 너비x높이+x위치+y위치
    
    # 최소/최대 크기 설정
    root.minsize(300, 200)
    root.maxsize(800, 600)
    
    # 윈도우 아이콘 설정 (ICO 파일이 있다면)
    # root.iconbitmap("icon.ico")
    
    print("윈도우 설정 완료:")
    print(f"  제목: {root.title()}")
    print(f"  크기: {root.geometry()}")
    print(f"  배경색: {root.cget('bg')}")
    
    root.mainloop()

# 설정된 윈도우 실행 (주석 해제하여 테스트)
# create_configured_window()

print("=" * 30)

# 3. Label 위젯 기초
print("🏷️ Label 위젯 기초")

def create_label_examples():
    """다양한 Label 예제"""
    root = tk.Tk()
    root.title("Label 예제")
    root.geometry("400x350")
    root.configure(bg="white")
    
    # 기본 Label
    label1 = tk.Label(root, text="안녕하세요! 파이썬 GUI입니다.")
    label1.pack(pady=10)
    
    # 스타일이 적용된 Label
    label2 = tk.Label(
        root,
        text="스타일 적용된 레이블",
        font=("맑은 고딕", 14, "bold"),
        fg="blue",  # 글자색
        bg="yellow"  # 배경색
    )
    label2.pack(pady=10)
    
    # 여러 줄 Label
    multiline_text = """이것은 여러 줄로 된
레이블입니다.
줄바꿈이 적용됩니다."""
    
    label3 = tk.Label(
        root,
        text=multiline_text,
        justify="center",  # 정렬: left, center, right
        font=("굴림", 11),
        relief="solid",  # 테두리: flat, solid, raised, sunken, ridge, groove
        bd=2  # 테두리 두께
    )
    label3.pack(pady=10)
    
    # 동적으로 변경되는 Label
    dynamic_label = tk.Label(
        root,
        text="이 텍스트는 3초 후 변경됩니다",
        font=("Arial", 12),
        fg="red"
    )
    dynamic_label.pack(pady=10)
    
    def change_text():
        """레이블 텍스트 변경"""
        dynamic_label.config(text="텍스트가 변경되었습니다!", fg="green")
    
    # 3초 후 텍스트 변경
    root.after(3000, change_text)  # 3000ms = 3초
    
    # 시간을 표시하는 Label
    import datetime
    
    time_label = tk.Label(
        root,
        text="",
        font=("Courier New", 10),
        fg="purple"
    )
    time_label.pack(pady=10)
    
    def update_time():
        """현재 시간 업데이트"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_label.config(text=f"현재 시간: {current_time}")
        root.after(1000, update_time)  # 1초마다 업데이트
    
    update_time()  # 시간 업데이트 시작
    
    root.mainloop()

# Label 예제 실행 (주석 해제하여 테스트)
# create_label_examples()

print("=" * 30)

# 4. Button 위젯 기초
print("🔘 Button 위젯 기초")

def create_button_examples():
    """다양한 Button 예제"""
    root = tk.Tk()
    root.title("Button 예제")
    root.geometry("400x400")
    root.configure(bg="lightgray")
    
    # 클릭 카운터
    click_count = [0]  # 리스트를 사용해서 함수 내에서 수정 가능하게
    
    # 제목 레이블
    title_label = tk.Label(
        root,
        text="버튼 예제 모음",
        font=("맑은 고딕", 16, "bold"),
        bg="lightgray"
    )
    title_label.pack(pady=10)
    
    # 상태 표시 레이블
    status_label = tk.Label(
        root,
        text="버튼을 클릭해보세요!",
        font=("맑은 고딕", 12),
        bg="lightgray",
        fg="blue"
    )
    status_label.pack(pady=5)
    
    # 기본 버튼
    def simple_click():
        """간단한 클릭 처리"""
        status_label.config(text="기본 버튼이 클릭되었습니다!", fg="green")
        messagebox.showinfo("알림", "안녕하세요! 첫 번째 버튼입니다.")
    
    button1 = tk.Button(
        root,
        text="기본 버튼",
        command=simple_click,
        font=("맑은 고딕", 11)
    )
    button1.pack(pady=5)
    
    # 카운터 버튼
    count_label = tk.Label(
        root,
        text=f"클릭 횟수: {click_count[0]}",
        font=("맑은 고딕", 11),
        bg="lightgray"
    )
    count_label.pack(pady=5)
    
    def count_click():
        """클릭 횟수 증가"""
        click_count[0] += 1
        count_label.config(text=f"클릭 횟수: {click_count[0]}")
        status_label.config(text=f"{click_count[0]}번 클릭했습니다!", fg="orange")
    
    button2 = tk.Button(
        root,
        text="카운터 버튼",
        command=count_click,
        font=("맑은 고딕", 11),
        bg="lightblue"
    )
    button2.pack(pady=5)
    
    # 스타일 버튼
    def style_click():
        """스타일 변경"""
        colors = ["red", "green", "blue", "purple", "orange"]
        color = random.choice(colors)
        status_label.config(text=f"색상이 {color}로 변경되었습니다!", fg=color)
    
    button3 = tk.Button(
        root,
        text="색상 변경 버튼",
        command=style_click,
        font=("맑은 고딕", 11, "bold"),
        bg="yellow",
        fg="red",
        relief="raised",
        bd=3
    )
    button3.pack(pady=5)
    
    # 비활성화/활성화 버튼
    def toggle_button():
        """버튼 상태 토글"""
        if button3['state'] == 'normal':
            button3.config(state='disabled', text="비활성화됨")
            toggle_btn.config(text="버튼 활성화")
            status_label.config(text="색상 변경 버튼이 비활성화되었습니다", fg="gray")
        else:
            button3.config(state='normal', text="색상 변경 버튼")
            toggle_btn.config(text="버튼 비활성화")
            status_label.config(text="색상 변경 버튼이 활성화되었습니다", fg="black")
    
    toggle_btn = tk.Button(
        root,
        text="버튼 비활성화",
        command=toggle_button,
        font=("맑은 고딕", 10)
    )
    toggle_btn.pack(pady=5)
    
    # 종료 버튼
    def quit_program():
        """프로그램 종료 확인"""
        result = messagebox.askyesno("종료 확인", "정말로 프로그램을 종료하시겠습니까?")
        if result:
            root.destroy()
    
    quit_button = tk.Button(
        root,
        text="프로그램 종료",
        command=quit_program,
        font=("맑은 고딕", 11, "bold"),
        bg="salmon",
        fg="white"
    )
    quit_button.pack(pady=10)
    
    root.mainloop()

# Button 예제 실행 (주석 해제하여 테스트)
# create_button_examples()

print("=" * 30)

# 5. pack() 레이아웃 매니저
print("📦 pack() 레이아웃 매니저")

def create_pack_examples():
    """pack() 레이아웃 예제"""
    root = tk.Tk()
    root.title("pack() 레이아웃 예제")
    root.geometry("500x400")
    
    # 제목
    title = tk.Label(
        root,
        text="pack() 레이아웃 매니저",
        font=("맑은 고딕", 14, "bold"),
        bg="navy",
        fg="white"
    )
    title.pack(fill="x", pady=5)  # 가로로 꽉 채우기
    
    # 상단 프레임
    top_frame = tk.Frame(root, bg="lightblue", relief="solid", bd=2)
    top_frame.pack(fill="x", padx=10, pady=5)
    
    tk.Label(top_frame, text="상단 영역", bg="lightblue").pack(pady=10)
    
    # 중앙 프레임 (좌우 배치)
    center_frame = tk.Frame(root, bg="lightgreen")
    center_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    # 왼쪽 영역
    left_frame = tk.Frame(center_frame, bg="lightyellow", relief="solid", bd=1)
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
    
    tk.Label(left_frame, text="왼쪽 영역", bg="lightyellow").pack(pady=20)
    
    tk.Button(
        left_frame,
        text="왼쪽 버튼 1",
        command=lambda: print("왼쪽 버튼 1 클릭")
    ).pack(pady=2)
    
    tk.Button(
        left_frame,
        text="왼쪽 버튼 2",
        command=lambda: print("왼쪽 버튼 2 클릭")
    ).pack(pady=2)
    
    # 오른쪽 영역
    right_frame = tk.Frame(center_frame, bg="lightpink", relief="solid", bd=1)
    right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))
    
    tk.Label(right_frame, text="오른쪽 영역", bg="lightpink").pack(pady=20)
    
    tk.Button(
        right_frame,
        text="오른쪽 버튼 1",
        command=lambda: print("오른쪽 버튼 1 클릭")
    ).pack(pady=2)
    
    tk.Button(
        right_frame,
        text="오른쪽 버튼 2",
        command=lambda: print("오른쪽 버튼 2 클릭")
    ).pack(pady=2)
    
    # 하단 프레임
    bottom_frame = tk.Frame(root, bg="lightgray", relief="solid", bd=2)
    bottom_frame.pack(fill="x", padx=10, pady=5)
    
    tk.Label(bottom_frame, text="하단 영역", bg="lightgray").pack(side="left", padx=10)
    
    tk.Button(
        bottom_frame,
        text="설정",
        command=lambda: print("설정 클릭")
    ).pack(side="right", padx=5)
    
    tk.Button(
        bottom_frame,
        text="도움말",
        command=lambda: print("도움말 클릭")
    ).pack(side="right", padx=5)
    
    # pack 옵션 설명
    info_text = """
pack() 주요 옵션:
• side: "top"(기본), "bottom", "left", "right"
• fill: "none"(기본), "x", "y", "both"
• expand: True/False (여유 공간 확장)
• padx, pady: 외부 여백
• ipadx, ipady: 내부 여백
    """
    
    info_label = tk.Label(
        root,
        text=info_text,
        justify="left",
        font=("Courier New", 9),
        bg="white",
        relief="sunken",
        bd=1
    )
    info_label.pack(fill="x", padx=10, pady=5)
    
    root.mainloop()

# pack() 예제 실행 (주석 해제하여 테스트)
# create_pack_examples()

print("=" * 30)

# 6. 실습 종합 - 간단한 인사 프로그램
print("🎪 실습 종합 - 간단한 인사 프로그램")

def create_greeting_app():
    """이름을 입력받아 인사하는 프로그램"""
    root = tk.Tk()
    root.title("인사 프로그램")
    root.geometry("350x250")
    root.configure(bg="lightsteelblue")
    
    # 제목
    title_label = tk.Label(
        root,
        text="👋 인사 프로그램 👋",
        font=("맑은 고딕", 16, "bold"),
        bg="lightsteelblue",
        fg="darkblue"
    )
    title_label.pack(pady=10)
    
    # 설명
    desc_label = tk.Label(
        root,
        text="이름을 입력하고 버튼을 클릭하세요",
        font=("맑은 고딕", 11),
        bg="lightsteelblue"
    )
    desc_label.pack(pady=5)
    
    # 이름 입력 프레임
    input_frame = tk.Frame(root, bg="lightsteelblue")
    input_frame.pack(pady=10)
    
    name_label = tk.Label(
        input_frame,
        text="이름:",
        font=("맑은 고딕", 12),
        bg="lightsteelblue"
    )
    name_label.pack(side="left", padx=5)
    
    name_entry = tk.Entry(
        input_frame,
        font=("맑은 고딕", 12),
        width=15
    )
    name_entry.pack(side="left", padx=5)
    
    # 결과 표시 레이블
    result_label = tk.Label(
        root,
        text="",
        font=("맑은 고딕", 14, "bold"),
        bg="lightsteelblue",
        fg="green",
        wraplength=300  # 자동 줄바꿈
    )
    result_label.pack(pady=15)
    
    # 버튼들
    button_frame = tk.Frame(root, bg="lightsteelblue")
    button_frame.pack(pady=10)
    
    def say_hello():
        """인사 메시지 표시"""
        name = name_entry.get().strip()
        if name:
            result_label.config(text=f"안녕하세요, {name}님! 만나서 반갑습니다! 🎉")
        else:
            result_label.config(text="이름을 입력해주세요!", fg="red")
    
    def say_goodbye():
        """작별 인사"""
        name = name_entry.get().strip()
        if name:
            result_label.config(text=f"안녕히 가세요, {name}님! 좋은 하루 되세요! 👋")
        else:
            result_label.config(text="이름을 입력해주세요!", fg="red")
    
    def clear_all():
        """모든 내용 지우기"""
        name_entry.delete(0, tk.END)
        result_label.config(text="", fg="green")
        name_entry.focus()  # 포커스를 입력창으로
    
    # 인사 버튼
    hello_btn = tk.Button(
        button_frame,
        text="안녕하세요!",
        command=say_hello,
        font=("맑은 고딕", 11),
        bg="lightgreen",
        width=10
    )
    hello_btn.pack(side="left", padx=5)
    
    # 작별 버튼
    goodbye_btn = tk.Button(
        button_frame,
        text="안녕히가세요!",
        command=say_goodbye,
        font=("맑은 고딕", 11),
        bg="lightcoral",
        width=12
    )
    goodbye_btn.pack(side="left", padx=5)
    
    # 지우기 버튼
    clear_btn = tk.Button(
        button_frame,
        text="지우기",
        command=clear_all,
        font=("맑은 고딕", 11),
        bg="lightgray",
        width=8
    )
    clear_btn.pack(side="left", padx=5)
    
    # Enter 키로도 인사할 수 있게
    def on_enter(event):
        say_hello()
    
    name_entry.bind('<Return>', on_enter)
    
    # 처음에 포커스를 입력창에
    name_entry.focus()
    
    # 프로그램 설명
    help_text = "💡 팁: Enter 키를 눌러도 인사할 수 있어요!"
    help_label = tk.Label(
        root,
        text=help_text,
        font=("맑은 고딕", 9),
        bg="lightsteelblue",
        fg="gray"
    )
    help_label.pack(pady=5)
    
    root.mainloop()

# 인사 프로그램 실행 (주석 해제하여 테스트)
# create_greeting_app()

print("=" * 30)

print("🎯 Part 1 요약:")
print("✅ tkinter 기본 윈도우 생성")
print("✅ Label 위젯으로 텍스트 표시")
print("✅ Button 위젯으로 사용자 상호작용")
print("✅ pack() 레이아웃으로 위젯 배치")
print("✅ 간단한 GUI 애플리케이션 완성")
```

---

### Part 2: 입력 위젯과 이벤트 (40분)

#### 📝 Entry와 Text 위젯

```python
print("📝 Entry와 Text 위젯")
print("=" * 18)

import tkinter as tk
from tkinter import messagebox, filedialog
import os

# 1. Entry 위젯 (한 줄 입력)
print("📄 Entry 위젯 기초")

def create_entry_examples():
    """Entry 위젯 다양한 예제"""
    root = tk.Tk()
    root.title("Entry 위젯 예제")
    root.geometry("450x500")
    root.configure(bg="lightyellow")
    
    # 제목
    tk.Label(
        root,
        text="Entry 위젯 예제",
        font=("맑은 고딕", 16, "bold"),
        bg="lightyellow"
    ).pack(pady=10)
    
    # 기본 Entry
    basic_frame = tk.Frame(root, bg="lightyellow")
    basic_frame.pack(pady=10, fill="x", padx=20)
    
    tk.Label(basic_frame, text="기본 입력:", bg="lightyellow").pack(side="left")
    basic_entry = tk.Entry(basic_frame, font=("맑은 고딕", 11))
    basic_entry.pack(side="left", padx=10, fill="x", expand=True)
    
    # 패스워드 Entry
    password_frame = tk.Frame(root, bg="lightyellow")
    password_frame.pack(pady=5, fill="x", padx=20)
    
    tk.Label(password_frame, text="비밀번호:", bg="lightyellow").pack(side="left")
    password_entry = tk.Entry(
        password_frame,
        font=("맑은 고딕", 11),
        show="*"  # 입력 내용을 *로 표시
    )
    password_entry.pack(side="left", padx=10, fill="x", expand=True)
    
    # 숫자만 입력 Entry
    number_frame = tk.Frame(root, bg="lightyellow")
    number_frame.pack(pady=5, fill="x", padx=20)
    
    tk.Label(number_frame, text="숫자만:", bg="lightyellow").pack(side="left")
    number_entry = tk.Entry(number_frame, font=("맑은 고딕", 11))
    number_entry.pack(side="left", padx=10, fill="x", expand=True)
    
    # 숫자만 입력 제한 함수
    def validate_number(char):
        """숫자만 입력 허용"""
        return char.isdigit() or char == ""
    
    # 입력 검증 등록
    vcmd = (root.register(validate_number), '%S')
    number_entry.config(validate='key', validatecommand=vcmd)
    
    # 읽기 전용 Entry
    readonly_frame = tk.Frame(root, bg="lightyellow")
    readonly_frame.pack(pady=5, fill="x", padx=20)
    
    tk.Label(readonly_frame, text="읽기전용:", bg="lightyellow").pack(side="left")
    readonly_entry = tk.Entry(
        readonly_frame,
        font=("맑은 고딕", 11),
        state="readonly",  # 읽기 전용
        bg="lightgray"
    )
    readonly_entry.pack(side="left", padx=10, fill="x", expand=True)
    
    # 읽기 전용에 초기값 설정
    readonly_entry.config(state="normal")
    readonly_entry.insert(0, "이 값은 수정할 수 없습니다")
    readonly_entry.config(state="readonly")
    
    # 결과 표시 영역
    result_text = tk.Text(
        root,
        height=8,
        width=50,
        font=("Courier New", 10),
        bg="white",
        relief="sunken",
        bd=2
    )
    result_text.pack(pady=10, padx=20, fill="both", expand=True)
    
    # 버튼들
    button_frame = tk.Frame(root, bg="lightyellow")
    button_frame.pack(pady=10)
    
    def show_values():
        """모든 입력값 표시"""
        basic_val = basic_entry.get()
        password_val = password_entry.get()
        number_val = number_entry.get()
        readonly_val = readonly_entry.get()
        
        result_text.delete(1.0, tk.END)  # 기존 내용 삭제
        result_text.insert(tk.END, "=== 입력된 값들 ===\n")
        result_text.insert(tk.END, f"기본 입력: '{basic_val}'\n")
        result_text.insert(tk.END, f"비밀번호: {'*' * len(password_val)} (길이: {len(password_val)})\n")
        result_text.insert(tk.END, f"숫자: '{number_val}'\n")
        result_text.insert(tk.END, f"읽기전용: '{readonly_val}'\n")
        
        # 입력값 검증
        result_text.insert(tk.END, "\n=== 검증 결과 ===\n")
        
        if basic_val:
            result_text.insert(tk.END, f"✅ 기본 입력이 채워짐\n")
        else:
            result_text.insert(tk.END, f"❌ 기본 입력이 비어있음\n")
        
        if len(password_val) >= 6:
            result_text.insert(tk.END, f"✅ 비밀번호가 6자 이상\n")
        else:
            result_text.insert(tk.END, f"❌ 비밀번호가 너무 짧음\n")
        
        if number_val and number_val.isdigit():
            result_text.insert(tk.END, f"✅ 올바른 숫자: {number_val}\n")
        else:
            result_text.insert(tk.END, f"❌ 숫자를 입력하세요\n")
    
    def clear_all():
        """모든 입력 지우기"""
        basic_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
        result_text.delete(1.0, tk.END)
        basic_entry.focus()
    
    def fill_sample():
        """샘플 데이터 채우기"""
        clear_all()
        basic_entry.insert(0, "홍길동")
        password_entry.insert(0, "password123")
        number_entry.insert(0, "12345")
    
    tk.Button(
        button_frame,
        text="값 확인",
        command=show_values,
        font=("맑은 고딕", 11),
        bg="lightblue"
    ).pack(side="left", padx=5)
    
    tk.Button(
        button_frame,
        text="모두 지우기",
        command=clear_all,
        font=("맑은 고딕", 11),
        bg="lightcoral"
    ).pack(side="left", padx=5)
    
    tk.Button(
        button_frame,
        text="샘플 데이터",
        command=fill_sample,
        font=("맑은 고딕", 11),
        bg="lightgreen"
    ).pack(side="left", padx=5)
    
    # Enter 키 바인딩
    def on_enter(event):
        show_values()
    
    basic_entry.bind('<Return>', on_enter)
    password_entry.bind('<Return>', on_enter)
    number_entry.bind('<Return>', on_enter)
    
    # 초기 포커스
    basic_entry.focus()
    
    root.mainloop()

# Entry 예제 실행 (주석 해제하여 테스트)
# create_entry_examples()

print("=" * 30)

# 2. Text 위젯 (여러 줄 입력)
print("📖 Text 위젯 기초")

def create_text_examples():
    """Text 위젯 다양한 예제"""
    root = tk.Tk()
    root.title("Text 위젯 예제")
    root.geometry("600x500")
    
    # 제목
    title_frame = tk.Frame(root, bg="lightcyan")
    title_frame.pack(fill="x")
    
    tk.Label(
        title_frame,
        text="📝 Text 위젯 예제",
        font=("맑은 고딕", 16, "bold"),
        bg="lightcyan",
        fg="darkblue"
    ).pack(pady=10)
    
    # 메인 프레임
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    # 왼쪽: 입력 영역
    left_frame = tk.Frame(main_frame)
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
    
    tk.Label(left_frame, text="메모 입력 영역:", font=("맑은 고딕", 12, "bold")).pack(anchor="w")
    
    # 스크롤바가 있는 Text
    text_frame = tk.Frame(left_frame)
    text_frame.pack(fill="both", expand=True, pady=5)
    
    text_widget = tk.Text(
        text_frame,
        width=30,
        height=15,
        font=("맑은 고딕", 11),
        wrap="word",  # 단어 단위 줄바꿈
        bg="white",
        relief="sunken",
        bd=2
    )
    
    # 스크롤바 추가
    scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # 초기 텍스트 삽입
    sample_text = """안녕하세요! 이것은 Text 위젯 예제입니다.

여러 줄의 텍스트를 입력할 수 있습니다.
마우스로 텍스트를 선택할 수도 있고,
키보드로 편집도 가능합니다.

아래 버튼들을 사용해서 다양한 기능을 테스트해보세요:
- 현재 텍스트 분석
- 특정 단어 찾기
- 텍스트 변환
- 파일 저장/불러오기

한글과 영어 모두 지원됩니다.
English text is also supported!
"""
    
    text_widget.insert("1.0", sample_text)
    
    # 오른쪽: 컨트롤 영역
    right_frame = tk.Frame(main_frame)
    right_frame.pack(side="right", fill="y", padx=(5, 0))
    
    tk.Label(right_frame, text="텍스트 조작:", font=("맑은 고딕", 12, "bold")).pack(anchor="w", pady=(0, 10))
    
    # 정보 표시 프레임
    info_frame = tk.Frame(right_frame, relief="solid", bd=1, bg="lightyellow")
    info_frame.pack(fill="x", pady=5)
    
    info_label = tk.Label(
        info_frame,
        text="텍스트 정보가 여기에\n표시됩니다",
        justify="left",
        font=("맑은 고딕", 10),
        bg="lightyellow"
    )
    info_label.pack(padx=10, pady=10)
    
    def analyze_text():
        """텍스트 분석"""
        content = text_widget.get("1.0", tk.END)
        lines = content.split('\n')
        words = content.split()
        chars = len(content) - 1  # 마지막 줄바꿈 제외
        
        info_text = f"""📊 텍스트 분석 결과:
        
줄 수: {len(lines) - 1}
단어 수: {len(words)}
문자 수: {chars}
공백 포함: {len(content) - 1}

최근 수정: {tk.datetime.datetime.now().strftime('%H:%M:%S')}"""
        
        info_label.config(text=info_text)
    
    def find_word():
        """단어 찾기"""
        word = tk.simpledialog.askstring("단어 찾기", "찾을 단어를 입력하세요:")
        if word:
            content = text_widget.get("1.0", tk.END)
            count = content.lower().count(word.lower())
            
            if count > 0:
                info_label.config(text=f"'{word}' 단어를\n{count}개 찾았습니다!")
                # 첫 번째 발견 위치로 이동
                start_pos = content.lower().find(word.lower())
                if start_pos != -1:
                    # 라인과 컬럼 계산
                    lines_before = content[:start_pos].count('\n')
                    col = start_pos - content.rfind('\n', 0, start_pos) - 1
                    
                    text_widget.mark_set("insert", f"{lines_before + 1}.{col}")
                    text_widget.see("insert")
            else:
                info_label.config(text=f"'{word}' 단어를\n찾을 수 없습니다")
    
    def convert_case():
        """텍스트 케이스 변환"""
        try:
            # 선택된 텍스트가 있으면 선택된 부분만, 없으면 전체
            selected = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            start, end = tk.SEL_FIRST, tk.SEL_LAST
        except tk.TclError:
            # 선택된 텍스트가 없으면 전체
            selected = text_widget.get("1.0", tk.END)
            start, end = "1.0", tk.END
        
        # 변환 옵션 선택
        options = ["대문자로 변환", "소문자로 변환", "첫글자만 대문자"]
        choice = tk.messagebox.askyesnocancel("변환 옵션", "대문자로 변환하시겠습니까?\n(예: 대문자, 아니오: 소문자, 취소: 첫글자만)")
        
        if choice is True:
            converted = selected.upper()
        elif choice is False:
            converted = selected.lower()
        elif choice is None:
            converted = selected.title()
        else:
            return
        
        # 텍스트 교체
        if start == "1.0" and end == tk.END:
            text_widget.delete("1.0", tk.END)
            text_widget.insert("1.0", converted)
        else:
            text_widget.delete(start, end)
            text_widget.insert(start, converted)
    
    def clear_text():
        """텍스트 지우기"""
        if messagebox.askyesno("확인", "모든 텍스트를 지우시겠습니까?"):
            text_widget.delete("1.0", tk.END)
            info_label.config(text="텍스트가 지워졌습니다")
    
    def save_to_file():
        """파일로 저장"""
        content = text_widget.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                info_label.config(text=f"파일 저장 완료:\n{os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("오류", f"저장 실패: {e}")
    
    def load_from_file():
        """파일에서 불러오기"""
        filename = filedialog.askopenfilename(
            filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert("1.0", content)
                info_label.config(text=f"파일 불러오기 완료:\n{os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("오류", f"불러오기 실패: {e}")
    
    # 버튼들
    buttons = [
        ("텍스트 분석", analyze_text, "lightblue"),
        ("단어 찾기", find_word, "lightgreen"),
        ("대소문자 변환", convert_case, "lightyellow"),
        ("모두 지우기", clear_text, "lightcoral"),
        ("파일 저장", save_to_file, "lightsteelblue"),
        ("파일 불러오기", load_from_file, "lightpink")
    ]
    
    for text, command, color in buttons:
        tk.Button(
            right_frame,
            text=text,
            command=command,
            font=("맑은 고딕", 10),
            bg=color,
            width=12
        ).pack(pady=2, fill="x")
    
    # 자동 분석 (텍스트 변경될 때마다)
    def on_text_change(event=None):
        """텍스트 변경시 자동 분석"""
        root.after_idle(analyze_text)  # 유휴 시간에 실행
    
    text_widget.bind('<KeyRelease>', on_text_change)
    text_widget.bind('<Button-1>', on_text_change)
    
    # 초기 분석
    analyze_text()
    
    root.mainloop()

# Text 예제 실행 (주석 해제하여 테스트)
# create_text_examples()

print("=" * 30)

# 3. grid() 레이아웃 매니저
print("🔲 grid() 레이아웃 매니저")

def create_grid_examples():
    """grid() 레이아웃 예제"""
    root = tk.Tk()
    root.title("grid() 레이아웃 예제")
    root.geometry("500x400")
    
    # 제목
    title_label = tk.Label(
        root,
        text="grid() 레이아웃 매니저",
        font=("맑은 고딕", 16, "bold"),
        bg="navy",
        fg="white"
    )
    title_label.grid(row=0, column=0, columnspan=4, sticky="ew", pady=5)
    
    # 그리드 구성 (4x4)
    colors = [
        ["lightblue", "lightgreen", "lightyellow", "lightpink"],
        ["lightcoral", "lightgray", "lightsteelblue", "lightseagreen"],
        ["lightsalmon", "lightgoldenrodyellow", "lightcyan", "lightviolet"]
    ]
    
    labels = []
    
    # 그리드 셀들 생성
    for row in range(3):
        label_row = []
        for col in range(4):
            cell_text = f"({row+1}, {col+1})"
            
            label = tk.Label(
                root,
                text=cell_text,
                font=("맑은 고딕", 12, "bold"),
                bg=colors[row][col],
                relief="solid",
                bd=2,
                width=8,
                height=3
            )
            label.grid(row=row+1, column=col, padx=2, pady=2, sticky="nsew")
            label_row.append(label)
        
        labels.append(label_row)
    
    # 컨트롤 프레임
    control_frame = tk.Frame(root, bg="lightgray", relief="solid", bd=2)
    control_frame.grid(row=4, column=0, columnspan=4, sticky="ew", padx=5, pady=10)
    
    tk.Label(
        control_frame,
        text="그리드 조작 버튼",
        font=("맑은 고딕", 12, "bold"),
        bg="lightgray"
    ).pack(pady=5)
    
    button_frame = tk.Frame(control_frame, bg="lightgray")
    button_frame.pack(pady=5)
    
    def highlight_row(row_idx):
        """특정 행 강조"""
        for row in range(3):
            for col in range(4):
                if row == row_idx:
                    labels[row][col].config(relief="raised", bd=5)
                else:
                    labels[row][col].config(relief="solid", bd=2)
    
    def highlight_column(col_idx):
        """특정 열 강조"""
        for row in range(3):
            for col in range(4):
                if col == col_idx:
                    labels[row][col].config(relief="raised", bd=5)
                else:
                    labels[row][col].config(relief="solid", bd=2)
    
    def reset_grid():
        """그리드 초기화"""
        for row in range(3):
            for col in range(4):
                labels[row][col].config(relief="solid", bd=2)
    
    def show_grid_info():
        """그리드 정보 표시"""
        info = """
grid() 주요 옵션:
• row, column: 위치 (0부터 시작)
• rowspan, columnspan: 셀 합치기
• sticky: 정렬 ("n"북, "s"남, "e"동, "w"서)
• padx, pady: 외부 여백
• ipadx, ipady: 내부 여백

예: widget.grid(row=0, column=1, sticky="nsew")
        """
        messagebox.showinfo("grid() 정보", info)
    
    # 행/열 강조 버튼들
    row_frame = tk.Frame(button_frame, bg="lightgray")
    row_frame.pack(side="left", padx=10)
    
    tk.Label(row_frame, text="행 강조:", bg="lightgray").pack()
    for i in range(3):
        tk.Button(
            row_frame,
            text=f"행 {i+1}",
            command=lambda r=i: highlight_row(r),
            width=6
        ).pack(side="left", padx=1)
    
    col_frame = tk.Frame(button_frame, bg="lightgray")
    col_frame.pack(side="left", padx=10)
    
    tk.Label(col_frame, text="열 강조:", bg="lightgray").pack()
    for i in range(4):
        tk.Button(
            col_frame,
            text=f"열 {i+1}",
            command=lambda c=i: highlight_column(c),
            width=6
        ).pack(side="left", padx=1)
    
    # 기타 버튼들
    other_frame = tk.Frame(button_frame, bg="lightgray")
    other_frame.pack(side="left", padx=10)
    
    tk.Label(other_frame, text="기타:", bg="lightgray").pack()
    tk.Button(
        other_frame,
        text="초기화",
        command=reset_grid,
        width=8
    ).pack(padx=1)
    
    tk.Button(
        other_frame,
        text="도움말",
        command=show_grid_info,
        width=8
    ).pack(padx=1)
    
    # 그리드 가중치 설정 (창 크기 변경 시 확장)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    
    root.mainloop()

# grid() 예제 실행 (주석 해제하여 테스트)
# create_grid_examples()

print("=" * 30)

# 4. 이벤트 처리
print("⚡ 이벤트 처리")

def create_event_examples():
    """다양한 이벤트 처리 예제"""
    root = tk.Tk()
    root.title("이벤트 처리 예제")
    root.geometry("550x450")
    root.configure(bg="lightsteelblue")
    
    # 제목
    tk.Label(
        root,
        text="⚡ 이벤트 처리 예제 ⚡",
        font=("맑은 고딕", 16, "bold"),
        bg="lightsteelblue",
        fg="darkblue"
    ).pack(pady=10)
    
    # 이벤트 로그 영역
    log_frame = tk.Frame(root)
    log_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    tk.Label(log_frame, text="이벤트 로그:", font=("맑은 고딕", 12, "bold")).pack(anchor="w")
    
    log_text = tk.Text(
        log_frame,
        height=12,
        font=("Courier New", 10),
        bg="black",
        fg="lime",
        insertbackground="lime"
    )
    log_scrollbar = tk.Scrollbar(log_frame, orient="vertical", command=log_text.yview)
    log_text.config(yscrollcommand=log_scrollbar.set)
    
    log_text.pack(side="left", fill="both", expand=True)
    log_scrollbar.pack(side="right", fill="y")
    
    # 로그 함수
    def log_event(message):
        """이벤트 로그 추가"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        log_text.see(tk.END)  # 자동 스크롤
    
    # 초기 로그
    log_event("이벤트 처리 시스템 시작")
    log_event("다양한 위젯과 상호작용해보세요!")
    
    # 컨트롤 영역
    control_frame = tk.Frame(root, bg="lightsteelblue")
    control_frame.pack(fill="x", padx=10, pady=5)
    
    # 버튼 이벤트
    button_frame = tk.Frame(control_frame, bg="lightgray", relief="solid", bd=1)
    button_frame.pack(fill="x", pady=2)
    
    tk.Label(button_frame, text="버튼 이벤트:", font=("맑은 고딕", 11, "bold"), bg="lightgray").pack(side="left", padx=5)
    
    def button_left_click():
        log_event("🔘 버튼 왼쪽 클릭!")
    
    def button_right_click(event):
        log_event("🔘 버튼 오른쪽 클릭!")
    
    def button_double_click(event):
        log_event("🔘 버튼 더블 클릭!")
    
    event_button = tk.Button(
        button_frame,
        text="이벤트 버튼",
        command=button_left_click,
        bg="lightblue"
    )
    event_button.pack(side="left", padx=5)
    event_button.bind("<Button-3>", button_right_click)  # 오른쪽 클릭
    event_button.bind("<Double-Button-1>", button_double_click)  # 더블 클릭
    
    # Entry 이벤트
    entry_frame = tk.Frame(control_frame, bg="lightgray", relief="solid", bd=1)
    entry_frame.pack(fill="x", pady=2)
    
    tk.Label(entry_frame, text="입력 이벤트:", font=("맑은 고딕", 11, "bold"), bg="lightgray").pack(side="left", padx=5)
    
    event_entry = tk.Entry(entry_frame, width=20)
    event_entry.pack(side="left", padx=5)
    
    def on_key_press(event):
        log_event(f"⌨️ 키 입력: '{event.char}' (코드: {event.keycode})")
    
    def on_focus_in(event):
        log_event("📝 입력창에 포커스 들어옴")
        event_entry.config(bg="lightyellow")
    
    def on_focus_out(event):
        log_event("📝 입력창에서 포커스 나감")
        event_entry.config(bg="white")
    
    def on_enter(event):
        text = event_entry.get()
        log_event(f"⏎ Enter 키 입력! 내용: '{text}'")
        if text.lower() == "clear":
            log_text.delete(1.0, tk.END)
            log_event("로그가 지워졌습니다")
            event_entry.delete(0, tk.END)
    
    event_entry.bind("<KeyPress>", on_key_press)
    event_entry.bind("<FocusIn>", on_focus_in)
    event_entry.bind("<FocusOut>", on_focus_out)
    event_entry.bind("<Return>", on_enter)
    
    # 마우스 이벤트 영역
    mouse_frame = tk.Frame(control_frame, bg="lightgreen", relief="solid", bd=2)
    mouse_frame.pack(fill="x", pady=2)
    
    mouse_label = tk.Label(
        mouse_frame,
        text="마우스 이벤트 영역 - 여기서 마우스를 움직여보세요",
        font=("맑은 고딕", 11),
        bg="lightgreen",
        height=3
    )
    mouse_label.pack(fill="x", padx=5, pady=5)
    
    def on_mouse_enter(event):
        log_event("🐭 마우스가 영역에 들어왔습니다")
        mouse_label.config(bg="yellow", text="마우스가 여기 있어요!")
    
    def on_mouse_leave(event):
        log_event("🐭 마우스가 영역을 벗어났습니다")
        mouse_label.config(bg="lightgreen", text="마우스 이벤트 영역 - 여기서 마우스를 움직여보세요")
    
    def on_mouse_motion(event):
        x, y = event.x, event.y
        mouse_label.config(text=f"마우스 위치: ({x}, {y})")
    
    def on_mouse_click(event):
        x, y = event.x, event.y
        button = event.num
        log_event(f"🐭 마우스 버튼 {button} 클릭! 위치: ({x}, {y})")
    
    mouse_label.bind("<Enter>", on_mouse_enter)
    mouse_label.bind("<Leave>", on_mouse_leave)
    mouse_label.bind("<Motion>", on_mouse_motion)
    mouse_label.bind("<Button>", on_mouse_click)
    
    # 윈도우 이벤트
    def on_window_resize(event):
        if event.widget == root:  # 메인 윈도우만
            width, height = event.width, event.height
            log_event(f"🖼️ 윈도우 크기 변경: {width}x{height}")
    
    def on_window_close():
        log_event("🖼️ 윈도우 닫기 시도")
        result = messagebox.askyesno("종료 확인", "정말로 종료하시겠습니까?")
        if result:
            log_event("🖼️ 윈도우 종료!")
            root.destroy()
    
    root.bind("<Configure>", on_window_resize)
    root.protocol("WM_DELETE_WINDOW", on_window_close)
    
    # 키보드 이벤트 (전역)
    def on_global_key(event):
        key = event.keysym
        if key in ["F1", "F2", "F3"]:
            log_event(f"⌨️ 전역 키 이벤트: {key}")
            if key == "F1":
                messagebox.showinfo("도움말", "F1: 도움말\nF2: 로그 지우기\nF3: 프로그램 정보")
            elif key == "F2":
                log_text.delete(1.0, tk.END)
                log_event("로그가 지워졌습니다 (F2)")
            elif key == "F3":
                log_event("프로그램 정보 표시 (F3)")
    
    root.bind("<KeyPress>", on_global_key)