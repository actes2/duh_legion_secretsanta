import os
import json
import requests as req

import mongo_queries
import steam_stuff

from flask import Flask, render_template, request, flash, session, redirect


app = Flask(__name__, static_folder="static")
app.config['APPLICATION_ROOT'] = '/duhchristmas'

database_credentials = (os.getenv("DB_USERNAME"), os.getenv("DB_PASSWORD"))
steam_api_key = os.getenv("STEAM_API_KEY")


@app.route("/register", methods=["POST"])
def register():
    name = session["name"] if "name" in session else "none"
    if request.method == "POST" and "name" not in session:
        print("New register!")
        details = request.form

        name = details["name"]
        steamid = details["steamid"]
        
        db = mongo_queries.connect_to_db(*database_credentials)

        if mongo_queries.check_steamid(db, steamid) is None:
            mongo_queries.create_new_record(database=db, name=name, steam_id=steamid, ip_addr=request.remote_addr)
            # To-Do: Check if our address exists! If it does, then say 'not a chance' otherwise add them to the database

            session["IP"] = request.remote_addr #  Store the users IP address in their session cache, as IP. We now can cite this and check it.
            session["name"] = name
            session["steamid"] = steamid

            return render_template("index.html", name=name)

            #return redirect("/duhchristmas")
        else:
            print("It would appear this account already exists! Or IP at-least.")
    return render_template("form.html", name="none")



@app.route("/duhchristmas")
@app.route("/")
def index():
    name = session["name"] if "name" in session else "none"


    if name != "none":
        datab = mongo_queries.connect_to_db(*database_credentials)

        record = mongo_queries.get_user_by_name(datab, name)
        if record is not None:
            # print(record["match"])

            if record["match"] != "none":
                matches_record = mongo_queries.get_user_by_name(datab, record["match"])
                if matches_record != None:
                    steam_uri = steam_stuff.get_profile_url_from_steamid(matches_record["steam_id"])
                #print("DING")
                    return render_template("waiting_room.html", name=name, match=record["match"], steam_url=steam_uri)
                return render_template("waiting_room.html", name=name, match=record["match"], steam_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            
            return render_template("waiting_room.html", name=name, match=record["match"], steam_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    return render_template("index.html", name=name)


@app.route("/form")
def form():
    name = session["name"] if "name" in session else "none"
    return render_template("form.html", name=name)

if __name__ == "__main__":
    print("Init!")
    # print(database_credentials)
    
    app.secret_key = "Jimmysacoolerguyyyyy" # Change this later to a github session token or something

    app.run("0.0.0.0", port=80, debug=True)
