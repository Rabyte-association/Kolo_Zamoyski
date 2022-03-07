import cv2 as cv

def get_camera_object(cameras_number=2):
    for i in range(cameras_number):
        cap =  cv.VideoCapture(i)
        if not (cap is None or not cap.isOpened() or cap.read()[1] is None):
            return cap

camera = get_camera_object()

while(True):

    _, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('face.xml') # wczytanie wytrenowanej klasyfikatora
    faces_rect =  haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3) #wykrywanie obiektów i zwrócenie ich koordynatów
    """
    Nie przejmujcie się zbytnio parametrami, minNeighbors jeżeli będzie zwiększone,
    zmniejszy wam ilość fałszywych wykryć (nie można przesadzać bo wam nic nie wykryje),
    a scaleFactor jeżeli zmniejszycie to będzie wam się dłużej liczyć ale też
    poprawi jakość wykrywania obiektu
    """
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (128,0,128), thickness=2)

    cv.imshow('Smile Detection', frame)

    if cv.waitKey(1) == ord('q'):
        break


camera.release()

cv.destroyAllWindows()
