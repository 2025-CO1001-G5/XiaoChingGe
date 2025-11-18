import customtkinter as ctk
import threading
import time

class Window:
    def __init__(self):
        # 設定主題與顏色模式
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # 主視窗
        self.app = ctk.CTk()
        self.app.title("小琴歌")
        self.app.state("zoomed")  # Windows 會最大化

        # 建立三個 Frame
        self.page1 = ctk.CTkFrame(self.app)
        self.page2 = ctk.CTkFrame(self.app)
        self.page3 = ctk.CTkFrame(self.app)

        for frame in (self.page1, self.page2, self.page3):
            frame.grid(row=0, column=0, sticky="nsew")

        # 允許主視窗在放大時，三個頁面自動調整大小
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

    def generate(self):
        self.generate_page1()
        self.generate_page2()
        self.generate_page3()
        self.page1.tkraise()

    def mainloop(self):
        self.app.mainloop()

    def generate_page1(self):
        # ===== 第1頁：主選單 =====
        label1 = ctk.CTkLabel(self.page1, text="🏠 PIANO MASTER", font=ctk.CTkFont(size=64, weight="bold"))
        label1.pack(pady=60)

        btn_start = ctk.CTkButton(self.page1, text="開始", width=350, height=100, font=ctk.CTkFont(size=32),
                                  command=lambda: self.page3.tkraise())
        btn_start.pack(pady=20)

        btn_help = ctk.CTkButton(self.page1, text="使用說明", width=350, height=100, font=ctk.CTkFont(size=32),
                                 command=lambda: self.page2.tkraise())
        btn_help.pack(pady=20)
        return

    def generate_page2(self):
        label2 = ctk.CTkLabel(self.page2, text="📖 使用說明", font=ctk.CTkFont(size=64, weight="bold"))
        label2.pack(pady=40)

        help_text = ctk.CTkTextbox(self.page2, width=1000, height=400, font=ctk.CTkFont(size=26))
        help_text.insert("0.0",
                         "🎹 使用說明：\n\n"
                         "操作方式：\n"
                         "　・透過鍵盤按鍵發出對應的聲音。\n"
                         "　・當你按下某個按鍵時，螢幕上對應的按鈕會閃爍變色以提示輸入成功。\n\n"
                         "音域對照：\n"
                         "　中央音階：\n"
                         "　　Q → Do\n　　W → Re\n　　E → Mi\n　　R → Fa\n　　T → Sol\n　　Y → La\n　　U → Si\n\n"
                         "　高音音階：\n"
                         "　　I → Do\n　　O → Re\n　　P → Mi\n　　[ → Fa\n　　Z → Sol\n　　X → La\n　　C → Si\n\n"
                         "　高高音音階：\n"
                         "　　V → Do\n　　B → Re\n　　N → Mi\n　　M → Fa\n　　,  → Sol\n　　.  → La\n　　/  → Si\n\n"
                         "升降記號：\n"
                         "　　2 → #Do\n　　3 → #Re\n　　5 → #Fa\n　　6 → #Sol\n　　7 → #La\n"
                         "　　9 → 高音#Do\n　　0 → 高音#Re\n　　A → 高音#Fa\n　　S → 高音#Sol\n　　D → 高音#La\n　　G → 高高音#Do\n　　H → 高高音#Re\n　　K → 高高音#Fa\n　　L → 高高音#Sol\n　　;  → 高高音#La\n\n"
                         "小技巧：\n"
                         "　・請使用英文輸入法、使用Caps Lock。\n"
                         "　・使用支援按多個鍵的KEYBOARD。\n"
                         "　・建議開啟全螢幕使用，體驗更佳！"
                         )
        help_text.configure(state="disabled")
        help_text.pack(pady=20)

        help_text.tag_add("red_title", "1.2", "1.7")  # 第一行的「使用說明」文字範圍
        help_text.tag_add("red_tips", "53.1", "53.23")  # 「小技巧」那一行（依實際行數調整）
        help_text.tag_add("red_tips", "54.1", "54.23")  # 「小技巧」那一行（依實際行數調整）
        help_text.tag_add("red_tips", "55.1", "55.23")  # 「小技巧」那一行（依實際行數調整）
        help_text.tag_config("red_title", foreground="red")
        help_text.tag_config("red_tips", foreground="red")

        help_text.configure(state="disabled")

        btn_back = ctk.CTkButton(self.page2, text="返回", width=280, height=80, font=ctk.CTkFont(size=32),
                                 command=lambda: self.page1.tkraise())
        btn_back.pack(pady=30)

        return

    def generate_page3(self):
        label3 = ctk.CTkLabel(self.page3, text="🎹 Let's PLAY !!!", font=ctk.CTkFont(size=64, weight="bold"))
        label3.pack(pady=30)

        # === 鍵盤排列設計（每列不同數量） ===
        key_rows = [
            ["2", "3", "5", "6", "7", "9", "0"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "["],
            ["A", "S", "D", "G", "H", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
        ]

        buttons = {}
        keyboard_frame = ctk.CTkFrame(self.page3)
        keyboard_frame.pack(pady=20)

        # 建立多列按鈕
        for r, row_keys in enumerate(key_rows):
            row_frame = ctk.CTkFrame(keyboard_frame)
            row_frame.pack(pady=5)
            for key in row_keys:
                btn = ctk.CTkButton(
                    row_frame,
                    text=key,
                    width=70,
                    height=70,
                    font=ctk.CTkFont(size=24, weight="bold"),
                    fg_color="gray60",
                    hover_color="gray50"
                )
                btn.pack(side="left", padx=6)
                buttons[key.lower()] = btn  # 小寫方便比對鍵盤輸入

        # === 鍵盤事件 ===
        def on_key_press(event):
            key = event.keysym.lower()
            if key in buttons:
                btn = buttons[key]
                btn.configure(fg_color="gold")
                threading.Thread(target=lambda: reset_button(btn), daemon=True).start()

        def reset_button(btn):
            time.sleep(0.17)
            btn.configure(fg_color="gray60")

        self.app.bind("<KeyPress>", on_key_press)

        # 回主選單
        btn_home = ctk.CTkButton(
            self.page3,
            text="Home",
            width=280,
            height=80,
            font=ctk.CTkFont(size=32),
            command=lambda: self.page1.tkraise()
        )
        btn_home.pack(pady=30)
