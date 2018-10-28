""" HorizontalHistogram """

def count_letter(word):
    """ Count letter and print """
    myset_upper = set()
    myset_lower = set()
    for i in word:
        if i.isupper():
            myset_upper.add(i)
        else:
            myset_lower.add(i)
    myset = sorted(list(myset_lower)) + sorted(list(myset_upper))

    for i in myset:
        if word.count(i) > 5:
            count = word.count(i)
            print("%s : " %i, end="")
            while count > 5:
                print("-----|", end="")
                count -= 5
            print("-"*count)
        else:
            print("%s :" %i, "-"*word.count(i))


count_letter(input())
