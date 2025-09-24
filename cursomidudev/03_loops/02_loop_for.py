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