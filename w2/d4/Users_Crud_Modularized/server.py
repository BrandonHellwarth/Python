from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from flask_app.models.users import User
app = Flask(__name__)
@app.route("/")
def read():
    # call the get all classmethod to get all friends
    return render_template("Read.html", users = User.get_all())

@app.route('/create_user')
def create_user():
    return render_template("Create.html")

@app.route('/process', methods=["POST"])
def process():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect("/")

@app.route('/process_user', methods = ["POST"])
def process_user():
    id = request.form["span"]
    session['user'] = User.get_one(id)
    return redirect("/read_one")

@app.route('/read_one')
def read_one():
    return render_template('read_one.html', user = session['user'])

if __name__ == "__main__":
    app.run(debug=True)