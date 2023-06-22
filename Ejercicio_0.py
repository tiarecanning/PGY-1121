'''
Actividad 2
Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
Calcular_Iva
Descuento
Calcular_Imc

Las cuales deben ser desarrolladas en funciones (métodos).

Donde:
Calcular_Iva: Es el precio del producto, multiplicado por el 19% (0.19)
descuento: Es el precio del producto menos el descuento por aplicar. Mostrar el valor final del producto.
Calcular_Imc: Índice de masa corporal. Su fórmula es:                    

además se debe mostrar el estado de la persona de acuerdo a la siguiente tabla:

'''
import numpy as nu
vMatriz = nu.array([[18.5, "Bajo Peso"], [24.9, "Peso Adecuado"], [29.9,"Sobre Peso"], [34.9, "Obesidad"], [39.9, "Obesidad Grado 2"], [40, "Obesidad Grado 3"]])
print(vMatriz)

def fun_Matriz(fil, masa):
  print(f"Su indice de masa corporal {masa} , indica {vMatriz[fil][1]}")
  input("Presione Tecla para continua...")


def fun_Cal_Iva(a):
  return a * 0.19

def fun_Cal_des():
  a = int(input("Ingrese Valor del Producto: "))
  b = int(input("Ingrese porcentaje descuento: "))
  return a - (a * b / 100)



#PROGRAMA PRINCIPAL
sw = 1
#print(vMatriz)
while sw == 1:
  print("MENU PRINCIPAL")
  print("==================")
  print("1.- Calcular Iva")
  print("2.- Calcular Descuento")
  print("3.- IMC")
  print("4.- Salir")
  print("------------------------------")
  try:
    vOp = int(input("Digite Opción: "))
    if vOp == 1:
      vValor = int(input("Ingrese Valor del Producto: "))
      print(fun_Cal_Iva(vValor))

    elif vOp == 2:
      print(f"Total con descuento es: {fun_Cal_des()}")

    elif vOp == 3:
      vPeso = float(input("Ingrese Su Peso en Kilos: "))
      vAltura = float(input("Altura en Metros: "))
      vIMC = vPeso / (vAltura ** 2)

      if vIMC < 18.5:
        print(fun_Matriz(0, vIMC))

      elif vIMC <= 24.9:
          print(fun_Matriz(1, vIMC))

      elif vIMC <= 29.9:
        print(fun_Matriz(2, vIMC))

      elif vIMC <= 34.9:
        print(fun_Matriz(3, vIMC))

      elif vIMC <= 39.9:
        print(fun_Matriz(4, vIMC))

      else:
        print(fun_Matriz(5, vIMC))

    elif vOp == 4:
      sw = 0
    input("Presione tecla para seguir..")
  except:
    print("Opción no Válida")

print("Programa Finalizado..")