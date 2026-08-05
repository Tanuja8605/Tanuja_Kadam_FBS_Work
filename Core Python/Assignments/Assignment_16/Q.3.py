# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.


class Shirt:
  dis = 10
  @staticmethod

  def calprice(size,price):
    size = size.lower()
    if size == "small":
      return price
    elif size == "medium":
      return price + (price*Shirt.dis)/100
    elif size == "largest":
      return price + 2 * (price*Shirt.dis)/100
    elif size == "xlargest":
      return price + 3 * (price*Shirt.dis)/100
    else:
      return price

   
  def __init__(self,sid=0,sname="",type="",size="",price=0):
    self.sid = sid
    self.sname = sname
    self.type = type
    self.size = size
    self.price = Shirt.calprice(price,size)


  def getsid(self):
    return self.sid
  def setsid(self,sid):
    self.sid = sid
  def getsname(self):
    return self.sname
  def setsize(self,sname):
    self.sname = sname
  def gettype(self):
    return self.type
  def settype(self,type):
    self.type = type
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price = price
  def getsize(self):
    return self.size
  def setsize(self,size):
    self.size = size


  def showproduct(self):
    print(f"sid: {self.sid}\tsname: {self.sname}\ttype: {self.type}\tprice: {self.price}\tsize: {self.size}")
  def __del__(self):
    print("Destructor called")

s = Shirt(11,"Raymond","formal",1000,"small")
s.showproduct()
s1 = Shirt(12,"Raymond","formal",1000,"xlargest")
s1.showproduct()
