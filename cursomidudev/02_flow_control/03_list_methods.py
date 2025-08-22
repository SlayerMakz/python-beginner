###
# 03 - Listas metodos.
# Los metodos mas importantes para trabajar con listas.
###

import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd', '@']


# Anadir o insertar elementos a la lista.
# Para anadir un elemento al final de las lista se usa esto:
lista1.append('e')
print(lista1)

# Esto inserta un elemento en la posicion que le indiquemos como primer argumento
lista1.insert(0, '@')
print(lista1)

# Agrega elementos al final de la linea.
lista1.extend(['Correr', 'Saltar'])
print(lista1)

# Eliminar elementos de la lista.
# Este nos permite eliminar la primera aparicion del primer elemento arroba @
lista1.remove('@')
print(lista1)

# Eliminar el ultimo elemento de la lista y ademas te lo devuelve.
ultimo = lista1.pop()
print(ultimo)
print(lista1)


# Eliminar el segundo elemento de la lista (indice 1)
lista1.pop(1)
print(lista1)

# Eliminar a lo bestia.
del lista1[-1]
print(lista1)

# Si quiero eliminar todos los elementos de una lista 
lista1.clear()
print(lista1)

# Eliminar un rango de elementos.
lista1 = ['F', 'G', 'H', 'I', 'J']
del lista1[1:3]
print(lista1)

# mas metodos utiles.
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Modificar listas creando una copia')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print('Ordenar una lista de cadenas de texto (todo minuscula)')
frutas = ['manzana', 'pera', 'limon', 'manzana', 'pera', 'limon']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print('Ordenar una lista de cadenas de texto (mezclas mayuscula y minuscula)')
frutas = ['manzana', 'Pera', 'Limon', 'manzana', 'pera', 'limon']
frutas.sort(key=str.lower)
print(frutas)

# Mas metodos utiles
animals = ['Perro', 'Vaca', 'Panda', 'Perro']
print(len(animals)) # Tamano de las listas = 4
print(animals.count('Perro')) # Cuantas veces aparece el elemento 'Perro' = 2
print('Vaca' in animals) # Comprueba si hay una 'Vaca' en la lista = True.
print('Gato' in animals) # False
