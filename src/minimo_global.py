def min_global(estaciones, estados_objetivo):

    solucion_estados = {}
    solucion_estaciones = {}
    num_estaciones = []
    
    maximo = 0
    for num, contenido in estaciones.items():
        maximo = max(maximo, len(contenido['Estados']))

    posible_primera_estacion = [num for num in range(len(estaciones)-1) if len(estaciones[num]['Estados']) >= maximo]
    
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

    min_num_estaciones = min(num_estaciones)
    estaciones_contratadas = zip(posible_primera_estacion, num_estaciones)

    mejor_primera_estacion = []
    num_mejor_primera_estacion = [estacion_principal for (estacion_principal, estaciones_totales) in estaciones_contratadas if estaciones_totales == min_num_estaciones]
    for estacion in num_mejor_primera_estacion:
         mejor_primera_estacion.append(estaciones[estacion]['ID'])

    print(f'Mejores primeras estaciones: {mejor_primera_estacion}\n')

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

            print(f'''Estación inicial: {estaciones[primera_estacion]['ID']}
Estados cubiertos: {len(solucion_estados)}/{len(estados_objetivo)}
Estaciones contratadas: {solucion_estaciones} ({len(solucion_estaciones)})
Iteraciones totales: {iteraciones}\n''')
            
    print(f'Mínimos globales encontrados: {len(mejor_primera_estacion)}\n')