class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
p1=Product("Milk",100)
p2=Product("Rice",50)
print(p1.name,p1.price)
print(p2.name,p2.price)