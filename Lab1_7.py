""" JumpAround """

def function1():
    """ Input Function """
    variable = input()
    variable = int(variable)
    calculate(variable)

def calculate(value):
    """ Calculate Function """
    print(value)
    print(value + 5)
    print(value - 17)
    print(value * 32)
    print(5 * value**2 + 10 * 5 * value + 3)

function1()
