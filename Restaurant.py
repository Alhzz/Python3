""" Restaurant """

def calculate(price, promo, discout, more):
    """ Calculate worthiness """
    new_price = price + more

    if price >= promo:
        price = price*(100 - discout)/100
    if new_price >= promo:
        new_price = new_price*(100 - discout)/100

    if price > new_price:
        print("Yes %.3f" %(abs(new_price - price)))
    elif price < new_price:
        print("No %.3f" %(abs(new_price - price)))
    else:
        print("Yes")

calculate(float(input()), float(input()), float(input()), float(input()))
