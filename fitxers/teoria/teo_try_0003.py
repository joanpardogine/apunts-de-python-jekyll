try:
  print(x)
except NameError:
  print("S'ha produït una excepció NameError")
  print("La variable x no s'ha definit")
except:
  print("S'ha produït una excepció que no és NameError")
  print("Alguna cosa més ha fallat!")