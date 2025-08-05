###
# 01-holamundo.py print
# El módulo print() es el módulo que nos permite imprimir en consola 
# La informacion que pongamos en el código.
###

print("hola mundo")

# Lo ideal es imprimir con una comilla para usar despues palabras entrecomillas
print('Esto se puede "imprimir" con una comilla')

# El modulo print nos permite también imprimir de esta forma, concatenando palabras.
print('Python', 'es', 'genial')

# Si quisieramos hacer una separacion con guion, usamos el parametro "sep"
# No necesariamente tiene que ser un guion, puede ser cualquier cosa.
print('Python', 'es', 'genial', sep = "-")

# Si queremos que no me genere un salto de linea despues de un print 
# usamos el parametro "end"
print('Esto se imprime', end = " ")
print('en una linea')

# También se pueden imprimir numeros.
print(45)