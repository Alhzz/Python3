""" BookWorm """

def cal(book):
    """ Calculate worm can read """
    for _ in range(book):
        full_time = float(input())
        all_time = list()
        total_time = 0
        count = 0
        for _ in range(int(input())):
            all_time += [float(input())]
        all_time.sort()
        for i in all_time:
            if full_time < total_time+i:
                break
            total_time += i
            count += 1
        print(count)

cal(int(input()))
