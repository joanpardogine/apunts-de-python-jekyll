if __name__ == '__main__':
# Definició de variables
    numero1 = int()
    numero2 = int()

# Inicialització de variables

    print("Entra el primer dels números: ", end="")
    numero1 = float(input())

    print("Entra el segon dels números: ", end="")
    numero2 = float(input())

    print(numero1, " + ", numero2, " = ", numero1 + numero2)
    print(numero1, " - ", numero2, " = ", numero1 - numero2)
    print(numero2, " - ", numero1, " = ", numero2 - numero1)
    print(numero1, " * ", numero2, " = ", numero1 * numero2)

    if (numero2 == 0):
        print("No és possible dividir per zero!")
    else:
        print(numero1, " / ", numero2, " = ", numero1/numero2)