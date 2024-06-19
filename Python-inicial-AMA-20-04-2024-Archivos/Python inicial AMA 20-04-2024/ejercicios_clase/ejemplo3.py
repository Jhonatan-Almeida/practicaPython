variable_global = "Soy una variable global"


def sumar(a, b):
    print(a)
    print(b)
    print(f"Voy a sumar: {a} + {b}")
    return a + b


def restar(a, b):
    variable_local = "Soy una variable local"
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir entre 0"


def calculadora():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese la operacion : '+' '-' '*' '/': ")
    match operacion:
        case "+":
            resultado = sumar(num1, num2)
        case "-":
            resultado = restar(num1, num2)
        case "*":
            resultado = multiplicar(num1, num2)
        case "/":
            resultado = dividir(num1, num2)
        case _:
            resultado = "Operacion invalida"
    return resultado


# if operacion == "+":
#     resultado = sumar(num1, num2)
# elif operacion == "-":
#     resultado = restar(num1, num2)
# elif operacion == "*":
#     resultado = multiplicar(num1, num2)
# elif operacion == "/":
#     resultado = dividir(num1, num2)
# else:
#     resultado = "Operacion invalida"


result = calculadora()
print(result)
