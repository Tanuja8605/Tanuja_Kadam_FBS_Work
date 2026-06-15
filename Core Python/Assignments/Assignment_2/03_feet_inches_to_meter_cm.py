# 3. Convert distant given in feet and inches into meter and centimeter.

###Take input from user
feet = int((input("Enter feet:")))
inch = int(input("Enter inches:"))

###Perform OPeration

total_inches = (feet * 12) + inch
total_cm = total_inches * 2.54
meter = total_cm // 100
centimeter = total_cm % 100

print(f'Given distance in meter and centimeter is {meter} meter & {centimeter}cm')

