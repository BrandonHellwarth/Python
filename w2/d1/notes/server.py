from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "shhhhhhhhhhh"#need this statement to use session(session is a global dictionary, compared to normal dictionary, it can be used by all functions while being embeded in one)


#Action Route
@app.route("/")
def hello_world():
    name = "brandon"
    return render_template('index.html', name=name)

#Display Route
@app.route('/process_info', methods=['POST'])
def process_info():
    print(f"You have now purchased a new {request.form['item']}!")
    print(request.form)
    # credit_card_number = request.form['credit_card_number']
    session['ccn'] = str(request.form['credit_card_number'])[-4:]
    #what you want to do
    return redirect('/tracking_info')
    #not what you want to do here
    #return render_template('index.html')

@app.route('/tracking_info')
def tracking_info():
    print("Your card number is: ")
    # print(session['ccn'])
    if 'ccn' not in session: #will redirect to main page if ccn cookie is deleted
        return redirect('/')
    #if session['ccn']: wont work if there is nothing there
    return render_template('tracking.html')

if __name__=="__main__":
    app.run(debug=True)