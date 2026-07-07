# a. 1+ 2 + 3 + 4+..... + n
def add():
    n = int(input("Enter value of n: "))
    total = 0

    for i in range(1, n + 1):
        if i < n:
            print(i, end=" + ")
        else:
            print(i, end=" = ")

        total += i

    return total

result = add()
print(result)

# b. 1!+ 2! + 3! + 4!+..... + n!  


def fact_sum(n):
    
    total = 0

    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j

        if i < n:
            print(fact, end= '+')
        else:
            print(fact, end= '=')

        total += fact

    return total
num = int(input('Enter value of n:'))
res = fact_sum(num)
print('factorial sum is:', res)

# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumpower(n):
  total = 0
  for i in range(1,n+1):
    if i < n:
      print(f'{i}^{i}', end = '+')
    else:
      print(f'{i}^{i}', end = '=')
    total += i**i
  return total

num = int(input('Enter num:'))
res = sumpower(num)
print('sum is:',res)