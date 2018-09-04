""" Inflation """

def main(money, var_k):
    """
    This function will return values of inflation in n year
    """
    font = int(money * 100)

    for _ in range(var_k):
        font = font * 10381
        font = int(font // 10000)

    back = font % 100
    font = int(font // 100)
    print('%d.%02d' %(font, back))

main(float(input()), int(input()))
