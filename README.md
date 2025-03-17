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
Beyoncé quiere que su nuevo disco *Cowboy carter* suene en los 22 estados anteriores contratando el menor número de estaciones de radio. El problema es que hay estaciones que cubren el mismo estado, por ejemplo 'kone' y 'ktwo', ambas cubren Idaho. El objetivo es encontrar la combinación mínima de estaciones que cubra todos los estados. Para eso se programará en python un algoritmo de ascensión de colinas para encotrar tanto [mínimos locales](/src/minimo_local.py) como el [mínimo global](/src/minimo_global.py).
