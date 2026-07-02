# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

no_passengers = int(input('Enter number of passengers: '))
ticket_cost = int(input('Enter ticket cost: '))

total_amount = 0

for i in range(no_passengers):
    print(f'\nPassenger {i+1}')
    age = int(input('Enter age: '))

    if age < 12:
        discount = ticket_cost * 30 / 100
        amount = ticket_cost - discount
        print('Children 30% off')

    elif age > 59:
        discount = ticket_cost * 50 / 100
        amount = ticket_cost - discount
        print('Senior citizen 50% off')

    else:
        amount = ticket_cost
        print('Need to pay full')

    total_amount += amount

print('Total amount is:', total_amount)