''' Calculate grade 2.0 '''

def calculate():
    ''' Input and calculate grade '''
    score = float(input())

    if score > 100 or score < 0:
        print('ERR')
    elif 95 <= score <= 100:
        print('A')
    elif 90 <= score:
        print('B+')
    elif 85 <= score:
        print('B')
    elif 80 <= score:
        print('C+')
    elif 75 <= score:
        print('C')
    elif 70 <= score:
        print('D+')
    elif 65 <= score:
        print('D')
    elif 60 <= score:
        print('F+')
    else:
        print('F')

calculate()
