###
# Ejercicio 1 Determinar el mayor de 2 numeros.
# Pide al usuario que introduzca 2 numeros y muestra un mensaje 
# indicando cuál es mayor o si son iguales. 
###

import os
os.system("clear")
# Declaramos las variables
# num1 = int(input("Escribe el primer numero:\n"))
# num2 = int(input("Escribe el segundo numero:\n"))

# if num1 > num2:
#     print(f"El primer numero es mayor que el segundo: {num1} > {num2}")
# elif num1 == num2:
#     print(f"Los 2 numeros son iguales: {num1} = {num2}")
# else:
#     print(f"El primer numero es menor que el segundo: {num1} < {num2}")
############################################

# Ejercicio 2. calculadora simple.

# num1 = int(input("Escribe el primer numero:\n"))
# num2 = int(input("Escribe el segundo numero:\n"))
# operacion = input("Introduce la operacion (+, -, *, /):\n")

# if operacion == "+":
#     resultado = num1 + num2
#     print(f"El resultado de la suma es: {resultado}")
# elif operacion == "-":
#     resultado = num1 - num2
#     print(f"El resultado de la resta es: {resultado}")
# elif operacion == "*":
#     resultado = num1 * num2
#     print(f"El resultado de la multiplicación es: {resultado}")
# elif operacion == "/":
#     resultado = num1 / num2
#     print(f"El resultado de la division es: {resultado}")
# else: 
#     print("No elegiste una opción correcta.")
###################################################################

# Ejercicio 3: Año bisiesto. 
# Pide el usuario que introduzca un año y determina si es bisiesto. 
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# año = int(input("Escribe un año para averiguar si es bisiesto:\n"))
# if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
#     print(f"{año} Es año bisiesto.")
# else:
#     print(f"{año} No es año bisiesto.")

# Ejercicio 4: Categorizar edades.
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
age = int(input("Ingresa tu edad:\n"))
if age <= 2:
    print("Eres un bebé 👶")
elif (age == 3 or age <= 12):
    print("Eres un niño 👦")
elif (age == 13 or age <= 17):
    print("Eres un adolescente 🙂")
elif (age == 18 or age <= 64):
    print("Eres un adulto 👨")
elif age >= 65:
    print("Eres un anciano")
else: 
    print("Edad no valida.")
