## Flask Application with User Authentication

### Overview

This Flask application provides basic user registration and login functionalities. It uses SQLAlchemy for database management, Bcrypt for password hashing, and CORS for handling cross-origin requests.

### Code Breakdown

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
```

```python 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
```

```python 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)
```

```python 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
```

```python 
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201
```

```python 
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

```

```python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This line is now inside an app context
    app.run(debug=True)
```