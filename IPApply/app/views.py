#encoding:utf-8

from flask import Flask, render_template, abort, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.wtf import Form
import wtforms
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
app.config['SECRET_KEY'] = 'caibudaoacaibudao'

@app.route('/index/<name>')
def index(name):
    if 'error' == name:
        abort(500)
    return render_template('user.html', name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_erorr(e):
    return render_template('error.html'), 500  
 
@app.route('/name/<name>', methods=['GET', 'POST'])
def getName(name): 
    name = None
    form=NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash(u"名字%s就是D啊" % session.get('name'))
        return redirect(url_for('getName', name=session.get('name')))
    return render_template('name.html', name=session.get('name'), form=form)
    
class NameForm(Form):
    name = wtforms.StringField(u'我次要内木？', validators=[Required()])
    passwd = wtforms.PasswordField(u'搞个密码：', validators=[Required()])
#    mydate = wtforms.DateField(u'时间：')
#    myfile = wtforms.FileField(u'搞个文件')
    apply_reason = wtforms.TextAreaField(u'说吧，为啥申请IP！')
    submit = wtforms.SubmitField('Submit')
    
if __name__ == "__main__":
    manager.run()