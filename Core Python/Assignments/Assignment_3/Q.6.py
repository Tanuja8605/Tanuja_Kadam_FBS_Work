# 6. Write a program to calculate profit or loss.
# Take input from user
Cp = int(input('Enter cost price:'))
Sp = int(input('Enter selling price:'))

dis_amount = Sp - Cp

if(dis_amount > 0):
  print(dis_amount,'It get Profit')
elif(dis_amount == 0):
  print('No profit No loss')
else:
  print(dis_amount,'It get Loss')