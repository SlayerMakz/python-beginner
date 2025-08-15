# Ejercicio 1: El mensaje secreto.
# Dada la siguiente lista.
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
import os
os.system("clear")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7:])

###################
# Ejercicio 2: Intercambio de posiciones.
# Intercambia la primera y última posición de la siguiente lista. 

numeros = [10, 20, 30, 40, 50]
numeros [0], numeros [-1] = numeros [-1], numeros [0] # Esto intercambia en una sola linea.
print(numeros)

###################
# Ejercicio 3: El sandwich de listas.
# Dadas las siguientes listas.
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes, y el pan de abajo en ese orden.  
pan = ["pan arriba"]
ingredientes = ["jamon", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)
####################

####################
# Ejercicio 4: Duplicando una lista.
# Dada una lista: 
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo = [1, 2, 3, 1, 2, 3]
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)
####################

####################
# Ejercicio 5: 
# Dada una lista con un numero impar de elementos, extrae el elemento del centro de la lista.
# Ejemplo = lista [10, 20, 30, 40, 50] el centro es [30]

lista = [10, 20, 30, 40, 50]
print(lista[2:3])

####################

####################
# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
# Al yo dividir la longitud de la lista en la mitad me permite que si la lista llega a cambiar no tendre que cambiar el valor y siempre se hara en automatico, si lo hago manualmente siempre voy a tener que cambiar los parametros en el código. 
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)

