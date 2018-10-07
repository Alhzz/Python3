""" BlackJack """

def deck(value, count, count_a):
    """ Calculate Card """
    for _ in range(value):
        card = input()
        if card not in "AJQK":
            card = int(card)
            count += card
        elif card in "JQK":
            count += 10
        else:
            count += 1
            count_a += 1

    for i in range(count_a, 0, -1):
        if count + 10*i <= 21:
            count += 10*i
    print(count)

deck(int(input()), 0, 0)
