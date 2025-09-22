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

print("---- Ejercicio 5 ----")
numero = int(input("Introduce un número: "))
multiplicador = 1

while multiplicador <= 100:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1