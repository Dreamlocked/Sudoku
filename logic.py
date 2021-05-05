import random
import numpy as np


def matrizProblem() -> np:
    matriz = np.zeros((9, 9), dtype=int)
    i = 0
    while(i < 30):
        k = random.randrange(1, 10)
        x = random.randrange(9)
        y = random.randrange(9)
        flag = 1
        if(matriz[x][y] == 0):
            for a in range(9):
                if(k == matriz[x][a]):
                    flag = 0
                    break
                elif(k == matriz[a][y]):
                    flag = 0
                    break
            n = x//3  # for matriz 3x3
            m = y//3
            for c in range(3*n, 3*n+3):
                for d in range(3*m, 3*m+3):
                    if(k == matriz[c][d]):
                        flag = 0
                        break
            if(flag):
                matriz[x][y] = k
                i += 1
    return matriz
