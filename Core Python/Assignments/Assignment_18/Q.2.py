# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator
class Distance:

 def __init__(self, km, m, cm):
    self.km = km
    self.m = m
    self.cm = cm

 def __add__(self, other):
    total_cm = self.cm + other.cm
    total_m = self.m + other.m
    total_km = self.km + other.km

    total_m += total_cm // 100
    total_cm = total_cm % 100

    # Convert m to km
    total_km += total_m // 1000
    total_m = total_m % 1000

    return Distance(total_km, total_m, total_cm)

 def __sub__(self, other):
    km = self.km - other.km
    m = self.m - other.m
    cm = self.cm - other.cm

    if cm < 0:
        cm += 100
        m -= 1

    if m < 0:
        m += 1000
        km -= 1

    return Distance(km, m, cm)

 def display(self):
   print(f"{self.km} km, {self.m} m, {self.cm} cm")

 def __del__(self):
    print("Destructor called")

d1 = Distance(2, 500, 80)
d2 = Distance(1, 600, 30)

print("Addition:")
result = d1 + d2
result.display()


print("Subtraction:")
result = d1 - d2
result.display()
