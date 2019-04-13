from random import sample, choice
from itertools import combinations

"""
Problema Planteado 2.4:

		Coloreo de grafos



		Definir como problema de busqueda

Pintar los nodos de un grafo, tal que los adyacentes no tengan el mismo
Heuristicas a programar:

		1) Cantidad de aristas entre dos nodos sin color
		2) Cantidad de aristas con uno o dos nodos sin color
		3) Cantidad de aristas entre dos nodos con color
		4) Diferencia entre la cantidad de nodos con el color mas usado y la cantidad con el color menos usado

chequear el sucesor a partir del choice - hacer choice de a nodo (de todo el resto de la lista) no seguir un orden, pero asegurarnos que agarramos todos
"""

GRAPH_01 = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 4), (2, 6), (3, 5), (5, 6)]


def randomGraphEdges(nodeCount=10, edgeCount=30):
    """Returns a list of `edgeCount` edges selected at random ,for a graph of
    `nodeCount` nodes.
    """
    allEdges = list(combinations(range(nodeCount), 2))
    return sample(allEdges, min(len(allEdges), edgeCount))


def nodes():
    nodes = {}
    for (x, y) in GRAPH_01:
        nodes[x] = ""
        nodes[y] = ""
    return nodes


def randomColouring(nodes, colours='RGB'):
    """Returns a random assignment of `colours` to nodes, as a dict.
    """
    return {n: choice(colours) for n in nodes}


def nodesFromEdges(edges):
    """Given a list of graph `edges`, returns the set of all nodes connected
    by said edges.
    """
    return set(sum(([x, y] for (x, y) in edges), []))


def adjacent(edges, node):
    """Returns the set of nodes connected to the given `node` according to the
    given `edges`.
    """
    return set(x if y == node else y for (x, y) in edges
               if x == node or y == node)


def colourCollisions(edges, colours):
    """Returns the `edges` that connect nodes painted with the same colour,
    according to the `colours` dict.
    """
    return set((x, y) for (x, y) in edges if colours[x] == colours[y])


def randomSearch(edges, colours='RGB', tries=1000):
    """Resolve a graph colouring problem by random search.
    """
    nodes = nodesFromEdges(edges)
    for _ in range(tries):
        colouring = randomColouring(nodes, colours)
        collisions = colourCollisions(edges, colouring)
        yield (colouring, collisions)
        if not collisions:
            break


def h1(colouring):
    """ 1) Cantidad de aristas entre dos nodos sin color
    """
    edges = 0
    for (x, y) in GRAPH_01:
        if colouring[x] == '' and colouring[y] == '':
            edges += 1
    return edges


def h2(colouring):
    """ 2) Cantidad de aristas con uno o dos nodos sin color
    """
    edges = 0
    for (x, y) in GRAPH_01:
        if colouring[x] == '' or colouring[y] == '':
            edges += 1
    return edges


def h3(colouring):
    """ 3) Cantidad de aristas entre dos nodos con color
    """
    edges = 0
    for (x, y) in GRAPH_01:
        if colouring[x] != '' and colouring[y] != '':
            edges += 1
    return edges


def h4(colouring):
    """ 4) Diferencia entre la cantidad de nodos con el color mas usado y la cantidad con el color menos usado
    """
    nodes_colour = {'R': 0, 'G': 0, 'B': 0}
    for k, v in colouring.items():
        if (v != ''):
            nodes_colour[v] += 1

    temp = sorted(nodes_colour.items(), key=lambda x: x[1], reverse=True)
    return temp[0][1] - temp[2][1]


def sucesor(nodes):
    soluciones = []
    for x, y in nodes.items():
        temp1 = nodes.copy()
        temp2 = nodes.copy()
        temp3 = nodes.copy()
        if y == '':
            temp1[x] = 'R'
            temp2[x] = 'G'
            temp3[x] = 'B'
            soluciones.extend([temp1, temp2, temp3])
    return soluciones


def colisiones(nodes):
    for x, y in nodes.items():
        for (a, b) in GRAPH_01:
            if (x == a and nodes[b] != '' and nodes[b] == y):
                return True
    return False


# (Dado un grafo no dirigido G con un conjunto de nodos N)
# (Dado un conjunto de colores C)
# (Asignar colores a nodos, tal que no haya nodos adyacentes del mismo color)
if __name__ == '__main__':
    nodes = nodes()

    soluciones = sucesor(nodes)

    if (len(soluciones) == 0):
        print('no es solución')
    else:
        for solucion_i in soluciones:
            if (colisiones(solucion_i)):
                print('hay colisiones')
            else:
                soluciones_r = sucesor(solucion_i)
