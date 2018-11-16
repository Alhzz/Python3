""" Day2011 """

def cal_day(day, mon):
    """ Calculate day in 2011 """
    month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    week = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday"\
    , 5: "Wednesday", 6: "Thursday", 0: "Friday"}

    for i in range(1, mon):
        day += month[i]
    print(week[day%7])

cal_day(int(input()), int(input()))
