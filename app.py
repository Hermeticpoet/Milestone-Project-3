import os
from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '9039e1a76014f85ad2fea4415a793bd8'
app.config["MONGO_DBNAME"] = 'recipesApp'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


#  Mongo Database Variable
mongo = PyMongo(app)


#  Landing Home Page
@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    cuisines = mongo.db.cuisines.find()
    courses = mongo.db.meal_type.find()
    
    return render_template("index.html", title="Home", courses=courses, cuisines=cuisines) 

    
# View All Recipes
@app.route("/recipes", methods=["GET"])
def all_recipes():
    recipes = mongo.db.recipes.find()
    courses = mongo.db.meal_type.find()
    
    return render_template("recipes.html", title="All Recipes", courses=courses, recipes=recipes)
    
# # View Single Recipe
@app.route("/view_recipe/<recipe_id>", methods=["GET"])
def view_recipe(recipe_id):
    recipes = mongo.db.recipes.find()
    recipe = mongo.db.recipes.find_one({ "_id":ObjectId(recipe_id) })
    courses = mongo.db.meal_type.find()
    
    return render_template("view_recipe.html", title="View Recipe", recipes=recipes, courses=courses, recipe=recipe)


# Add a New Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    '''
    User form generated that allows users to create their own recipes
    and send them to the database to be stored
    '''
    if request.method == "POST":
        recipes = mongo.db.recipes
        recipes.insert_one({
            "created_by": request.form['created_by'],
            "recipe_name": request.form['recipe_name'],
            "description": request.form['description'],
            "ingredients": request.form['ingredients'],
            "instructions": request.form['instructions'],
            "cuisine_origin": request.form['cuisine_origin'],
            "dietary_name": request.form['dietary_name'],
            "course_name": request.form['course_name'],
            "chef_skillz": request.form['chef_skillz'],
            "allergens": request.form['allergens']
        })
    return render_template("add_recipe.html", title="Add Recipe")
    
@app.route('/delete_recipe/<recipe_id>', methods=["GET", "POST"])
def delete_recipe(recipe_id):
    """ allowing users to delete recipes easily with a click of a button"""
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('index'))
    

# Route for Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # Validate Form Entry
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)
    

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@yahoo.com' and form.password.data == 'password':
            flash(f"You have been successfully logged in")
            return redirect(url_for('index'))
        else:
            flash("Login Failed, please check username & password")
    return render_template("login.html", title="Login", form=form)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

