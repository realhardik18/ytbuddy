from flask import Flask, render_template, request
import pydaisi

app = Flask('')
ytbuddy = pydaisi.Daisi("realhardik18/ytbuddy")


@app.route('/')
def home():
    return render_template("index.html")


app.run()
# wrok on ui
# work on dynamic routing for stats
# add more features
# landing page for reports feautes and link buddy grpo insta
