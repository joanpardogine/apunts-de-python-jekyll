## Tractament d'excepcions amb **```try```** i **```except```**

### [Python Try Except (***```w3schools.com```***)](https://www.w3schools.com/python/python_try_except.asp)

|Bloc<br>Paraula clau|Permet|
|----|----|
|[**```try```** i<br>**```except```**](#blocs-try-i-except)|bloc **```try```** per **provar** un bloc de codi **per detectar errors** i<br>bloc **```except```** per **gestionar l'error** si s'ha produit|
|[**```else```**](#bloc-else-sino)|**executar** codi si **no hi ha cap error**|
|[**```finally```**](#bloc-finally)|**executar** codi, **independentment** del resultat dels blocs **```try```** i **```except```**|

Quan es produeix un **error** (o una **excepció** així és com s'anomena entre els *desenvolupadors*), **```Python```** aturarà l'execució del programa i mostrarà el missatge d'error de l'error s'ha produit. 

> ## ***NOTA***: Això és una situació que cal evitar, ja que el que es vol és que ***MAI*** s'aturi el nostre codi degut a un error.

Per exemple, aquest és el codi que conté el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0001.py" target="_blank"> <code>teo_try_0001.py</code></a>

```python
print(x)
```

En executar el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0001.py" target="_blank"><code>teo_try_0001.py</code></a> es generarà la següent sortida:

```bash
/bin/python3 ./_00_try_error.py
Traceback (most recent call last):
  File "/00_try_error.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
```

Com es pot veure, en executar el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0001.py" target="_blank"><code>teo_try_0001.py</code></a> hi hagut un error (**excepció**), s'aturat l'execució del programa i apareix el següent text ```NameError: name 'x' is not defined```.

> ## **NOTA**: Per tant, ha passat allò que MAI hauria de passar, que el nostre programa o aplicació s'aturi degut a un error.

## Blocs **```try```** i **```except```**

El que hem de fer, és gestionar aquestes ***excepcions***, i per poder-ho fer, tan amb **python**, com amb la majoria de llenguatges de programació es poden gestionar mitjançant la instrucció **```try```** (***intenta***) seguida de **```catch```** (***enxampa***):

Per exemple:

El bloc **```try```** del codi contingut en el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0002.py" target="_blank"> <code>teo_try_0002.py</code></a> **intentarà** (***will try***) executar el tros de codi que hi ha al bloc **```try```** i si l'execució d'aquest codi genera una **excepció**, llavors, per no acabar l'execució del codi mostrant un error, executarà el codi que hi hagi al bloc **```except```**. En aquest cas, efectivament, degut a què la variable **```x```** no està definida, l'execució del tros de codi que hi ha al bloc **```try```** genera una **excepció**, i com s'ha comentat, es procedeix a executar el codi que hi hagi al bloc **```except```**.

```python
try:
  print(x)
except:
  print("S'ha produït una excepció!")
```

Veiem la sortida de l'execució del fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0002.py" target="_blank"><code>teo_try_0002.py</code></a>:

```bash
/bin/python3 ./teo_try_0002.py
S'ha produït una excepció!
```

> ## **Resum**: Com que el bloc **```try```** genera una **excepció** (**error**), s'executa el bloc **```except```**.

### Gestionar les excepcions generades de manera especifica

Com ja s'ha vist anteriorment, la sortida de l'execució del fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0001.py" target="_blank"><code>teo_try_0001.py</code></a> és la següent:

```bash
/bin/python3 ./teo_try_0001.py
Traceback (most recent call last):
  File "/00_try_error.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
```

Com ja s'ha comentat anteriorment, es veu com s'ha produit és una **excepció** anomenada **```NameError```** i l'execució del programa s'ha aturat. 

A partir d'aquesta situació, el que es pot fer, és definir un **bloc d'excepció** per gestionar especificament l'excepció anomenada **```NameError```**.

El bloc **```try```** del codi contingut en el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0003.py" target="_blank"> <code>teo_try_0003.py</code></a> generarà un **error** o **excepció**, degut a què la variable **```x```** no està definida. Per degut a que hem creat el bloc **```except NameError:```** es pot executar un tros de codi especial per quan es produeix una **excepció** del tipus **```NameError```**. I també hem creat el bloc **```except```** executarà un tros de codi especial per quan es produeix qualsevol altra **excepció** que **NO** sigui del tipus **```NameError```**. 

```python
try:
  print(x)
except NameError:
  print("S'ha produït una excepció NameError")
  print("La variable x no s'ha definit")
except:
  print("S'ha produït una excepció que no és NameError")
  print("Alguna cosa més ha fallat!")
```

> ## **Resum**: es poden desenvolupar diferents parts de codi per què s'executin en funció de cada tipus d'***excepció*** que es produeixin.

### Bloc **```else```** (***sino***)

Com ja s'ha vist anterior, i tant amb **python**, com amb la majoria de llenguatges de programació, també ens pot interessar que s'executi un tros de codi, en el cas en que **no s'ha produït cap *excepció***.

Efectivament, per aquesta situació es pot crear el bloc **```else```** que, com hem comentat, s'executarà quan **NO** es produeix cap **excepció**, tot just després d'executar un bloc **```try```**.

Aquest **bloc** es crea amb la paraula clau **```else```** (**sino**).

El bloc **```try```** del codi contingut en el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0004.py" target="_blank"> <code>teo_try_0004.py</code></a> generarà una excepció, si la línia que conté **```print("Hola món!")```** genera una excepció. Pero com que aquesta línia no generarà cap excepció, llavors el codi procedirà a executar el codi que estigui dins del bloc **```else```**.

```python
try:
  print("Hola món!")
except:
  print("Alguna cosa ha fallat!")
else:
  print("No ha fallat res!")
```

A la sortida de l'execució del fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0004.py" target="_blank"><code>teo_try_0004.py</code></a>:

```bash
/bin/python3 ./teo_try_0004.py
Hola món!
No ha fallat res!
```

## Bloc **```finally```**

El bloc **```finally```**, si s'especifica, és a dir que **és opcional**, s'executarà independentment de si el bloc **```try```** genera una excepció o no.

El bloc **```try```** del codi contingut en el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0005.py" target="_blank"> <code>teo_try_0005.py</code></a> generarà una excepció, si la línia que conté **```print(x)```** genera una excepció.

```python
try:
  print(x)
except NameError:
  print("S'ha produït una excepció NameError")
  print("La variable x no s'ha definit")
except:
  print("S'ha produït una excepció que no és NameError")
  print("Alguna cosa més ha fallat!")
finally:
  print("El bloc 'try' i els dos blocs 'except' han acabat!")
```

A la sortida de l'execució del fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0005.py" target="_blank"><code>teo_try_0005.py</code></a>:

```bash
/bin/python3 ./teo_try_0005.py
S'ha produït una excepció NameError
La variable x no s'ha definit
El bloc 'try' i els dos blocs 'except' han acabat!
```

Veiem que l'**excepció** que s'ha produit és una excepció anomenada **```NameError```**. 

## Arguments que genera una excepció 

 <!-- i el que volem és obtenir els arguments d'aquesta excepció. Per això el que farem és associar un nom de variable a aquesta excepció de la següent manera. -->

Quan es produeix una excepció, aquesta pot tenir valors associats, també coneguts com a arguments (**```args```**) de l'excepció. La presència i els tipus dels arguments depenen del tipus d'excepció.

La clàusula **```except```** pot especificar una variable després del nom de l'excepció. La variable està lligada a la instància d'excepció que normalment té un atribut *```args```* que emmagatzema els arguments. Per comoditat, els tipus d'excepció integrats defineixen **```__str__()```** per imprimir tots els arguments sense accedir explícitament a **```.args```**.


El bloc **```try```** del codi contingut en el fitxer <a href="https://github.com/joanpardogine/apunts-de-python-jekyll/raw/main/fitxers/teoria/teo_try_0006.py" target="_blank"> <code>teo_try_0003.py</code></a> generarà un **error** o **excepció**, degut a què la variable **```x```** no està definida:

És a dir, s'imprimeix un missatge si el bloc **```try```** genera un **```NameError```** i aquesta  un altre missatge si el bloc **```try```** genera qualsevol altre error.


## Personalitza una excepció 

Com a desenvolupador de **```Python```**, podeu intentar provocar una excepció si es produeix una condició.

Per provocar (o **raise** -> **aixecar**) una excepció, cal fer servir la paraula clau **```raise```**.


Exemple
Generar una excepció i aturar el programa si **```x```** és inferior a **```0```**:

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
