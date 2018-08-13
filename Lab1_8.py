""" Boomerang """

def function():
    """ Main Function """
    var_x = int(input())
    var_y = int(input())
    var_z = int(input())

    print(function_1(var_x))
    print(function_2(var_y))
    print(function_3(var_z))
    print(function_4(var_x, var_y))
    print(function_5(var_x, var_y, var_z))

def function_1(var_x):
    """ Function 1 """
    return var_x + 1

def function_2(var_y):
    """ Function 2 """
    return 7 * var_y**3 + 2 * var_y**2 - 31 * var_y + 1

def function_3(var_z):
    """ Function 3 """
    return -var_z

def function_4(var_x, var_y):
    """ Function 1 """
    return (var_x + var_y) * (var_x - var_y)

def function_5(var_x, var_y, var_z):
    """ Function 3 """
    return (var_y - (var_y**2 - 4 * var_x * var_z)**0.5) / (2 * var_x)

function()
