import random


def Y(p=0.5):

    if random.random() < p:
        return 1
    else:
        return -1


def X(t):

    xL = [0]
    yL = [0]
    for i in range(1, t+1):
        y = Y()
        yL.append(y)
        x = xL[i-1] + y
        xL.append(x)

    return (yL, xL)


def simulate(t, n):

    Xtrajecotries = []
    for i in range(n):
        Xtrajecotries.append(X(t))

    Xmeans = []
    Ymeans = []
    for i in range(t):
        sumY = 0
        sumX = 0
        for j in range(n):
            sumY += Xtrajecotries[j][0][i]
            sumX += Xtrajecotries[j][1][i]
            Xmeans.append(sumX/n)
            Ymeans.append(sumY/n)

    return (Ymeans, Xmeans)


if __name__ == "__main__":

    print(simulate(2, 100000)[1])
