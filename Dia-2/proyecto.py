nombre = input("Digite el nombre del empleado: ")
ventas = input("Digite las ventas del empleado: ")
comisiones  = (float(ventas) * 13) / 100
print(f"Nombre del empleado: {nombre} y sus comisiones son de: {round(comisiones,4)}")