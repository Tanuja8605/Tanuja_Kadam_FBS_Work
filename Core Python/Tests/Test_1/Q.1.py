# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:
# Take input from user
length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))

radius = breadth / 2

area = (length * breadth) + (0.5 * 3.14 * radius * radius)

perimeter = (2 * length) + breadth + (3.14 * radius)

print("Area =", area)
print("Perimeter =", perimeter)