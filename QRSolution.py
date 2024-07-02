import numpy as np
import math, numbers
import Triangular as tri

def add(v1, v2):
    final = []
    for i in range(len(v1)):
        final.append(v1[i] + v2[i])
    return final

def sub(v1, v2):
    final = []
    for i in range(len(v1)):
        final.append(v1[i] - v2[i])
    return final

def scalar(v1, scalar):
    final = []
    for i in range(len(v1)):
        final.append(v1[i] * scalar)
    return final

def div(v1, scalar):
    final = []
    for i in range(len(v1)):
        final.append(v1[i] / scalar)
    return final

def dot(v1, v2):
    final = 0
    for i in range(len(v1)):
        final += v1[i] * v2[i]
    return final

def norm(v1):
    return math.sqrt(dot(v1,v1))

def proj(v1, v2):
    return scalar(v2, dot(v1,v2)/dot(v2,v2))


def grahmSchimidt(basis):

    ob = []

    ob.append(div(basis[0], norm(basis[0])))
    for i in range(1,len(basis)):
        newVector = basis[i]
        projection = [0]*len(basis[0])
        for element in ob:
            projection = add(projection , proj(newVector, element))

        final = sub(newVector,projection)
        ob.append(div(final,norm(final)))

    return ob

def qrDecomposition(matrix):
    m,n = np.shape(matrix)
    columns = np.transpose(matrix)

    r = np.zeros((n,n))

    qColumns = grahmSchimidt(columns)

    for i, line in enumerate(r):
        for j, column in enumerate(line):
            if j >= i:
                r[i][j] = dot(qColumns[i], columns[j])

    q = np.transpose(qColumns)

    return q,r


def solveQR(a, b):
    q, r = qrDecomposition(a)

    qtb = np.matmul(np.transpose(q), b)
    solution = tri.solveU(r, qtb)
    return solution

a = [
    [2, 3, -1],
    [4, 1, 1],
    [-2, 1, 1]
]

b = [0, 7, 4]

if __name__ == "__main__":
    print(solveQR(a,b))
