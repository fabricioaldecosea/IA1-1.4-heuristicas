from random import sample, choice
from itertools import combinations

GRAPH_01 = [(0,1), (0,2), (1,2), (1,6), (2,4), (2,6), (3,5), (5,6)]

def randomGraphEdges(nodeCount=10, edgeCount=30):
	"""Returns a list of `edgeCount` edges selected at random ,for a graph of 
	`nodeCount` nodes.
	"""
	allEdges = list(combinations(range(nodeCount), 2))
	return sample(allEdges, min(len(allEdges), edgeCount))

def randomColouring(nodes, colours='RGB'):
	"""Returns a random assignment of `colours` to nodes, as a dict.
	"""
	return {n: choice(colours) for n in nodes}
	
def nodesFromEdges(edges):
	"""Given a list of graph `edges`, returns the set of all nodes connected 
	by said edges.
	"""
	return set(sum(([x,y] for (x,y) in edges), []))

def adjacent(edges, node):
	"""Returns the set of nodes connected to the given `node` according to the
	given `edges`.
	"""
	return set(x if y == node else y for (x,y) in edges 
		if x == node or y == node)
	
def colourCollisions(edges, colours):
	"""Returns the `edges` that connect nodes painted with the same colour, 
	according to the `colours` dict.
	"""
	return set((x,y) for (x,y) in edges if colours[x] == colours[y])

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

if __name__ == '__main__':
	print("Graph colouring with random search with graph %s" % GRAPH_01)
	step = 1
	for (colouring, collisions) in randomSearch(GRAPH_01):
		print("\t%d: %s\t%d collisions found." % (step, colouring, len(collisions)))
		step = step + 1
	if collisions:
		print("No solution found!")
	else:
		print("Solution: %s" % colouring)