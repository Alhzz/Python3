""" Donut """

def main():
    """ Calculate """
    price = int(input())
    buy = int(input())
    free = int(input())
    want = int(input())

    pack = buy + free
    get = 0
    total = 0

    if want == buy:
        get += pack
        total += price*buy
    elif buy > want:
        get += want
        total += want*price
    else:
        cycle = int(want / pack)
        var = want - cycle*pack
        if var < buy:
            get += cycle * pack + var
            total += (cycle * buy + var)*price
        else:
            cycle += 1
            get += cycle * pack
            total += (cycle * buy)*price

    print(total, get)

main()
