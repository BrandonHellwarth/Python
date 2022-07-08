from flask import Flask 
app = Flask(__name__)
# THIS IS GOING TO MOVE IN THE FUTURE
@app.route('/') 
def hello_world():
    return 'Hello world!'
# END OF MOVING AREA

#THIS MUST BE ON THE BOTTOM OF THIS FILE
if __name__=="__main__":
    app.run(debug=True)