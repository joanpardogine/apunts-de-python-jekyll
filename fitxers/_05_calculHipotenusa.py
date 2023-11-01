from math import sqrt

if __name__ == '__main__':
# Definició de variables
    catet1 = float()
    catet2 = float()
    hipotenusa = float()

# Inicialització de variables
    print('Entra el primer dels catets: ', end='')
    catet1 = float(input())

    print('Entra el segon dels catets: ', end='')
    catet2 = float(input())

    hipotenusa = sqrt(catet1**2 + catet2**2 )
    # hipotenusa = sqrt(pow(catet1,2) + pow(catet2,2))

    print(f"La hipotenusa del triangle amb els catets de {catet1} i de {catet2} és {hipotenusa}.")

