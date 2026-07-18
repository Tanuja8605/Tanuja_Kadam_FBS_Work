# 8. Print 1 to 100 in snakes and ladder pattern.
def snake_ladder():
    start = 91

    for row in range(10):
        end = start + 9

        if row % 2 == 0:
            for j in range(end, start - 1, -1):
                print(j, end=" ")
        else:
            for j in range(start, end + 1):
                print(j, end=" ")

        print()
        start -= 10


snake_ladder()