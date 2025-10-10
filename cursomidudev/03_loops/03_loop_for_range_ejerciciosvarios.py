print("Generando una secuencia de numeros del 0 al 9\n")
for num in range(10):
    print(num)

print("\nrange: inicio, fin")
for num in range(5, 10):
    print(num)

print("\ninicio, fin, paso")
for num in range(0, 100, 5):
    print(num)

print("\nConteo al reves")
for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

print("Crear una lista")
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)


for _ in range(5):
    print("Hacer 5 veces algo")