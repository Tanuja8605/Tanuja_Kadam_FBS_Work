# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag

        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag

        return ComplexNumber(real, imag)

    def display(self):
        print(self.real, "+", self.imag, "i")

    def __del__(self):
        print("ComplexNumber object destroyed")


c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(2, 5)

c3 = c1 + c2
print("Addition:")
c3.display()

c4 = c1 - c2
print("Subtraction:")
c4.display()