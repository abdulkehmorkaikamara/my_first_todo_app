from flask import Flask, request, render_template;
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def member():
    return render_template('members.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        firstname =  request.form.get('fname')
        lastname =  request.form.get('lname')
        email = request.form.get('email')
        print(firstname, lastname, email)
    else: 
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)