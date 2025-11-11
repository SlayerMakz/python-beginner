# Enteros
# Podemos sumar, restar, multiplicar y dividir.

suma = 2 + 3
print(suma)

resta = 3 - 2
print(resta)

multiplicacion = 2 * 3
print(multiplicacion)

division = 10 / 2
print(division)  # Aunque dividamos numeros enteros y den resultados exactos, siempre devolverá un flotante, más adelante se explica.

# Potencias
print("\n")
pot1 = 3 ** 2
print(pot1)

pot2 = 3 ** 3
print(pot2)

pot3 = 10 ** 6
print(pot3)

# Python respeta el orden de las operaciones, así que pueden usar varias en una expresión. También se pueden emplear paréntesis para modificar el orden de las operaciones y que python evalúe las expresiones en el orden que especifiquemos

#Eje:
print("\n")
op1 = 2 + 3 * 4
print(op1)

op2 = (2 + 3) * 4
print(op2)

#Float, en python se considera "float" cualquier numero con un decimal.
print("\n")
op3 = 3.2 + 2.2
print(f"Esto es un float: {op3}")

op4 = 2 * 0.1
print(f"Esto también es un float: {op4}")

# Es posible obtener un número arbitrario de posiciones muchas posiciones decimales.
op5 = 0.2 + 0.1
print(f"Muchos numeros decimales: {op5}")

# Si mezclamos un flotante y un entero en una operación, también obtendremos un flotante. 
op6 = 1 + 2.0 
print(f"Esto es un entero + flotante: {op6}")