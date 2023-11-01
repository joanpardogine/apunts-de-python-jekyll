if __name__ == '__main__':
# Definició de variables
    factorial = int()
    nombre = int()
    
# Inicialització de variables
    factorial = 1
    
    print('Entra el nombre del que vols conèixer el factorial: ', end='')
    nombre = int(input())

    while (nombre>1):
        factorial = factorial * nombre
        nombre = nombre - 1

    print(f'El factorial és {factorial}')
