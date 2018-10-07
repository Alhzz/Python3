"""
Taxi v.1
Ason Uthatham
"""
import math

def main():
    """ Input and Print """
    dist = int(input())     #Distance in kilomater
    slow = int(input())     #Time in traffic jame in minute

    total = traffic_jame(slow)
    total += calculate_dist(dist)
    print(total)

def traffic_jame(time):
    ''' Calculate coat and time when traffic jame '''
    baht = time * 1.5
    baht = math.floor(baht)
    if baht % 2 != 0:
        baht -= 1
    return baht

def calculate_dist(dist):
    ''' Calculate cost and return '''
    if dist >= 0:
        baht = 35
    if 2 <= dist <= 12:
        baht += (dist - 1) * 5
    elif 13 <= dist <= 20:
        baht += 55
        baht += (dist - 12) * 5.5
    elif 21 <= dist <= 40:
        baht += 99
        baht += (dist - 20) * 6
    elif 41 <= dist <= 60:
        baht += 219
        baht += (dist - 40) * 6.5
    elif 61 <= dist <= 80:
        baht += 349
        baht += (dist - 60) * 7.5
    elif dist > 80:
        baht += 499
        baht += (dist - 80) * 8.5
    baht = math.ceil(baht)
    if baht % 2 == 0:
        baht += 1
    return baht

main()
