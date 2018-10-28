""" LetterFrequency """
import string

def frequency(word):
    """ Find the most used letter """
    word_list = list()
    letter_list = list()
    time = 0

    for i in word:
        if i in string.ascii_letters:
            word_list.append(i.lower())
    letter_list = set(word_list)
    for i in letter_list:
        if word_list.count(i) > time:
            time = word_list.count(i)
            letter = i
    print(letter)

frequency(input())
