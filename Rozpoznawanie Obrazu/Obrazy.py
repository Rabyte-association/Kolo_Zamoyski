#Aby kod działał w folderze z tym kodem muszą znajdować się pliki astronom.png i cars.png (można pobrać z neta)
import numpy    #biblioteka do macierzy
from PIL import Image   #biblioteka do obrazów

##################################################

def png_read(filepath): #zamiana obrazu na macierz
    img = Image.open(filepath)
    assert len(img.size)==2 
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath): #zamiana macierzy na obraz
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

##################################################

def negatyw(macierz):                       #funkcja robi negatyw z obrazka
    l_wierszy=len(macierz)
    l_kolumn=len(macierz[0])
    for w in range(l_wierszy):
        for k in range(l_kolumn):
            macierz[w][k]=1-macierz[w][k]  
    return macierz

def przeksztalcaj(A):                       #funkcja zmienia jasność obrazka
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]=0.02*A[i][j]
    return A

def kolory(image):                          #funkcja zmienia kolory obrazka np. niebieski=zielony
    red, green, blue = image.split()
    new_image = Image.merge("RGB", (red, blue, green)) #W tym miejscu zmieniamy kolory r,g,b na r,b,g
    new_image.save('result.jpg')

def usun_kolor(image_data,image):           #funkcja usuwa kolor, który chcemy 
    height,width = image.size
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            image_data[loop1,loop2] = 0,g,b #domyślnie w tym miejscu usuwa kolor czerwony
    image.save('changed.jpeg')

def main():
    m=0
    image = Image.open('cars.png') #zmienna która przechowuje obrazek
    image_data = image.load() #zmienna do operowania na danych obrazka (wysokosc, szerekosc itd)
    macierz=png_read('astronom.png') #zmienna która przechowuje obrazek przekonwertowany do macierzy
    #1 
    usun_kolor(image_data,image)
    #2
    kolory(image)
    #3
    wynik1=negatyw(macierz)
    png_write(wynik1, 'wynik.png')
    #4
    wynik2=negatyw(macierz)
    png_write(wynik2, 'wynik.png')

if __name__ == '__main__':
   main()
