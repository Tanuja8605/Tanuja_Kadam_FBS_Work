# 6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

###Take input from user
basic_sal = int(input("Enter basic salry:"))

###Perform Operation
Da = 10 * basic_sal/100
Ta = 12 * basic_sal/100
Hra = 15 * basic_sal/100
Total_sal = basic_sal + Da + Ta + Hra

print(f'Total salary of employee is {Total_sal}')