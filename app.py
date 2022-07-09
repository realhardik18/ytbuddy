from flask import Flask, render_template, request
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return render_template('index.html')


app.run()
