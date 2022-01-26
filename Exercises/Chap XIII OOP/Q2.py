class Product:
    def __init__ (self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def get_price (self):
        return self.amount * self.price
    def make_purchase (self):
        if self.amount > 10:
            return self.get_price 
        elif self.amount > 100:
            return self.get_price * 0.1
        elif self.amount <= 100:
            return self.get_price * 0.2

e = Product (3, 8, 10)

print (e.make_purchase)
