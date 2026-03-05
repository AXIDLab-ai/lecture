
**[← Week 13](./week13.md) | [목차](lecture/04_PythonProgramming/lectureMap.md)**

Week 14: 미니 프로젝트

---

## 🎯 학습 목표

14주 과정의 마지막 주! 지금까지 배운 모든 내용을 종합하여 실전 프로젝트를 완성합니다:

1. **종합 기술 활용**: 변수부터 데이터베이스까지 모든 기술을 통합적으로 사용합니다
2. **실전 프로젝트 개발**: 실제 사용할 수 있는 완성도 높은 프로그램을 만듭니다
3. **문제 해결 능력**: 복합적인 문제를 분석하고 단계적으로 해결합니다
4. **코드 설계**: 객체지향 설계와 모듈화를 통해 유지보수 가능한 코드를 작성합니다
5. **사용자 인터페이스**: GUI와 사용자 경험을 고려한 프로그램을 개발합니다
6. **포트폴리오 구축**: 취업이나 진학에 활용할 수 있는 포트폴리오를 완성합니다

---

## 📚 14주 학습 내용 총정리

### 🎓 지금까지 배운 기술들

| 주차 | 핵심 기술 | 활용 분야 | 프로젝트 적용 |
|------|-----------|-----------|---------------|
| **Week 1** | Python 기초, IDLE | 개발 환경 | 모든 프로젝트 기반 |
| **Week 2** | input/output, 기본 프로그램 | 사용자 입출력 | 사용자 인터페이스 |
| **Week 3** | 변수, 데이터 타입 | 데이터 저장 | 모든 데이터 처리 |
| **Week 4** | 연산자, 표현식 | 계산과 논리 | 비즈니스 로직 |
| **Week 5** | 조건문 | 프로그램 제어 | 의사결정 시스템 |
| **Week 6** | 반복문 | 자동화 처리 | 대량 데이터 처리 |
| **Week 7** | 리스트, 튜플 | 데이터 구조 | 데이터 관리 |
| **Week 8** | 딕셔너리, 집합 | 고급 자료구조 | 복잡한 데이터 관리 |
| **Week 9** | 함수, 모듈 | 코드 재사용 | 모듈화 설계 |
| **Week 10** | tkinter GUI | 사용자 인터페이스 | 데스크톱 앱 |
| **Week 11** | 파일 입출력 | 데이터 영속성 | 설정, 로그 저장 |
| **Week 12** | 객체지향 프로그래밍 | 설계 패턴 | 확장 가능한 구조 |
| **Week 13** | 데이터베이스 | 체계적 데이터 관리 | 실전 데이터 시스템 |

### 🔧 통합 기술 스택

```
┌─────────────────────────────────────────────┐
│              사용자 인터페이스                │
│         (tkinter GUI / Console)            │
├─────────────────────────────────────────────┤
│              비즈니스 로직                   │
│    (클래스, 함수, 알고리즘, 데이터 구조)      │
├─────────────────────────────────────────────┤
│              데이터 처리                     │
│        (파일 I/O, 데이터베이스)              │
├─────────────────────────────────────────────┤
│              파이썬 기초                     │
│     (변수, 연산자, 제어문, 자료구조)          │
└─────────────────────────────────────────────┘
```

---

## 💡 프로젝트 선택 가이드

### 📊 난이도별 프로젝트 분류

| 난이도 | 프로젝트 | 주요 기술 | 예상 시간 | 적합한 학습자 |
|--------|----------|-----------|-----------|---------------|
| **⭐⭐☆** | 개인 일정 관리 | GUI + 파일 | 1.5시간 | GUI 위주 학습 원하는 분 |
| **⭐⭐⭐** | 학생 성적 관리 | OOP + DB | 2시간 | 체계적 설계 학습 원하는 분 |
| **⭐⭐☆** | 간단한 게임 | GUI + 로직 | 1.5시간 | 재미있는 프로젝트 원하는 분 |
| **⭐⭐☆** | 텍스트 분석 도구 | 파일 + 자료구조 | 1.5시간 | 데이터 분석에 관심 있는 분 |
| **⭐⭐⭐** | 미니 쇼핑몰 | 종합 기술 | 2시간+ | 모든 기술 통합 원하는 분 |

### 🎯 프로젝트 선택 기준

**시간이 부족한 경우**: 개인 일정 관리 → 간단한 게임 → 텍스트 분석 도구
**체계적 학습 원하는 경우**: 학생 성적 관리 → 미니 쇼핑몰
**포트폴리오 목적**: 미니 쇼핑몰 → 학생 성적 관리 → 개인 일정 관리

---

## 🚀 미니 프로젝트 모음 (2시간)

### 프로젝트 1: 개인 일정 관리 프로그램 📅

**사용 기술**: tkinter GUI + JSON 파일 저장 + 날짜 처리

