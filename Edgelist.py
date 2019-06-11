import networkx as nx
import matplotlib.pylab as plt

#a=nx.read_weighted_edgelist('/Users/Ebrahim/Desktop/Edgelist.txt')
a=nx.read_edgelist('/Users/Ebrahim/Desktop/Edgelist.txt')
print(nx.info(a,))
#nx.draw_circular(a, with_labels=True,)
#nx.draw_kamada_kawai(a, with_labels=True)
#nx.draw_planar(a, with_labels=True)
#nx.draw_spectral(a, with_labels=True)
nx.draw_random(a, with_labels=True, node_shape="*")
#nx.draw_spring(a, with_labels=True)
#nx.draw_shell(a, with_labels=True)
#nx.draw(a, with_labels=True)
#nx.draw_networkx(a, arrows=True, with_labels=True)
#nx.draw_networkx_nodes(a, pos='karachi' , nodelist=None, node_size=300, node_color='#1f78b4', node_shape='o', alpha=1.0, cmap=None, vmin=None, vmax=None, ax=None, linewidths=None, edgecolors=None, with_labels=True)

plt.show()
