if __name__ == '__main__':

# Definició de variables
    base = float()
    alcada = float()
    area = float()
    perimetre = float()

# Inicialització de variables

    print('Entra la base del rectangle: ', end='')
    base = float(input())

    print("Entra l'alçada del rectangle: ", end="")
    alcada = float(input())

    area = (base * alcada)
    perimetre = (2 * (base + alcada))

    print(f"L'area d'un rectangle de base {base} i alçada {alcada} és {area}")
    print(f"El perímetre d'un rectangle de base {base} i alçada {alcada} és {perimetre}")