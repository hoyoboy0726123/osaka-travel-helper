# 🚀 5分鐘部署 USJ 票價計算器到 Render

## 📦 已準備好的檔案

✅ 所有檔案已推送到 GitHub：
**https://github.com/hoyoboy0726123/osaka-travel-helper**

包含：
- `web_app.py` - Flask 應用程式（含前端）
- `requirements.txt` - Python 依賴清單
- `README_DEPLOY.md` - 部署說明

---

## 🎯 部署步驟（超簡單！）

### **Step 1: 訪問 Render**
🌐 打開瀏覽器，前往：https://render.com

### **Step 2: 註冊/登入**
- 點擊「Sign Up」或「Log In」
- **建議：用 GitHub 帳號登入**（最方便）

### **Step 3: 新增 Web Service**
1. 登入後，點擊 **「New +」**
2. 選擇 **「Web Service」**

### **Step 4: 連接 GitHub Repo**
1. 選擇「Connect a repository」
2. 找到並選擇 **「osaka-travel-helper」**
3. 點擊 **「Connect」**

### **Step 5: 設定服務**

填寫以下資訊：

| 欄位 | 填入內容 |
|------|----------|
| **Name** | `usj-calculator`（或任何你喜歡的名字） |
| **Region** | `Singapore (Southeast Asia)`（最接近台灣） |
| **Branch** | `master` |
| **Root Directory** | 留空 |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn web_app:app` |

### **Step 6: 選擇方案**
- **Free（免費方案）** ✅
  - 足夠使用！
  - 15 分鐘無活動會休眠
  - 首次訪問需等 30 秒喚醒

### **Step 7: 部署！**
- 點擊 **「Create Web Service」**
- 等待 2-3 分鐘部署完成
- ✅ 完成！會得到一個網址，例如：
  `https://usj-calculator.onrender.com`

---

## 🎉 部署完成後

訪問你的網站網址，你會看到：

```
🎢 USJ 票價計算器
👨‍👩‍👧‍👦 成人人數（12歲以上）
👶 兒童人數（4-11歲）
📅 票價類型
💰 計算總價
```

輸入人數 → 點計算 → 立即顯示日幣和台幣價格！

---

## ⚙️ 進階設定（選用）

### 自訂網域名稱
1. 在 Render Dashboard 點你的服務
2. 進入「Settings」
3. 在「Custom Domain」新增你的網域

### 環境變數
如果需要設定 API Key 等：
1. 「Settings」→「Environment」
2. 新增環境變數

---

## 🆘 常見問題

**Q: 免費方案有限制嗎？**
A: 會休眠，但對個人使用完全足夠！

**Q: 第一次訪問很慢？**
A: 正常！休眠喚醒需要 30 秒。之後就快了。

**Q: 如何更新程式碼？**
A: 推送新 commit 到 GitHub，Render 會自動重新部署！

```bash
git add .
git commit -m "更新功能"
git push
# Render 會自動偵測並部署
```

**Q: 需要付費嗎？**
A: 免費方案完全夠用！除非需要不休眠或更多資源。

---

## 📱 分享你的計算器

部署完成後，你可以：
- 📲 分享網址給親友
- 🔗 加到旅遊助手網頁
- 📱 加入手機主畫面（PWA）

---

## 🎁 額外功能建議

想要更多功能嗎？我可以幫你加：
- 💾 儲存計算歷史
- 📊 預算規劃工具
- 🗓️ 整合行程表
- 🎫 其他景點票價

**就告訴我！** 😊
