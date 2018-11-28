import retriever as rt
from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from classifier import Classifier

app = Flask(__name__)

template = 'classify.html'
classifier = Classifier()
classifier.initialize()

posts = []

@app.route("/")
def hello():
    return "<h1>Hello!</h1>"

@app.route("/classify", methods=['GET', 'POST'])
def classifty():
    gender = ''
    tweet = ''
    
    if request.method == 'POST':
        try:
            tweet_url = request.form['tweet']
            tweet = rt.find_tweet(tweet_url)
            gender_num = classifier.classify(tweet)
            if gender_num == 0:
                gender = "Male"
            else:
                gender = "Female"
        except:
            print("Error")
    return render_template(template, tweet=tweet, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)