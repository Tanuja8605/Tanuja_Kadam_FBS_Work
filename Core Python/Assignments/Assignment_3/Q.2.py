# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
# Take input from user
alpha = input('Enter any alphabet:')

# Use conditions
if alpha in 'aeiouAEIOU':
  print('It is Vowel')
else:
  print('It is Consonant')