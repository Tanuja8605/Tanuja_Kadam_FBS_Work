# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:
  def __init__(self,stud_id,sname,age,percentage):
    self.stud_id = stud_id
    self.sname = sname
    self.age = age
    self.percentage = percentage

  def getstudid(self):
    return self.stud_id
  def setstudid(self,stud_id):
    self.stud_id = stud_id
  def getname(self):
    return self.sname
  def setname(self,sname):
    self.sname = sname
  def getage(self):
    return self.age
  def setage(self,age):
    self.age = age
  def getpercentage(self):
    return self.percentage
  def setpercentage(self,percentage):
    self.percentage = percentage

  def cal_rank(self):
    if self.percentage >= 90:
      return "Rank1"
    elif self.percentage >= 75:
      return "Rank2"
    elif self.percentage >= 50:
      return "Rank3"
    else:
      return "Rank4"
    


  def display(self):
    print(f"stud_id: {self.stud_id}\tsname: {self.sname}\tage: {self.age}\tpercentage: {self.percentage}")

  def accept(self):
    self.stud_id = int(input("Enter student_id:"))
    self.sname = input("Enter student name:")
    self.age = int(input("Enter student age:"))
    self.percentage = float(input("Enter percentage:"))


  def __str__(self):
    return f"stud_id: {self.stud_id}\tsname: {self.sname}\tage: {self.age}\tpercentage: {self.percentage}\tRank: {self.cal_rank()}"
     
    
s1 = Student(101,"Vinay",23,89)
# s1.display()
# s1.accept()
# s1.display()
# print(s1)
# print(s1.getname())
print(s1.cal_rank())