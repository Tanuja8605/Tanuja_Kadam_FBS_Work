####4.Ladder_if_elif statement
gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >= 18):
       print('Eligible for marriage')
    else:
      print('Not Eligible for marriage')

elif(gender == 'M'):
    if(age >= 21):
     print('Boy Eligible for marriage')
    else:
           print('Not Eligible for marriage')

else:
    print('INVALID INPUT')


  
