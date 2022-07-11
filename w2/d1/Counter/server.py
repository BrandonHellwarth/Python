from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "abcdefg"

@app.route('/') 
def Counter():
    session['visits'] = 1
    session['num'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    return redirect('/')

@app.route('/process_click', methods = ['POST'])
def process_click():
    session['visits'] +=1
    session['num'] +=1
    return redirect('/newcount')

@app.route('/process_plustwo', methods = ['POST'])
def process_plustwo():
    session['visits'] +=1
    session['num'] +=2
    return redirect('/newcount2')

@app.route('/process_custom', methods = ['POST'])
def process_custom():
    session['visits'] +=1
    session['num'] += int(request.form['custom'])
    return redirect('/newcountcustom')

@app.route('/process_reset', methods = ['POST'])
def process_reset():
    return redirect('/')

@app.route('/newcount')
def new_count():
    return render_template('index.html')

@app.route('/newcount2')
def new_count2():
    return render_template('index.html')

@app.route('/newcountcustom')
def newcountcustom():
    return render_template('index.html')

    #THIS MUST BE ON THE BOTTOM OF THIS FILE
if __name__=="__main__":
    app.run(debug=True)