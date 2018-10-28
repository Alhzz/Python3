""" AndAgain """

def find_word(sentense):
    """ Find words and sort """
    if sentense[len(sentense) - 1] == ".":
        sentense = sentense[:len(sentense) - 1]
    sentense = sentense.split(" ")
    sentense.sort()
    fail = 0

    for i in sentense:
        count = 0
        for j in i:
            if j in "aeiou":
                count += 1
        if count > 1:
            if i[len(i) - 1] == ".":
                i = i[:len(i) - 1]
            print(i)
        else:
            fail += 1

    if len(sentense) == fail:
        print("Nope")

find_word(input())
