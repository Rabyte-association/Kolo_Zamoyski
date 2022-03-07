import cv2 as cv

img = cv.imread("poglod.jpg")
cv.imshow('poglod',img)

cv.waitKey(0)

# Konwersja na odcienie szarosci
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # zmiana przestrzeni kolorystycznej z BGR na skalę szarości
cv.imshow('gray poglod',gray)
cv.waitKey(0)

"""
HSV separates luma, or the image intensity,
from chroma or the color information. This is very useful in many applications.
"""
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) # zmiana przestrzeni kolorystycznej z BGR na HSV
cv.imshow('hsv poglod',hsv)
cv.waitKey(0)

img_hsv = cv.imread("HSV_cone.jpg")
cv.imshow('what is hsv?',img_hsv)
cv.waitKey(0)

# Podstawowa metoda rozmycia obrazu aby pozbyć się niepotrzebnych szczegółów
"""
Rozmycie obrazu, 7x7 to romiar macierzy "rozmywającej", możecie sobie doczytać jak ten algorytm działa
aczkolwiek potrzebujecie ogarniać bardziej matmę niż poziom licealny
"""
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)

# Wykrywanie krawędzi
cany = cv.Canny(img,125,175) #threshold values
cv.imshow('edge detection',cany)
cv.waitKey(0)

cany_blur = cv.Canny(blur,125,175)
cv.imshow('edge detection',cany_blur)
cv.waitKey(0)
