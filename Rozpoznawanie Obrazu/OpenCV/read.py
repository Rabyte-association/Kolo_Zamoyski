import cv2 as cv # łatwiej w ten sposób pisać kod
# Funkcja sprawdzająca dostępne kamery
def get_camera_object(cameras_number=2):
    for i in range(cameras_number):
        cap =  cv.VideoCapture(i) # to jest linijka zwracająca obiekt kamery, który może wam zwrócić klatki
        if not (cap is None or not cap.isOpened() or cap.read()[1] is None):
            return cap
# Odczytywanie obrazów
img = cv.imread('RaByte_Logo512.png') # odczytania obrazu
cv.imshow('Title',img) # wyświetlenie okna z obrazem i nadanie mu nazwy
"""
waitKey([value])
funkcja, która determinuje po ilu ms okno się zamknie
(albo odśiweży w przypadku kamery), jeżeli podacie 0 to czeka na wciśnięcie przycisku.
Zawsze zwraca kod ACII wciśniętego klawisza
"""
cv.waitKey(0)
# Reading Vidoes
capture = cv.VideoCapture('RECAP.mp4') # wczytanie pliku video
while True:
    isTrue, frame = capture.read() # isTrue bool czy się wczytało, frame obiekt obrazu odpowiadający aktualnej klatki
    cv.imshow('Video', frame)
    #if cv.waitKey(20) & 0xFF==ord('q') kaczka programistyczna omawiana na zajęciach
    if cv.waitKey(20)==ord('q'):
        break

capture.release() # oczyszcznie pamięci, warto dodać przy wideo ale nie jest to konieczne

# Camera input
camera = get_camera_object()
while(True):

    isTrue, frame = camera.read()

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break


camera.release()

cv.destroyAllWindows() # zamknięcie okien i zczyszczenie pamięci 
