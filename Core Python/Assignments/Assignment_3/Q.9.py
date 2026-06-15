# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input('Enter Subject_1 Marks:'))
m2 = int(input('Enter Subject_2 Marks:'))
m3 = int(input('Enter Subject_3 Marks:'))
m4 = int(input('Enter Subject_4 Marks:'))
m5 = int(input('Enter Subject_5 Marks:'))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if(percentage >= 60):
    print('First Class')
elif(percentage >= 50):
    print('Second Class')
elif(percentage >= 35):
    print('Pass')
else:
    print('Fail')