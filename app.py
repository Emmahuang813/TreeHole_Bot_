import tkinter as tk
from tkinter import scrolledtext
from groq import Groq

# ==========================================
# 1. 請在此處填入你剛剛申請的 Groq API Key 🔑
# ==========================================
API_KEY = "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"

# 初始化 Groq 客戶端
client = Groq(api_key=API_KEY)

# 2. 建立視窗與 UI 設計
window = tk.Tk()
window.title("🌙 深夜樹洞：你的心事垃圾桶")
window.geometry("500x650")
window.configure(bg="#1A1A2E") # 深夜藍背景

FONT_STYLE = ("Microsoft JhengHei", 12)
TITLE_FONT = ("Microsoft JhengHei", 16, "bold")

# 標題
title_label = tk.Label(window, text="這裡是樹洞，你可以說任何事...", font=TITLE_FONT, fg="#E2E2E2", bg="#1A1A2E", pady=20)
title_label.pack()

# 聊天顯示區
chat_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, width=50, height=20, font=FONT_STYLE,
    bg="#16213E", fg="#FFFFFF", padx=10, pady=10, state='disabled'
)
chat_area.pack(padx=20, pady=10)

# 輸入欄位
entry = tk.Entry(window, font=FONT_STYLE, width=35, bg="#0F3460", fg="white", insertbackground="white")
entry.pack(side=tk.LEFT, padx=(25, 0), pady=20)

# 3. 定義發送訊息的功能
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    
    # 顯示使用者訊息
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, f"🌟 你：\n{user_input}\n\n", "user_text")
    chat_area.tag_config("user_text", foreground="#00D2FF")
    chat_area.configure(state='disabled')
    entry.delete(0, tk.END)
    window.update()

    try:
        # 呼叫免費的 Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "你是一個貼心、溫暖、講話直率且真誠的深夜陪伴好朋友。當使用者分享心情時，請遵守：\n"
                        "1. 絕對不要用『像雲朵、像星空、像海浪』這種文青、文學的比喻，這樣很假。\n"
                        "2. 請用口語、接地氣、像真實好朋友在通訊軟體（如 LINE）上打字的語氣。\n"
                        "3. 優先直接同理對方的辛苦、幫對方抱不平（例如：天啊，這老闆也太過分了吧！）。\n"
                        "4. 不要給生硬的大道理，單純給予溫暖的拍拍與陪伴。\n"
                        "5. 每次回覆嚴格控制在 2-3 句話以內（約 60 字），可以適度加上『QQ』、『😭』等表情符號。"
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"喔喔，樹洞暫時聽不到聲音... (請檢查 API Key 是否正確。錯誤訊息: {str(e)})"

    # 顯示樹洞回覆
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, f"🍂 樹洞：\n{bot_reply}\n\n", "bot_text")
    chat_area.tag_config("bot_text", foreground="#FFD369")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)

# 送出按鈕
send_button = tk.Button(window, text="傾訴", command=send_message, bg="#E94560", fg="white", font=FONT_STYLE, activebackground="#FF2E63")
send_button.pack(side=tk.LEFT, padx=10)

# 綁定 Enter 鍵送出
window.bind('<Return>', lambda event: send_message())

window.mainloop()