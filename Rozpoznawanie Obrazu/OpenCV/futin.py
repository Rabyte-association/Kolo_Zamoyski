import cv2 as cv
import numpy as np

ANIMATION_TIME = 0
TITLE = "Futin"
canvas = np.zeros((420,420,3), dtype='uint8') # stworzenie obrazu o podanych wymiarach składającego się z samych czarnych pikseli w przestrzeni BGR
def show(): # Funkcja pokazująca nowo powstały obrazek
    cv.imshow(TITLE,canvas)
    cv.waitKey(ANIMATION_TIME)
# Tworzenie macierzy; color channels
show()

# Kolorowanie pixeli
canvas[:] = (226,43,138) #bgr
"""
'[:]' oznacza pobranie wszystkich elementów z n wymiarowej listy. Powyższa
linijka nadaje wszystkim pikselom określony kolor
"""

show()

canvas[:210,:] = (255,0,0)
canvas[210:,:] = (0,255,255)

"""
Powyżej widzicie jak wybrać konkretne piksele: [a:b,c:d]
Taki zapis oznacza, że kolor zostanie nadany pikselom w przedziale od a do b dla x
i od c do d dla y (UWAGA w grafice kompouterowej y jest najczęściej odwrócone o 180 stopni czyli rośnie w dół)
"""

show()

canvas[:] = (0,0,0)
cv.rectangle(canvas, (180,10), (240,250), (255,0,0), thickness=42) # funnkcja do tworzenia prosokąta
"""
Aby stworzyć prosotkąt na obrazku musicie podać, na jakiej klatce narysować dany kształtem,
podać dwa punkty (x0,y0),(x1,y1) tworzące prostoką, kolor prostokąta i jego grubość
jeżeli w grubości dacie -1 to będzie on wypełniony
"""

show()

cv.circle(canvas, (160,250), 50, (255,255,255), thickness=-1)
cv.circle(canvas, (260,250), 50, (0,0,255), thickness=-1)
"""
Tworzenie koła działa tak samo jak prostokąt, tylko zamiast dwóch punktów
podajecie jeden i promień koła
"""
show()

cv.putText(canvas, "Futin", (120,370), cv.FONT_HERSHEY_TRIPLEX, 2.1, (203,192,255))
"""
Tekst działa podobnie tylko musicie podać czcionkę i przeskalowanie czcionki
w powyższym wypadku skalarem jest '2.1'
"""
show()
