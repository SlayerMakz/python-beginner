def imprimir_numeros():
    for num in range(1, 11):
        print(num)
        
imprimir_numeros()

print("\n")
def numeros_impar(*args):
    for num in range(*args):
        if num % 2 == 0:
            continue
        print(num)

numeros_impar(1, 100)

print("\n")
def ejercicio3():
    for num in range(5, 51, 5):
        print(num)

ejercicio3()