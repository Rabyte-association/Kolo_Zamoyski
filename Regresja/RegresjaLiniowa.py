import matplotlib.pyplot as plt

def oblicz(key,a,b):
    y=a*key+b
    print(f"Przy sile {key} newtonów robot będzie miał uszkodzenia na poziomie około {y}%")

def main():
    dane_x=[200,160,500,311,863.5]
    dane_y=[10,9,28,22,42]
    a = 0.044
    b = 3.24

    key=int(input())
    oblicz(key,a,b)
    
    # wykres rozproszenia:
    plt.scatter(dane_x, dane_y)

    # rysowanie odcinka [xmin, xmax], [ymin, ymax]:
    plt.plot([0, 1000], [b+a*(0), b+a*1000], color="red")
    plt.show()
    
if __name__ == '__main__':
    main()
