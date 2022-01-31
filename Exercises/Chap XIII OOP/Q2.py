class Product:
    def __init__ (self, amount, price):
        #self.name = "Product"
        self.amount = amount
        self.price = price
       
    def get_price (self):
        return self.amount * self.price

    def make_purchase (self):
        if self.amount < 10:
            return self.get_price() 
        elif self.amount < 100:
            return self.get_price() * 0.9
        elif self.amount >= 100:
            return self.get_price() * 0.8

e = Product (100, 10)

print (e.make_purchase())
