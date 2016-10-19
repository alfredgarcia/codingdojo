from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    session['guess'] = request.form['guess']
    rand = random.randrange(0, 101)
    low = 'Too Low'
    high = 'Too High'
    if rand > session['guess']:
        session['output'] = low
    else:
        session['output'] = high
    return render_template('result.html')
if __name__ == "__main__":
    app.run(debug=True)
