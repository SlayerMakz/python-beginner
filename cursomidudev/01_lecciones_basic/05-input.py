###
# 05 - Entrada de usuario (input()) - version simplificada
# La funcion input() permite obtener datos del usuario a traves de la consola
### 

#print('Hola, como te llamas?')
#nombre = input()

#print('Mi nombre es ' + nombre)

# Tambien lo podemos poner de este modo mas directo. 
nombre = input('Hola, como te llamas?\n')
print(f'Hola {nombre}, encantado de conocerte')

# NOTA: Es muy importante saber que todo input es un string.
# Entonces en este ejemplo al asignar un valor, sera en cadena de texto.

age = input('cuantos a;os tienes?\n')
print(f'Yo tengo {age} a;os')

# Si yo en anterior input le agregara + 5 en la variable age generaria un error. 

#age = input('cuantos a;os tienes?\n')
#print(f'Yo tengo {age + 5} a;os')

# Esto se debe a que el input string no se le puede agregar un valor int o integer.
##########################################################3

# Hay una forma tambien de pedirle al usuario multiples valores a la vez e imprimirlos. 

country, city = input('En que pais y ciudad vives?\n').split()
print(f'Vives en {country}, {city}')


