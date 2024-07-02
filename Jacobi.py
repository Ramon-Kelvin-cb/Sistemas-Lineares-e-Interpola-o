import numpy as np
import QRSolution as vec

def iterDecomp(a, b):
    n = len(a[0])
    c = np.zeros((n,n))
    g = np.copy(b)

    for i in range(n):
        for j in range(n):
            if i == j:
                c[i][j] = 0
            else:
                c[i][j] -= a[i][j]/a[i][i]
        g[i] = g[i]/a[i][i]

    return c, g


def jaobiIter(a, b, x0, error):
    c, g = iterDecomp(a, b)

    x = vec.add(np.matmul(c, x0), g)

    #||b - Ax|| < error
    test = vec.norm(vec.sub(b, np.matmul(a, x)))

    while test > error:
        x0 = x
        x = vec.add(np.matmul(c, x0), g)
        test = vec.norm(vec.sub(b, np.matmul(a, x)))

    return x

a = [
    [5, 1, 1],
    [3, 4, 1],
    [3, 3, 6]
]

b = [5., 6., 0.]

print(jaobiIter(a, b, [0., 0., 0.], 0.000005))
