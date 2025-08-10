##
# 04 - Variables
# Las variables sirven para guardar datos en memoria. 
# Python es un lenguaje de tipado dinamico, y de tipado fuerte.
###

# Asignar una variable. 
#mi_nombre = "Orlando"
#print(mi_nombre)
#age = 26
#print(age)

# Python permite cambiar el valor de las variables.
#age = 30 
#print(age)

# Tipado dinamico significa que el tipo de dato se determine en tiempo de ejecucion
# significa que no tienes que declararlo explicitamente. 
name = 'Orlando'
print(type(name))

edad = 26
print(type(edad))

# Tipado fuerte: python no realiza conversiones de tipo automatico.
# Esto seria un f-string (cadena de formato) 
print(f'hola {name}, tengo {edad + 5} a;os')