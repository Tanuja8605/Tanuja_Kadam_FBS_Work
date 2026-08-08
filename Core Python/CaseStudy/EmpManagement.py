from hr import Hr
from trainer import Trainer


class Empmanagement:

    empdata = {}

    def AddEmp(self):

        print("------------ Add Employee ----------")

        emp_id = int(input("Enter Id: "))

        if emp_id in Empmanagement.empdata:
            print("Employee already exist...")
            return

        name = input("Enter Employee name: ")
        sal = float(input("Enter salary: "))

        print("1. HR")
        print("2. Trainer")

        ch = int(input("Select one: "))

        if ch == 1:
            com = float(input("Enter commission: "))
            emp = Hr(emp_id, name, sal, com)

        elif ch == 2:
            bonus = float(input("Enter bonus: "))
            emp = Trainer(emp_id, name, sal, bonus)

        else:
            print("Invalid Input")
            return

        Empmanagement.empdata[emp_id] = emp

        print("Employee Added Successfully......")

    def DisplayEmp(self):

        print("--------- Employee Records ---------")

        if len(Empmanagement.empdata) == 0:
            print("No employee records found.")
            return

        print(Empmanagement.empdata)

    def SearchEmp(self):

        print("--------- Search Employee ---------")


        emp_id = int(input("Enter employee emp_id: "))

        if emp_id in Empmanagement.empdata:
          emp = Empmanagement.empdata[emp_id]
          print("Employee Found")
          print(emp)
        else:
          print("Employee not found")

        

    def UpdateEmp(self):
        print("---------------Update Employee------------")
        emp_id = int(input("Enter your id:"))
        if emp_id not in Empmanagement.empdata:
            print("Employee not found:")
            return
        emp = Empmanagement.empdata[emp_id]
        print("Employee found")
        print(emp)

        print("1.Update name")
        print("2.Update salary")

        ch = int(input("Enter your choice:"))
        if ch == 1:
            emp.name = int(input("Enter new name:"))
        elif ch == 2:
            emp.sal = float(input("Enter new salary:"))
        else:
            print("Invalid choice")
            return
        print("Employee update successfully...")
        print(emp)

        
    def DeleteEmp(self):
        emp_id = int(input("Enter Employee id:"))
        if emp_id in self.empdata:
            del self.empdata[emp_id]
            print("Employee deleted")
        else:
            print("Employee not found")

    def Exit(self):
        print("Thank you for visiting")