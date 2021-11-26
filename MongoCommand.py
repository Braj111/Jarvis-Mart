# imports

import pymongo
from StartPage import StartPage


# class
class cust_class(object):
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])




# function prototypes
def add_cust(name,age,phone,amount,freq):
    collection = StartPage.db.cust_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for i in i.values():
            num = i
    new_cust = {"Name": name, "Age": age, "Phone": phone, "Amount": amount, "Frequency": freq, "Customer Score": amount/freq}


    

# remove function -  works fine but there's a clash with _id
def remove_cust():

    collection = StartPage.db.cust_db


# FUNCTIONS TO FETCH DATA
def fetch_by_id():
    collection = StartPage.db.cust_db

def fetch_by_phone():
    collection = StartPage.db.cust_db
    

