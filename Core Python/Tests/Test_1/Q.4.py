# Take input from user
area = int(input("Area of wall's:"))
interior_cost = int(input('Enter Interior cost:'))
exterior_cost = int(input('Enter Exterior cost:'))

# Perform Operation
interior_area = 8 * area
exterior_area = 7 * area

interior_cost = interior_area * interior_cost
exterior_cost = exterior_area * exterior_cost

final_cost = interior_cost + exterior_cost

print("final cost of both wall's",final_cost)