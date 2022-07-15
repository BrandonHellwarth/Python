from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.model.model_driver import Driver
# DISPLAY ROUTE
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_drivers = Driver.get_all()
    print(all_drivers)
    return render_template("index.html", all_drivers=all_drivers)
# ACTION ROUTE
@app.route('/driver/create', methods=['POST'])
def driver_create():
    driver_id = Driver.create(request.form)
    session['driver_id']
    return redirect ('/')

    # RESTFULL
    # table_name/id(if possible)/action
    # driver/new --> DISPLAY ROUTE
    # driver/create --> Creates a driver(ACTION ROUTE)
    # driver/<int:id> --> DISPLAY ROUTE
    # driver/<int:id>/edit --> DISPLAY ROUTE
    # driver/<int:id>/update --> ACTION ROUTE
    # driver/<int:id>/delete --> ACTION ROUTE