# 10. Write a program to check if entered year is a leap year or not.
def isleap():
  year = int(input('Enter year:'))
  if year % 4 == 0:
    print(f'{year} is leap year')
  else:
    print(f'{year} is not leap year')

isleap()
