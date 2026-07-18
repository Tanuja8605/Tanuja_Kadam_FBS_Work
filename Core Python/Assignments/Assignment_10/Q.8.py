# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
def list_copy(li):
    copy_list = []

    for item in li:
        copy_list.append(item)

    return copy_list


li = [40, 33, 41, 12, 23, 65]

res = list_copy(li)

print("Original List:", li)
print("Copied List  :", res)