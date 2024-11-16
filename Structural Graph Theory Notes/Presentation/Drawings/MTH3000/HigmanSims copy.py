import networkx as nx
from itertools import combinations, tee, count
from scipy.optimize import linprog
import numpy as np
from math import comb

# defining a graph, used to find cliques
G = nx.read_graph6("graph_1165.g6")
G = nx.complement(G)
size = G.number_of_nodes()

print(nx.greedy_color(G, strategy='DSATUR', interchange=False))