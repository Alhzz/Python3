""" Inflation """

def main(money, var_k):
    """
    This function will return values of inflation in n year
    """
    rate = 1 + 0.0381

    if (var_k > 9999):
        var_k = 1000
    result = money * (rate ** var_k)
    precision = int((result - int(result))*money)
    if (precision >= 10):
        print(str(int(result)) + "."+ str(precision))
    else:
        print(str(int(result)) + ".0"+ str(precision))
main(float(input()), float(input()))