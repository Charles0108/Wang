from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# 首页路由，展示“随机抽取”按钮
@app.route('/')
def index():
    return render_template_string("""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>随机抽取应用</title>
    </head>
    <body>
        <h1>随机抽取应用程序</h1>
        <button onclick="fetchResult()">随机抽取</button>
        <p id="result"></p>

        <script>
            // 使用AJAX请求来调用Python后端随机抽取函数
            function fetchResult() {
                fetch('/draw')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerText = "抽取结果：" + data.result;
                    });
            }
        </script>
    </body>
    </html>
    """)

# 随机抽取的路由
@app.route('/draw')
def draw():
    items = ['柯南', '小兰']
    selected_item = random.choice(items)
    return jsonify({"result": selected_item})

if __name__ == '__main__':
    app.run()
if __name__ == '__main__':
    app.run(debug=True)
