from flask import Flask, render_template, request, url_for, flash, redirect
from distutils.log import debug
from fileinput import filename
from flask import * 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}]
    

@app.route('/')
def index():
    return render_template('base.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/file')  
def main():  
    return render_template("inn.html") 

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("upload.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug=True)