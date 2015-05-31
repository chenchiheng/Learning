#encoding:utf-8

from flask import Flask
from flask.ext.script import Manage
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
manage = Manage(app)
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')
    
    