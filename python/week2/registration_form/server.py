# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^\D+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    error = False
    if len(request.form['email']) < 1:
        error = True
        flash("Email Cannot Be Blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        error = True
        flash("Invalid Email Address")
    if len(request.form['first_name']) < 1:
        error = True
        flash("First Name Cannot Be Blank")
    elif not NAME_REGEX.match(request.form['first_name']):
        error = True
        flash("First Name Cannot Contain Numbers")
    if len(request.form['last_name']) < 1:
        error = True
        flash("Last Name Cannot Be Blank")
    elif not NAME_REGEX.match(request.form['last_name']):
        error = True
        flash("Last Name Cannot Contain Numbers")
    if len(request.form['password']) < 8:
        error = True
        flash("Password Cannot Be Blank And Should Be At Least 8 Characters")
    if len(request.form['confirm_password']) != len(request.form['password']):
        error = True
        flash("Password Don't Match")
    if error:
        return redirect('/')
    return render_template('show.html')
app.run(debug=True)
