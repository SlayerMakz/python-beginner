# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

import os
os.system("clear")

print("--------------Ejercicio 1-------------")
lista1 = [1, 2, 3, 4, 5]
print(lista1)

lista1.append(6)
print(lista1)

lista1.insert(2, 10)
print(lista1)

lista1[0] = 0
print(lista1)

print('------------------------------------\n')
print("--------------Ejercicio 2-------------")
# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(lista_a)

lista_a.remove(1)
print(lista_a)

ultimo = lista_a.pop(3)
print(lista_a)
print(ultimo)

lista_b.clear()
print(lista_b)

print("--------------------------------------\n")

print("--------------Ejercicio 3-------------")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista2[2:5]
print(lista2)

print("--------------------------------------\n")

print("--------------Ejercicio 4-------------")
# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

numbers = [5, 2, 8, 1, 9, 4, 2]
numbers.sort()
print(numbers)
sorted_numers = numbers.count(2)
print(f"Cuantos numeros 2 hay?: {sorted_numers}")
in_list = (7 in numbers)
print(f"El 7 aparece en la lista?: {in_list}")