from flask import Flask, render_template
app = Flask(__name__)
# THIS IS GOING TO MOVE IN THE FUTURE
@app.route('/') 
def hello_world():
    return render_template('index.html')#searches for a folder called templates and returns given file name as a string

@app.route('/claire')
def claire():
    return "Hello Claire"

@app.route('/name/<name>')#<>adds a variable in the route method
def name(name):
    print(name)
    return f"Hello {name}!"

@app.route('/name/<name>/<int:age>')
def name_age(name,age):
    #rendering template page, passing in some variables as key word argument (kwargs)
    return render_template('people.html', name = name, age = age)



# END OF MOVING AREA

#THIS MUST BE ON THE BOTTOM OF THIS FILE
if __name__=="__main__":
    app.run(debug=True)