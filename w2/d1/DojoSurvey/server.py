from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'abcdefg'

@app.route('/') 
def root():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['Name']
    session['dojo_location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('info.html')

@app.route('/home', methods = ['POST'])
def home():
    return redirect('/')

#THIS MUST BE ON THE BOTTOM OF THIS FILE
if __name__=="__main__":
    app.run(debug=True)