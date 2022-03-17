import matplotlib.pyplot as plt
import math

def macierz_startowa(n):
    A = [[0]*n for j in range(n)] #Tworzymy macierz 
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i][j]=1 #ustawiamy ze nie znamy nikogo innego oprócz siebie
    return A

def nowe_grono(A, N):
    n = len(A)
    B = [[0]*N for i in range(N)] #Tworzymy nową macierz powiększoną o N-n znajomych 
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j] #przepisyjemy poprzednią macierz A na nową macierz B
            if i==j:
                A[i][j]=1
    return B

def licznosc_stopni(A):
    n = len(A)
    stopnie_popularnosci = [sum(A[i]) for i in range(n)]
    max_deg = max(stopnie_popularnosci)
    l = [0] * (max_deg+1)
    for i in stopnie_popularnosci:
        l[i] += 1
    return l
def p(k, m):
    if k >= m:
        return math.e**(1-k/m)/m
    return 0

def bledy():
    # Pomocnicza funkcja obliczająca błędy w pojedynczej symulacji
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
    n=5
    N=10
    A=macierz_startowa(n) #początkowo wstawiamy n uzytkownikow ktorzy sie nie znają
    for row in A:
        print(row)
    print("------------------------")

    B=macierz_startowa(N) #dodajemy kolejnych N-n uzytkownikow ktorzy sie nie znaja
    for row in B:
        print(row)
    print("------------------------")

    #zapytamy kto kogo zna?
    ile=int(input("ile osob się poznało?"))
    for i in range(ile):
        os1=int(input("podaj osobe która poznała"))
        os2=int(input("podaj z kim poznała"))
        B[os1][os2]=1
        B[os2][os1]=1
    
    #mozemy teraz sprawdzic kto kogo zna, podamy osoby które chcemy sprawdzic:
    sprawdz1=int(input("sprawdz 1. osobe"))
    sprawdz2=int(input("sprawdz 2. osobe"))
    if B[sprawdz1][sprawdz2]==1:
        print("te osoby się znają")
    if B[sprawdz1][sprawdz2]==0:
        print("te osoby się nie znają")

    #mozemy tez sprobowac narysowac rzut naszej macierzy na wykres:
    dane_x=[]
    dane_y=[]
    for i in range(N):
        for j in range(N):
            dane_x.append(B[i][0])
            dane_y.append(B[0][j])
    plt.scatter(dane_x, dane_y)
    plt.show()


if __name__ == "__main__":
    main()
