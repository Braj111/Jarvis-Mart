# In this class fetched data will be stored

class cust:
    def __init__(self, name, age, amount, freq) -> None:
        self.name = name
        self.age = age
        self.amount = amount
        self.freq = freq
        self.score = int(round(amount/freq))



