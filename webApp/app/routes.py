from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm



@app.route('/')
def root():
    return redirect('/login')

@app.route('/index')
def index():
    flash('flash is downloaded!')
    return render_template('index.html')

@app.route('/home')
def home():
    user='Connor'
    return render_template('home.html', user=user)

@app.route('/cliff')
def cliff():
    return render_template('cliff.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')