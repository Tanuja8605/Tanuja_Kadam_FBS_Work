# 2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
       
stud = int(input('Enter number of students:'))
total_per = 0

for i in range(stud):
    print(f'Student {i+1}')

    s1 = int(input('S1 marks: '))
    s2 = int(input('S2 marks: '))
    s3 = int(input('S3 marks: '))
    s4 = int(input('S4 marks: '))
    s5 = int(input('S5 marks: '))

    obtained_marks = s1 + s2 + s3 + s4 + s5
    percentage = (obtained_marks / 500) * 100

    print('Percentage =', percentage)

    total_per += percentage

Average_per = total_per / stud
print('Average Percentage =', Average_per)