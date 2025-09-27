###
# Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras se cumple una condicion
###

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas: 
    print(fruta)
    
# Iterar sobre cualquier cosa que sea iterable
cadena = "midudev"
for caracter in cadena:
    print(caracter)
    
# enumerate()
# Nos sirve para darnos el indice de una lista y también el valor. 
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"El indice es {index} y la fruta es {fruta}")

#############################################
# Bucles anidados
# Meter un bucle dentro de otro.  
######
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")
        
###
# Uso de break

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales): 
    print(animal)
    if animal == "loro": # perro, gato, raton, loro. Aquí termina el código.
        print(f"El loro está escondido en el indice {idx}")
        break

# Continue 
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales): 
    if animal == "loro":
        continue
    print(animal)
    
# Comprensión de listas. (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# muestra los numeros pares de una lista
pares = [num for num in [1, 2 ,3, 4, 5, 6] if num % 2 == 0 ]
print(pares)

#i in range
for i in range (0, 15):
    print(i)
