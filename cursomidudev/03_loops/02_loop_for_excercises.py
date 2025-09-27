import os
os.system("clear")
# Ejercicio 1: Imprimir numeros pares. 
# Imprime todos los numeros pares del 2 al 20 (inclusive) usando un bucle for
print("----------------------------------")
for i in range(2, 21, 2): 
    print(i)
print("----------------------------------")
# Ejercicio 2: Calcular la media de una lista.
# Dada la siguiente lista.
numeros = [10, 20, 30, 40, 50]
for num in numeros:
    suma_total = sum(numeros)
    media = suma_total / len(numeros)
print(media)
print("----------------------------------")
# Ejercicio 3: Buscar el máximo de una lista. 
# Dada la siguiente lista de numeros. 
numeros = [15, 5, 25, 10, 20, 35, 87]
for idx, num in enumerate(numeros): 
    if num == max(numeros): #Sirve para conocer el numero mas grande
        print(f"El numero máximo de esta lista es: {num}")
print("----------------------------------")
# Ejercicio 4: Filtrar cadenas por longitud.
# Crea una lista que contenga solo las palabras con más de 5 letras.
# Usando un bucle for y list comprehension
palabras = [pal for pal in ["casa", "arbol", "sol", "elefante", "luna"] if len(pal) > 5]
print(palabras)
print("----------------------------------")
# Ejercicio 5: Contar palabras que empiezan con una letra.
# Pide al usuario que introduzca una letra. 
# Cuenta cuantas palabras en la lista empiezan con esa letra.
lista_palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Ingresa una letra: ").lower() #Se pone el .lower para que sea indistintivo si el usuario pone una letra mayuscula o minuscula
contador = 0 # Esta variable va a almacenar y guardar las palabras que lleven la letra.
for palabra in lista_palabras:
    if palabra.lower().startswith(letra): #Aqui usamos 2 funciones que es .lower() que va a leer la palabra sin importar si empieza con mayuscula o minuscula y el startswith nos ayudara a que también pueda verificar solamente las palabras que lleven la letra que ingreso el usuario.
        contador += 1 #Esto nos permite agregar al contador e ir sumando las palabras que encuentre.
print(f"Hay {contador} palabras que empiezan con la letra: {letra}")

###############################################
# Ejercios extra.
##############################
texto = "python"
for i in texto[::-1]:
    print(i)