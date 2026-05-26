# TreeHole_Bot_
期末實作
# 🌙 深夜樹洞：情緒療癒機器人 (Midnight Tree Hole Bot)

> **2026 生成式 AI 應用實作期末報告**
> 
> 💡 *這是一個結合 Python GUI 介面與 Llama-3.3 大語言模型的深夜陪伴系統，專為緩解現代人深夜焦慮與情緒壓力而設計。*

---

## 👥 團隊分工與貢獻度

獨自創作。
111316109@gms.tcu.edu.tw 黃琬芸

---

### 🛠️ 實作項目
* **前端介面設計：** 使用 Python Tkinter 模組，獨自設計沉浸式深夜深色模式 GUI 視窗。
* **後端核心串接：** 串接 Groq Cloud API，獨立完成 Llama-3.3-70b-versatile 模型之異步請求與多輪對話邏輯。
* **提示詞工程優化：** 負責 System Role 提示詞的調校，成功實現「去文學化、高度共情、真誠口語」的人格特質。
* **系統除錯與運維：** 獨立分析並解決 Python PEP 668 環境保護衝突，並於部署至 GitHub 時即時啟動資安應變（金鑰去敏感化與憑證廢除）。

---

## 📸 成果展示 (Demo)

<img width="496" height="673" alt="image" src="https://github.com/user-attachments/assets/04552981-d967-4691-9159-42be6b96f5df" />

* 🌟 **對話範例 1：**
  * **使用者：** 「我今天好累。」
  * **樹洞：** 「天啊，這樣很辛苦吧 😭！還好現在有我陪你聊天QQ。休息一下吧！」

---

## 🛠️ 技術除錯經驗 (Debug Notes)

在開發本專案的過程中，團隊遇到了以下工程挑戰並成功解決：

* **挑戰 1：環境保護機制 (PEP 668)**
  * *問題：* 在安裝套件時遇到 `externally-managed-environment` 阻擋。
  * *解決：* 正確分析報錯，使用 `--break-system-packages` 強制參數成功解決環境衝突。
* **挑戰 2：資安憑證外洩 (Secret Scanning)**
  * *問題：* 上傳程式碼時遭 GitHub 偵測到內含實體 API Key。
  * *解決：* 團隊立即啟動應變，進行**「金鑰去敏感化（Masking）」**，將程式碼改為由外部輸入 Key，並至 Groq 控制台廢除外洩憑證，展現良好的資安意識。

---

## 📦 如何在本地端執行此專案

1. **安裝必要套件：**
   ```bash
   pip install groq
填入妳的 API Key：
打開 app.py，在 API_KEY 變數中填入妳的 Groq 憑證。

啟動程式：

```bash
  python app.py
```
---

### 💾 步驟 3：儲存變更 (Commit)
1. 貼上後，把裡面的 `[妳的名字]`、`[組員A]` 等中括號字眼，換成妳們組的實際姓名。
2. 滾動到網頁最下方，點擊綠色的 **"Commit changes..."** 按鈕，再按一次確認。

---
