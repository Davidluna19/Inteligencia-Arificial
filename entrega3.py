### ---- Entrega 3 - Inteligenia Atificial - David Luna ---- ###

import random
from simpleai.search.viewers import WebViewer
from simpleai.search import SearchProblem
from simpleai.search import hill_climbing, hill_climbing_stochastic, hill_climbing_random_restarts, beam, simulated_annealing, genetic

INITIAL = '123\n456\n789'


def str2list(state):
    return [list(fila) for fila in state.split('\n')]


def list2str(state):
    return '\n'.join(''.join(fila) for fila in state)


def find(state, numero):
    for numero_fila, fila in enumerate(state):
        for columna, numero_act in enumerate(fila):
            if numero_act == numero:
                return numero_fila, columna


class Entrega3(SearchProblem):
    def actions(self, state):
        actions = []
        state = str2list(state)

        for numero in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            fila, columna = find(state, numero)

            if fila > 0:
                actions.append((numero, fila - 1, columna))
            if fila < 2:
                actions.append((numero, fila + 1, columna))
            if columna > 0:
                actions.append((numero, fila, columna - 1))
            if columna < 2:
                actions.append((numero, fila, columna + 1))

        return actions

    def result(self, state, action):
        numero, nueva_fila, nueva_columna = action
        state = str2list(state)
        otro_numero = state[nueva_fila][nueva_columna]
        fila_numero, columna_numero = find(state, numero)

        state[nueva_fila][nueva_columna] = numero
        state[fila_numero][columna_numero] = otro_numero

        return list2str(state)

    def value(self, state):
        multisumageneidad = 0
        suma_filas = 0
        suma_columnas = 0
        state = str2list(state)

        #Filas
        for fila in state:
            multiplo_fila = 1
            for numero in fila:
                multiplo_fila = multiplo_fila * int(numero)
            suma_filas += multiplo_fila

        #Columnas
        for columna in range(3):
            multiplo_columna = 1
            for fila in range(3):
                multiplo_columna = multiplo_columna * int(state[fila][columna])
            suma_columnas += multiplo_columna
        multisumageneidad = abs(suma_filas - suma_columnas)

        return -multisumageneidad

    def generate_random_state(self):
        numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        random.shuffle(numeros)
        fila1 = numeros[:3]
        fila2 = numeros[3:6]
        fila3 = numeros[6:]
        state = [fila1, fila2, fila3]
        return list2str(state)

my_viewer = WebViewer()

#result = hill_climbing(Entrega3(INITIAL), viewer=my_viewer)
#result = hill_climbing_stochastic(Entrega3(INITIAL), viewer=my_viewer)
#result = hill_climbing_random_restarts(Entrega3(), restarts_limit=15, viewer=my_viewer)
result = beam(Entrega3(), beam_size=5, viewer=my_viewer)
#result = simulated_annealing(Entrega3(INITIAL), iterations_limit=20, viewer=my_viewer)

print result

