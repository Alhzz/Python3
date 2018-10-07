""" HelloWorldComeBack """

def print_hello():
    """ Print hello in your language """
    word = input()

    for i in word:
        if 65 <= ord(i) <= 122:
            print("Hello", word + ".")
        else:
            print("สวัสดี", word)
        break

print_hello()
