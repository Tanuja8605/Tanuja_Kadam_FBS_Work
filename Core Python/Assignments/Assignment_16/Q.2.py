# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
  discount = 10
  @staticmethod

  def setdiscount():
    Product.discount
  @staticmethod
  def applydis(p):
    dis = p - (p * Product.discount)/100
    return dis



  def __init__(self,pid = 0,pname = "",price = 0,quantity = 0):
    self.pid = pid
    self.pname = pname
    self.price = price
    self.quantity = quantity
    
    

  def getpid(self):
    return self.pid
  def setpid(self,pid):
    self.pid = pid
  def getpname(self):
    return self.pname
  def setpname(self,pname):
    self.pname = pname
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price = price
  def getquantity(self):
    return self.quantity
  def setquantity(self,quantity):
    self.quantity = quantity

  def ShowProduct(self):
    print(f"P_id: {self.pid}\tpname: {self.pname}\tprice: {Product.applydis(self.price)}\tquantity: {self.quantity}")

  def __del__(self):
    print("Destructor called")



p = Product(101,"Ram",500,2)
p.ShowProduct()
p1 = Product(102,"sam",1000,3)
p1.ShowProduct()



  



    