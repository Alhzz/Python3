''' Stepper II '''

def main():
    ''' Count 1 to n '''
    var_a = int(input())
    var_b = int(input())

    if var_a <= var_b:
        for i in range(var_a, var_b + 1):
            print(i)
    elif var_a > var_b:
        for i in range(var_a, var_b - 1, -1):
            print(i)

main()
