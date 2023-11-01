# Try Except

## [Python Try Except (***```w3schools.com```***)](https://www.w3schools.com/python/python_try_except.asp)

* El bloc **```try```** us permet **provar** un bloc de codi **per detectar errors**.

* El bloc **```except```** us permet **gestionar l'error**.

* El bloc **```else```** us permet **executar** codi quan **no hi ha cap error**.

* El bloc **```finally```** us permet **executar** codi, **independentment** del resultat dels blocs **```try```** i **```except```**.

## Tractament d'excepcions

Quan es produeix un **error**, o una **excepció** com s'anomena entre els desenvolupadors, **```Python```** normalment s'aturarà i generarà un missatge d'error.

Aquestes **excepcions** es poden gestionar mitjançant la instrucció **```try```**:

Per exemple:
El bloc **```try```** generarà un error o excepció, degut al fet de que la variable **```x```** no està definida:

```python
try:
  print(x)
except:
  print("S'ha produït una excepció!")
```

Com que el bloc **```try```** genera un error, s'executarà el bloc **```except```**.

Sense el bloc **```try```**, el programa es bloquejarà i generarà un error:

```python
Traceback (most recent call last):
  File "fitxer.py", line 3, in <module>
    print(x)
NameError: name 'x' is not defined
```

## Diverses excepcions

Es poden definir tants blocs d'excepció com vulgueu, si per exemple voleu executar un bloc especial de codi per a un tipus d'error especial:

Imprimiu un missatge si el bloc **```try```** genera un **```NameError```** i un altre per a altres errors:
```python
try:
  print(x)
except NameError:
  print("La variable x no s'ha definit")
except:
  print("Alguna cosa més ha fallat!")
```

## Sino (**```else```**)

Podeu utilitzar la paraula clau **```else```** per definir un bloc de codi que s'executarà si no s'ha produït cap error:

```python
try:
  print("Hola món!")
except:
  print("Alguna cosa ha fallat!")
else:
  print("No ha fallat res!")
```

## Sino (**```Finally```**)

El bloc **```finally```**, si s'especifica, s'executarà independentment de si el bloc **```try```** genera un error o no.

```python
try:
  print(x)
except:
  print("Alguna cosa ha fallat!")
finally:
  print("El bloc 'try except' ha acabat!")
```

## Personalitza una excepció 

Com a desenvolupador de **```Python```**, podeu intentar provocar una excepció si es produeix una condició.

Per provocar (o **raise** -> **aixecar**) una excepció, cal fer servir la paraula clau **```raise```**.


Exemple
Generar un error i aturar el programa si **```x```** és inferior a **```0```**:

```python
x = -1

if x < 0:
   raise Excepction("Ho sento, el valor no pot ser negatiu")
```

La paraula clau **```raise```** s'utilitza per generar una excepció.

Podeu definir quin tipus d'error **```raise```** i el text que cal imprimir a l'usuari.

Exemple

Creeu un **```TypeError```** si **```x```** no és un **nombre enter**:

```python
x = "hola"

if not type(x) is int:
   raise TypeError("Només es permeten nombres enters!")
```
