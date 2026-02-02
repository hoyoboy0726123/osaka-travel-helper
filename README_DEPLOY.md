# 🚀 USJ 票價計算器 - 部署指南

## 本地測試
```bash
python3 web_app.py
# 訪問 http://localhost:5000
```

## 部署到 Render.com

1. **推送到 GitHub**
   ```bash
   git add web_app.py requirements.txt
   git commit -m "Add USJ calculator web app"
   git push
   ```

2. **在 Render.com**
   - 連接 GitHub repo
   - 選擇 Web Service
   - 啟動命令：`gunicorn web_app:app`
   - 完成！

## 檔案清單
- `web_app.py` - Flask 應用程式
- `requirements.txt` - Python 依賴
- `README_DEPLOY.md` - 本檔案
