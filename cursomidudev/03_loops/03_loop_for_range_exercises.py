# Ejercicio 1: Imprime los numeros del 1 al 10
# Imprime los numeros del 1 al 10 inclusive usando un bucle for y range()
print("Ejercicio 1.")
for num in range(1, 11):
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20.
# Imprime los numeros impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2.")
for num in range(1, 21):
    if num % 2 == 0:
        continue
    print(num)

# Ejercicio 3. Imprimir multiplos de 5.
# Imprime los múltiplos de 5 desde 5 hasta 50 usando un bucle for y range().
print("\nEjercicio 3.")
for num in range(5, 51, 5):
    print(num)

# Ejercicio 4. Imprimir numeros en orden inverso. 
# Imprime los numeros del 10 al 1 inclusive en orden inverso.
print("\nEjercicio 4.")
for num in range(10, 0, -1):
    print(num)

# Ejercicio 5. Suma de números en rango.
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
suma_num = 0
for num in range(1, 101):
    suma_num += num
print(suma_num)

# Ejercicio 6. Tabla de multiplicar.
# Pide al usuario que introduzca un numero. 
# Imprime la tabla de multiplicar de ese numero del (1 al 10) usando un bucle for y range()
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")