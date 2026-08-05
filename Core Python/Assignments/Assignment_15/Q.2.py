# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
  def __init__(self,pid,pname,price,quantity):
    self.pid = pid
    self.pname = pname
    self.price = price
    self.quantity = quantity
  def getpname(self):
    return self.pname
  def setpname(self,pname):
    self.pname = pname
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price = price
  

  def diaplay(self):
    print("Product details:")
    print("Product Id:",self.pid)
    print("Product name:",self.pname)
    print("Quantity:",self.quantity)


  def __del__(self):
    print("Destructor called")

p1 = Product(101,"Electronics",43000,4)
p1.setpname("Appliances")
print(p1.getprice())

p1.diaplay()


