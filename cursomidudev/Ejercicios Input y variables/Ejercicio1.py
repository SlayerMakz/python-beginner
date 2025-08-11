#Ejercicio 1
print("----------------------------------------")
print("Ejercicio 1: Imprimir mensajes.\n")
print("Orlando, Monclova")
print("----------------------------------------")

#Ejercicio 2.
print("Ejercicio 2: Muestra los tipos de datos de las siguientes variables:\n")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable\n")
a = 15
b = 3.14159
c = "Hola Mundo"
d = True 
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("----------------------------------------")
print("Ejercicio 3: Casting de tipos\n")
print("Convierte la cadena '12345' a un entero y luego a un float")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?\n")

cadena = "12345"
numero_entero = int(cadena)
numero_float = float(numero_entero)

print(numero_entero)
print(numero_float)

float_num = 3.99
numero_convertido_entero = int(float_num)
print(numero_convertido_entero)

print("----------------------------------------")
print("Ejercicio 4: Variables\n")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.\n")
name = "Orlando"
edad = 26
altura = 1.72

print(f"Hola mi nombre es {name}, tengo {edad} años y mi estatura es de {altura} cm")

print("----------------------------------------")