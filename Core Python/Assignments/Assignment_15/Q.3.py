# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
  increment = 10
  def __init__(self,sid = 0,sname = "",stype = "",price = 0,size=""):
    self.sid = sid
    self.sname = sname
    self.stype = stype
    self.price = price
    self.size = size

    if self.size == "M":
      self.price += self.price * Shirt.increment / 100
    elif self.size == "L":
      self.price += self.price * 2 * Shirt.increment / 100
    elif self.size == "XL":
      self.price += self.price * 3 * Shirt.increment / 100
    
  def getsid(self):
    return self.sid
  def setsid(self,sid):
    self.sid = sid
  def getname(self):
    return self.sname
  def setname(self,sname):
    self.sname = sname

  def getprice(self):
    return self.price
  def setprice(self,price):
     self.price = price
  
  def getsize(self):
    return self.size
  def setsize(self,size):
    self.size = size


  def showshirt(self):
    print("Shirt id: ",self.sid)
    print("name: ",self.sname)
    print("shirt type: ",self.stype)
    print("size: ",self.size)
    print("price:",self.price)

  def __del__(self):
    print("Destructor is called")


# s1 = Shirt ()
s1 = Shirt(101,"Denim","Casual",2300,"s")
s1.showshirt()

s2 = Shirt(102,"siyaram","formal",2500,"XL")
s2.showshirt()
print(s2.getprice())


