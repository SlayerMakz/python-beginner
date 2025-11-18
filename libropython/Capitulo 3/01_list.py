'''
Una lista es una colección de elementos dispuestos en orden particular. Podemos crear una lista que incluya las letras del abecedario, los números del 0 al 9, o los nombres de todos nuestros familiares. Podemos incluir todo lo que queramos en una lista y esos elementos no tienen por qué estar relacionados de una forma concreta.
'''
'''En python, el uso de [] indica una lista. Dentro de ella los elementos se separan mediante comas'''

bicicletas = ['trek', 'cannondale','redline', 'specialized']
print(bicicletas)

# Dado que no es esa la salida que queremos que vean nuestros usuarios, vamos a aprender a acceder a los elementos individuales de una lista.

''' Acceder a los elementos de una lista'''
# Las listas son colecciones ordenadas, así que podemos acceder a cualquiera de sus elementos indicando a Python la posición, o el índice del elemento deseado.

# Para acceder a un elemento de una lista, escriba el nombre de la lista seguido del indice del elemento entre corchetes.
# Eje

characters = ['walter white', 'jesse pinkman', 'mike', 'gustavo fring']
# Posiciones:       0                1            2            3
print(characters[0])
print(characters[1])
print(characters[2])
print(characters[3])

# También podemos usar los métodos de cadena del capítulo 2 con cualquier elemento de esta lista como por eje: title()

print(characters[0].title()) 

# Si ponemos el indice -1, python siempre devolverá el último de la lista: "gustavo fring"
print(characters[-1])

# Podemos usar valores individuales de una lista igual que haríamos con cualquier otra variable. Por ejemplo, podemos usar cadenas f para crear un mensaje basado en un valor de una lista. 

message = f"My primer bicicleta fue una: {bicicletas[0].title()}"
print(message)
print('-------------------------------------------------')

''' Modificar, añadir y eliminar elementos.'''
'''La mayoría de las listas que cree serán dinámicas, lo que significa que creará la lista para posteriormente añadir y eliminar elementos a medida que el programa siga su curso. Por ejemplo, podría crear un juego en el que un jugador tenga que disparar alienígenas en el espacio. Podría guardar el conjunto inicial de alienígenas en una lista y eliminar uno cada vez que le disparen. La lista de extraterrestres aumentará y disminuirá en el transcurso del juego.
'''

'''Modificar'''
# La sintaxis para modificar un elemento es similar a la usada para acceder un elemento de una lista. Para hacerlo, usamos el nombre de la lista seguido del indice del elemento y luego "=" agregamos el valor que queremos reemplazar en el indice que asignamos.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modificamos el indice 0
motorcycles[0] = 'ducati'
print(motorcycles) # Podemos cambiar el valor de cualquier elemento de la lista, no solo el primero.

'''Añadir'''
# Puede que le interese añadir un elemento nuevo. La forma más fácil de añadir un elemento nuevo es adjuntarlo a la lista. Al hacerlo, el nuevo elemento se añade al final, usaremos el metodo .append() y dentro de los parentesis añadiremos el valor nuevo.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

''' El metodo .append() facilita la creación dinámica de listas. Eje, podemos empezar con una lista vacía y añadir elementos después con una serie de llamadas a .append(). Usando una lista en blanco, vamos a añadirle los elementos'''

motorcycles = []
# Puede pedirle al usuario el valor que quiera en la lista con input o bien ingresarlo manualmente en el código.
motorcycles.append(input('Ingrese una marca de motos:').strip()) # Podemos usar el metodo .strip() para eliminar errores de espacio que ingrese el usuario.
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print('-------------------------------------------------')

''' Insertar elementos a una lista'''
# Podemos añadir un elemento nuevo a una lista en cualquier posición con el método insert(). Para ello, especificaremos el índice del nuevo elemento y su valor. Esta operación desplaza todos los demás valores de la lista una posición a la derecha.

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Puede ser en cualquier posición.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)
print('-------------------------------------------------')

''' Eliminar elementos de una lista '''
# Con frecuencia, necesitará eliminar un elemento o varios de una lista. Por ejemplo, cuando un jugador dispare a un extraterestre, tendrá que quitarlo de la lista de alienígenas activos. O, si un usuario decide cancelar su cuenta en una aplicación web,tendrá que quitarlo de la lista de usuarios activos. Puede eliminar un elemento según su posición en la lista o según su valor.

# Si conoce la posición del elemento que desea eliminar de la lista, puede usar la sentencia "del"

''' Eliminar un elemento con la sentencia del'''
# En este ejemplo utilizamos la sentencia del para eliminar el primer elemento, 'honda', de la lista de motos:
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Podemos eliminar un elemento en cualquier posición de una lista. Por ejemplo, para quitar el seundo elmento de la lista.

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)