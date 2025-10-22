
### Ejemplo de una función para imprimir algo en consola.
def saludar():
    print("Hola!")
    
saludar()
saludar()
saludar()
saludar()

# Ejemplo de una función con parametro.
def saludar_a(nombre):
    print(f"Hola, {nombre}!")
    
saludar_a("Midudev")
saludar_a("Orlando")
saludar_a("Juan")

# El parametro es lo que acepta la función.
# El argumento es lo que se le pasa a la función.

# -----------------------------------------------------

# Ejemplo de función con más parametros.
def sumar (a, b):
    suma = a + b
    return suma

print(sumar(2, 3))

# Se pueden documentar las funciones con docstring

def restar(a, b):
    """ Resta dos numeros y devuelve el resultado"""
    return a - b

# Parametros por defecto.
def multiplicar(a, b = 2):
    return a * b
print(multiplicar(5)) # = 10

# Argumentos por posición
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")
    
# Los parametros son posicionales.
# Aquí importan los parametros en el orden que lo ponga
describir_persona("orlando", 26, "hombre")
describir_persona("hombre", "madeval", 22) #soy hombre, tengo madeval y soy 22

# Argumentos por clave
# Parámetros nombrados
describir_persona(sexo="gato", nombre="orlando", edad=26)
# Al hacer esto tendremos el enunciado correcto sin importar el orden en que ponga los parametros

# Argumentos de longitud de variable (*args)
def sumar_numeros(*args): #Si por ejemplo, no conozco cuantos argumentos voy a usar se utiliza el args para que al definir los parametros agarren el total.
    suma = 0
    for numero in args:
        suma += numero
    return suma
print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
print("\n")
mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")