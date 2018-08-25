""" Check Weight """

def calculate():
    """ Calculate weight and print"""
    average = float(input())
    var_x1 = float(input())
    var_x2 = float(input())
    var_x3 = float(input())
    var_x4 = average * 4 - (var_x1 + var_x2 + var_x3)
    more = average/2 + average
    less = average - average/2

    #Calculate and Print
    total = var_x1 + var_x2 + var_x3 + var_x4
    if total > 15000:
        print('Overweight')
    elif var_x1 > more or var_x2 > more or  var_x3 > more or var_x4 > more:
        print('Unbalance')
    elif var_x1 < less or var_x2 < less or  var_x3 < less or var_x4 < less:
        print('Unbalance')
    else:
        print('Pass %.2f' % (var_x4))

calculate()
