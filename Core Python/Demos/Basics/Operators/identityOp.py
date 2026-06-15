# 1.is
x = 10
y = 10
Z = 20
print(x is y)

li1 = [10,20,30]
li2 = [10,20,30]
print(li1 is li2)

# 2.is not
print(li1 is not li2)
print(x is not y)

print(id(x)) ## it shows memory adddress
print(id(y))
print(id(Z))

print(id(li1))
print(id(li2))