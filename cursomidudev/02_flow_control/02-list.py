###
# 03 - Listas 
# Secuencias mutables de elementos. 
# Pueden contener elementos de diferentes tipos.
###

# Creacion de listas.
import os
os.system("clear")
 
print("\nCrear listas")
lista1 = [1, 2, 3 ,4 ,5] # Lista de enteros. 
lista2 = ["manzanas", "peras", "platanos"] # Lista de cadenas.
lista3 = [1, "hola", 3.14, True] # Lista de tipos mixtos. 

lista_vacia = []
lista_de_listas = [[1, "calcetin"], [3, 4]]
matrices = [[1, 2]], [[3, 4]], [[5, 6]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrices)

# Acceder a elementos por indice.
print("\nAcceder a elementos por indice")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # Se pueden acceder a los indices al reves en negativo platanos.
print(lista2[-2]) # peras

# Acceso a elementos con más indices.
print(lista_de_listas[1][0])
print(lista_de_listas[0][1])

# Slicing (rebanado) de listas.
lista4 = [1, 2, 3, 4, 5]
print(lista4[1:4]) # [2, 3, 4] El ultimo indice sin incluir. 
print(lista4[:3]) # [1, 2, 3] Esto devuelve los 3 primeros numeros.
print(lista4[3:]) # Esto devuelve los ultimos numeros hasta el indice 3 [4, 5]
print(lista4[:]) # Esto te devuelve una copia de la lista para guardarla o modificarla y tener un respaldo

# Extras.
lista5 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista5[::2]) # Esto hace que se salte los indices pares e imprima los impares. 
print(lista5[::-1]) # De vuelva la lista invertida.


# Modificar una lista.
lista5[0] = 20
print(lista5)

##############################################
# Añadir elementos a una lista.
lista1 = [1, 2, 3]

# Forma larga y menos eficiente.
lista1 = lista1 + [4, 5, 6]
print(lista1)

# Forma corta y más eficiente.
lista1 += [7, 8, 9]
print(lista1)
#############################################

