if __name__ == '__main__':
# Definició de variables
    numeroEntrat = int()

# Inicialització de variables
    print("Entra un nombre: ", end="")
    numeroEntrat = float(input())

    if(numeroEntrat==0):
        print(f"El nombre {numeroEntrat} és zero")
    else:
        if (numeroEntrat % 2 == 0):
            print(f"El nombre {numeroEntrat} és parell")
        else:
            print(f"El nombre {numeroEntrat} és senar")
