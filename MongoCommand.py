# imports
from StartPage import StartPage


# class
class cust_class(object):
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])





# function prototypes
def add_cust(name,age,phone,amount,freq):
    collection = StartPage.db.customer_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for j in i.values():
            num = j
    
    new_cust = {"_id": num+1, "Name": name, "Age": age, "Phone": phone, "Amount": amount, "Frequency": freq, "Customer Score": amount/freq}
    collection.insert_one(new_cust)



# remove function - 
def remove_cust(cust_id):
    collection = StartPage.db.customer_db
    collection.delete_one({"_id": cust_id})
    


# FUNCTIONS TO FETCH DATA
def fetch_by_id(cust_id):
    collection = StartPage.db.customer_db
    cust = collection.find_one({"_id": cust_id})
    customer = cust_class(cust)

def fetch_by_phone(phone):
    collection = StartPage.db.customer_db
    cust = collection.find_one({"Phone": phone})
    customer = cust_class(cust)

def fetch_by_star(star):
    collection = StartPage.db.customer_db
    cust = collection.find({"star": star}).sort("_id", 1)
    return cust



# customer = fetch_by_star(3)

# for i in customer:
#     print(tuple(i.values()))
    
