''' SurprisingVote '''

def find_surprise():
    '''
    Find possibility of Surprising
    '''
    total = float(input())  #Total score
    high = float(input())   #The highest score

    #Calculate
    low = ((total - high) / 2)
    if low >= 1:
        low -= 1

    #Check possibility
    if high - low > 2:
        print('Surprising')
    else:
        print('Not surprising')

find_surprise()
