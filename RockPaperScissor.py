""" RockPaperScissor """

def calculate():
    """ Calculate who win """
    result = input()
    win_a = 0
    win_b = 0

    for i in range(len(result)):
        if i % 2 == 0:
            judge = result[i]
        else:
            judge += result[i]
            if judge == 'PR' or judge == 'SP' or judge == 'RS':
                win_a += 1
            elif judge == 'RP' or judge == 'PS' or judge == 'SR':
                win_b += 1
            else:
                pass
    if win_a == win_b:
        print("DRAW", win_a)
    elif win_a > win_b:
        print("A win", str(win_a) + "-" + str(win_b))
    elif win_a < win_b:
        print("B win", str(win_b) + "-" + str(win_a))

calculate()

