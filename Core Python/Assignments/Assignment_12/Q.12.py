# 13. Python Program to count number of digits and letters in a string.
def count_digit_letter(s):
  digit_count = 0
  letter_count = 0
  for ch in s:

    if '0' <= ch <= '9':
     digit_count += 1
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
     letter_count += 1
     
  return digit_count,letter_count
  

s = 'Python123'
digit_count , letter_count = count_digit_letter(s)
print('digit_count is:',digit_count)
print('letter count is:',letter_count)

