###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de codigo mediante una condicion 
###
import os
os.system("clear")
print("\n Bucle while: ")

# Bucle con una simple condicion
contador = 0
while contador <= 5:
    print(contador)
    contador += 1 # es super importante para evitar un bucle infinito

# Si utilizamos la palabra break, podemos romper el bucle
print("\n Bucle while con break: ")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

# continue, lo que hace es saltar esa iteracion en concreto y continuar con el bucle.
print("\n Bucle con continue: ")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue

    print(contador)

# else, esta condicion cuando se ejecuta?
print("\n Bucle con else: ")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# pedirle al usuario un numero que tiene que ser positivo, si no no lo dejamos en paz.

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: \n"))
        if numero < 0:
            print("El numero debe ser positivo. Intenta otra vez.")
    except:
        print("Lo que introduces debe ser un numero.")

print(f"El numero que has introducido es {numero}")