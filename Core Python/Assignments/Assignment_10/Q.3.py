# 3. Write a program to find the second largest element in the list.
def secondmax(li):
  largest = li[0]
  second_large = li[0]
  for i in range(1,len(li)):
    if li[i] > largest:
      second_large = largest
      largest = li[i]
    elif(li[i] < largest and li[i] > second_large):
     second_large = li[i]
  return second_large

li = [30,45,67,10,80,94,36]
res = secondmax(li)
print(f'Second largest element is {res}')
