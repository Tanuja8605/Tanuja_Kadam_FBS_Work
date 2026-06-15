# 8. Write a program to convert days into years, weeks and days.

###Take input from user
days = int(input("Enter the days: "))

###Perform Operation
years = days // 365
days = days % 365  # reassigning days

weeks = days // 7
days = days % 7

print(f'{years} years, {weeks} weeks and {days} days')



