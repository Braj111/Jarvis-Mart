# imports
from StartPage import StartPage
import datetime

# class
class cust_class(object):
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])





# function prototypes
def add_cust(name,age,phone,amount,freq,star):
    collection = StartPage.db.customer_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for j in i.values():
            num = j
    
    new_cust = {"_id": num+1, "Name": name, "Age": age, "Phone": phone, "Amount": amount, "Frequency": freq, "Customer Score": amount/freq, "star": star}
    collection.insert_one(new_cust)
    return num+1



# remove function - 
def remove_cust(cust_id):
    collection = StartPage.db.customer_db
    collection.delete_one({"_id": cust_id})
    


# FUNCTIONS TO FETCH DATA
def fetch_by_id(cust_id):
    collection = StartPage.db.customer_db
    cust = collection.find_one({"_id": cust_id})
    customer = cust_class(cust)
    return customer

def fetch_by_phone(phone):
    collection = StartPage.db.customer_db
    cust = collection.find_one({"Phone": phone})
    customer = cust_class(cust)
    return customer
    
def fetch_by_star(star):
    collection = StartPage.db.customer_db
    cust = collection.find({"star": star}).sort("_id", 1)
    return cust

def fetch_discount(star):
    collection = StartPage.db.Discount_db
    st = collection.find_one({"star": star},{"discount": 1, "_id": 0})
    return st['discount']

def update_discount(star,dis):
    collection = StartPage.db.Discount_db
    collection.find_one_and_update({"star":star},{"$set":{"discount":dis}})


# this funciton updates the star by customer id
def star_update(cust_id):
    collection = StartPage.db.customer_db
    customer = fetch_by_id(cust_id)
    avg = customer.Avg
    if avg  < 1000:
        collection.find_one_and_update({"_id":cust_id},{"$set":{"star":1}})
    elif avg >= 1000 and avg < 2000:
        collection.find_one_and_update({"_id":cust_id},{"$set":{"star":2}})
    elif avg >= 2000 and avg < 3000:
        collection.find_one_and_update({"_id":cust_id},{"$set":{"star":3}})
    elif avg >= 3000 and avg < 4000:
        collection.find_one_and_update({"_id":cust_id},{"$set":{"star":4}})
    elif avg >= 4000:
        collection.find_one_and_update({"_id":cust_id},{"$set":{"star":5}})       


    
def update_cusotmer(id, billamount):
    collection = StartPage.db.customer_db
    customer = fetch_by_id(id)
    collection.find_one_and_update({"_id":id},
                                    {"$inc":{"Amount": billamount,'Frequency': 1},
                                     "$set":{"Avg": round(customer.Amount/customer.Frequency)}})
    star_update(id)


def invoice_creation(id, billamount, items, discount):
    collection = StartPage.db.invoice_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for j in i.values():
            num = j
    dtn = datetime.datetime.now()
    dtn = dtn.strftime("%d/%m/%Y %H:%M:%S")
    invoice = {'_id': num+1, 'cid': id, 'invamount': billamount,'discount': discount, 'items': items, 'invdate':dtn, }
    collection.insert_one(invoice)

def fetch_prod():
    collection = StartPage.db.prod_db
    prod = dict()
    fetprods = collection.find({},{'_id':0})
    for i in fetprods:
        prod[i['product']] = i['price']
    return prod

