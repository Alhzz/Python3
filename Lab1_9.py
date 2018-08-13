""" TheFunctionWithin """

def function_1(var_a, var_b, var_c, var_d):
    """ Print Function """
    print(func_f(func_f(var_a)))
    value_fg = (func_g(func_f(var_a - var_b)))
    print(value_fg)
    print(func_h(func_f(var_a + var_b), func_f(var_a + var_c), func_g(func_f(var_d**2))))
    print(func_i(func_h(func_f(var_a + var_b), func_f(var_a - var_c), func_g(func_f(var_d**2)))\
        , value_fg, func_f(func_f(func_f(func_f(func_f(var_c))))), var_d**8))

def func_f(var_x):
    """ f(x) Function """
    return 2 * var_x

def func_g(var_x):
    """ g(x) Function """
    return 3 * var_x**4 - var_x**3 + 2 * var_x**2 + 10

def func_h(var_x, var_y, var_z):
    """ h(x, y, z) Function """
    return (var_z + var_x)**2 - var_x * var_y + var_y**2

def func_i(var_a, var_b, var_c, var_d):
    """ i(a, b, c, d) Function """
    return (var_a**2 + var_b**2 - var_c**2) / (var_d**2 - 2 * var_a * var_d + 2 * var_a)

function_1(float(input()), float(input()), float(input()), float(input()))
