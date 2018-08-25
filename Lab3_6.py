'''
Calculate leap year from year in AD
'''

def calculate(year):
    ''' Calculate leap year '''
    if year % 4 == 0 and year % 100 != 0:
        return 'Yes'
    elif year % 400 == 0 and year % 100 == 0:
        return 'Yes'
    else:
        return 'No'

def main():
    ''' Input and print '''
    year = int(input())
    print(calculate(year))

main()
