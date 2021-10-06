from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from form.baseform import LoginForm, RegisterForm


app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "SkillChenSecretKey"



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