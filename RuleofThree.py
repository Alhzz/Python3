""" RuleofThree """

def find_best():
    """ Find Best Price """
    number = int(input())
    best = 0
    best_p = 0

    for i in range(number):
        price = float(input())
        weight = float(input())
        total = weight/price
        if i == 0 or total > best or (total == best and price < best_p):
            best_p = price
            best_w = weight
            best = total
    print("%.2f %.2f" %(best_p, best_w))

find_best()
