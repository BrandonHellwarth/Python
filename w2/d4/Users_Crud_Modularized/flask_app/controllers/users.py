from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
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

@app.route('/read_one/<int:id>')
def read_one(id):
    data = {
        "id":id
    }
    return render_template('read_one.html', user=User.get_one(data))

@app.route('/edit/<int:id>')
def displayedit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', user = User.get_one(data))

@app.route('/process/edit/<int:id>', methods = ["POST"])
def edit(id):
    data = {
        "id" : id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    User.edit(data)
    return redirect("/read_one/" + str(id))

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect("/")