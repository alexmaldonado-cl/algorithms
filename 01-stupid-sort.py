import random as rnd 

def verificar(arreglo):
    for i in range(0, len(arreglo)-1):
        if arreglo[i] > arreglo[i+1]:
            return False
    
    return True


def ordenar(arreglo):
    while not(verificar(arreglo)):
        posA = rnd.randint(0, len(arreglo)-1)
        posB = rnd.randint(0, len(arreglo)-1)

        aux = arreglo[posA]
        arreglo[posA] = arreglo[posB]
        arreglo[posB] = aux

    return arreglo

print(verificar([1, 2, 3, 4, 5, 6]))
print(verificar([1, 2, 3, 4, 6, 5]))

arreglo = [4, 5, 1, 2, -1, 5, 10, 8, 0]
print(ordenar(arreglo))