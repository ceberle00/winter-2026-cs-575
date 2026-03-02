import networkx as nx
import matplotlib.pyplot as plt
import random

#L4 = nx.ladder_graph(20)
#a = nx.barabasi_albert_graph(50, 34, seed=None, initial_graph=None, create_using=None)

G = nx.barbell_graph(6, 4)
#pos = nx.nx_pydot.graphviz_layout(a,prog="neato")
#pos = nx.circular_layout(a)
#pos = nx.spring_layout(a)
node_sizes = [random.randint(300, 3000) for _ in G.nodes()]
node_colors = list(range(len(G.nodes())))
labels = {n: str(n) for n in G.nodes()}
# Draw the graph (requires Matplotlib)
#nx.draw(a, pos, with_labels=True)
#plt.show()

nx.draw(G, with_labels=True, label=labels, node_color=node_colors, node_size=node_sizes)
plt.show()