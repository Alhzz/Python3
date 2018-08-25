''' FoodGrade I '''

def main():
    ''' Main Function '''
    good = 0
    good += check()
    good += check()
    good += check()
    good += check()
    print(good)

def check():
    ''' Input and Check '''
    good = 0
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    num = int(input())
    if 50 <= num <= 70:
        good += 1
    return good

main()
