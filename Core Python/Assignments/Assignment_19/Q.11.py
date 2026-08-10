###Decorator Asssignment:

# 1. Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.
    
  
def memoization(func):
  catch = {}
  def wrapper(n):
    if n in catch:
      print("Result from catch")
      return catch[n]
    else:
      result = func(n)
      catch[n] = result
      print("calculated result:")
      return result
  return wrapper

@memoization
def square(n):
  return n*n
print(square(5))