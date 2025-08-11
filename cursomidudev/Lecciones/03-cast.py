###
# 03 - casting de tipos de datos. 
# Transformar un tipo de valor a otro.  
###

print('Conversion de tipos')

print(2 + int("200")) #Convierte la cadena "200" a entero y suma 2
print("200" + str(2)) #Convierte el número 2 a cadena y los concatena: "2002"

print(type(float("3.1416"))) # Convierte la cadena "3.1416" a float
print(int(3.1416)) # Convierte el float 3.1416 a entero sin la parte decimal. 3
print(int(2.5)) # 2 
print(round(2.4)) # Redondea el valor flotante al numero más cercano, en este caso 2.

print(bool(3)) # True, porque cualquier múmero distinto de 0 es verdadero.
print(bool(0)) # False, porque 0 es considerado falso.
print(bool(-1)) # True, porque es un número distinto de 0.

print(bool("")) # False, porque es una cadena vacia.
print(bool(" ")) # True, una cadena con espacio no esta vacia. 
print(bool("False")) # True, porque la cadena no esta vacia. 

# Errores al convertir.
# No todos los valores pueden convertirse entre tipos. Por ejemplo, intentar convertir texto que no representa un numero int 


