# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def unique_combin3(li,target):
  for i in range(len(li)):
    for j in range(i+1,len(li)):
      for k in range(j+1,len(li)):
        current_sum = li[i] + li[j] + li[k]

        if current_sum == target:
          print('combination of:',li[i],li[j],li[k])
 

li = [3,6,8,9,4,2,7,1,5]

target = int(input('Enter target value:'))

unique_combin3(li,target)

