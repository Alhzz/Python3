""" Key_Midterm2014 """

def calculate():
    """ Calculate Key """
    id_card = input()
    last_digit = (int(id_card)%1000)*10
    total = 0

    for i in id_card:
        total += int(i)
    total += last_digit
    if total < 1000:
        total += 1000
    total = total%10000
    print("%04d" %total)

calculate()
