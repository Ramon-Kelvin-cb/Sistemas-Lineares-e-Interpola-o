import numpy as np

def solveU(a, b):
    n = len(a[0])
    solution = [0] * n
    solution[n - 1] = b[-1]/a[-1][-1]

    for i in range(n - 2, -1, -1):
        acc = 0
        for j in range(i, n):
            acc += a[i][j] * solution[j]

        solution[i] = (b[i] - acc)/a[i][i]

    return solution

def solveL(a, b):
    n = len(a[0])
    solution = [0] * n
    solution[0] = b[0]/a[0][0]

    for i in range(1, n):
        acc = 0
        for j in range(0, i):
            acc += a[i][j] * solution[j]

        solution[i] = (b[i] - acc)/a[i][i]

    return solution
