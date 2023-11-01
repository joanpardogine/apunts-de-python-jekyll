#  31 Estan en majúscules?
# Enunciat: Programa que llegeixi una cadena
# per teclat i comproveu si totes les lletres
# estan en majúscules.

if __name__ == '__main__':
# Definició de variables
    cadenaLlegida = str()

# Inicialització de variables
    print("Entra el nom d'usuari: ", end="")
    cadenaLlegida = str(input())

    if (cadenaLlegida.isupper()):
        print(f"La cadena llegida {cadenaLlegida} està en majúscules!")
    else:
        print(f"La cadena llegida {cadenaLlegida} NO està en majúscules!")

