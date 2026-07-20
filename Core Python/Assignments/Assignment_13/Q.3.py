# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def check_dict(di, key):
    if key in di:
        print("Key exists in dictionary")
    else:
        print("Key doesn't exist in dictionary")

d = {'name': 'Ram', 'city': 'Pune', 'Salary': 45000}

key = input("Enter key: ")
check_dict(d, key)
