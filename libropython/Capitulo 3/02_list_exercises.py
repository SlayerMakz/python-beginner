''' Ejercicios listas parte 2'''
''' Si pudiese invitar a cualquiera, vivo o muerto, a cenar, ¿a quién
invitaría? Haga una lista de al menos tres personas a las que le gustaría invitar a una cena y úsela para imprimir un mensaje para cada persona invitándole a cenar.
 '''
 
lista_invitados = ['walter', 'jesse', 'gustavo']
print(f"Hola {lista_invitados[0].title()}, te invito a mi fiesta")
print(f"Hola {lista_invitados[1].title()}, te invito a mi fiesta")
print(f"Hola {lista_invitados[2].title()}, te invito a mi fiesta\n")


''' Cambiar la lista de invitados'''
print("Ejercicio 2")
print(f"El invitado {lista_invitados[1].title()}, no podrá asistir.")
lista_invitados[1] = 'hank'
print(f"Hola {lista_invitados[0].title()}, te invito a mi fiesta")
print(f"Hola {lista_invitados[1].title()}, te invito a mi fiesta")
print(f"Hola {lista_invitados[2].title()}, te invito a mi fiesta\n")
# Hola Walter, te invito a mi fiesta
# Hola Hank, te invito a mi fiesta
# Hola Gustavo, te invito a mi fiesta

''' Se ha encontrado una mesa más grande del comedor '''
print("Se ha encontrado una mesa más grande, y habran más invitados")
print(lista_invitados)
lista_invitados.insert(1, 'skyler')
lista_invitados.insert(2, 'walter jr')
lista_invitados.append('mary')
for i in lista_invitados:
    print(f"Hola te invito a mi fiesta")
