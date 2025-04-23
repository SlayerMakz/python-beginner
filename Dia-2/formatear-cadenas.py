"""
# Formatear cadenas en Python
Si nosotros queremos formatear una cadena, podemos hacerlo de varias maneras:
1.. con el método format()
Eje: print("Mi auto es{} y tiene la matricula {}".format(color_auto, matricula))
2.. con el método f-string
Ej: print(f"Mi auto es {color_auto} y tiene la matricula {matricula}")
3.. con el método %s 
Ej: print("Mi auto es %s y tiene la matricula %s" % (color_auto, matricula))
"""

nombre_asociado = "Walter White"
numero_asociado = "07091958"
casado = False
conyuge = "Skyler White"
hijos =  "Walter Jr y Holy White"
ocupacion = "Profesor de quimica" 
vehiculo = "Pontiac Aztek 2004"
matricula = "327-2153"
color_auto = "Verde helecho"


x = 5
y = 10
z = x + y

#Ejemplos básicos
print(f"Mi auto es {color_auto} y tiene la matricula {matricula}")
print("Mis numeros son {} y {}".format(x, y))
print(f"El resultado de la suma de {x} y {y} es {z}")

print(f"Nombre del sujeto: {nombre_asociado} \nNumero del asociado: {numero_asociado} \nCasado: {"Si" if casado else "No"} \nConyuge: {conyuge} \nHijos: {hijos} \nOcupación del sujeto: {ocupacion} \nVehículo: {vehiculo} \nMatricula del vehículo: {matricula} \nColor del vehículo: {color_auto}")


