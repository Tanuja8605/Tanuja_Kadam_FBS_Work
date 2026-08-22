try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    opr = input("Enter operator (+, -, *, /): ")

    valid_operators = ["+", "-", "*", "/"]

    if opr not in valid_operators:
        raise ValueError("Invalid operator")

    if opr == "+":
        print("Result:", num1 + num2)

    elif opr == "-":
        print("Result:", num1 - num2)

    elif opr == "*":
        print("Result:", num1 * num2)

    elif opr == "/":
        print("Result:", num1 / num2)

except ValueError:
    print("Please enter valid numbers or a valid operator.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Calculater Completed...")