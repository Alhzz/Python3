""" Nearer """

def find_nearer(num1, num2, car):
    """ Find who nearest the car """
    if abs(car - num1) < abs(car - num2):
        print("Alice", abs(car - num1))
    elif abs(car - num1) > abs(car - num2):
        print("Bob", abs(car - num2))
    else:
        print("Sundaes", abs(car - num1))

find_nearer(int(input()), int(input()), int(input()))
