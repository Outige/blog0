from flask import Flask, render_template, url_for

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

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)