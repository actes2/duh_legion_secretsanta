import os
import json
import requests as req
import mongo_queries
from flask import Flask, render_template, request, flash, session


app = Flask(__name__, static_folder="static")




@app.route("/register", methods=["POST"])
def register():
    name = session["name"] if "name" in session else "none"
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
    name = session["name"] if "name" in session else "none"
    return render_template("index.html", name=name)


@app.route("/form")
def form():
    name = session["name"] if "name" in session else "none"
    return render_template("form.html", name=name)

if __name__ == "__main__":
    print("Init!")
    
    app.secret_key = "Jimmysacoolerguyyyy" # Change this later to a github session token or something

    app.run("0.0.0.0", port=80, debug=True)
