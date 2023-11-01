# 32 Càlcul de potencia
# Enunciat: Realitza un algorisme que calculi
# la potència, per això cal demanar per teclat
# la base i l'exponent.
# Poden passar tres coses: 
# L'exponent sigui positiu, només heu d'imprimir
# la potència.
# L'exponent sigui 0, el resultat és 1.
# L'exponent sigui negatiu, el resultat és 1/potència
# amb l'exponent positiu.

if __name__ == '__main__':
# Definició de variables
    base = float()
    exponent = float()
    potencia = float()

# Inicialització de variables
    print("Entra la base: ", end="")
    base = float(input())

    print("Entra l'exponent: ", end="")
    exponent = float(input())


    if (exponent>0):
        potencia = base ** exponent
    else:
        if (exponent==0):
            potencia = 1
        else:
            potencia = (1/(base**(exponent*(-1))))

    print(f"La potencia de {base} elevat a {exponent} és igual {potencia}")
