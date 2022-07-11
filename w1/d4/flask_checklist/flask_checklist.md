# Pre-rec
```
In git bash:
pip install pipenv
```
# Checklist
- Create a folder / dir for your assignment
- Navigate into that folder
- create your virtual env
    ```
    pipenv install flask
    ```
- WARNING check for the files "pipfile" and "pipfile.lock"
    - If you dont see those you need to fix it right away!
-launch the virtual env
    ```
    pipenv shell or varient
    ```
- create a server.py file
    ```py
    from flask import Flask, render_template, request, redirect
    app = Flask(__name__)
    # THIS IS GOING TO MOVE IN THE FUTURE
    @app.route('/') 
    def hello_world():
        return 'Hello world!'
    # END OF MOVING AREA

    #THIS MUST BE ON THE BOTTOM OF THIS FILE
    if __name__=="__main__":
        app.run(debug=True)
    ```