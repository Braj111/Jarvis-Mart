import pymongo

if __name__ == "__main__":
    dbclient = pymongo.MongoClient("mongodb+srv://<harsh92>:<harsh92>@cluster0.ldhgj.mongodb.net/test")
    
    db = dbclient["CSEActivity"]
    collection = db["CustomerDatabase"]
    

    