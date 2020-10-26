'''
Busqueda binaria: Consiste en una busqueda que ocupa el "Divide and Conquer", donde busca el elemento en mitades,
                    es por eso que su complejidad es O(nlogn)
                    Importante: El arreglo tiene estrictamente que estar ordenado!!!!
'''
import sys
def busquedaBinariaRecursiva(a,k,Left,Right):
    if (Left>Right):
        return None ## Caso base, he acabado y no lo encontré
    Half = (Left+Right)//2

    if a[Half] == k: #Si el de enmedio es mi llave
        return Half
    elif a[Half] > k: #"Mas abajo, mi numero es mas chico"
        return busquedaBinariaRecursiva(a,k,Left,Half-1)
    else: #"Mas arriba"
        return busquedaBinariaRecursiva(a,k,Half+1,Right)
     

sys.setrecursionlimit(20000)
a = [2,4,8,2,9,4,4,3]
a.sort()
print(a)
key = 8
print(key)
encontrado = busquedaBinariaRecursiva(a,key,0,len(a)-1)
print("Index , Key = {},{}".format(encontrado,key))