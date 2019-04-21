# coding=utf-8
import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
from flask_wtf import FlaskForm

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"
bootstrap = Bootstrap(app)

from wtforms import StringField, SubmitField

# 导入相关验证器

from wtforms.validators import Length


# 创建表单类

class NameForm(FlaskForm):
  # name = StringField('用户名')
  # submit = SubmitField('提交')
  name = StringField('用户名', validators=[Length(3, 6, message='用户名必须是3~6个字符')])
  submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    form = NameForm()
    return render_template('form.html', form=form)

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
