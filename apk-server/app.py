from flask import Flask, send_file, render_template_string

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>앱 다운로드</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .download-btn {
                display: inline-block;
                padding: 15px 40px;
                font-size: 18px;
                color: white;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border: none;
                border-radius: 30px;
                text-decoration: none;
                cursor: pointer;
                transition: transform 0.3s;
            }
            .download-btn:hover {
                transform: scale(1.05);
            }
            .info {
                margin-top: 20px;
                color: #666;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📱 앱 다운로드</h1>
            <a href="/download" class="download-btn">⬇️ 다운로드</a>
            <p class="info">Android 기기에서 설치하세요</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

# APK 다운로드
@app.route('/download')
def download():
    return send_file('app.apk', as_attachment=True, download_name='app.apk')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
