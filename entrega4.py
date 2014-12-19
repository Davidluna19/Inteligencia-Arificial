### ---- Entrega 4 - Inteligenia Atificial - David Luna ---- ###
from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE


#Barcos a colocar (numero de barco, y numeracion si es necesario)
barcos = ['00', '01', '02', '10', '11', '12', '2', '3', '4', '5']

#Celdas con Agua
agua = [(0, 1), (2, 1), (2, 2), (3, 4), (4, 3)]

#cant_pos = [(cant_X_fila,cant_X_columna)] (cada indice en la lisa indica el numero de fila/columna)
cantidades_posibles = [(2, 2), (4, 2), (1, 3), (2, 0), (1, 3)]

#Genero el tablero completo
tablero = []
filas = columnas = 5
for fila in range(filas):
    for columna in range(columnas):
        tablero.append((fila, columna))


#Funcion para eliminar del tablero las posiciones con agua
def eliminarAgua(tablero):
    for celda in agua:
        if celda in tablero:
            tablero.remove(celda)
    return tablero


def contarFilasColumnas(indice, valor1, valor2, valor3, valor4, valor5):
    #Recibe un numero de fila, las cantidades de barcos en cada fila (contadores)
    #y retorna el valor actualizado de los valores.
    if indice == 0:
        valor1 += 1
    elif indice == 1:
        valor2 += 1
    elif indice == 2:
        valor3 += 1
    elif indice == 3:
        valor4 += 1
    else:
        valor5 += 1
    return (valor1, valor2, valor3, valor4, valor5)


#Limpio el tablero de celdas inaccesibles o inutilizables
#celdas de agua y filas o columna con cantidades posibles iguales  a 0
tablero = eliminarAgua(tablero)

for cantidades in cantidades_posibles:
    por_fila, por_columna = cantidades
    if por_fila == 0:
        for columna in range(columnas):
            if (cantidades_posibles.index(cantidades), columna) in tablero:
                tablero.remove((cantidades_posibles.index(cantidades), columna))
    if por_columna == 0:
        for fila in range(filas):
            if (fila, cantidades_posibles.index(cantidades)) in tablero:
                tablero.remove((fila, cantidades_posibles.index(cantidades)))

#Dominios
dominios = dict([(barco, list(celda for celda in tablero)) for barco in barcos])


#Resticciones
def cantidad_x_fila_y_Columna(variables, valores):
    #Verificar las restricciones de cantidad por fila y columna
    ubicacion = valores
    correcto = True
    columna1 = columna2 = columna3 = columna4 = columna5 = 0
    fila1 = fila2 = fila3 = fila4 = fila5 = 0

    for celda in ubicacion:
        fila, columna = celda
        fila1, fila2, fila3, fila4, fila5 = contarFilasColumnas(fila, fila1, fila2, fila3, fila4, fila5)
        columna1, columna2, columna3, columna4, columna5 = contarFilasColumnas(columna, columna1, columna2, columna3, columna4, columna5)

    if (fila1 > cantidades_posibles[0][0]):
        correcto = False
    if (fila2 > cantidades_posibles[1][0]):
        correcto = False
    if (fila3 > cantidades_posibles[2][0]):
        correcto = False
    if (fila4 > cantidades_posibles[3][0]):
        correcto = False
    if (fila5 > cantidades_posibles[4][0]):
        correcto = False

    if (columna1 > cantidades_posibles[0][1]):
        correcto = False
    if (columna2 > cantidades_posibles[1][1]):
        correcto = False
    if (columna3 > cantidades_posibles[2][1]):
        correcto = False
    if (columna4 > cantidades_posibles[3][1]):
        correcto = False
    if (columna5 > cantidades_posibles[4][1]):
            correcto = False

    return correcto


def tresJuntos(variables, valores):
    #colocar juntas las tres partes de los barcos grandes
    parte1, parte2 = variables
    celda1, celda2 = valores
    correcto = False

    #esta horizontal?
    if celda1[0] == celda2[0]:
        if abs(celda1[1] - celda2[1]) == abs(int(parte1[1]) - int(parte2[1])):
            correcto = True
    else:
        #esta vertical?
        if celda1[1] == celda2[1]:
            if abs(celda1[0] - celda2[0]) == abs(int(parte1[1]) - int(parte2[1])):
                correcto = True

    return correcto


def celdas_diferentes(variables, valores):
    #Verificar de no ccolocar dos barcos en la misma celda
    return len(valores) == len(set(valores))


restricciones = []
restricciones.append((barcos, cantidad_x_fila_y_Columna))
for barco in barcos:
    for barco2 in barcos:
        if barco != barco2:
            restricciones.append(((barco, barco2), celdas_diferentes))
        if (len(barco) > 1) and (len(barco2) > 1):
            if  barco[0] == barco2[0]:
                restricciones.append(((barco, barco2), tresJuntos))


problema = CspProblem(barcos, dominios, restricciones)

result = backtrack(problema,
                   variable_heuristic=MOST_CONSTRAINED_VARIABLE,
                   value_heuristic=LEAST_CONSTRAINING_VALUE,
                   inference=True)

#result = min_conflicts(problema, iterations_limit=100)

print result