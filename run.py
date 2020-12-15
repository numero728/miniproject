from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', name='사용자명')


@app.route('/news')
def news():
    return render_template('news.html', name='사용자명')


@app.route('/index')
def index():
    return render_template('index.html', name='사용자명')


@app.route('/chat')
def chat():
    return render_template('chat.html', name='사용자명')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
