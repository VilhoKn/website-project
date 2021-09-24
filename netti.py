from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
import datetime

app = Flask(__name__)
app.secret_key = 'CkmD1kimpX'
app.permanent_session_lifetime = datetime.timedelta(minutes=30)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")

if __name__ == '__main__':
	app.run(debug=True)
