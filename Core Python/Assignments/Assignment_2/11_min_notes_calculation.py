# 11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
###Take input from user
amount = int(input("Enter Amount: "))

###Perform Opearation
original_amount = amount

notes_2000 = amount // 2000
amount = amount % 2000

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_10 = amount // 10
amount = amount % 10

print(f"For amount of {original_amount} Rs:")
print(f"2000 notes = {notes_2000}")
print(f"500 notes = {notes_500}")
print(f"200 notes = {notes_200}")
print(f"100 notes = {notes_100}")
print(f"50 notes = {notes_50}")
print(f"10 notes = {notes_10}")