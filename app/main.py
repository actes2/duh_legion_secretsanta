import os
import json
import requests as req
from flask import Flask, render_template, request, flash, session


app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    print("Init!")

    app.run("0.0.0.0", port=80, debug=True)
