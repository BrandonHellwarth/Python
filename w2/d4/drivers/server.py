from flask_app import app
from flask_app.controllers import controller_car, controller_driver
if __name__ == "__main__":
    app.run(debug=True)