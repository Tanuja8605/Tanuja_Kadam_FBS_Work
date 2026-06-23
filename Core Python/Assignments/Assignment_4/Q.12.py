# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)
num = int(input('Enter number:'))
temp = num
count = 0
while temp > 0:
  count += 1
  temp = temp // 10
print(count)
sum = 0
temp = num
while temp > 0:
  digit = temp % 10
  sum += digit ** count
  temp = temp // 10
if(sum == num):
  print(f'{num} is Armstrong') 
else:
  print(f'{num} is not Armstrong')
