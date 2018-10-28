""" MissingCard I """

def gen_all_card():
    """ Generate all card and return as a setm """
    rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    all_card = list()
    for i in rank:
        all_card.append(i+"S")
        all_card.append(i+"H")
        all_card.append(i+"D")
        all_card.append(i+"C")
    return set(all_card)

def missing():
    """ Find missing card """
    all_card = gen_all_card()
    card = set()
    for _ in range(51):
        card.add(input())
    print(*(all_card - card))

missing()
