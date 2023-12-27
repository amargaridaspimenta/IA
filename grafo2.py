import networkx as nx
import matplotlib.pyplot as plt

class Grafo2:
    def __init__(self):
        self.m_nodes = [
            'Rua Serpa Pinto',
            'Rua Garrett',
            'Rua Anchieta',
            'Rua Capelo',
            'Baixa-Chiado',
            'Rua Vitor Cordon',
            'Rua António Maria Cardoso'
        ]
        self.m_graph = {
            'Rua Serpa Pinto': [('Rua Garrett', 11), ('Rua Vitor Cordon', 14)],
            'Rua Garrett': [('Rua Capelo', 6), ('Rua Anchieta', 3), ('Rua António Maria Cardoso', 7)],
            'Rua Anchieta': [('Rua Capelo', 4)],
            'Rua Capelo': [('Baixa-Chiado', 5), ('Rua Serpa Pinto', 4)],
            'Baixa-Chiado': [('Rua António Maria Cardoso', 7)],
            'Rua Vitor Cordon': [('Rua Anchieta', 12)],
            'Rua António Maria Cardoso': []
        }

    def desenha(self):
        lista_v = self.m_nodes
        g = nx.Graph()

        for nodo in lista_v:
            n = nodo
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g, seed=39)  
        
        plt.figure(figsize=(12, 8))  
        
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold', node_size=800, node_color='skyblue')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.title("Mapa da Freguesia de Santa Maria Maior (Lisboa)")
        plt.show()

