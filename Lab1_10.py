""" Timing """

def time_convert():
    """ Time Convertor """
    sec = int(input())
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    minute = sec // 60
    sec %= 60

    print(day, hour, minute, sec)

time_convert()
