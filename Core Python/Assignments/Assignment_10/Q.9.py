# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def separate_even_odd(li):
    even_li = []
    odd_li = []

    for ele in li:
        if ele % 2 == 0:
            even_li.append(ele)
        else:
            odd_li.append(ele)

    return even_li, odd_li


li = [2, 1, 3, 4, 5, 67, 8, 10, 11, 12]

even_list, odd_list = separate_even_odd(li)

print("Even List:", even_list)
print("Odd List :", odd_list)