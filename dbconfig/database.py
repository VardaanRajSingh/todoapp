from pymongo import MongoClient
import os

#connecting to DB
try:
    print("connecting to db")
    mongo_url=os.getenv("MONGO_URI")
    conn = MongoClient(mongo_url)
    server_info=conn.server_info()
    print("db connected")
    db = conn['project']
    collection_name = db['Task']


except Exception as ex:
    print("Error - cannot Connect to db")
    print(ex)
