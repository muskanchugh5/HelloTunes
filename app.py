from flask import Flask,render_template,request,flash,redirect,url_for
import subprocess
# from forms import MusicSearchForm
# from models import Album
# from db_setup import init_db,db_session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
@app.route("/download/<var>")
def hello(var):
    cmd = ['spotdl','--song',var,'--avconv']
    p = subprocess.Popen(cmd,stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        stdin = subprocess.PIPE)
    out,err = p.communicate()
    if out:
        return "Success"
    else:
        return "Failure"

@app.route('/',methods=['GET','POST'])
def index():
    # form = ReusableForm(request.form)
    # if(request.method=='POST'):
    #     text=request.form['text']
    # if form.validate():
    #     downloader(textstr = form['text'])
    return render_template('index.html')

# class ReusableForm(Form):
    # name=TextField('Text':validators=[validators.required()])
    
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
        result = request.form.to_dict()
        return redirect(url_for('hello',var=result['query']))

if __name__ == '__main__':
    app.run(debug=True)