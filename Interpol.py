import numpy as np
import QRSolution as qr

def vandermondMatrix(list):
    n = len(list)
    result = np.zeros((n ,n))

    for i, line in enumerate(result):
        for j, element in enumerate(line):
            result[i][j] = element + list[i][0] ** j

    return result


def interpolCoeficients(list):
    a = vandermondMatrix(list)
    b = [element[1] for element in list]
    return qr.solveQR(a,b)


list = [(-1.,4.), (0.,1.), (2.,-1.)]

if __name__ == "__main__":
    print(interpolCoeficients(list))
