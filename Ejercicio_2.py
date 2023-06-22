'''
Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos números 
serán las dimensiones de un arreglo bidimensional. Posteriormente, 
poblar la matriz con números reales. Finalmente, muestre:
.- El arreglo poblado.
.- La suma por filas.
.- El promedio por columnas.

'''
import numpy as np
import random
print("Creación de Matriz Dinamica")
print("===========================")
vFil = int(input("Ingrese Número de Filas de la Matriz: "))
vCol = int(input("Ingrese Número de Columnas de la Matriz: "))
vLista = []

for n in range(0,vFil):
    vLista.append([]*vCol)

vMatriz = np.array(vLista)

#print(vLista)
#print(vMatriz)

# Poblar Matriz
vMatriz = np.random.randint(0,10, size=[vFil, vCol])
print(vMatriz)


# SUMAR FILAS
for x in range(vFil):
    vSum = 0
    for y in range(vCol):
        vSum += vMatriz[x][y]
    print(f"La Suma de la Fila {x} es {vSum}")


# PROMEDIO COLUMNAS
for x in range(vCol):
    vSum = 0
    for y in range(vFil):
        vSum += vMatriz[x][y]
    print(f"El Promedio de la Columna {x} es {vSum/vFil}")
