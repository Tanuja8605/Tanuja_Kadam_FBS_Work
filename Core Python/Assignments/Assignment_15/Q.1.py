# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
  def __init__(self,bid,bname,price,author):
    self.bid = bid
    self.bname = bname
    self.price = price
    self.author = author

  def getbname(self):
    return self.bname
  def setbname(self,bname):
    self.bname = bname
  def getprice(self):
    return self.price
  def setprice(self,price):
    self.price = price

  def ShowBook(self):
    print("\nBook Details: ")

    print("Book Id:",self.bid)
    print("Book Name:",self.bname)
    print("Price:",self.price)
    print("Author is:",self.author)

  def __del__(self):
    print("Destructor Called")

b1 = Book(101,"Shriman Yogi",450,"Ranjit Desai")

print(b1.getbname())
b1.setbname("Swami")

b1.ShowBook()


print("----------------")

b2 = Book(102,"Musafir",150,"Achyut G.")

b2.setprice(200)
print("Updated Price:", b2.getprice())
b2.ShowBook()

del b1
del b2


    


