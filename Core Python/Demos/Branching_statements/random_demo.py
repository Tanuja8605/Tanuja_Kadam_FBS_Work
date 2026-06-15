import random

Username = 'admin'
Password = '12345'

captcha_num = random.randint(1000,9999)

User_name = input('Enter Username:')
Pass = input('Enter Password:')

if(Username == User_name and Password == Pass):
  print(captcha_num)

  user_captcha = int(input('Enter a captcha:'))
  
  if(captcha_num == user_captcha):
    print('Login Successfully')
  else:
    print('Invalid Captcha')
else:
        print('Invalid credentials')


        
        



