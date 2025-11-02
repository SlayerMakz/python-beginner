###
## 03 - range()
# Permite crear una secuencia de numeros. Puede ser útil para for, pero no solo para eso.

print("\nrange()")

# Generando una secuencia de numeros del 0 al 9 
for num in range(10):
    print(num)

# Range(inicio, fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 1001, 5):
    print(num)