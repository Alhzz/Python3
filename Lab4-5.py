''' Gift III '''

def main():
    ''' Find gift '''
    amoung = int(input())
    heavy = 0
    heaviest = 0

    #Input and find 2nd of heaviest
    for _ in range(amoung):
        thing = int(input())
        if thing > heavy and thing != heaviest:
            heavy = thing
            if heavy > heaviest:
                heaviest, heavy = heavy, heaviest


    #Compare and print
    if amoung <= 1 or heavy == 0:
        print('Exit')
    else:
        print(heavy)

main()
