import networkx as nx
from itertools import combinations, tee, count
from scipy.optimize import linprog
import numpy as np
from math import comb

# defining a graph, used to find cliques
G = nx.read_adjlist("graph_1165.lst", nodetype=int)
G = nx.complement(G)
size = G.number_of_nodes()

# inbuilt function to find cliques, can be replaced with other algorithms.
cliques, dmy = tee(nx.find_cliques(G))

# Finding the number of cliques by burning an iterator.
numclq = sum(1 for _ in dmy)

# array for the cliques.
arr_ub = np.zeros((numclq,size + 1))


# adds a 1 if an item is in the row, and we have that the array is clique - r.
for row, clique in enumerate(cliques):
    for item in clique:
        arr_ub[row, item - 1] = 1
    arr_ub[row, size] = -1

# want to have that the sum of all edges is 1.
arr_eq = np.ones((1, size + 1))
arr_eq[0, size] = 0

# want to minimise r, the final number at the end of the list.
c = np.zeros(size + 1)
c[size] = 1

# upper bound of clique - r is 1
b_ub = np.zeros(numclq)
# sum of all vertex inflations is 1.
b_eq = [1]

# runs the linear programming problem on the array. Inbuilt assumption all values in [0, inf).
out = linprog(c, arr_ub, b_ub, arr_eq,b_eq)

print(out)
print(out.x)