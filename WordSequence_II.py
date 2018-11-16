""" WordSequence II """

def convert(word1, word2):
    """ Convert word1 to word2 """
    for i in range(max(len(word1), len(word2))+1):
        print(word2[:i] + word1[i:])

convert(input(), input())
