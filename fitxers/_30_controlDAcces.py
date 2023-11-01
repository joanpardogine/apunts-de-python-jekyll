#  30 Control d'accés
# Enunciat: Escriu un programa que demani un nom d'usuari
# i una contrasenya i si s'ha introduït "joan" i
#  "ginebro" s'indica "Has entrat al sistema", si no hi ha un error.*
if __name__ == '__main__':
# Definició de variables
    nomUsuari = str()
    motDePas = str()

# Inicialització de variables
    print("Entra el nom d'usuari: ", end="")
    nomUsuari = str(input())


    print("Entra el mot de pas: ", end="")
    motDePas = str(input())

    if ((nomUsuari == 'joan') and (motDePas == 'ginebro')):
        print("Has entrat al sistema!")
    else:
        print("ERROR!!!\nNo has entrat al sistema!")