from EmpManagement import Empmanagement
def login():
  emp = Empmanagement()
  userid = input("Enter userid:")
  password = input("Enter password:")
  if userid == "admin" and password == "12345":
   while True:
     print("Please select one option from below:")
     print("1.Add Employee")
     print("2.Display Employee")
     print("3.Search Employee")
     print("4.Update Employee")
     print("5.Delete Employee")
     print("6.Exit")
     choice = int(input("Enter your choice:"))
     if choice == 1:
       emp.AddEmp()
     elif choice == 2:
       emp.DisplayEmp()
     elif choice == 3:
      emp.SearchEmp() 
     elif choice == 4:
       emp.UpdateEmp()
     elif choice == 5:
      emp.DeleteEmp()
     elif choice == 6:
        emp.Exit()

        break
  else:
       print("Invalid credentials")

        



login()
       
       