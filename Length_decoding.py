""" Run Length Decoding """

def decode(word):
    """ Decode words """
    newword = ""
    for i in range(len(word)):
        if i == 0:
            count = str(word[i])
        elif word[i] in "1234567890":
            count += str(word[i])
        else:
            newword += word[i]*int(count)
            count = ""
    print(newword)

decode(input())
