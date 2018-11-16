""" CaesarV1 """

def decode(num, text):
    """ Decode text """
    new_text = ""
    if num > 26:
        num %= 26
    elif num < -26:
        num = abs(num) % 26 * -1

    for i in text:
        if i.isupper():
            new_text += chr(cal(ord(i)-65, num) + 65)
        elif i.islower():
            new_text += chr(cal(ord(i)-97, num) + 97)
        else:
            new_text += i
    print(new_text)

def cal(alph, num):
    """ Calculate letter """
    if alph + num < 0:
        return 26 + num + alph
    elif alph + num > 25:
        return alph + num - 26
    else:
        return alph + num

decode(int(input()), input())
