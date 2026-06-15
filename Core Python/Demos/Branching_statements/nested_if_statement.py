####3.nested_if statement
gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))

if(gender == 'F'):
  if(age >= 18):
    print('Girl Eligible for marriage')
  else:
    print('Not Eligible for marriage')
else:
  if(age >= 21):
    print('Boy is Eligible for marriage')
  else:
    print('Not Eligible for marriage')


