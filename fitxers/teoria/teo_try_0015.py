try:
    print(x)

except Exception as excepcioOcorreguda:
    tipusDExcepcio = type(excepcioOcorreguda)   # Obtenim el tipus d'excepció
    print(f"tipusDExcepcio = {tipusDExcepcio}") # Mostrem el tipus de l'excepció

    argumentsDeLExcepcio = excepcioOcorreguda.args
        # El mètode __str__ ens permet, amb la propietat args
        # obtenim els parametres o arguments de l'excepció

    quantitatDArguments = len(argumentsDeLExcepcio)         # Obtenim la quantitat d'arguments que té l'excepció
    print(f'quantitatDArguments = {quantitatDArguments}')   # Mostrem la quantitat d'arguments que té l'excepció
    
    for argument in (argumentsDeLExcepcio):
        print(f'Argument = {argument}')                     # Mostrem tots els arguments que té l'excepció

finally:
    print(f"final")