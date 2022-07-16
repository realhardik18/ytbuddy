from flask import Flask, render_template, request
from threading import Thread
from VideoInfoGetter import infoOfAllVids, Top15MostVeiwed

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def post():
    user_input = request.form['text']
    # return render_template('result.html', data=infoOfAllVids(user_input))
    return render_template('result.html', data=Top15MostVeiwed(user_input))


app.run(debug=True)
# wrok on ui
# work on dynamic routing for stats
# add more features
# landing page for reports feautes and link buddy grpo insta
