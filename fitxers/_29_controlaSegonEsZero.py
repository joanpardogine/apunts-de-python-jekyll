if __name__ == '__main__':
# Definició de variables
    numero1 = int()
    numero2 = int()

# Inicialització de variables

    print("Entra el primer dels números: ", end="")
    numero1 = float(input())

    print("Entra el segon dels números: ", end="")
    numero2 = float(input())

    if (numero2 == 0):
        print("El segon nombre és zero i no és possible dividir per zero!")
    else:
        print(numero1, " / ", numero2, " = ", numero1/numero2)