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