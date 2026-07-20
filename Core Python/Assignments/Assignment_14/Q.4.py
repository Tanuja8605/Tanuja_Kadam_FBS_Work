# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def find_pairs(li,target):
  for i in range(len(li)):
    for j in range(i+1,len(li)):
      if li[i] + li[j] == target:
        print(li[i],li[j])




lli = [1,2,3,4,5]
target = int(input('enter target ele:'))
find_pairs(lli,target)