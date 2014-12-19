### ---- Entrega 2 - Inteligenia Atificial - David Luna ---- ###
from simpleai.search import SearchProblem
from simpleai.search.viewers import WebViewer
import math

### ---- Busqueda No Informada ---- ###
#from simpleai.search import breadth_first
#from simpleai.search import uniform_cost
#from simpleai.search import depth_first
#from simpleai.search import limited_depth_first
#from simpleai.search import iterative_limited_depth_first

### ---- Busqueda Informada ---- ###
from simpleai.search import astar
#from simpleai.search import greedy

pcs = {1: (37, 26), 2: (25, 12), 3: (41, 16), 4: (55, 28), 6: (68, 31), 7: (59, 51), 8: (63, 21), 9: (66, 5),
    10: (54, 6), 11: (46, 2), 12: (32, 2), 13: (6, 3), 14: (4, 14), 15: (15, 19), 16: (15, 39), 17: (20, 53),
    18: (25, 43), 19: (13, 10), 20: (25, 43)}

movs = [
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 20],
    [2, 19],
    [3, 10],
    [3, 12],
    [4, 6],
    [4, 7],
    [4, 8],
    [7, 17],
    [8, 9],
    [9, 10],
    [10, 11],
    [11, 12],
    [12, 19],
    [13, 19],
    [14, 19],
    [15, 19],
    [15, 16],
    [16, 20],
    [17, 20],
    [18, 20]
    ]
costo = [25, 10, 20, 30, 10, 25, 25, 15, 35, 10, 80, 55, 10, 10, 40, 60, 10, 10, 10, 65, 10, 10, 5]

GOAL = 9
INITIAL = 15


class Entrega2(SearchProblem):
    def is_goal(self, state):
        return state == GOAL

    def cost(self, state1, action, state2):
        global movs
        global costo
        #Calcular costo
        for mov in movs:
            if state1 in mov:
                if state2 in mov:
                    return costo[movs.index(mov)]

    def actions(self, state):
        global movs
        actions = []

        for pc1, pc2 in movs:
            if state == pc1:
                actions.append(pc2)
            elif state == pc2:
                actions.append(pc1)

        return actions

    ### Heuristica ###
    def heuristic(self, state):
        distance = 0
        cor_x_state, cor_y_state = pcs[state]
        cor_x_goal, cor_y_goal = pcs[GOAL]
        distance = math.sqrt((abs(cor_y_state - cor_y_goal) ** 2) + (abs(cor_x_goal - cor_x_state) ** 2))

        return distance

    def result(self, state, action):
        state = action
        return (state)

my_viewer = WebViewer()

### ---- Resultados Busqueda No Informada ---- ###
#result = breadth_first(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)
#result = uniform_cost(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)
#result = depth_first(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)
#result = limited_depth_first(Entrega2(INITIAL), 8, graph_search=True, viewer=my_viewer)
#result = iterative_limited_depth_first(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)

### ---- Resultados Busqueda Informada ---- ###
result = astar(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)
#result = greedy(Entrega2(INITIAL), graph_search=True, viewer=my_viewer)
