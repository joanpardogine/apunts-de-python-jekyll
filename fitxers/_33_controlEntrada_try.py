# 33 Control d'entrada
# Enunciat: Algorisme que demani dos nombres
# nota i edat i un caràcter sexe i mostrar el
# missatge: ACCEPTADA si:
# 1. la nota és major o igual a cinc,
# 1. l'edat és major o igual a divuit i
# 1. el sexe és F.
# En cas que es compleixi el mateix, però el
#  sexe sigui M, heu de mostrar el missatge: POSSIBLE.
# Si no es compleixen aquestes condicions cal
# mostrar el missatge: NO ACCEPTADA.

if __name__ == '__main__':
# Definició de variables
    notaEntrada = float()
    edatEntrada = int()
    sexeEntrat = str()
    MAJOR_DE_EDAT = 18
    APROVAT = 5
    valorCorrecte = bool()

# Inicialització de variables

    while(True):
        try:
            print("Entra la nota: ", end="")
            notaEntrada = int(input())
            break

        except ValueError:
            print("\tERROR!\n\tCal que entris un nombre!\n")

    while(True):
        try:
            print("Entra l'edat: ", end="")
            edatEntrada = int(input())
            break

        except ValueError:
            print("\tERROR!\n\tCal que entris un nombre!\n")

    while(True):
        print("Entra el teu sexe (M=masculí, F=femení): ", end="")
        sexeEntrat = str(input()).upper()
        if ((sexeEntrat == 'M') or (sexeEntrat=='F')):
            break
        else:
            print("\nERROR!\tCal que entris un dels valors demanats!")
            print("\tQue eren: M per masculí i F per femení!\n")

 
#    if ( (notaEntrada>=5) and (edatEntrada>=18) ):
    if ( (notaEntrada>=APROVAT) and (edatEntrada>=MAJOR_DE_EDAT) ):
        if ( (sexeEntrat=="F") ):
            print("\nACCEPTADA\n")
        else:
            print("\nPOSSIBLE\n")
    else:
        print("\nNO ACCEPTADA\n")