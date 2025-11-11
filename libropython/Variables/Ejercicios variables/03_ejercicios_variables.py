''' Mensaje personal: Use una variable para representar el nombre de una persona e imprima
un mensaje para esa persona. El mensaje debería ser sencillo, por ejemplo: "Hola, Eric, ¿te gustaría
aprender Python hoy?".'''
print('\n')
nombre = 'jesse pinkman'
print(f'Walter: Hola, {nombre}, listo para cocinar?')
print('\n')
'''
Grafía de nombres: Use una variable para representar el nombre de una persona e
imprima ese nombre en minúsculas, mayúsculas y con mayúscula inicial.
'''
print(nombre.upper())
print(nombre.lower())
print(nombre.title())
print('\n')
'''
Cita célebre: Busque una cita de un personaje al que admire. Imprima la cita y el nombre del
autor. La salida debería tener un aspecto similar a esto, incluidas las comillas:
Albert Einstein once said, "A person who never made a mistake never tried anything new."
'''

walter = 'Walter White una vez dijo: "No estoy en peligro, Skyler, yo soy el peligro."'
print(walter)
print('\n')

'''
Cita célebre 2: Repita el ejercicio 2-5, pero, esta vez, represente el nombre de la persona
usando una variable llamada famous_person. Después, componga el mensaje y represéntelo con una
nueva variable llamada message. Imprima su mensaje
'''

famous_person = 'Walter White'
famous_person2 = 'Skyler'
message = (f'{famous_person} una vez dijo: "No estoy en peligro, {famous_person2}, yo soy el peligro."')
print(message)
print('\n')


'''Eliminar espacios de nombres: Use una variable para representar el nombre de una persona e incluya algunos caracteres de espacio en blanco al principio y al final del nombre.
Asegúrese de usar cada combinación de caracteres, "\t" y "\n", al menos una vez. Imprima el nombre una vez, de modo que se muestren los espacios de alrededor.
A continuación, imprima el nombre usando cada una de las tres funciones que hemos visto:
lstrip(), rstrip() y strip().
'''
jesse = '   jesse   '
print(jesse)
print(jesse.strip())

'''Python cuenta con el método removesuffix(), que funciona
exactamente igual que el método removeprefix(). Asigne el valor 'python_notes.txt' a una variable llamada filename. A continuación, utilice el método removesuffix() para mostrar el nombre
del archivo sin la extensión de archivo, como ocurre con algunos exploradores de archivo. '''

filename = 'ejercicios_python.txt'
print(filename.removesuffix('.txt'))