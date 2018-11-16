""" CoinChangev1 """

def change(money):
    """ Calculate coin you have to change """
    coin = [25, 10, 5, 1]
    total = 0
    for i in coin:
        total += money//i
        money %= i
    print(total)

change(int(input()))
