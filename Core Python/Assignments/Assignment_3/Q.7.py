# 7. Write a program to check if user has entered correct userid and password.

Username = 'admin'
Password = '12345'

# Take input from user
User_Id = input('Enter Username:')
Pass = input('Enter Password:')

if((Username == User_Id)and(Password == Pass)):
     print('Login Successfully')
else:
     print('Invalid credentials')
