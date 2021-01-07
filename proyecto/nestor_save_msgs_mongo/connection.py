from pymongo import MongoClient
import os

host = os.environ["MONGO_HOST"]
port = int(os.environ["MONGO_PORT"])
print("host: " + str(host) + " | port: " + str(port))

client = MongoClient(host, port)

def save_msg(obj):
    db = client.test
    collection = db.test.messages
    return collection.insert_one(obj)
