""" Largest Number """

def main():
    """ Input and Display """
    num1, num2, num3 = int(input()), int(input()), int(input())
    num1, num2 = compare(num1, num2)
    num2, num3 = compare(num2, num3)
    num1, num2 = compare(num1, num2)
    print(int(num1+num2+num3))

def compare(num1, num2):
    """ Compare between 2 number """
    num1, num2 = str(num1), str(num2)
    count = 0
    while True:
        if num1[count%len(num1)] > num2[count%len(num2)]:
            return num1, num2
        if num1[count%len(num1)] < num2[count%len(num2)]:
            return num2, num1
        count += 1
        if count > len(num1) and count > len(num2):
            return num1, num2

main()
