# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

class College:
  def __init__(self,no_of_students):
    self.no_of_students = no_of_students
    self.students = []

  def addStudent(self,student):
    self.student = student
    if len(self.students) < self.no_of_students:
      self.students.append(self.student)
      print("Added student Successfully")
    else:
      print("College is full")
    print("----------------------------")

  def getStudent(self,stud_id):
    for s in self.students:
      if s.stud_id == stud_id:
        return s
    return "student not found"
  print("-----------------------------------")
    
  def removeStudent(self,stud_id):
    for s in self.students:
      if s.stud_id == stud_id:
        self.students.remove(s)
        print("student remove successfully")
    print("student not found")
    print("--------------------------------------")

  def __str__(self):
        result = "College Students:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result

class Student:
  def __init__(self,stud_id,name,age):
    self.stud_id = stud_id
    self.name = name
    self.age = age
  def getstud_id(self):
    return self.stud_id
  def setstud_id(self,stud_id):
    self.stud_id = stud_id
  def getname(self):
    return self.name
  def setname(self,name):
    self.name = name

  def __str__(self):
    return f"stud_id:{self.stud_id}\tName:{self.name}\tage:{self.age}"

cc = College(3)

ss = Student(10,"Rohit",27)
ss1 = Student(11,"Rohan",26)
ss2 = Student(12,"Shubham",30)
ss3 = Student(13,"Munna",24)

cc.addStudent(ss)
cc.addStudent(ss1)
cc.addStudent(ss2)

print(cc)

print(cc.getStudent(11))

# cc.removeStudent(11)

print(cc)
cc.addStudent(ss3)
print(cc)








    
    
    









    
    
  
