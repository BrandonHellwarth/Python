from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_register', methods=["POST"])
def process_register():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
        'pword' : bcrypt.generate_password_hash(request.form['pword'])
    }
    all_users = User.get_all()
    for user in all_users:
        if data['email'] == user.email:
            flash("Email address is already registerd to an account.", "reg")
            return redirect('/')
    User.save(data)
    session['user'] = data
    return redirect('/welcome/' + str(User.get_one_by_email(data)[0]['id']))

@app.route('/process_login', methods=["POST"])
def process_login():
    if not User.validate_login(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email'],
        'pword' : request.form['pword']
    }
    account = User.get_one_by_email(data)
    if not bcrypt.check_password_hash(account[0]['password'], data['pword']):
        flash("Invalid password", "log")
        return redirect('/')
    else:
        session['user'] = data
        return redirect('/welcome/' + str(User.get_one_by_email(data)[0]['id']))

@app.route('/welcome/<int:id>')
def welcome(id):
    if not session:
        flash("No user logged in", "log")
        return redirect('/')
    else:
        data = {
            'id' : id
        }
        return render_template('welcome.html', user = User.get_one(data)[0])

@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect('/')