```python
"""
📅 개인 일정 관리 프로그램
- GUI 기반 일정 관리
- JSON 파일로 데이터 저장
- 일정 추가/수정/삭제/검색 기능
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import os
from datetime import datetime, date, timedelta

class ScheduleManager:
    """일정 관리 메인 클래스"""
    
    def __init__(self):
        self.data_file = "schedules.json"
        self.schedules = self.load_schedules()
        
        # GUI 초기화
        self.root = tk.Tk()
        self.root.title("📅 개인 일정 관리")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.create_widgets()
        self.refresh_schedule_list()
    
    def load_schedules(self):
        """JSON 파일에서 일정 로드"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_schedules(self):
        """JSON 파일에 일정 저장"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.schedules, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            messagebox.showerror("오류", f"저장 실패: {e}")
            return False
    
    def create_widgets(self):
        """GUI 위젯 생성"""
        # 상단 프레임 (제목)
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill='x', pady=(0, 10))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="📅 나의 일정 관리", 
            font=('맑은 고딕', 20, 'bold'),
            fg='white', 
            bg='#2c3e50'
        )
        title_label.pack(expand=True)
        
        # 메인 컨테이너
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # 좌측 프레임 (일정 목록)
        left_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # 일정 목록 제목
        list_title = tk.Label(
            left_frame, 
            text="📋 일정 목록", 
            font=('맑은 고딕', 14, 'bold'),
            bg='white'
        )
        list_title.pack(pady=10)
        
        # 일정 목록 (Treeview)
        self.tree_frame = tk.Frame(left_frame)
        self.tree_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Treeview 설정
        columns = ('날짜', '시간', '제목', '중요도')
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', height=15)
        
        # 컬럼 설정
        self.tree.heading('날짜', text='날짜')
        self.tree.heading('시간', text='시간')
        self.tree.heading('제목', text='일정 제목')
        self.tree.heading('중요도', text='중요도')
        
        self.tree.column('날짜', width=100)
        self.tree.column('시간', width=80)
        self.tree.column('제목', width=200)
        self.tree.column('중요도', width=80)
        
        # 스크롤바
        scrollbar = ttk.Scrollbar(self.tree_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # 우측 프레임 (버튼들)
        right_frame = tk.Frame(main_frame, bg='#f0f0f0', width=200)
        right_frame.pack(side='right', fill='y')
        right_frame.pack_propagate(False)
        
        # 버튼 스타일 설정
        button_style = {
            'font': ('맑은 고딕', 12),
            'width': 15,
            'height': 2,
            'relief': 'raised',
            'bd': 2
        }
        
        # 버튼들
        buttons = [
            ("➕ 일정 추가", self.add_schedule, '#3498db'),
            ("✏️ 일정 수정", self.edit_schedule, '#f39c12'),
            ("🗑️ 일정 삭제", self.delete_schedule, '#e74c3c'),
            ("🔍 일정 검색", self.search_schedule, '#9b59b6'),
            ("📊 통계 보기", self.show_statistics, '#27ae60'),
            ("💾 내보내기", self.export_schedules, '#95a5a6')
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(
                right_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                **button_style
            )
            btn.pack(pady=10)
        
        # 하단 상태바
        self.status_var = tk.StringVar()
        self.status_var.set("📌 일정을 추가해보세요!")
        
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bg='#34495e',
            fg='white',
            font=('맑은 고딕', 10),
            relief='sunken',
            bd=1
        )
        status_bar.pack(fill='x', side='bottom')
    
    def refresh_schedule_list(self):
        """일정 목록 새로고침"""
        # 기존 항목 삭제
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 날짜순 정렬
        sorted_schedules = sorted(
            self.schedules, 
            key=lambda x: (x['date'], x['time'])
        )
        
        # 항목 추가
        for schedule in sorted_schedules:
            # 중요도에 따른 표시
            priority_display = {
                'high': '🔴 높음',
                'medium': '🟡 보통',
                'low': '🟢 낮음'
            }.get(schedule.get('priority', 'medium'), '🟡 보통')
            
            # 날짜 포맷팅
            try:
                date_obj = datetime.strptime(schedule['date'], '%Y-%m-%d')
                date_display = date_obj.strftime('%m/%d(%a)')
                
                # 오늘/내일 표시
                today = date.today()
                if date_obj.date() == today:
                    date_display = f"📍 {date_display}"
                elif date_obj.date() == today + timedelta(days=1):
                    date_display = f"⭐ {date_display}"
                    
            except:
                date_display = schedule['date']
            
            self.tree.insert('', 'end', values=(
                date_display,
                schedule['time'],
                schedule['title'],
                priority_display
            ))
        
        # 상태 업데이트
        total = len(self.schedules)
        today_count = len([s for s in self.schedules if s['date'] == str(date.today())])
        self.status_var.set(f"📊 총 {total}개 일정 | 오늘 일정 {today_count}개")
    
    def add_schedule(self):
        """일정 추가 다이얼로그"""
        dialog = ScheduleDialog(self.root, "일정 추가")
        if dialog.result:
            self.schedules.append(dialog.result)
            self.save_schedules()
            self.refresh_schedule_list()
            messagebox.showinfo("성공", "일정이 추가되었습니다!")
    
    def edit_schedule(self):
        """선택된 일정 수정"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("알림", "수정할 일정을 선택해주세요.")
            return
        
        # 선택된 항목의 인덱스 찾기
        item_values = self.tree.item(selection[0])['values']
        title = item_values[2]  # 제목으로 검색
        
        for i, schedule in enumerate(self.schedules):
            if schedule['title'] == title:
                dialog = ScheduleDialog(self.root, "일정 수정", schedule)
                if dialog.result:
                    self.schedules[i] = dialog.result
                    self.save_schedules()
                    self.refresh_schedule_list()
                    messagebox.showinfo("성공", "일정이 수정되었습니다!")
                break
    
    def delete_schedule(self):
        """선택된 일정 삭제"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("알림", "삭제할 일정을 선택해주세요.")
            return
        
        if messagebox.askyesno("확인", "정말로 이 일정을 삭제하시겠습니까?"):
            item_values = self.tree.item(selection[0])['values']
            title = item_values[2]
            
            self.schedules = [s for s in self.schedules if s['title'] != title]
            self.save_schedules()
            self.refresh_schedule_list()
            messagebox.showinfo("성공", "일정이 삭제되었습니다!")
    
    def search_schedule(self):
        """일정 검색"""
        keyword = simpledialog.askstring("검색", "검색할 키워드를 입력하세요:")
        if keyword:
            # 기존 항목 삭제
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # 검색 결과 표시
            results = [
                s for s in self.schedules 
                if keyword.lower() in s['title'].lower() or 
                   keyword.lower() in s.get('description', '').lower()
            ]
            
            for schedule in results:
                priority_display = {
                    'high': '🔴 높음',
                    'medium': '🟡 보통',
                    'low': '🟢 낮음'
                }.get(schedule.get('priority', 'medium'), '🟡 보통')
                
                self.tree.insert('', 'end', values=(
                    schedule['date'],
                    schedule['time'],
                    schedule['title'],
                    priority_display
                ))
            
            self.status_var.set(f"🔍 '{keyword}' 검색 결과: {len(results)}개")
            
            # 3초 후 전체 목록 복원
            self.root.after(3000, self.refresh_schedule_list)
    
    def show_statistics(self):
        """일정 통계 표시"""
        if not self.schedules:
            messagebox.showinfo("통계", "등록된 일정이 없습니다.")
            return
        
        # 통계 계산
        total = len(self.schedules)
        
        # 중요도별 통계
        priority_count = {'high': 0, 'medium': 0, 'low': 0}
        for schedule in self.schedules:
            priority_count[schedule.get('priority', 'medium')] += 1
        
        # 이번 주 일정
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        
        this_week = len([
            s for s in self.schedules 
            if week_start <= datetime.strptime(s['date'], '%Y-%m-%d').date() <= week_end
        ])
        
        # 다음 주 일정
        next_week_start = week_end + timedelta(days=1)
        next_week_end = next_week_start + timedelta(days=6)
        
        next_week = len([
            s for s in self.schedules 
            if next_week_start <= datetime.strptime(s['date'], '%Y-%m-%d').date() <= next_week_end
        ])
        
        stats_text = f"""📊 일정 통계
        
📋 전체 일정: {total}개

🎯 중요도별:
  🔴 높음: {priority_count['high']}개
  🟡 보통: {priority_count['medium']}개
  🟢 낮음: {priority_count['low']}개

📅 기간별:
  이번 주: {this_week}개
  다음 주: {next_week}개
  
💡 가장 바쁜 요일: {self.get_busiest_day()}
"""
        
        messagebox.showinfo("일정 통계", stats_text)
    
    def get_busiest_day(self):
        """가장 바쁜 요일 계산"""
        if not self.schedules:
            return "없음"
        
        weekdays = ['월', '화', '수', '목', '금', '토', '일']
        day_count = [0] * 7
        
        for schedule in self.schedules:
            try:
                date_obj = datetime.strptime(schedule['date'], '%Y-%m-%d')
                day_count[date_obj.weekday()] += 1
            except:
                continue
        
        if max(day_count) == 0:
            return "없음"
        
        busiest_day = day_count.index(max(day_count))
        return f"{weekdays[busiest_day]}요일 ({max(day_count)}개)"
    
    def export_schedules(self):
        """일정을 텍스트 파일로 내보내기"""
        if not self.schedules:
            messagebox.showinfo("내보내기", "내보낼 일정이 없습니다.")
            return
        
        try:
            filename = f"내_일정_{datetime.now().strftime('%Y%m%d')}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("📅 나의 일정표\n")
                f.write("=" * 50 + "\n\n")
                
                sorted_schedules = sorted(
                    self.schedules, 
                    key=lambda x: (x['date'], x['time'])
                )
                
                for schedule in sorted_schedules:
                    f.write(f"📅 날짜: {schedule['date']}\n")
                    f.write(f"⏰ 시간: {schedule['time']}\n")
                    f.write(f"📝 제목: {schedule['title']}\n")
                    f.write(f"🎯 중요도: {schedule.get('priority', '보통')}\n")
                    
                    if schedule.get('description'):
                        f.write(f"📄 설명: {schedule['description']}\n")
                    
                    f.write("-" * 30 + "\n\n")
            
            messagebox.showinfo("성공", f"일정이 '{filename}'으로 내보내기 완료!")
            
        except Exception as e:
            messagebox.showerror("오류", f"내보내기 실패: {e}")
    
    def run(self):
        """프로그램 실행"""
        self.root.mainloop()

class ScheduleDialog:
    """일정 추가/수정 다이얼로그"""
    
    def __init__(self, parent, title, schedule=None):
        self.result = None
        
        # 다이얼로그 창 생성
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("400x500")
        self.dialog.resizable(False, False)
        self.dialog.grab_set()  # 모달 다이얼로그
        
        # 부모 창 중앙에 배치
        self.dialog.transient(parent)
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 200
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 250
        self.dialog.geometry(f"+{x}+{y}")
        
        self.create_widgets(schedule)
        
        # 엔터 키로 저장
        self.dialog.bind('<Return>', lambda e: self.save_schedule())
        
        # 첫 번째 입력 필드에 포커스
        self.title_entry.focus_set()
        
        # 다이얼로그가 닫힐 때까지 대기
        self.dialog.wait_window()
    
    def create_widgets(self, schedule):
        """다이얼로그 위젯 생성"""
        main_frame = tk.Frame(self.dialog, bg='white', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # 제목
        title_label = tk.Label(
            main_frame, 
            text="✏️ 일정 정보를 입력하세요",
            font=('맑은 고딕', 14, 'bold'),
            bg='white'
        )
        title_label.pack(pady=(0, 20))
        
        # 입력 필드들
        fields = [
            ("📝 일정 제목", "title_entry"),
            ("📅 날짜 (YYYY-MM-DD)", "date_entry"),
            ("⏰ 시간 (HH:MM)", "time_entry"),
        ]
        
        for label_text, entry_name in fields:
            frame = tk.Frame(main_frame, bg='white')
            frame.pack(fill='x', pady=5)
            
            label = tk.Label(frame, text=label_text, font=('맑은 고딕', 10), bg='white', width=20, anchor='w')
            label.pack(side='left')
            
            entry = tk.Entry(frame, font=('맑은 고딕', 10), width=20)
            entry.pack(side='right')
            
            setattr(self, entry_name, entry)
        
        # 중요도 선택
        priority_frame = tk.Frame(main_frame, bg='white')
        priority_frame.pack(fill='x', pady=5)
        
        priority_label = tk.Label(priority_frame, text="🎯 중요도", font=('맑은 고딕', 10), bg='white', width=20, anchor='w')
        priority_label.pack(side='left')
        
        self.priority_var = tk.StringVar(value="medium")
        priority_combo = ttk.Combobox(
            priority_frame, 
            textvariable=self.priority_var,
            values=["low", "medium", "high"],
            state="readonly",
            width=17
        )
        priority_combo.pack(side='right')
        
        # 설명 입력
        desc_label = tk.Label(main_frame, text="📄 상세 설명", font=('맑은 고딕', 10), bg='white', anchor='w')
        desc_label.pack(fill='x', pady=(10, 5))
        
        self.desc_text = tk.Text(main_frame, height=8, width=40, font=('맑은 고딕', 10))
        self.desc_text.pack(fill='both', expand=True, pady=(0, 10))
        
        # 기존 값 설정 (수정 모드)
        if schedule:
            self.title_entry.insert(0, schedule.get('title', ''))
            self.date_entry.insert(0, schedule.get('date', ''))
            self.time_entry.insert(0, schedule.get('time', ''))
            self.priority_var.set(schedule.get('priority', 'medium'))
            self.desc_text.insert('1.0', schedule.get('description', ''))
        else:
            # 새 일정인 경우 오늘 날짜 기본값
            today = date.today().strftime('%Y-%m-%d')
            self.date_entry.insert(0, today)
            self.time_entry.insert(0, "09:00")
        
        # 버튼 프레임
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill='x', pady=(10, 0))
        
        save_btn = tk.Button(
            button_frame,
            text="💾 저장",
            command=self.save_schedule,
            bg='#3498db',
            fg='white',
            font=('맑은 고딕', 12),
            width=10,
            height=2
        )
        save_btn.pack(side='left', padx=(0, 10))
        
        cancel_btn = tk.Button(
            button_frame,
            text="❌ 취소",
            command=self.dialog.destroy,
            bg='#95a5a6',
            fg='white',
            font=('맑은 고딕', 12),
            width=10,
            height=2
        )
        cancel_btn.pack(side='right')
    
    def save_schedule(self):
        """일정 저장"""
        title = self.title_entry.get().strip()
        date_str = self.date_entry.get().strip()
        time_str = self.time_entry.get().strip()
        
        # 입력 검증
        if not title:
            messagebox.showerror("오류", "일정 제목을 입력해주세요.")
            self.title_entry.focus_set()
            return
        
        if not date_str:
            messagebox.showerror("오류", "날짜를 입력해주세요.")
            self.date_entry.focus_set()
            return
        
        # 날짜 형식 검증
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("오류", "날짜 형식이 올바르지 않습니다. (YYYY-MM-DD)")
            self.date_entry.focus_set()
            return
        
        # 시간 형식 검증
        if time_str:
            try:
                datetime.strptime(time_str, '%H:%M')
            except ValueError:
                messagebox.showerror("오류", "시간 형식이 올바르지 않습니다. (HH:MM)")
                self.time_entry.focus_set()
                return
        else:
            time_str = "09:00"  # 기본값
        
        # 결과 생성
        self.result = {
            'title': title,
            'date': date_str,
            'time': time_str,
            'priority': self.priority_var.get(),
            'description': self.desc_text.get('1.0', 'end-1c').strip()
        }
        
        self.dialog.destroy()

if __name__ == "__main__":
    print("📅 개인 일정 관리 프로그램을 시작합니다!")
    app = ScheduleManager()
    app.run()
```

