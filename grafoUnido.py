from grafo import Grafo
from grafo2 import Grafo2
import networkx as nx
import matplotlib.pyplot as plt

class GrafoUnido(Grafo, Grafo2):
    def __init__(self):
        super().__init__()

    def desenha(self):
        # Cria uma instância única de nx.Graph para representar todos os grafos
        g_unido = nx.Graph()

        # Adiciona nós e arestas do Grafo1
        for nodo in self.m_nodes:
            g_unido.add_node(nodo)
            for (adjacente, peso) in self.m_graph[nodo]:
                g_unido.add_edge(nodo, adjacente, weight=peso)

        # Adiciona nós e arestas do Grafo2
        for nodo in self.m_nodes:
            for (adjacente, peso) in self.m_graph[nodo]:  # Use m_graph do Grafo2
                g_unido.add_edge(nodo, adjacente, weight=peso)

        # Adiciona ruas de conexão
        rua_conexao_1 = [('Rua do Alecrim', 'Rua Garrett', 5)]
        
        g_unido.add_weighted_edges_from(rua_conexao_1)

        # Desenha o grafo unido
        pos_unido = nx.spring_layout(g_unido, seed=39)
        plt.figure(figsize=(12, 8))
        nx.draw_networkx(g_unido, pos_unido, with_labels=True, font_weight='bold', node_size=800, node_color='skyblue')
        labels_unido = nx.get_edge_attributes(g_unido, 'weight')
        nx.draw_networkx_edge_labels(g_unido, pos_unido, edge_labels=labels_unido)
        plt.title("Mapa Unido")
        plt.show()

