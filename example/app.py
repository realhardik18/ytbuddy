from flask import Flask, render_template, request
import pydaisi

app = Flask('')
ytbuddy = pydaisi.Daisi("realhardik18/ytbuddy")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/channle')
def channle():
    return render_template("index.html")


@app.route('/video', methods=['GET', "POST"])
def video():
    if request.method == "GET":
        return render_template("video.html")
    elif request.method == 'POST':
        video = request.form['videourl']
        return ytbuddy.stats(video).value


app.run(debug=True)
