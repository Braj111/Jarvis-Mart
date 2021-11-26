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
    collection.insert_one(new_cust)

    

# remove function -  works fine but there's a clash with _id
def remove_cust():
    collection = StartPage.db.cust_db
    cust_id = int(input("Enter Customer ID: "))
    collection.delete_one({"_id": cust_id})

# FUNCTIONS TO FETCH DATA
def fetch_by_id():
    collection = StartPage.db.cust_db
    cust_id = int(input("Enter Customer ID: "))
    cust = collection.find_one({"_id": cust_id})
    customer = cust_class(cust)
    print(customer.Name)

def fetch_by_phone():
    collection = StartPage.db.cust_db
    phone = int(input("Enter Phone No.: "))
    cust = collection.find_one({"Phone": phone})
    customer = cust_class(cust)
    print(customer.Name)

    

# main 
#if __name__ == "__main__":
    # connection to db  
    

    # calling function to add new customer to the database
    #add_cust()


    # function call to remove customer from the database
    #remove_cust()

    # function call to fetch doc by id
    #fetch_by_id()

    # funciton call to fetch doc by phone number
    #fetch_by_phone()

    # Task:-  I will add another function to update existing customer in the database
    # (If someone revisit the amount and frequency will get updated)



    # Task:- searching data from the database and printing their details

    


