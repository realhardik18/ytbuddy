from flask import Flask, render_template, request
from threading import Thread
from VideoInfoGetter import infoOfAllVids

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def post():
    user_input = request.form['text']
    return render_template('result.html', data=infoOfAllVids(user_input))


app.run()
