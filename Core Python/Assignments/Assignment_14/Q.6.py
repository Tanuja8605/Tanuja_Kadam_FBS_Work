# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
def max_product(s):
  li = list(s)
  max_product = 0
  num1 = 0
  num2 = 0

  for i in range(len(li)):

    for j in range(i+1,len(li)):

      product = li[i] * li[j]

      if product > max_product:
        max_product = product
        num1 = li[i]
        num2 = li[j]

  
  print(num1, num2)
  print(max_product)


s = {1,2,3,4,5,6}
max_product(s)


