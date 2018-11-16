""" Catalan """
 
def calculate(num):
    """ Calculate Catalan """
    if num == 1:
        print(num)
    else:
        node = [1]
        for i in range(1, num):
            node.append(int((4*i + 2)/(i + 2)*node[i-1]))
        print(node[num-1])
calculate(int(input()))
