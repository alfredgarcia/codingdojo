from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods = ['POST'])
def create():
    data = request.form
    print data
    return render_template('result.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)
