""" AlmostMean """

def find_avarage(amoung):
    """ Find nearest score that under avarage """
    dic = dict()
    avarage = 0
    for _ in range(amoung):
        before_dic = input().split("\t")
        dic.update({before_dic[0]: float(before_dic[1])})
        avarage += float(before_dic[1])

    avarage /= amoung
    all_keys = list(dic.keys())
    count = 0
    for i in all_keys:
        if dic[i] <= avarage:
            if count == 0:
                near = avarage - dic[i]
                count += 1
                detail = "%s" %i + "\t" + "%s" %dic[i]
            elif avarage - dic[i] <= near:
                near = avarage - dic[i]
                detail = "%s" %i + "\t" + "%s" %dic[i]
    print(detail)

find_avarage(int(input()))
