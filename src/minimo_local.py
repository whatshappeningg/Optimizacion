import random

def min_local(estaciones, estados_objetivo):

    minimo_encontrado = True
    min_estaciones = len(estaciones)

    while minimo_encontrado:

        primera_estacion = random.choice(range(len(estaciones)-1))

        solucion_estados = estaciones[primera_estacion]['Estados']
        solucion_estaciones = [estaciones[primera_estacion]['ID']]
        iteraciones = 0
        

        for num, contenido in estaciones.items():
            if contenido['Estados'] - solucion_estados != set():
            # if estados_objetivo != solucion_estados ó if solucion_estados - contenido['Estados'] != set() => + iteraciones, + estaciones
                solucion_estados = set(solucion_estados) | set(contenido['Estados'])
                solucion_estaciones.append(contenido['ID'])
                iteraciones += 1

        if min_estaciones > len(solucion_estaciones):
            min_estaciones = len(solucion_estaciones)

        else:
            print('------------------------------------')
            print(f'Estación inicial: {estaciones[primera_estacion]['ID']}\n')
            solucion_estados = estaciones[primera_estacion]['Estados']
            solucion_estaciones = [estaciones[primera_estacion]['ID']]
            iteraciones = 0
            print(f'Estados añadidos: {solucion_estados} ({len(solucion_estados)})\n')

            for num, contenido in estaciones.items():
                if contenido['Estados'] - solucion_estados != set():
                # if estados_objetivo != solucion_estados ó if solucion_estados - contenido['Estados'] != set() => + iteraciones, + estaciones
                    print(f'Estados añadidos: {contenido['Estados'] - solucion_estados} ({len(contenido['Estados'] - solucion_estados)})\n')
                    solucion_estados = set(solucion_estados) | set(contenido['Estados'])
                    solucion_estaciones.append(contenido['ID'])
                    iteraciones += 1


            print(f'''Solución:
Estados cubiertos: {solucion_estados} ({len(solucion_estados)}/{len(estados_objetivo)})
Estaciones: {solucion_estaciones} ({len(solucion_estaciones)})
Iteraciones totales: {iteraciones}
''')
            minimo_encontrado = False
