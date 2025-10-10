# Ejercicio 1. Cuenta Atras.
# Imprime los números del 10 al 1 usando un bucle while. 
import os
os.system("clear")

print("---- Ejercicio 1 ----")
contador = 10 
while contador >= 0:
    print(contador)
    contador -= 1 
    
print("---- Ejercicio 2 ----")
numero = 1
suma_pares = 0
while numero <= 20:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    numero += 1
print(f"La suma de los numeros pares hasta 20 es: {suma_pares}")

print("---- Ejercicio 3 ----")
numero = int(input("Ingrese un numero entero positivo: \n"))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es: {factorial}")

print("---- Ejercicio 4 ----")
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
contraseña = ""
while len(contraseña) < 8:
    contraseña = input("Introduce una contrasena (al menos 8 caracteres): ")
    if len(contraseña) < 8:
        print("La contrasena debe tener al menos 8 caracteres. Intentalo de nuevo.")
print(f"Contrasena valida: {contraseña}")

print("---- Ejercicio 5 ----")
# Pide al usuario que introduzca un numero
# Imprime la tabla de multiplicar de ese numero del 1 al 10 usando un bucle while. 

numero = int(input("Introduce un numero positivo: "))
multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')
    multiplicador += 1

