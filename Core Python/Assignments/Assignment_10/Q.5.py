# 5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

def checkEle(li,num):
 count = 0

 for i in li:
     if i == num:
         count += 1
 return count

li = [20,40,30,20,10,56,70]
num = int(input('Enter number: '))

res = checkEle(li,num)
if res > 0:
     print(f'{num} is present {res} times')
else:
     print(f'{num} is not present in the list')