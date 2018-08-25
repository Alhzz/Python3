''' Check pass '''

def check(score):
    ''' Judge that fail or pass '''
    if score < 450:
        print('Fail\nProcess is terminated')
    else:
        print('Pass\nProcess is terminated')

check(float(input()))
