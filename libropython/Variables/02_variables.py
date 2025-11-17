# Vamos a generar un error en python a propósito. Cuando se produce un error en un programa, el interprete intenta por todos los medios, averiguar dónde está el error y ofrece un rastro o (traceback) cuando un programa no puede ejecutarse correctamente. 

message = "Hello Python"
print(message)

# Si queremos que nuestra variable aparezca con la primer letra de cada palabra en mayuscula, se usa el metodo .title() al final de la variable a imprimir.

# Si en algun momento necesitamos que lo que ingrese el usuario no tenga espacios, podemos usar el metodo .strip(), si queremos que quite espacios de la izquiera sera 

favorite_language = 'python'
favorite_language.strip()
print(favorite_language)

# Eliminar prefijos, por ejemplo si queremos eliminar el prefijo 'https://' lo podemos hacer de la siguiente manera con el metodo .removeprefix() 

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

