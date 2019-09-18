from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'name':'lonel'}
    return render_template('index.html',title='Home',user=user)

@app.route('/login',methods=['GET','POST'])
def login():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for OpenID="' + login_form.openid.data + '", remember_me=' + str(login_form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=login_form,providers = app.config['OPENID_PROVIDERS'])