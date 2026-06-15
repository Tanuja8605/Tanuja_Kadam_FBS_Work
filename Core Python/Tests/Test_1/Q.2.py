#2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)
# Take input from user
P = int(input('Entre Principal:'))
R = float(input('Enter Rate:'))
T = int(input('Enter Time:'))

# Perform Operation
SI = P*R*T/100
print(f'Simple Interest of {P} is {SI}')