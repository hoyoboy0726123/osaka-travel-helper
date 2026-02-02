#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
USJ 票價計算器 - Flask Web App
可以部署到 Render.com
"""
from flask import Flask, render_template_string, request
import json

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎢 USJ 票價計算器</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 { color: #333; margin-bottom: 20px; text-align: center; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #666; font-weight: bold; }
        input, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #eee;
            border-radius: 10px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover { transform: scale(1.02); }
        .result {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        .price { font-size: 24px; color: #667eea; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎢 USJ 票價計算器</h1>
        <form method="POST">
            <div class="form-group">
                <label>👨‍👩‍👧‍👦 成人人數（12歲以上）</label>
                <input type="number" name="adults" value="{{ adults }}" min="0" required>
            </div>
            <div class="form-group">
                <label>👶 兒童人數（4-11歲）</label>
                <input type="number" name="children" value="{{ children }}" min="0" required>
            </div>
            <div class="form-group">
                <label>📅 票價類型</label>
                <select name="ticket_type">
                    <option value="weekday">平日（¥8,400/¥5,400）</option>
                    <option value="weekend">週末（¥9,200/¥5,900）</option>
                    <option value="peak">高價日（¥9,800/¥6,300）</option>
                </select>
            </div>
            <button type="submit">💰 計算總價</button>
        </form>
        
        {% if total %}
        <div class="result">
            <h2>計算結果</h2>
            <p>成人票 x {{ adults }}: <span class="price">¥{{ adult_total }}</span></p>
            <p>兒童票 x {{ children }}: <span class="price">¥{{ child_total }}</span></p>
            <hr style="margin: 15px 0;">
            <p>總計（日幣）: <span class="price">¥{{ total }}</span></p>
            <p>約台幣: <span class="price">NT${{ twd }}</span></p>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        adults = int(request.form.get('adults', 0))
        children = int(request.form.get('children', 0))
        ticket_type = request.form.get('ticket_type', 'weekday')
        
        # 票價對照表
        prices = {
            'weekday': {'adult': 8400, 'child': 5400},
            'weekend': {'adult': 9200, 'child': 5900},
            'peak': {'adult': 9800, 'child': 6300}
        }
        
        price = prices[ticket_type]
        adult_total = adults * price['adult']
        child_total = children * price['child']
        total = adult_total + child_total
        twd = int(total / 4.65)
        
        return render_template_string(HTML_TEMPLATE, 
            adults=adults, children=children,
            adult_total=f"{adult_total:,}",
            child_total=f"{child_total:,}",
            total=f"{total:,}",
            twd=f"{twd:,}"
        )
    
    return render_template_string(HTML_TEMPLATE, adults=2, children=2, total=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
