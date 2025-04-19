animal = "chanCHito feliz"
print(animal.upper()) # Convierte a mayúsculas
print(animal.lower()) # Convierte a minúsculas
print(animal.title()) # Convierte la primera letra de cada palabra a mayúscula  
print(animal.strip().capitalize()) # Convierte la primera letra de la cadena a mayúscula
print(animal.strip()) # Elimina los espacios en blanco al principio y al final de la cadena
print(animal.lstrip()) # Elimina los espacios en blanco al principio de la cadena
print(animal.rstrip()) # Elimina los espacios en blanco al final de la cadena
print(animal.find("CH")) # Busca la posición de la primera aparición de "ch" en la cadena (si no existe devuelve -1)
print(animal.replace("CH", "j")) # Reemplaza "ch" por "j" en la cadena