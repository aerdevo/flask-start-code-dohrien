# This is your library
#dont touch
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# This initiates the flask app (dont touch)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)


# Database Class dont touch
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String)


# Todo class
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    complete = db.Column(db.Boolean)

# We are telling flask where to go for home page
@app.route('/', methods=['GET'])
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/purchase', methods=['GET'])
def purchase():
    todos = Todo.query.all()
    return render_template('purhcase.html', todos=todos)

# Runs your flask app (dont touch)
if (__name__ == "__main__"):
    app.run(debug=True)
