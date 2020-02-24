from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about/')
def about():
    return render_template("index.html")


@app.route('/products/')
def products():
    return render_template("index.html")


@app.route('/blog/')
def blog():
    return render_template("index.html")


@app.route('/specials/')
def specials():
    return render_template("index.html")


@app.route('/contact/')
def contact():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
