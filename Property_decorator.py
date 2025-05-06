#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,name,price):
        self.name=name
        self._price = price

@property
def price(self):
    return self._price

@price.setter
def price(self,value):
    if value < 0:
        print("price cannot be negative")

    else:
        self._price = value         

@price.deleter
def price (self):
    print(f"deleting the price of {self.name}")
    del self._price         


product =Product("Mobile",10000)

print(product._price)
#add in price
product.price = 12000
print(product.price)
#subtract from price
product.price = -1000
del product.price