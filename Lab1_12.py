""" MissionImImpossible """

def function():
    ''' Calculate x, y, z '''
    #Input equation
    var_a, var_b, var_c, var_d = int(input()), int(input()), int(input()), int(input())
    var_e, var_f, var_g, var_h = int(input()), int(input()), int(input()), int(input())
    var_i, var_j, var_k, var_l = int(input()), int(input()), int(input()), int(input())

    #Find detA
    det_a = var_a * var_f * var_k
    det_a += var_b * var_g * var_i
    det_a += var_c * var_e * var_j
    det_a += -(var_i * var_f * var_c)
    det_a += -(var_j * var_g * var_a)
    det_a += -(var_k * var_e * var_b)

    #Find x
    total = var_d * var_f * var_k
    total += var_b * var_g * var_l
    total += var_c * var_h * var_j
    total += -(var_l * var_f * var_c)
    total += -(var_j * var_g * var_d)
    total += -(var_k * var_h * var_b)
    print(int(total / det_a), end=' ')

    #Find y
    total = var_a * var_h * var_k
    total += var_d * var_g * var_i
    total += var_c * var_e * var_l
    total += -(var_i * var_h * var_c)
    total += -(var_l * var_g * var_a)
    total += -(var_k * var_e * var_d)
    print(int(total / det_a), end=' ')

    #Find z
    total = var_a * var_f * var_l
    total += var_b * var_h * var_i
    total += var_d * var_e * var_j
    total += -(var_i * var_f * var_d)
    total += -(var_j * var_h * var_a)
    total += -(var_l * var_e * var_b)
    print(int(total / det_a))

function()
