from flask import Flask, render_template, redirect, request, session
# import the class from friend.py
from model.model_driver import Driver
app = Flask(__name__)
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
    print("I made it here")
    print(request.form)
    driver_id = Driver.create(request.form)
    return redirect ('/')

    # RESTFULL
    # table_name/id(if possible)/action
    # driver/new --> DISPLAY ROUTE
    # driver/create --> Creates a driver(ACTION ROUTE)
    # driver/<int:id> --> DISPLAY ROUTE
    # driver/<int:id>/edit --> DISPLAY ROUTE
    # driver/<int:id>/update --> ACTION ROUTE
    # driver/<int:id>/delete --> ACTION ROUTE

if __name__ == "__main__":
    app.run(debug=True)