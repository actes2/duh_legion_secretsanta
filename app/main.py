import os
import json
import requests as req
from flask import Flask, render_template, request, flash, session


app = Flask(__name__, static_folder="static")




@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST" and "IP" not in session:
        print("New register!")
        details = request.form

        name = details["name"]
        steamid = details["steamid"]

        # To-Do: Check if our address exists! If it does, then say 'not a chance' otherwise add them to the database

        session["IP"] = request.remote_addr #  Store the users IP address in their session cache, as IP. We now can cite this and check it.
        session["name"] = name
        session["steamid"] = steamid

        return render_template("index.html", name=name)
    return render_template("form.html", name="none")




@app.route("/")
def index():
    if "name" in session:
        return render_template("index.html", name=session["name"])
    return render_template("index.html", name="none")


@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    print("Init!")

    app.secret_key = "Jimmysacoolguyyyy" # Change this later to a github session token or something

    app.run("0.0.0.0", port=80, debug=True)
