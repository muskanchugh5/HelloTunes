from flask import Flask, redirect, url_for, request, render_template
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER']='/static'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

@app.route('/score/<int:score>')
def hello_score(score):
    return render_template('hello.html',marks=score)

@app.route('/hello/<user>')
def hello(user):
    return render_template('hello.html',name=user)

@app.route('/result')
def result():
    dict = {'phy':50,'che':60,'math':70}
    return render_template('dict.html',result=dict)

@app.route('/upload')
def upload_f():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug = True)