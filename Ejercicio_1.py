'''
Declarar y poblar un arreglo unidimensional de largo 10 con números 
enteros positivos, utilizando la función random, luego ingrese un número 
e indique si éste se encuentra en el arreglo.
'''
import numpy as np
import random

vLista=[]
# Llenar Lista con numeros aleatorios
for n in range(10):
    #vLista.append(random.randrange(50))
    vLista.append(random.randint(1, 50))
    
vArray = np.array(vLista)
print(vArray)

# Verificar si el numero ingresado existe en el array
vNum = int(input("Ingrese número a Buscar en el Array: "))
if vNum in vArray:
    print(f"El Número {vNum} existe en el Array")
else:
    print(f"El Número {vNum} No existe en el Array")


