from flask_blog import app,db
from flask import render_template, request, url_for,redirect, flash
from werkzeug.security import generate_password_hash,check_password_hash
from flask_blog.forms import RegistrationForm,LoginForm
from flask_blog.models import User
from flask_login import login_user,logout_user,login_required
posts = [
    {
        'author': 'Nkosingiphile Phungula',
        'title': 'Blog Post 1',
        'content': 'firs post content',
        'date_posted': 'April 21, 2018'
        
    }
]


@app.route('/')
@app.route('/index')
def index():
    user = {"name": "nkosingiphile"}
    return render_template('index.html', posts=posts, title='Home page', user=user)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email =form.email.data,password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if  user and check_password_hash(user.password,form.password.data):
            login_user(user=user,remember=form.remember.data)
            flash('You have been logged in!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html')