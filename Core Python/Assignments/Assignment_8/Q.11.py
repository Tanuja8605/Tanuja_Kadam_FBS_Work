# 11. WAP to check if a given number is Armstrong number or not. For  each task create separate functions.
def countdigit(num):
  count = 0
  temp = num
  while(temp > 0):
    count+=1
    temp = temp//10
  return count
def power(base,exp):
  result = 1
  for i in range(exp):
    result = result*base
  return result

def armstrong(num):
  count = countdigit(num)
  
  temp = num
  sum = 0
  while(temp > 0):
    d = temp % 10

    power_value = power(d,count)
    sum+=power_value
    temp = temp // 10

  if num == sum:
     return True
  else:
    return False
  
  

x = int(input('Enter number:'))
res = armstrong(x)
print(res) 


