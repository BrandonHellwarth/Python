from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "abcdefg"

@app.route('/') 
def Counter():
    print(request.form)
    session['num'] = 0
    return render_template('index.html')

@app.route('/process_click', methods = ['POST'])
def process_click():
    session['num'] +=1
    return redirect('/newcount')

@app.route('/process_reset', methods = ['POST'])
def process_reset():
    return redirect('/')

@app.route('/newcount')
def new_count():
    return render_template('index.html')
    #THIS MUST BE ON THE BOTTOM OF THIS FILE
if __name__=="__main__":
    app.run(debug=True)