from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

template = 'classify.html'

posts = []

@app.route("/")
def hello():
    return "<h1>Hello!</h1>"

@app.route("/classify", methods=['GET', 'POST'])
def classifty():
    if request.method == 'POST':
        try:
            tweet = request.form['tweet']
        except:
            print("Error")
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)