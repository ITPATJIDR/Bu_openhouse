from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return redirect(url_for('register'))

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        if User.query.filter_by(username=username).first():
            return "Username already exists!"

        new_user = User(username=username, password=password, firstname=firstname, lastname=lastname)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['firstname'] = user.firstname
            session['lastname'] = user.lastname
            return redirect(url_for('congratulation'))

        return "Invalid credentials", 403

    return render_template('login.html')

# Route for the congratulation page
@app.route('/congratulation')
def congratulation():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    firstname = session.get('firstname')
    lastname = session.get('lastname')
    return render_template('congratulation.html', firstname=firstname, lastname=lastname)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
