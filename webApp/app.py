from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    user = 'Connor'
    return render_template('home.html', user=user)

@app.route('/cliff')
def cliff():
    return render_template('cliff.html')
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')