if __name__ == '__main__':
# Definició de variables
    tempEnFahrenheit = float()   
    tempEnCelsius = float()

# Inicialització de variables

    print("Entra la temperatura en Fahrenheit per convertir-la a Celsius: ", end="")
    tempEnFahrenheit = float(input())

    tempEnCelsius = (tempEnFahrenheit-32)/1.8

    print(f"{tempEnFahrenheit} F són {tempEnCelsius} ºC")
    
