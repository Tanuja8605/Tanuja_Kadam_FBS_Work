from SY.Symarks import Symarks
from TY.Tymarks import Tymarks

class Student:
    def __init__(self, rollno, name, symarks, tymarks):
        self.rollno = rollno
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

        self.total = (
            self.symarks.Computer_total
            + self.tymarks.theory
            + self.tymarks.practical
        )

        if self.total >= 70:
            self.grade = "A"
        elif self.total >= 60:
            self.grade = "B"
        elif self.total >= 50:
            self.grade = "C"
        elif self.total >= 40:
            self.grade = "Pass Class"
        else:
            self.grade = "Fail"

    def __str__(self):
        return f"""
Roll No: {self.rollno}
Name: {self.name}
SY Computer: {self.symarks.Computer_total}
TY Theory: {self.tymarks.theory}
TY Practical: {self.tymarks.practical}
Computer Total: {self.total}
Grade: {self.grade}
"""


stud_1 = Symarks(75, 80, 73)
stud_2 = Tymarks(60, 48)

stud = Student(101, "Rahul", stud_1, stud_2)

print(stud)