###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones.
###

import os
os.system("clear")

print('\nSentencia simple condicional if, else')

edad = 15

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')


print('\nSentencia condicional con elif')
nota = 5
if nota >= 9:
    print('Sobresaliente')
elif nota >= 7:
    print('OK')
elif nota >= 6:
    print('Aprobado')
else:
    print('No aprobado')

# Python
# && -> and
# || -> or

# and
print('\nCondiciones multiples')
edad = 15
tiene_licencia = False

# Cuando usas "and" las 2 condiciones se tienen que cumplir.
if edad >= 18 and tiene_licencia:
    print('Puedes conducir')
else:
    print('No puedes conducir')

# or
# Con que 1 de cualquier de las 2 condiciones se cumpla funciona. 
if edad >= 18 or tiene_licencia:
    print('Puedes conducir')
else:
    print('No puedes conducir')

# Tambien tenemos el operador logico "not"
# que nos permite negar una condicion.

es_fin_de_semana = True
if not es_fin_de_semana:
    print('\nHay que trabajar entresemana')
else:
    print('\nEs fin de semana')

