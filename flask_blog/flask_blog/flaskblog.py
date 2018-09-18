'''
Created on Jun 30, 2018

@author: Yan
'''

from flask import Flask, render_template, url_for
from .forms import registrationform, loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = '12d8822e1ace6826867e470a7c78f5c1'

posts = [
    {
        'author': 'kaime mzii',
        'title': 'blog post 1',
        'content': 'fitst post content',
        'date': 'april 20, 2018'
    },
    {
        'author': 'dope mkali',
        'title': 'blog post 2',
        'content': 'second post content',
        'date': 'april 20, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = registrationform()
    return render_template('register.html', title='register', form=form)


@app.route("/login")
def login():
    form = loginform()
    return render_template('login.html', title='login', form=form)
