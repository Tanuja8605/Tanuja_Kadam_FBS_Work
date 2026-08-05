# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:
    count = 0
    @staticmethod
    def getcount( ):
       return Book.count
   

    def __init__(self, bid = 0, bname = "", price = 0,author = ""):
      self.bid = bid
      self.bname = bname
      self.price = price
      self.author = author
      Book.count += 1

    def getbid(self):
      return self.bid
    def setbid(self,bid):
      self. bid = bid
    def getbname(self):
      return self.bname
    def setbname(self, bname):
      self. bname = bname
    def getprice(self):
      return self.price
    def setprice(self,price):
      self.price = price
    def getauthor(self):
      return self.author
    def setauthor(self,author):
      self.author = author
 
    def showBook(self):
     print(f"Book_id: {self.bid}\tbname: {self.bname}\tprice: {self.price}\tauthor: {self.author}")
   
    def __del__(self):
      print("Destructor called")

b = Book(12,"Swammi",500,"Ranjit")
# b2 = Book()
b.showBook()

# b2.showBook()
print(Book.count)





 

      
