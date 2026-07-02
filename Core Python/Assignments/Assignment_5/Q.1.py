# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

user_id = 'admin'
pass_wd = '12345'

for i in range(3):
 username = input('Enter username:')
 password = input('Enter password:')
 if user_id==username and pass_wd==password:
  print('login successfully')
  break
 else:
  print('re-enter credentials')
else:
  print('program terminated')
