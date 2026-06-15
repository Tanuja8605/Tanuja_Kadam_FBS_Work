####2.if_else statement

User_name = 'admin'
Password = '12345'

UserId = input("Enter UserId:")
Pass = input("Enter Password:")

if(User_name == UserId and Password == Pass):
  print('Login Successfully')
else:
  print('Invalid Credentials')