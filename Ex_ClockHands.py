"""
ClockHands
Ason Uthatham
"""

def main():
    """ Prove that long shot equal """
    hour = float(input())
    minute = float(input())
    prove = hour * 5 + (minute / 12)

    #Compare
    if prove == minute:
        print('True')
    elif prove > minute and (prove - minute) < 1:
        print('True')
    else:
        print('False')

main()
