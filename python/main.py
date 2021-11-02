# imports
import pymongo
from add_cust import add_cust


# function prototypes
def add_cust():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    amount = int(input("Enter amount: "))
    freq = int(input("Enter frequency: "))

    new_cust = {"Name": name, "Age": age, "Amount": amount, "Frequency": freq, "Customer Score": amount/freq}

    collection.insert_one(new_cust)

# main 
if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://harsh92:harsh92@cluster0.ldhgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["g10"]
    collection = db["cust_db"]

    # calling function to add new customer to the data base
    add_cust()

    # after this I will add another function to update existing customer in the database
    # (If someone revisit the amount and frequency will get updated)


    