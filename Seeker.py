""" Seeker """

def find_num(string, total):
    """ Find number """
    keep = ""
    for i in range(len(string)):
        if string[i].isdigit():
            keep += string[i]
        elif keep != "":
            total += int(keep)
            keep = ""
        if len(string) - 1 == i and keep != "":
            total += int(keep)
            keep = ""
    print(total)

find_num(input(), 0)
