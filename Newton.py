import numpy as np

def difDiv(list):
    if len(list) == 1:
        return list[0][1]
    else:
        return (difDiv(list[1:]) - difDiv(list[:-1]))/(list[-1][0] - list[0][0])


def newtonCoefs(list):
    coefs = []
    for i in range(1,len(list) + 1):
        coefs.append(difDiv(list[:i]))
    return coefs

list = [(-1,3),(0,1),(1,3),(3,43)]
print(newtonCoefs(list))
