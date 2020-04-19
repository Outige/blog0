from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Tieg O',
        'title': 'Post 0',
        'content': 'Post 0 content',
        'date_posted': 'April 18 2020'
    },
    {
        'author': 'Erin O',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date_posted': 'April 18 2020'
    },
    {
        'author': 'Tieg O',
        'title': 'Post 0',
        'content': 'Post 0 content',
        'date_posted': 'April 18 2020'
    },
    {
        'author': 'Erin O',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date_posted': 'April 18 2020'
    },
    {
        'author': 'Tieg O',
        'title': 'Post 0',
        'content': 'Post 0 content',
        'date_posted': 'April 18 2020'
    },
    {
        'author': 'Erin O',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date_posted': 'April 18 2020'
    }
]

app = Flask(__name__)

# python3
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '8f3edecd56acb3840c27f4bb1a7420c2'

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('about')) #! fixme, this should be home
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('about')) #! fixme, this should be home
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
            
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)