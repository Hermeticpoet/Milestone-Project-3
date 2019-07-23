import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '9039e1a76014f85ad2fea4415a793bd8'
app.config["MONGO_DBNAME"] = 'recipesApp'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
login = LoginManager(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")
    
@app.route("/get_recipes")
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register" form=form)
    

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login" form=form)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

