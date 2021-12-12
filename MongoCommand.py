# imports
from MenuPage import MenuPage
import datetime

# class
class cust_class(object):
    def __init__(self, dict):
        for key in dict:
            setattr(self, key, dict[key])





# function prototypes
def add_cust(name,age,phone):
    collection = MenuPage.db.customer_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for j in i.values():
            num = j
    
    new_cust = {"_id": num+1, "Name": name, "Age": age, "Phone": phone, "Amount": 0, "Frequency": 0, "Avg": 0, "star": 1}
    collection.insert_one(new_cust)
    return num+1



# remove function - 
def remove_cust(cust_id):
    collection = MenuPage.db.customer_db
    collection.delete_one({"_id": cust_id})
    


# FUNCTIONS TO FETCH DATA
def fetch_by_id(cust_id):
    collection = MenuPage.db.customer_db
    cust = collection.find_one({"_id": cust_id})
    customer = cust_class(cust)
    return customer

def fetch_by_phone(phone):
    collection = MenuPage.db.customer_db
    cust = collection.find_one({"Phone": phone})
    customer = cust_class(cust)
    return customer
    
def fetch_by_star(star):
    collection = MenuPage.db.customer_db
    cust = collection.find({"star": star}).sort("_id", 1)
    return cust

def fetch_discount(star):
    collection = MenuPage.db.Discount_db
    st = collection.find_one({"star": star},{"discount": 1, "_id": 0})
    return st['discount']

def update_discount(star,dis):
    collection = MenuPage.db.Discount_db
    collection.find_one_and_update({"star":star},{"$set":{"discount":dis}})


# this funciton updates the star by customer id
def star_update(cust_id):
    collection = MenuPage.db.customer_db
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
    collection = MenuPage.db.customer_db
    
    collection.find_one_and_update({"_id":id},{"$inc":{"Amount": billamount,'Frequency': 1}})
    customer = fetch_by_id(id)
    collection.find_one_and_update({"_id":id}, {"$set":{"Avg": round(customer.Amount/customer.Frequency)}})
    star_update(id)

def get_invoice_number():
    collection = MenuPage.db.invoice_db
    n = collection.find({}, {"_id": 1}).sort("_id", -1).limit(1)
    for i in n:
        for j in i.values():
            num = j
    return num+1


def invoice_creation(id, billamount, items, discount):
    collection = MenuPage.db.invoice_db
    dtn = datetime.datetime.now()
    dtn = dtn.strftime("%d/%m/%Y %H:%M:%S")
    invoice = {'_id': get_invoice_number(), 'cid': id, 'invamount': billamount,'discount': discount, 'items': items, 'invdate':dtn, }
    collection.insert_one(invoice)



def fetch_prod():
    collection = MenuPage.db.prod_db
    prod = dict()
    fetprods = collection.find({},{'_id':0})
    for i in fetprods:
        prod[i['product']] = i['price']
    return prod

def fetch_products():
    collection = MenuPage.db.prod_db
    fetprods = collection.find({},{'_id':0})
    return fetprods

def fetch_invoice():
    collection = MenuPage.db.invoice_db
    return collection.find()

def insert_product(name, price):
    collection = MenuPage.db.prod_db
    doc = {'product': name, 'price': price}
    collection.insert_one(doc)