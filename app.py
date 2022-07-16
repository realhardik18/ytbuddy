from flask import Flask, render_template, request
import pydaisi

app = Flask('')
ytbuddy = pydaisi.Daisi("realhardik18/ytbuddy")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def post():
    user_input = request.form['text']
    # return render_template('result.html', data=infoOfAllVids(user_input))
    return render_template('result.html', data=ytbuddy.Top15LeastVeiwed(user_input))


app.run(debug=True)
# wrok on ui
# work on dynamic routing for stats
# add more features
# landing page for reports feautes and link buddy grpo insta
