if __name__ == '__main__':
# Definició de variables
    num1 = int()
    num2 = int()

# Inicialització de variables
    print('Entra el primer dels nombres: ', end='')
    num1 = int(input())

    print('Entra el segon dels nombres: ', end='')
    num2 = int(input())

    if (num1>num2):
        print('El primer valor és més gran!')
    else:
        if (num1<num2):
            print('El primer valor és més petit!')
        else:
            print('Els dos valors son iguals!')
