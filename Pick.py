""" Pick """
import json

def pick(dic, var):
    """ Find the value in Dic """
    dic = json.loads(dic)
    if dic.get(var) == None:
        print("No")
    else:
        print("Yes", dic[var], sep="\n")

pick(input(), input())
