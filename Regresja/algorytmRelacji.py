import numpy as np
import random
import math
import matplotlib.pyplot as plt

def macierz_startowa(n):
    A = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 0
    return A

def licznosc_stopni(A):
    n = len(A)
    stopnie_popularnosci = [sum(A[i]) for i in range(n)]
    max_deg = max(stopnie_popularnosci)
    l = [0] * (max_deg+1)
    for i in stopnie_popularnosci:
        l[i] += 1
    return l

def nowe_grono(A, N, m):
    if not 0 < m <= len(A) < N:
        raise ValueError("Bledne dane")
    n = len(A)
    final_matrix = [[0 for i in range(N)] for j in range(N)]
    # Wpisuję już istniejące relacje w macierz finalną
    for i in range(n):
        for j in range(n):
            final_matrix[i][j] = A[i][j]
    for i in range(n, N):
        new_friends = random.sample(range(i), m)
        for j in new_friends:
            final_matrix[i][j] = 1
            final_matrix[j][i] = 1
    return final_matrix

def p(k, m):
    if k >= m:
        return math.e**(1-k/m)/m
    return 0

def bledy():
    N = 100
    m = 3
    n = 5
    A = macierz_startowa(n)
    B = nowe_grono(A, N, m)
    l = licznosc_stopni(B)
    bledy = [l[i] - N*p(i, m) for i in range(len(l))]
    return bledy

def srednie_bledy(T):
    N = 100
    wszystkie_bledy = [0 for i in range(N+1)]
    for i in range(T):
        nowe_bledy = bledy()
        for j in range(len(nowe_bledy)):
            wszystkie_bledy[j] += nowe_bledy[j]
    return [wszystkie_bledy[i]/T for i in range(len(wszystkie_bledy))]

def main():
    x = srednie_bledy(1000)
    plt.scatter(range(len(x)), x)
    plt.show()


if __name__ == "__main__":
    main()
