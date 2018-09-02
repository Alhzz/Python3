''' SceneSwitch I '''

def main():
    ''' Count light function '''
    var = 0
    count = 0
    cool = 0
    warm = 0
    start = 0

    while var != 'End':
        var = input()
        if var != 'End':
            var = float(var)
            count += 1
            if count == 1:
                cool = 1
            elif count % 2 == 0:
                start = var
            else:
                if var - start <= 6 and cool == 1:
                    warm += 1
                    cool = 0
                else:
                    cool = 1

    print(warm)

main()
