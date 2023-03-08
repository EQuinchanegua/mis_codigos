## Algoritmo_para_Determinar_Si_Un Numero es par o impar
## Autor: codeweawers. 
## Fecha 2023-03-22

## Inicio
## Declaración de Variables
numero : int

## Mensaje De Bienvenida

print("\t \t \t Programa número par o impar \n \t \t \t Por codeweawers")
print("Ingresa un número entero: ")

numero = int(input())

print("\t \t \t clasificación del número dado")
## Operaciones
if numero%2 != 0:
    print("el numero ",numero,"es un numero impar")
else:
    print("el numero ",numero,"es un numero par")
                                            
print(" Fin del programa")    