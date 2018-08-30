''' Grade III '''

def main():
    ''' Count 1 to n '''
    subject = int(input())
    grade = 0

    #Input all score and calculate grade
    for _ in range(subject):
        grade += calculate(float(input()))

    #Calculate GPA
    grade /= subject
    grade = int(grade * 100) * 0.01
    print('%.2f' % grade)

def calculate(score):
    ''' Calculate grade and Return'''
    if 95 <= score <= 100:
        score = 4
    elif 90 <= score:
        score = 3.5
    elif 85 <= score:
        score = 3
    elif 80 <= score:
        score = 2.5
    elif 75 <= score:
        score = 2
    elif 70 <= score:
        score = 1.5
    elif 65 <= score:
        score = 1
    elif 60 <= score:
        score = 0.5
    else:
        score = 0
    return score

main()
