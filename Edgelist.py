import networkx as nx
import matplotlib.pylab as plt

#a=nx.read_weighted_edgelist('/Users/Ebrahim/Desktop/Edgelist.txt')
a=nx.read_edgelist('/Users/Ebrahim/Desktop/Edgelist.txt')
print(nx.info(a))
#nx.draw_circular(a, with_labels=True,)
#nx.draw_kamada_kawai(a, with_labels=True)
#nx.draw_planar(a, with_labels=True)
#nx.draw_spectral(a, with_labels=True)
nx.draw_random(a, with_labels=True, node_shape="o")
#nx.draw_spring(a, with_labels=True)
#nx.draw_shell(a, with_labels=True)
#nx.draw(a, with_labels=True)
#nx.draw_networkx(a, arrows=True, with_labels=True)

plt.show()