---

### 프로젝트 2: 학생 성적 관리 시스템 🎓

**사용 기술**: 객체지향 프로그래밍 + SQLite 데이터베이스 + 통계 처리

```python
"""
🎓 학생 성적 관리 시스템
- 객체지향 설계 (클래스 활용)
- SQLite 데이터베이스
- 성적 통계 및 분석
- 사용자 친화적 콘솔 인터페이스
"""

import sqlite3
import os
from datetime import datetime
from statistics import mean, median
import json

class Student:
    """학생 클래스"""
    
    def __init__(self, student_id, name, grade, class_name=""):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.class_name = class_name
        self.scores = {}  # 과목별 점수
    
    def add_score(self, subject, score):
        """과목 점수 추가"""
        if 0 <= score <= 100:
            self.scores[subject] = score
            return True
        return False
    
    def get_average(self):
        """평균 점수 계산"""
        if not self.scores:
            return 0
        return round(mean(self.scores.values()), 2)
    
    def get_grade_rank(self):
        """성적 등급 반환"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        avg = self.get_average()
        rank = self.get_grade_rank()
        return f"{self.name} (ID: {self.student_id}) - 평균: {avg}점 ({rank}등급)"

class Subject:
    """과목 클래스"""
    
    def __init__(self, subject_id, name, credits=3, professor=""):
        self.subject_id = subject_id
        self.name = name
        self.credits = credits
        self.professor = professor
    
    def __str__(self):
        return f"{self.name} ({self.credits}학점, {self.professor})"

class GradeManager:
    """성적 관리 시스템 메인 클래스"""
    
    def __init__(self, db_name="grade_management.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.students = {}
        self.subjects = {}
        
        self.init_database()
        self.load_data()
    
    def init_database(self):
        """데이터베이스 초기화"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            # 학생 테이블
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    class_name TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # 과목 테이블
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    credits INTEGER DEFAULT 3,
                    professor TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # 점수 테이블
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    subject_id INTEGER,
                    score INTEGER CHECK (score >= 0 AND score <= 100),
                    exam_type TEXT DEFAULT '중간고사',
                    exam_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (student_id) REFERENCES students (id),
                    FOREIGN KEY (subject_id) REFERENCES subjects (id)
                )
            ''')
            
            self.conn.commit()
            print("✅ 데이터베이스 초기화 완료")
            
        except sqlite3.Error as e:
            print(f"❌ 데이터베이스 초기화 실패: {e}")
    
    def load_data(self):
        """데이터베이스에서 데이터 로드"""
        try:
            # 학생 로드
            self.cursor.execute("SELECT * FROM students")
            for row in self.cursor.fetchall():
                student_id, name, grade, class_name, _ = row
                student = Student(student_id, name, grade, class_name)
                self.students[student_id] = student
            
            # 과목 로드
            self.cursor.execute("SELECT * FROM subjects")
            for row in self.cursor.fetchall():
                subject_id, name, credits, professor, _ = row
                subject = Subject(subject_id, name, credits, professor)
                self.subjects[subject_id] = subject
            
            # 점수 로드
            self.cursor.execute("""
                SELECT student_id, subject_id, score 
                FROM scores
            """)
            for student_id, subject_id, score in self.cursor.fetchall():
                if student_id in self.students and subject_id in self.subjects:
                    subject_name = self.subjects[subject_id].name
                    self.students[student_id].add_score(subject_name, score)
            
            print(f"📚 데이터 로드 완료: 학생 {len(self.students)}명, 과목 {len(self.subjects)}개")
            
        except sqlite3.Error as e:
            print(f"❌ 데이터 로드 실패: {e}")
    
    def add_student(self, student_id, name, grade, class_name=""):
        """학생 추가"""
        try:
            if student_id in self.students:
                print(f"❌ 학번 {student_id}는 이미 존재합니다.")
                return False
            
            self.cursor.execute(
                "INSERT INTO students (id, name, grade, class_name) VALUES (?, ?, ?, ?)",
                (student_id, name, grade, class_name)
            )
            self.conn.commit()
            
            student = Student(student_id, name, grade, class_name)
            self.students[student_id] = student
            
            print(f"✅ 학생 추가 완료: {name} (학번: {student_id})")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 학생 추가 실패: {e}")
            return False
    
    def add_subject(self, subject_id, name, credits=3, professor=""):
        """과목 추가"""
        try:
            if subject_id in self.subjects:
                print(f"❌ 과목 ID {subject_id}는 이미 존재합니다.")
                return False
            
            self.cursor.execute(
                "INSERT INTO subjects (id, name, credits, professor) VALUES (?, ?, ?, ?)",
                (subject_id, name, credits, professor)
            )
            self.conn.commit()
            
            subject = Subject(subject_id, name, credits, professor)
            self.subjects[subject_id] = subject
            
            print(f"✅ 과목 추가 완료: {name} ({credits}학점)")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 과목 추가 실패: {e}")
            return False
    
    def add_score(self, student_id, subject_id, score, exam_type="중간고사"):
        """점수 추가"""
        try:
            if student_id not in self.students:
                print(f"❌ 학번 {student_id} 학생이 존재하지 않습니다.")
                return False
            
            if subject_id not in self.subjects:
                print(f"❌ 과목 ID {subject_id}가 존재하지 않습니다.")
                return False
            
            if not (0 <= score <= 100):
                print(f"❌ 점수는 0-100 사이여야 합니다. (입력값: {score})")
                return False
            
            # 기존 점수가 있으면 업데이트, 없으면 추가
            self.cursor.execute(
                "SELECT id FROM scores WHERE student_id=? AND subject_id=? AND exam_type=?",
                (student_id, subject_id, exam_type)
            )
            
            if self.cursor.fetchone():
                self.cursor.execute(
                    "UPDATE scores SET score=?, exam_date=CURRENT_TIMESTAMP WHERE student_id=? AND subject_id=? AND exam_type=?",
                    (score, student_id, subject_id, exam_type)
                )
                action = "수정"
            else:
                self.cursor.execute(
                    "INSERT INTO scores (student_id, subject_id, score, exam_type) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, score, exam_type)
                )
                action = "추가"
            
            self.conn.commit()
            
            # 메모리 업데이트
            subject_name = self.subjects[subject_id].name
            self.students[student_id].add_score(subject_name, score)
            
            student_name = self.students[student_id].name
            subject_name = self.subjects[subject_id].name
            print(f"✅ 점수 {action} 완료: {student_name} - {subject_name}: {score}점")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ 점수 추가 실패: {e}")
            return False
    
    def get_student_report(self, student_id):
        """학생별 성적표"""
        if student_id not in self.students:
            print(f"❌ 학번 {student_id} 학생이 존재하지 않습니다.")
            return
        
        student = self.students[student_id]
        
        print(f"\n📋 {student.name}님의 성적표")
        print("=" * 50)
        print(f"학번: {student.student_id}")
        print(f"학년: {student.grade}")
        print(f"반: {student.class_name}")
        print("-" * 50)
        
        if not student.scores:
            print("등록된 점수가 없습니다.")
            return
        
        print(f"{'과목명':<15} {'점수':>6} {'등급':>4}")
        print("-" * 30)
        
        total_credits = 0
        weighted_sum = 0
        
        for subject_name, score in student.scores.items():
            # 해당 과목의 학점 찾기
            credits = 3  # 기본값
            for subject in self.subjects.values():
                if subject.name == subject_name:
                    credits = subject.credits
                    break
            
            grade = self.score_to_grade(score)
            print(f"{subject_name:<15} {score:>6}점 {grade:>4}")
            
            total_credits += credits
            weighted_sum += score * credits
        
        print("-" * 30)
        print(f"평균 점수: {student.get_average():.2f}점")
        print(f"전체 등급: {student.get_grade_rank()}")
        
        if total_credits > 0:
            weighted_avg = weighted_sum / total_credits
            print(f"학점 가중 평균: {weighted_avg:.2f}점")
    
    def score_to_grade(self, score):
        """점수를 등급으로 변환"""
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "B+"
        elif score >= 80:
            return "B"
        elif score >= 75:
            return "C+"
        elif score >= 70:
            return "C"
        elif score >= 65:
            return "D+"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def get_class_ranking(self, grade=""):
        """반별 또는 전체 순위"""
        students_list = []
        
        for student in self.students.values():
            if grade and student.grade != grade:
                continue
            
            if student.scores:  # 점수가 있는 학생만
                students_list.append(student)
        
        # 평균 점수로 정렬
        students_list.sort(key=lambda s: s.get_average(), reverse=True)
        
        title = f"{grade} 순위" if grade else "전체 순위"
        print(f"\n🏆 {title}")
        print("=" * 60)
        print(f"{'순위':>4} {'학번':>8} {'이름':<10} {'평균':>6} {'등급':>4} {'과목수':>6}")
        print("-" * 60)
        
        for rank, student in enumerate(students_list, 1):
            print(f"{rank:>4} {student.student_id:>8} {student.name:<10} "
                  f"{student.get_average():>6.1f} {student.get_grade_rank():>4} "
                  f"{len(student.scores):>6}")
        
        return students_list
    
    def get_subject_statistics(self, subject_id):
        """과목별 통계"""
        if subject_id not in self.subjects:
            print(f"❌ 과목 ID {subject_id}가 존재하지 않습니다.")
            return
        
        subject = self.subjects[subject_id]
        subject_scores = []
        
        for student in self.students.values():
            if subject.name in student.scores:
                subject_scores.append(student.scores[subject.name])
        
        if not subject_scores:
            print(f"📊 {subject.name} 과목에 등록된 점수가 없습니다.")
            return
        
        print(f"\n📊 {subject.name} 과목 통계")
        print("=" * 40)
        print(f"담당교수: {subject.professor}")
        print(f"학점: {subject.credits}")
        print(f"응시 학생 수: {len(subject_scores)}명")
        print("-" * 40)
        
        avg_score = mean(subject_scores)
        median_score = median(subject_scores)
        max_score = max(subject_scores)
        min_score = min(subject_scores)
        
        print(f"평균 점수: {avg_score:.2f}점")
        print(f"중간 점수: {median_score:.2f}점")
        print(f"최고 점수: {max_score}점")
        print(f"최저 점수: {min_score}점")
        
        # 등급 분포
        grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for score in subject_scores:
            grade = self.score_to_grade(score)[0]  # A+, A 등에서 첫 글자만
            grade_count[grade] += 1
        
        print("\n등급 분포:")
        for grade, count in grade_count.items():
            percentage = (count / len(subject_scores)) * 100
            print(f"  {grade}등급: {count}명 ({percentage:.1f}%)")
    
    def export_to_excel_like_text(self, filename=None):
        """엑셀 형태의 텍스트 파일로 내보내기"""
        if filename is None:
            filename = f"성적표_{datetime.now().strftime('%Y%m%d')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("🎓 학생 성적 관리 시스템 - 종합 성적표\n")
                f.write("=" * 80 + "\n")
                f.write(f"생성일: {datetime.now().strftime('%Y년 %m월 %d일 %H:%M')}\n\n")
                
                # 전체 통계
                f.write("📊 전체 통계\n")
                f.write("-" * 20 + "\n")
                f.write(f"등록 학생 수: {len(self.students)}명\n")
                f.write(f"개설 과목 수: {len(self.subjects)}개\n\n")
                
                # 학생별 상세 성적
                f.write("📋 학생별 상세 성적\n")
                f.write("=" * 80 + "\n")
                
                for student in sorted(self.students.values(), key=lambda s: s.student_id):
                    f.write(f"\n학번: {student.student_id} | 이름: {student.name} | 학년: {student.grade}\n")
                    f.write("-" * 50 + "\n")
                    
                    if student.scores:
                        f.write(f"{'과목명':<20} {'점수':>8} {'등급':>6}\n")
                        f.write("-" * 35 + "\n")
                        
                        for subject_name, score in student.scores.items():
                            grade = self.score_to_grade(score)
                            f.write(f"{subject_name:<20} {score:>8}점 {grade:>6}\n")
                        
                        f.write("-" * 35 + "\n")
                        f.write(f"평균: {student.get_average():.2f}점 | 등급: {student.get_grade_rank()}\n")
                    else:
                        f.write("등록된 점수가 없습니다.\n")
                
                # 과목별 통계
                f.write("\n\n📊 과목별 통계\n")
                f.write("=" * 50 + "\n")
                
                for subject in self.subjects.values():
                    subject_scores = []
                    for student in self.students.values():
                        if subject.name in student.scores:
                            subject_scores.append(student.scores[subject.name])
                    
                    f.write(f"\n과목: {subject.name} ({subject.credits}학점, {subject.professor})\n")
                    
                    if subject_scores:
                        avg = mean(subject_scores)
                        f.write(f"응시자: {len(subject_scores)}명 | 평균: {avg:.2f}점\n")
                        f.write(f"최고점: {max(subject_scores)}점 | 최저점: {min(subject_scores)}점\n")
                    else:
                        f.write("응시자가 없습니다.\n")
            
            print(f"✅ 성적표가 '{filename}'으로 내보내기 완료!")
            return True
            
        except Exception as e:
            print(f"❌ 내보내기 실패: {e}")
            return False
    
    def close(self):
        """데이터베이스 연결 종료"""
        if self.conn:
            self.conn.close()

def run_grade_management_system():
    """성적 관리 시스템 실행"""
    print("🎓 학생 성적 관리 시스템을 시작합니다!")
    
    # 기존 DB 삭제 (데모용)
    if os.path.exists("grade_management.db"):
        os.remove("grade_management.db")
        print("🗑️ 기존 데이터베이스 삭제")
    
    manager = GradeManager()
    
    # 샘플 데이터 추가
    print("\n📚 샘플 데이터 추가 중...")
    
    # 과목 추가
    subjects_data = [
        (101, "파이썬프로그래밍", 3, "김교수"),
        (102, "데이터베이스", 3, "이교수"),
        (103, "자료구조", 3, "박교수"),
        (104, "알고리즘", 2, "최교수"),
        (105, "운영체제", 3, "정교수")
    ]
    
    for subject_id, name, credits, professor in subjects_data:
        manager.add_subject(subject_id, name, credits, professor)
    
    # 학생 추가
    students_data = [
        (20231001, "김철수", "3학년", "A반"),
        (20231002, "이영희", "3학년", "A반"),
        (20231003, "박민수", "3학년", "B반"),
        (20231004, "최지원", "3학년", "B반"),
        (20231005, "정다영", "2학년", "C반"),
        (20231006, "한상우", "2학년", "C반"),
        (20231007, "오세진", "2학년", "D반"),
        (20231008, "윤미라", "1학년", "E반")
    ]
    
    for student_id, name, grade, class_name in students_data:
        manager.add_student(student_id, name, grade, class_name)
    
    # 성적 추가
    print("\n📊 랜덤 성적 생성 중...")
    import random
    
    for student_id in range(20231001, 20231009):
        for subject_id in range(101, 106):
            if random.choice([True, True, False]):  # 70% 확률
                score = random.randint(60, 100)
                manager.add_score(student_id, subject_id, score)
    
    # 메뉴 시스템
    while True:
        print("\n" + "=" * 50)
        print("🎓 학생 성적 관리 시스템")
        print("=" * 50)
        print("1. 📋 학생별 성적표 조회")
        print("2. 🏆 순위 보기")
        print("3. 📊 과목별 통계")
        print("4. ➕ 새 학생 추가")
        print("5. ➕ 새 과목 추가")
        print("6. ✏️ 점수 입력/수정")
        print("7. 💾 성적표 내보내기")
        print("8. 📈 전체 현황")
        print("0. 🚪 종료")
        print("-" * 50)
        
        try:
            choice = input("메뉴를 선택하세요 (0-8): ").strip()
            
            if choice == '1':
                student_id = int(input("조회할 학번을 입력하세요: "))
                manager.get_student_report(student_id)
                
            elif choice == '2':
                grade = input("학년을 입력하세요 (전체 조회는 엔터): ").strip()
                manager.get_class_ranking(grade if grade else "")
                
            elif choice == '3':
                print("\n📚 과목 목록:")
                for subject_id, subject in manager.subjects.items():
                    print(f"{subject_id}: {subject.name}")
                
                subject_id = int(input("통계를 볼 과목 ID를 입력하세요: "))
                manager.get_subject_statistics(subject_id)
                
            elif choice == '4':
                student_id = int(input("학번을 입력하세요: "))
                name = input("이름을 입력하세요: ")
                grade = input("학년을 입력하세요: ")
                class_name = input("반을 입력하세요 (선택사항): ")
                manager.add_student(student_id, name, grade, class_name)
                
            elif choice == '5':
                subject_id = int(input("과목 ID를 입력하세요: "))
                name = input("과목명을 입력하세요: ")
                credits = int(input("학점을 입력하세요 (기본 3): ") or "3")
                professor = input("담당교수를 입력하세요 (선택사항): ")
                manager.add_subject(subject_id, name, credits, professor)
                
            elif choice == '6':
                student_id = int(input("학번을 입력하세요: "))
                
                print("\n📚 과목 목록:")
                for subject_id, subject in manager.subjects.items():
                    print(f"{subject_id}: {subject.name}")
                
                subject_id = int(input("과목 ID를 입력하세요: "))
                score = int(input("점수를 입력하세요 (0-100): "))
                exam_type = input("시험 유형 (기본 중간고사): ") or "중간고사"
                
                manager.add_score(student_id, subject_id, score, exam_type)
                
            elif choice == '7':
                filename = input("파일명을 입력하세요 (기본값: 자동생성): ").strip()
                manager.export_to_excel_like_text(filename if filename else None)
                
            elif choice == '8':
                print(f"\n📈 시스템 현황")
                print("=" * 30)
                print(f"총 학생 수: {len(manager.students)}명")
                print(f"총 과목 수: {len(manager.subjects)}개")
                
                # 성적 입력된 학생 수
                scored_students = sum(1 for s in manager.students.values() if s.scores)
                print(f"성적 입력 완료: {scored_students}명")
                
                # 평균 점수 계산
                all_averages = [s.get_average() for s in manager.students.values() if s.scores]
                if all_averages:
                    overall_avg = mean(all_averages)
                    print(f"전체 평균: {overall_avg:.2f}점")
                
            elif choice == '0':
                print("👋 성적 관리 시스템을 종료합니다.")
                break
                
            else:
                print("❌ 잘못된 선택입니다. 0-8 사이의 숫자를 입력하세요.")
                
        except ValueError:
            print("❌ 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            print("\n👋 프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류가 발생했습니다: {e}")
        
        input("\n계속하려면 엔터를 누르세요...")
    
    manager.close()

if __name__ == "__main__":
    run_grade_management_system()
```

---

### 프로젝트 3: 간단한 게임 (클릭 게임) 🎮

**사용 기술**: tkinter GUI + 게임 로직 + 타이머 + 점수 시스템

```python
"""
🎮 클릭 게임 (Whack-a-Mole 스타일)
- tkinter를 이용한 GUI 게임
- 타이머 기반 게임플레이
- 점수 시스템 및 하이스코어
- 레벨 시스템과 난이도 조절
"""

import tkinter as tk
from tkinter import messagebox
import random
import json
import os
from datetime import datetime

class ClickGame:
    """클릭 게임 메인 클래스"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 두더지 잡기 게임")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # 게임 상태
        self.score = 0
        self.level = 1
        self.time_left = 60
        self.game_running = False
        self.moles = []
        self.high_scores = self.load_high_scores()
        
        # 게임 설정
        self.mole_speed = 2000  # 두더지 등장 간격 (밀리초)
        self.mole_lifetime = 1500  # 두더지 생존 시간
        self.points_per_mole = 10
        
        self.create_widgets()
        self.update_display()
    
    def load_high_scores(self):
        """하이스코어 로드"""
        if os.path.exists("high_scores.json"):
            try:
                with open("high_scores.json", 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_high_scores(self):
        """하이스코어