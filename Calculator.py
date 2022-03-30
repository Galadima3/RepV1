from itertools import product
from re import S

class Calculator:
    def __init__(self, firstnum, secondnum):
        self.firstnum = firstnum
        self.secondnum = secondnum

    def add(self):
        return self.firstnum + self.secondnum

    def subtract(self):
        return self.firstnum - self.secondnum

    def product(self):
        return self.firstnum * self.secondnum

    def division(self):
        if (self.firstnum % self.secondnum == 0):
            return self.firstnum / self.secondnum
        else:
            print(
                f'Division can not go! Answer = {int(self.firstnum / self.secondnum)} & Remainder = {self.firstnum % self.secondnum}')


a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))

print('Press 1 for Addition | Press 2 for Subtraction | Press 3 for Multiplication | Press 4 for Division')
input = int(input('Enter your Choice >>> '))

if (input == 1):
    Sum = Calculator (a, b)
    print('Sum: ',Sum.add())
elif (input == 2):
    Difference = Calculator(a, b)
    print('Subtraction: ', Difference.subtract())
elif (input == 3):
    Multiply = Calculator(a, b)
    print('Multiplication: ', Multiply.product())
elif (input == 4):
    Division = Calculator(a, b)
    print('Division: ',Division.division())



