from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    session['user'] = False
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
    account = User.get_one_by_email(data)
    session['user'] = account[0]
    return redirect('/welcome/' + str(User.get_one_by_email(data)[0]['id']))

@app.route('/process_login', methods=["POST"])
def process_login():
    data = {
        'email' : request.form['email'],
        'pword' : request.form['pword']
    }
    bool = False
    for user in User.get_all():
        if data['email'] == user.email:
            bool = True
            break
    if bool:
        account = User.get_one_by_email(data)
        if not bcrypt.check_password_hash(account[0]['password'], data['pword']):
            flash("Invalid password", "log")
            return redirect('/')
        else:
            session['user'] = account[0]
            return redirect('/welcome/' + str(User.get_one_by_email(data)[0]['id']))
    else:
        flash("No such email address is registered", "log")
        return redirect('/')

@app.route('/welcome/<int:id>')
def welcome(id):
    if not session['user']:
        flash("No user logged in", "log")
        return redirect('/')
    else:
        data = {
            'id' : id
        }
        return render_template('welcome.html', user = User.get_one(data)[0], recipes = Recipe.get_all())

@app.route('/view/<int:id>/<int:reid>')
def view(id, reid):
    if not session['user']:
        flash("No user logged in", "log")
        return redirect('/')
    else:
        redata = {
            'reid' : reid
        }
        data = {
            'id' : id
        }
        return render_template('view.html', user = User.get_one(data)[0], recipe = Recipe.get_one(redata)[0])

@app.route('/create/<int:id>')
def create(id):
    if not session['user']:
        flash("No user logged in", "log")
        return redirect('/')
    else:
        data = {
            'id' : id
        }
        return render_template('create.html', user = User.get_one(data)[0])

@app.route('/process_add_recipe/<int:id>', methods=["POST"])
def process_add_recipe(id):
    if not Recipe.validate_entry(request.form):
        return redirect('/create/' + str(id))
    iddata = {
        'id' : id
    }
    data = {
        'name' : request.form['name'],
        'description' : request.form['desc'],
        'instructions' : request.form['instr'],
        'date_made' : request.form['date'],
        'under' : request.form['under'],
        'posted_by' : User.get_one(iddata)[0]['first_name'],
        'user_id' : id
    }
    Recipe.save(data)
    account = User.get_one(iddata)
    session['user'] = account[0]
    return redirect('/welcome/' + str(User.get_one(iddata)[0]['id']))

@app.route('/edit/<int:id>/<int:reid>')
def edit(id, reid):
    if not session['user']:
        flash("No user logged in", "log")
        return redirect('/')
    else:
        redata = {
            'reid' : reid
        }
        data = {
            'id' : id
        }
        return render_template('edit.html', user = User.get_one(data)[0], recipe = Recipe.get_one(redata)[0])

@app.route('/process_edit_recipe/<int:id>/<int:reid>', methods=["POST"])
def process_edit(id, reid):
    if not Recipe.validate_entry(request.form):
        return redirect('/edit/' + str(id) + "/" + str(reid))
    data = {
        'name' : request.form['name'],
        'description' : request.form['desc'],
        'instructions' : request.form['instr'],
        'date_made' : request.form['date'],
        'under' : request.form['under'],
        'id' : id,
        'reid' : reid
    }
    Recipe.update(data)
    account = User.get_one(data)
    session['user'] = account[0]
    return redirect('/welcome/' + str(User.get_one(data)[0]['id']))

@app.route('/delete/<int:id>/<int:reid>')
def delete(id, reid):
    iddata = {
        'id' : id
    }
    data = {
        'reid' : reid
    }
    Recipe.delete(data)
    return redirect('/welcome/' + str(User.get_one(iddata)[0]['id']))
