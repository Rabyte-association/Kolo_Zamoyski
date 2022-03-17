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


if __name__ == "__main__":
    main()
