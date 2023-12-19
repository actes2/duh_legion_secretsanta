import os
import random
import time
import pymongo

def grab_all_records(database):
    """This function grabs all documents in the specified database->collection"""
    collection = database["duh_legion_christmas"]
    result = collection.find({})

    return list(result)


def match_the_boys(database):
    """This function will be what dictates who will be secret santa for who"""
    collection = database["duh_legion_christmas"]

    all_people = grab_all_records(database)
    print(all_people)
    random.seed(time.time() * 10000)
    random.seed(time.time() + random.randint(1, 100000))
    random.seed(time.time() * random.randint(1, 1000))

    for _ in range(1, random.randint(2,3)):
        random.shuffle(all_people)
    

    for i, person in enumerate(all_people):
        next_person_index = (i + 1) % len(all_people)
        next_person = all_people[next_person_index]
        
        person["match"] = next_person["name"]
        
        update_query = {"name": person["name"]}
        collection.update_one(update_query, {"$set": person})

    print("All matched!")


def get_user_by_name(database, name):
    """This function connects to the database, then connects to the 'duh_legion_christmas'
     collection and checks for the provided IP"""
    collection = database["duh_legion_christmas"]

    query = { "name": { "$regex": name}}

    result = collection.find(query)
    for item in result:
        #print(f"Document: {item}")
        return item
    return None


def check_steamid(database, id):
    """This function connects to the database, then connects to the 'duh_legion_christmas'
     collection and checks for the provided IP"""
    collection = database["duh_legion_christmas"]

    query = { "steam_id": { "$regex": id}}

    result = collection.find(query)
    for item in result:
        #print(f"Document: {item}")
        return item
    return None


def check_ip_addr(database, addr):
    """This function connects to the database, then connects to the 'duh_legion_christmas'
     collection and checks for the provided IP"""
    collection = database["duh_legion_christmas"]

    query = { "ip_addr": { "$regex": addr}}

    result = collection.find(query)
    for item in result:
        #print(f"Document: {item}")
        return item
    return None


def create_new_record(database, name, steam_id, ip_addr):
    """This function creates a new record in the database - 
    specifically for the duh_legion_christmas collection"""
    collection = database["duh_legion_christmas"]

    new_document = {
        "name": name,
        "steam_id": steam_id,
        "ip_addr": ip_addr,
        "match": "none",
    }

    result = collection.insert_one(new_document)
    print("New Entry ID:", result.inserted_id)


def connect_to_db(username, password):
    """This function connects to the database and outputs a database object."""
    client = pymongo.MongoClient(host="localhost", port=27017, username=username, password=password)

    db = client["testarino"]
    return db


#if __name__ == "__main__":
    #print("Init!")


    #match_the_boys(database)
    #blah = grab_all_records(database)

    #print(blah[1]["name"])

    # blah = check_ip_addr(database, "192.168.1.3")
    # if blah is not None:
    #     print("Ahoy")
    #     print(blah["name"])
    # else:
    #     print("Nothing there chief!")
    ## createNewRecord(database, "Jimmy", "STEAMID:42069", "192.168.1.5")
    ## createNewRecord(database, "Carl", "STEAMID:694120", "72.16.5.49")
    # collection = database["duh_legion_christmas"]
    # all_entries = collection.find()
    # for entry in all_entries:
    #     print(entry)
