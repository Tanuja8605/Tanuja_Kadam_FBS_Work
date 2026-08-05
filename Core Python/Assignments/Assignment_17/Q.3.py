# 3. Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship

# b. Add the following methods :

# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:
  def __init__(self,stud_id = 0,name = "",age = 0,marks = 0):
    self.stud_id = stud_id
    self.name = name
    self.age = age
    self.marks = marks

  def getstud_id(self):
    return self.stud_id
  def setstud_id(self,stud_id):
    self.stud_id = stud_id
  def getname(self):
    return self.name
  def setname(self,name):
    self.name = name
  def getage(self):
    return self.age
  def setage(self,age):
    self.age = age
  def getmarks(self):
    return self.marks
  def setmarks(self,marks):
    self.marks = marks

  def accept(self):
    self.stud_id = int(input("Enter student_id:"))
    self.name = input("Enter name:")
    self.age = int(input("Enter age:"))
    self.marks = int(input("Enter marks:"))

  def cal_Rank(self):
    total_marks = self.marks
    if total_marks >= 90:
      return "Rank 1"
    elif total_marks >= 75:
      return "Rank 2"
    elif total_marks >= 50:
      return "Rank 3"
    else:
      return "Rank 4"

  def __str__(self):
    return f"Stud_id: {self.stud_id}\tName: {self.name}\tAge: {self.age}"

    
  def display(self):
    print(f"Stud_id: {self.stud_id}\tName: {self.name}\tAge: {self.age}")

class MedicalStud(Student):
  def __init__(self, stud_id=0, name="", age=0, marks=0,specialization = "",intership_marks = 0):
    super().__init__(stud_id, name, age, marks)

    self.specialization = specialization
    self.intership_marks = intership_marks

  def accept(self):
      self.specialization = int(input("Enter student specialization:"))
      self.intership_marks = int(input("Enter marks:"))
      

  def getspecialization(self):
    return self.specialization
  def setspecialization(self,specialization):
    self.specialization = specialization
  def getintership_marks(self):
    return self.intership_marks
  def setintership_marks(self,intership_marks):
    self.intership_marks = intership_marks

  def cal_Rank(self):
    total_marks = self.marks + self.intership_marks
    if total_marks >= 90:
      return "Rank 1"
    elif total_marks >= 75:
      return "Rank 2"
    elif total_marks >= 50:
      return "Rank 3"
    else:
      return "Rank 4"

  def display(self):
    print(F"Specialization: {self.specialization}\tintership_marks: {self.intership_marks}")
    return super().display()
   

  def __str__(self):
    return f"{super().__str__()}\tSpecialization: {self.specialization}\tintership_marks: {self.intership_marks}"

# ms = MedicalStud(20,"Rahul",35,87,"Psycology",92)
# ms.display()
# # print(ms)
# print(ms.cal_Rank())

ss = Student(21,"Ram",20,89)
ss.display()
    


  

  
    