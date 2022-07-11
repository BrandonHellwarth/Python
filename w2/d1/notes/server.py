from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#Action Route
@app.route("/")
def hello_world():
    name = "brandon"
    return render_template('index.html', name=name)

#Display Route
@app.route('/process_info', methods=['POST'])
def process_info():
    print(f"You have now purchased a new {request.form['item']}!")
    #what you want to do
    return redirect('/tracking_info')
    #not what you want to do here
    #return render_template('index.html')

@app.route('/tracking_info')
def tracking_info():
    return render_template('tracking.html')

if __name__=="__main__":
    app.run(debug=True)