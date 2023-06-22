
import numpy as np
matrizBus=np.empty((10,4),dtype=object)
print(matrizBus)
asiento=0
for f in range (10):
  for c in range(4):
      asiento=asiento+1
      matrizBus[f,c]=asiento

print(matrizBus)

while True:

    fila=int(input("Ingrese la fila de su asiento: "))
    columna=int(input("Ingrese la columna de su asiento: "))
    matrizBus[fila,columna]='X'
    print(matrizBus)
