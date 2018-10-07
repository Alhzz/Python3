""" Milk """

def calculate(price, promo, reciev, money):
    """ Calculate amoung of bottom """
    bottom = money//price
    total = bottom
    while bottom >= promo and promo != 0:
        bottom = bottom - promo
        bottom += reciev
        total += reciev
    print(total)

calculate(int(input()), int(input()), int(input()), int(input()))
