# 5. WAP to calculate selling price of book based on cost price and discount.

###Take input from user
cost_price = int(input("Enter cost price of book:"))
discount = int(input("Enter discount:"))

###Perform Operation
discount_amount = cost_price * discount/100
selling_price = cost_price - discount_amount

print(f'For cost price {cost_price} and discount {discount}%, selling price is {selling_price}')