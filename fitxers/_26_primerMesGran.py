if __name__ == '__main__':
# Definició de variables
    numero1 = int()
    numero2 = int()

# Inicialització de variables

    print("Entra el primer dels números: ", end="")
    numero1 = float(input())

    print("Entra el segon dels números: ", end="")
    numero2 = float(input())

    if (numero1 > numero2):
        print("El primer número és més gran que el segon.")
    else:
        if (numero2 > numero1):
            print("El primer número és més petit que el segon.")
        else:
            print("Els dos números són iguals.")