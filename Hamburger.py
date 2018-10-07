""" Hamburger """

def calculate():
    """ Calculate size of humburger """
    right = int(input())
    left = int(input())
    centre = (right + left)*2
    print("|"*right + "*"*centre + "|"*left)

calculate()
