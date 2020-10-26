import random
import time
from matplotlib import pyplot as plt
import sys


def Busq_Lineal(a, k):
    i = 0
    while(i < len(a)-1):
        if a[i] == k:
            return i
        i += 1
    return None


def busquedaBinariaRecursiva(a, k, Left, Right):
    if (Left > Right):
        return None  # Caso base, he acabado y no lo encontré
    Half = (Left+Right)//2

    if a[Half] == k:  # Si el de enmedio es mi llave
        return Half
    elif a[Half] > k:  # "Mas abajo, mi numero es mas chico"
        return busquedaBinariaRecursiva(a, k, Left, Half-1)
    else:  # "Mas arriba"
        return busquedaBinariaRecursiva(a, k, Half+1, Right)


# Recibe cada caso para saber que es lo que va a graficar
def graficarTiempos(numDatos, tiempos_BusqLineal, tiemposMerge, case):
    fig, ax = plt.subplots()
    ax.plot(numDatos, tiempos_BusqLineal,
            label="Ordenamiento de la Burbuja", marker="*", color="r")  # Le doy parametros para personalizar la grafica
    ax.plot(numDatos, tiemposMerge,
            label="Ordenamiento de Merge", marker=".", color="g")
    ax.set_xlabel("Numero de Datos ")  # Eje de las x
    ax.set_ylabel("Tiempo [s]")  # Eje de las Y
    ax.grid(True)
    ax.legend(loc=2)  # En que cuadrante se encuentra
    plt.title(case)
    plt.show()  # Muestra la gráfica.


def eficienciaAlgoritmos(numDatos, case):

    # Creamos las listas vacias para medir tiempo
    tiempos_BusqLineal = []
    tiempos_BusqBin = []

    for n in numDatos:

        lista_Burbuja = random.sample(range(0, 1000000), n)  # genera(n)

        if case == "Mejor de los casos":
            print("\n\t", case)
            lista_Burbuja.sort()
        elif case == "El peor de los casos":
            print("\n\t", case)
            lista_Burbuja.sort(reverse=True)
        else:
            print("\n\t", case)

        lista_Busq_BinR = lista_Burbuja.copy()
        print("\n=========\n")
        t0 = time.monotonic()  # Toma el tiempo (preferentemente largo) que nunca se moverá para atrás ni aunque cambies la configuracion del sistema
        Busq_Lineal(lista_Burbuja)
        dt = round(time.monotonic() - t0, 6)
        tiempos_BusqLineal.append(dt)  # meto el tiempo marcado
        print("\nBurbuja(n={}): \tTiempo transcurrido: {} seg".format(n, round(dt, 5)))

        t0 = time.monotonic()
        busquedaBinariaRecursiva(lista_Busq_BinR)
        dt = round(time.monotonic() - t0, 6)
        tiempos_BusqBin.append(dt)
        print("Busqueda Binaria(n={}): \tTiempo transcurrido: {} seg".format(
            n, round(dt, 5)))

    return tiempos_BusqLineal, tiempos_BusqBin


def main():
    for k in range(1, 4):
        cases = {1: 'Mejor de los casos',
                 2: 'Aleatorio', 3: 'El peor de los casos'}
        # numDatos = [100,200,300,400,....,2000]
        # Haremos 2000 datos en una lista para graficarlos posteriormente
        numDatos = [n*100 for n in range(1, 21)]
        tiempos_BusqLineal = []
        tiemposMerge = []
        tiempos_BusqLineal, tiemposMerge = eficienciaAlgoritmos(
            numDatos, cases[k])
        graficarTiempos(numDatos, tiempos_BusqLineal, tiemposMerge, cases[k])


sys.setrecursionlimit(20000)
main()
