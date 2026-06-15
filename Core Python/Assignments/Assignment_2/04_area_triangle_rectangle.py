# 4. WAP to calculate area of triangle and rectangle

###Take input from user
l = int(input("Enter length:"))
h = int(input("Enter height:"))
b = int(input("enter base:"))
br = int(input("Enter breadth:"))

###Perform Operation

triangle_area = (0.5) * b * h 
rectangle_area = l * br

print(f'area of triangle is {triangle_area} & area of reactangle {rectangle_area}')
