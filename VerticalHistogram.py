""" VerticalHistogram """

def histogram(word, dic):
    """ Seperate word to Histogram """
    picture = ""
    for i in word:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    key = list(dic.keys())
    key.sort(key=str.swapcase)
    var_max = max(dic, key=lambda x: dic[x])
    var_max = dic[var_max]

    for i in range(var_max, 0, -1):
        picture += "%03d " %i
        for j in key:
            if dic[j] < i:
                picture += "  "
            else:
                picture += "* "
        if i != 1:
            picture += "\n"
    print(picture)
    print("   ", *key)

histogram(input(), dict())
