# 12. Write a program to create three lists of numbers, their squares
# and cubes
def generate_square_cube(li):
    square_li = []
    cube_li = []

    for num in li:
        square_li.append(num ** 2)
        cube_li.append(num ** 3)

    return li, square_li, cube_li


li = [2, 4, 5, 6, 8, 10]

numbers, squares, cubes = generate_square_cube(li)

print("Original List :", numbers)
print("Square List   :", squares)
print("Cube List     :", cubes)