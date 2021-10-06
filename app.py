from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from form.baseform import LoginForm, RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "SkillChenSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    email = db.Column(db.String(128), primary_key=True)
    password = db.Column(db.String(128))



@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "It's valid!"
    return render_template("login.html",form=form)
    
@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "It's valid!"
    return render_template("register.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)