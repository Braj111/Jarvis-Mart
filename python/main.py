# imports
import pymongo

# class
class cust_class(object):
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])


# function prototypes
def add_cust():
    client = pymongo.MongoClient("mongodb+srv://harsh92:harsh92@cluster0.ldhgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]
    collection = db["cust_db"]

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone = int(input("Enter phone no.: "))
    amount = int(input("Enter amount: "))
    freq = int(input("Enter frequency: "))
    n = collection.estimated_document_count() #Task- Here we have to use some other logic to give the _id to the doc
    
    new_cust = {"_id": n+1 ,"Name": name, "Age": age, "Phone": phone, "Amount": amount, "Frequency": freq, "Customer Score": amount/freq}
    collection.insert_one(new_cust)

# remove function -  works fine but there's a clash with _id
def remove_cust():
    client = pymongo.MongoClient("mongodb+srv://harsh92:harsh92@cluster0.ldhgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]
    collection = db["cust_db"]

    cust_id = int(input("Enter Customer ID: "))
    collection.delete_one({"_id": cust_id})

# FUNCTIONS TO FETCH DATA
def fetch_by_id():
    client = pymongo.MongoClient("mongodb+srv://harsh92:harsh92@cluster0.ldhgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]
    collection = db["cust_db"]

    cust_id = int(input("Enter Customer ID: "))
    cust = collection.find_one({"_id": cust_id})
    customer = cust_class(cust)
    print(customer.Name)

def fetch_by_phone():
    client = pymongo.MongoClient("mongodb+srv://harsh92:harsh92@cluster0.ldhgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]
    collection = db["cust_db"]

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

    


