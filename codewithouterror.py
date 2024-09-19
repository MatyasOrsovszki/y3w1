problem = input("Please input the problem in the format a # b where # is the operator and a and b are numbers")
number1 = float(problem.split()[0])
number2 = float(problem.split()[-1])
operation = str(problem.split()[1])

class CALCULATOR:
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b

CALC = CALCULATOR()

operations = {"+" : CALC.add(number1,number2), "-" : CALC.subtract(number1,number2), "*" : CALC.multiply(number1,number2), "/": CALC.divide(number1,number2)}

print(operations[operation])
