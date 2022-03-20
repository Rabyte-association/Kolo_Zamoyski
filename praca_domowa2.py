# Stworzymy program do rezerwacji podróży lotniczych
# Miejsce wolne oznaczymy przez 0, zajęte przez 1. Na początku wszystkie miejsca są wolne 
# Należy najpierw zaimplementować macierz 7:5 (7 wierszy, 5 kolumn) ilustrującą miejsca w samolocie:
# Wynik 1:
#
#     1  2  3  4  5 
#  A [0, 0, 0, 0, 0]
#  B [0, 0, 0, 0, 0]
#  C [0, 0, 0, 0, 0]
#  D [0, 0, 0, 0, 0]
#  E [0, 0, 0, 0, 0]
#  F [0, 0, 0, 0, 0]
#  G [0, 0, 0, 0, 0]
#
# Następnie wylosujemy 8 miejsc, które będą zajęte. W pythonie losujemy liczby z przedziału w następujący sposób:
#
import random
i=random.randint(1,7)
j=random.randint((1,5)
#
# Wynik 2:
#
#     1  2  3  4  5 
#  A [0, 0, 0, 0, 1]
#  B [0, 1, 0, 0, 0]
#  C [0, 1, 0, 0, 0]
#  D [0, 1, 1, 0, 0]
#  E [0, 0, 0, 1, 0]
#  F [0, 1, 0, 0, 0]
#  G [1, 0, 0, 0, 0]
#                
# Trzecim etapem jest zrobienie terminala, który będzie obsługiwał następujące pytania:
#                 
# 1. Sprawdzał miejsce i odpowiadał na pytanie czy jest zajęte, czy wolne
# 2. Zajmował miejsce, które chcemy, w przypadku gdy jest zajęte zwracał informacje, że miejsce jest zajęte
# 3. Stworzenie drugiej macierzy reprezentującej miejsca w drugim samolocie (Też zajmujemy losowo tym razem 13 miejsc).
# Wprowadzenie funkcji porównującej te dwa samoloty tzn. funkcja wykonuje dodawanie i odejmowanie macierzy. 
# W przypadku gdy w obydwu samolotach to samo miejsce jest zajęte (1 i 1) dodawanie zwraca 1.
# 4.(*) Narysowanie wykresu rozproszenia, który bierze dane z obydwu samolotów i w ten sposób narysuje wykres, w którym więcej 
# punktów (zajętych miejsc) będzie w samolocie, w którym zajęto więcej miejsc. Przykładowy wykres rozproszenia:
#                 
# http://www.miroslawmamczur.pl/wp-content/uploads/2019/12/11.png 
plt.scatter(x,y) #wykres rysujący rozproszenie punktów (z zajęć 1)                
                 
                 
