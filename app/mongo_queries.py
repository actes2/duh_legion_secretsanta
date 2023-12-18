import os
from pymongo import MongoClient


def createNewRecord(database, name, steam_id, ip_addr):
    collection = database["duh_legion_christmas"]

    new_document = {
        "name": name,
        "steam_id": steam_id,
        "ip_addr": ip_addr
    }

    result = collection.insert_one(new_document)

    print("New Entry ID:", result.inserted_id)
    

def connect_toDB(username, password):
    client = MongoClient(host="localhost", port=27017, username=username, password=password)

    db = client["testarino"]
    return db


if __name__ == "__main__":
    print("Init!")
    db_creds = (
        os.getenv("DB_USERNAME"),
        os.getenv("DB_PASSWORD")
    )

    database = connect_toDB(*db_creds)

    createNewRecord(database, "Jimmy", "STEAMID:42069", "192.168.1.5")
    createNewRecord(database, "Carl", "STEAMID:694120", "72.16.5.49")
    # collection = database["duh_legion_christmas"]
    # all_entries = collection.find()
    # for entry in all_entries:
    #     print(entry)
