""" Calculate good day """

def good_day():
    """ Find amount of good day """
    count = 0
    everyday = input().split(",")
    for i in range(len(everyday)):
        if i == 0:
            if int(everyday[0]) >= 80:
                count += 1
            yester = int(everyday[0])
            continue
        else:
            if int(everyday[i]) >= 80 or int(everyday[i]) - yester >= 10:
                count += 1
            yester = int(everyday[i])
    print(count)

good_day()
