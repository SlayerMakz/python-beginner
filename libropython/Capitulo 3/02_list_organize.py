''' Organizar una lista '''
# Con frecuencia, las listas se crean siguiendo un orden impredecible, ya que no siempre podemos controlar el orden en el que los usuarios introducen sus datos. Python ofrece distintas formas de organizar listas, dependiendo la situación. 

#----------------------------------------------------------------------
''' Ordenar una lista de manera permanente con método sort()'''
# Imagine que tenemos una lista de cochesitos y queremos ordenarla para guardarlos alfabéticamente. Para simplificar la tarea, asumiremos que todos los valores son en minúsculas.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Este metodo ordena en orden alfabetico y ya no se puede volver al orden original
print(cars)

# También se puede ordenar en orden alfabetico inverso con el argumento reverse=True al metodo sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#---------------------------------------------------------------------

''' Ordenar una lista temporalmente son sorted()'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here, is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)
# Esta función también acepta sorted(cars, reverse=True) 

#---------------------------------------------------------------------

''' Imprimir una lista en orden inverso con reverse()'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
