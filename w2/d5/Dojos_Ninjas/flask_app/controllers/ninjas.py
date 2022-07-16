from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def home():
    return render_template("dojo.html", dojos = Dojo.get_all())

@app.route("/dojo_show/<int:id>")
def dojo_show(id):
    data = {
        "id" : id
    }
    return render_template("dojo_show.html", dojo = Dojo.get_dojo_with_ninjas(data))

@app.route("/process_dojo", methods = ["POST"])
def process():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")

@app.route("/add_ninja")
def new_ninja():
    return render_template("new_ninja.html", dojos = Dojo.get_all())

@app.route("/process_ninja", methods = ["POST"])
def process_ninja():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "djid" : request.form["dojo"]
    }
    Ninja.save(data)
    return redirect("/dojo_show/" + str(data["djid"]))