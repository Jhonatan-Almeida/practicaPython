def factorial(n):
    print(n)
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("ingresa el numero para calcular su factorial"))
resultado = factorial(num)
print(f"El resultado de factorial es: {resultado}")
7
