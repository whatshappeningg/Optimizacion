# Ejercicio de optimización
## Introducción
En los algoritmos de búsqueda se parte de un estado inicial para llegar a uno objetivo, con lo que se quiere encontrar el mejor camino según ciertos parámetros. Por otro lado, en cuanto a la optimización, se busca un estado óptimo en base a una función objetivo, sin importar el camino. A diferencia de las búsquedas, esto garantiza entontrar una solución aunque el espacio de estados tienda a infinito.

En resumen, las búsquedas encuentran el mejor camino y la optimización el estado óptimo.

Con el método de ascención de colinas (o greedy local search) para solucionar problemas de optimización, se parte de un estado inicial (aleatorio o fijo) y se valoran los estados vecinos. La finalidad es encontrar el estado con una mayor valoración. Si la valoración de los estados vecinos es menor que la actual, se ha encontrado un **máximo local**. Si la valoración del estado actual es la máxima posible, se ha encontrado un **máximo global**. Esta es la mejor solución que se puede encontrar.

## Problema
### Datos
Estación | Estados Cubiertos |
:---: | :---: |
kone | Idaho (ID), Nevada (NV), Utah (UT) |
ktwo | Washington (WA), Idaho (ID), Montana (MT) |
kthree | Oregon (OR), Nevada (NV), California (CA) |
kfour | Nevada (NV), Utah (UT) |
kfive | California (CA), Arizona (AZ) |
ksix | New Mexico (NM), Texas (TX), Oklahoma (OK) |
kseven | Oklahoma (OK), Kansas (KS), Colorado (CO) |
keight | Kansas (KS), Colorado (CO), Nebraska (NE) |
knine | Nebraska (NE), South Dakota (SD), Wyoming (WY) |
kten | North Dakota (ND), Iowa (IA) |
keleven | Minnesota (MN), Missouri (MO), Arkansas (AR) |
ktwelve | Louisiana (LA) |
kthirteen | Missouri (MO), Arkansas (AR) |

Estados: Idaho, Nevada, Utah, Washington, Montana, Oregon, California, Arizona, New Mexico, Texas, Oklahoma, Kansas, Colorado, Nebraska, South Dakota, Wyoming, North Dakota, Iowa, Minnesota, Missouri, Arkansas, Louisiana.

### Enunciado
Beyoncé quiere que su nuevo disco *Cowboy carter* suene en los 22 estados anteriores contratando el menor número de estaciones de radio. El problema es que hay estaciones que cubren el mismo estado, por ejemplo 'kone' y 'ktwo', ambas cubren Idaho. El objetivo es encontrar la combinación mínima de estaciones que cubra todos los estados. Para eso se programará en python un algoritmo de ascensión de colinas para encotrar tanto el [mínimo global](/src/minimo_global.py) como [mínimos locales](/src/minimo_local.py).

## Solución
### Mínimo global
Esta función recibe un diccionario con las estaciones más sus estados y una lista con los todos estados a cubrir (es decir, los [datos](#datos)).

La solución puede variar según el primer estado que se escoga, por lo que lo primero es encontrar el mejor estado del que partir, en este caso la estación de radio que cubra el mayor número de estados. A partir de ahí se evaluarán para saber si se obtiene un resultado óptimo.

Recorriendo el diccionario y con la función `max()`, se compara la longitud de estados cubiertos por estación, obteniendo el máximo. Después se crea una lista (`posible_primera_estacion`) con las estaciones que cumplan la condición de tener el máximo de estados cubiertos.
```
    maximo = 0
    for num, contenido in estaciones.items():
        maximo = max(maximo, len(contenido['Estados']))

    posible_primera_estacion = [num for num in range(len(estaciones)-1) if len(estaciones[num]['Estados']) >= maximo]
```

Se procede a la evaluación de las estaciones recogidas en esta lista.

Por cada estación se inicializan:
- Número de iteraciones del código (`iteraciones`)
- Una lista que almacena los estados cubiertos (`solucion_estados`) con los estados de la estación a evaluar.
- Una lista que almacena las estaciones contratadas (`solucion_estaciones`) con la estación a evaluar.

Luego se recorre el diccionario de estaciones. Por cada estación se comprueba si hay estados que todavía no se encuentran en la solución de estados. Si es así, tanto la estación como los estados se unen a las soluciones y se añade una iteración.  
Antes de reinicializar, el número de estaciones contratadas se almacena en una lista (`num_estaciones`).
```
    for primera_estacion in posible_primera_estacion:

        iteraciones = 0
        solucion_estados = estaciones[primera_estacion]['Estados']
        solucion_estaciones = [estaciones[primera_estacion]['ID']]

        for num, contenido in estaciones.items():

            if contenido['Estados'] - solucion_estados != set():
            # if estados_objetivo != solucion_estados ó if solucion_estados - contenido['Estados'] != set() => + iteraciones, + estaciones
                solucion_estados = set(solucion_estados) | set(contenido['Estados'])
                solucion_estaciones.append(contenido['ID'])
                iteraciones += 1

        num_estaciones.append(len(solucion_estaciones))
```
Con esta lista se comprueba el número mínimo de estaciones necesarias para cubrir todos los estados. Se crea una lista de tuplas que asocie las potenciales primeras estaciones con el número de estaciones a contratar de cada una y, con esto, se consigue saber qué estaciones de radio obtienen mejor resultado si se utilizan como estación inicial.
```
    min_num_estaciones = min(num_estaciones)
    estaciones_contratadas = zip(posible_primera_estacion, num_estaciones)

    mejor_primera_estacion = []
    num_mejor_primera_estacion = [estacion_principal for (estacion_principal, estaciones_totales) in estaciones_contratadas if estaciones_totales == min_num_estaciones]
    for estacion in num_mejor_primera_estacion:
         mejor_primera_estacion.append(estaciones[estacion]['ID'])

    print(f'Mejores primeras estaciones: {mejor_primera_estacion}\n')
```
Teniendo esta lista de mejores primeras estaciones (`mejor_primera_estacion`) se realiza el proceimiento de evaluación anterior, pero esta vez imprimiendo por pantalla qué estados se añaden en cada iteración.
```
    for primera_estacion in num_mejor_primera_estacion:

            iteraciones = 0
            solucion_estados = estaciones[primera_estacion]['Estados']
            solucion_estaciones = [estaciones[primera_estacion]['ID']]
            print(f'Estados añadidos: {solucion_estados} ({len(solucion_estados)})\n')

            for num, contenido in estaciones.items():

                if contenido['Estados'] - solucion_estados != set():
                    print(f'Estados añadidos: {contenido['Estados'] - solucion_estados} ({len(contenido['Estados'] - solucion_estados)})\n')
                    solucion_estados = set(solucion_estados) | set(contenido['Estados'])
                    solucion_estaciones.append(contenido['ID'])
                    iteraciones += 1
```
Como conclusión, la solución incluye el estado inicial, de los estados a cubrir cuántos se cubrieron (siendo un mínimo global, solo es aceptable que todos estén cubiertos), las estaciones a contratar y el total de iteraciones, así como el total de mínimos globales encontrados.
```
            print(f'''Estación inicial: {estaciones[primera_estacion]['ID']}
Estados cubiertos: {len(solucion_estados)}/{len(estados_objetivo)}
Estaciones contratadas: {solucion_estaciones} ({len(solucion_estaciones)})
Iteraciones totales: {iteraciones}\n''')
            
    print(f'Mínimos globales encontrados: {len(mejor_primera_estacion)}\n')
```
