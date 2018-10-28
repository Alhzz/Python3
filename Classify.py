""" Classify """

def classifi():
    """ Classify student """
    all_student = list()
    year = set()
    while True:
        student = input()
        if student == "END":
            break
        all_student.append(student)
        year.add(student[0:4])
    year = sorted(year)
    start = ""
    for i in year:
        count = 0
        front = i[0:2]
        for j in all_student:
            if i in j[0:4]:
                count += 1
        if front != start:
            print(i[0:2], int(i[2:4]), count)
            start = front
        else:
            print("--", int(i[2:4]), count)

classifi()
