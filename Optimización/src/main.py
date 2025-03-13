# Cubrir todos los estados con el menor número de estaciones
from minimo_global import min_global
from minimo_local import min_local

estaciones = {}

estaciones[0] = {'Estados': {'ID', 'NV', 'UT'}, 'ID': 'kone'}
estaciones[1] = {'Estados': {'WA', 'ID', 'MT'}, 'ID': 'ktwo'}
estaciones[2] = {'Estados': {'OR', 'NV', 'CA'}, 'ID': 'kthree'}
estaciones[3] = {'Estados': {'NV', 'UT'}, 'ID': 'kfour'}
estaciones[4] = {'Estados': {'CA', 'AZ'}, 'ID': 'kfive'}
estaciones[5] = {'Estados': {'NM', 'TX', 'OK'}, 'ID': 'ksix'}
estaciones[6] = {'Estados': {'OK', 'KS', 'CO'}, 'ID': 'kseven'}
estaciones[7] = {'Estados': {'KS', 'CO', 'NE'}, 'ID': 'keight'}
estaciones[8] = {'Estados': {'NE', 'SD', 'WY'}, 'ID': 'knine'}
estaciones[9] = {'Estados': {'ND', 'IA'}, 'ID': 'kten'}
estaciones[10] = {'Estados': {'MN', 'MO', 'AR'}, 'ID': 'keleven'}
estaciones[11] = {'Estados': {'LA'}, 'ID': 'ktwelve'}
estaciones[12] = {'Estados': {'MO', 'AR'}, 'ID': 'kthirteen'}

estados_objetivo = {'ID', 'NV', 'UT', 'WA', 'MT', 'OR', 'CA', 'AZ', 'NM', 'TX', 'OK', 'KS', 'CO', 'NE', 'SD', 'WY', 'ND', 'IA', 'MN', 'MO', 'AR', 'LA'}


if __name__ == '__main__':

    while True:
        print('Calcular mínimo local (ML) o mínimo global (MG):')
        minimo = input().upper()
        print('------------------------------------')
        if minimo == 'ML':
            min_local(estaciones, estados_objetivo)
        elif minimo == 'MG':
            min_global(estaciones, estados_objetivo)
        else:
            break