# 2. Create a derived class from Student as EngStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:
  def __init__(self,stud_id = 0,name = "",marks = 0):
    self.stud_id = stud_id
    self.name = name
    self.marks = marks


  def getstud_id(self):
    return self.stud_id
  def setstud_id(self,stud_id):
    self.stud_id = stud_id
  def getname(self):
    return self.name
  def setname(self,name):
    self.name = name
  def getmarks(self):
    return self.marks
  def setmarks(self,marks):
    self.marks = marks

  def cal_rank(self):
    total_marks = self.marks
    print(f"total_marks:{total_marks}")
    if total_marks >= 90:
      return "Rank1"
    elif total_marks >= 75:
      return "Rank2"
    elif total_marks >= 50:
      return "Rank3"
    else:
        return "Rank4"
  def __str__(self):
    return f"Stud_id: {self.stud_id}\tName: {self.name}\tMarks: {self.marks}"
  
  def display(self):
    print(f"Stud_id: {self.stud_id}\tName:{self.name}\tMarks: {self.marks}")

class EngStudent(Student):
    def __init__(self, stud_id = 0, name = "", marks = 0,branch = "",internal_marks = 0):
      super().__init__(stud_id, name, marks)
      self.branch = branch
      self.internal_marks = internal_marks
    
    def getbranch(self):
      return self.branch
    def setbranch(self,branch):
      self.branch = branch
    def getinternal_marks(self):
       return self.internal_marks
    def setinternal_marks(self,internal_marks):
      self.internal_marks = internal_marks

    def cal_rank(self):
      total_marks = self.marks + self.internal_marks
      if total_marks >= 90:
         return "Rank1"
      elif total_marks >= 75:
          return "Rank2"
      elif total_marks >= 50:
          return "Rank3"
      else:
          return "Rank4"

    def __str__(self):
     return f"{super().__str__()}\tBranch: {self.branch}\tInternal_marks: {self.internal_marks}"

    def display(self):
      print(f"Branch: {self.branch}\tinternal_marks: {self.internal_marks}")
      return super().display()
          
      

# e1 = EngStudent(11,"Ram",78,"Computer_science",35)
# # e1.display()
# print(e1.cal_rank())
# e1.setname("Rohit")
# print(e1.getname())
# print(e1)
# e1.display()
e1 = EngStudent()
e1.display()
