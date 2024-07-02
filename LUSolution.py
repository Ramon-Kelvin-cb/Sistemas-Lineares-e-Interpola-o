import QRSolution as vec
import Triangular as tri
import numpy as np

def decomposition(a):
    u = np.copy(a)
    n = np.shape(a)[0]
    l = np.eye(n)
    for j in range(n - 1):
        for i in range(j + 1, n):
            l[i][j] = u[i][j] / u[j][j]
            u[i] = vec.sub(u[i], vec.scalar(u[j], l[i][j]))
    return l, u

def solveLU(a, b):
    l, u = decomposition(a)
    y = tri.solveL(l, b)
    return tri.solveU(u, y)

a = [
    [1, 1, 1],
    [2, 1, -1],
    [2, -1, 1]
]

b = [-2, 1, 3]

if __name__ == "__main__":
    print(solveLU(a,b))
