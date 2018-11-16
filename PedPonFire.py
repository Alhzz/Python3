""" PedPonFire """

def cal(amoung):
    """ Calculate amoung of duck can fly """
    all_duck = list()
    total = 0
    for _ in range(amoung):
        all_duck.append(int(input()))
    var_k = int(input())
    lst1 = list(filter(lambda x: x > var_k//2, all_duck))
    lst2 = list(filter(lambda x: x <= var_k//2, all_duck))
    if len(lst1) >= len(lst2):
        for i in lst2:
            var_x = var_k - i
            total += lst1.count(var_x)
    else:
        for i in lst1:
            var_x = var_k - i
            total += lst2.count(var_x)
    print(total)

cal(int(input()))
