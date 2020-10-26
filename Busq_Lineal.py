def Busq_Lineal(a,k):
    i=0
    while(i<len(a)-1):
        if a[i]==k:
            return i
        i+=1;
    return None

a = [3,5,6,1,4,7,7]
key = 6
indice = Busq_Lineal(a,key)
print("El indice del numero {} es {}".format(key,indice))