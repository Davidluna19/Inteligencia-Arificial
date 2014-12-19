from simpleai.search import SearchProblem
#from simpleai.search import breadth_first
#from simpleai.search import uniform_cost
#from simpleai.search import depth_first
from simpleai.search import limited_depth_first
#from simpleai.search import iterative_limited_depth_first

from simpleai.search.viewers import WebViewer

GOAL = 'K L T\n\n0'
INITIAL = '\nK L T\n1'


def str2list(state):
    state = state.split('\n')
    state[0] = state[0].split(' ')
    state[1] = state[1].split(' ')
    return state


def list2str(state):
    state[0].sort()
    state[0] = ' '.join(state[0])
    state[1].sort()
    state[1] = ' '.join(state[1])
    return '\n'.join(state)


def find(state, element):
    for lado in state:
        if element in lado:
            return state.index(lado)


class Entrega1(SearchProblem):
    def is_goal(self, state):
        state = str2list(state)
        if 'K'and 'L' and 'T' in state[0] and state[1] == [''] and state[2] == '0':
            return True
        else:
            return False
        #return state == GOAL

    def cost(self, state1, action, state2):
        return 1

    def actions(self, state):
        viajes = [1, -1]

        state = str2list(state)
        actions = []
        compras = list(element for element in state[int(state[2])])
        compras.append('e')
        if '' in compras:
            compras.remove('')

        for mov in viajes:
            for compra in compras:
                if compra == 'e':
                    n_lado = int(state[2]) + mov
                else:
                    lado = find(state, compra)
                    n_lado = lado + mov

                n_state = state[:]

                if (0 <= n_lado <= 1):
                    if compra == 'e':
                        flag = True
                        if 'T' in n_state[lado]:
                            if 'K' in n_state[lado]:
                                flag = False
                        if 'L'in n_state[lado]:
                            if 'K' in n_state[lado]:
                                flag = False
                        if flag:
                            actions.append(compra)
                    else:
                        n_state[lado].remove(compra)
                        flag = True
                        if 'T' in n_state[lado]:
                            if 'K' in n_state[lado]:
                                flag = False
                        if 'L'in n_state[lado]:
                            if 'K' in n_state[lado]:
                                flag = False
                        if flag:
                            actions.append(compra)
                        n_state[lado].append(compra)

        return actions

    def result(self, state, action):
        state = str2list(state)
        lado_act = int(state[2])

        if lado_act == 0:
            lado_sg = 1
        else:
            lado_sg = 0
        if action == 'e':
            state[2] = str(lado_sg)
        else:
            state[lado_act].remove(action)
            state[lado_sg].append(action)
            state[2] = str(lado_sg)
        state = list2str(state)
        return (state)

my_viewer = WebViewer()

#result = breadth_first(Entrega1(INITIAL), viewer=my_viewer)
#result = uniform_cost(Entrega1(INITIAL), viewer=my_viewer)
#result = depth_first(Entrega1(INITIAL), viewer=my_viewer)
result = limited_depth_first(Entrega1(INITIAL), 7, viewer=my_viewer)
#result = iterative_limited_depth_first(Entrega1(INITIAL), viewer=my_viewer)
