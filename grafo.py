import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.m_nodes = [
            'Largo do Barão da Quintela',
            'Rua do Alecrim',
            'Travessa Guilherme Cossoul',
            'Rua da Horta Seca',
            'Rua da Emenda',
            'Rua de Chagas',
            'Rua de Ataíde'
        ]
        self.m_graph = {
            'Largo do Barão da Quintela': [('Rua do Alecrim', 5), ('Travessa Guilherme Cossoul', 3)],
            'Rua do Alecrim': [('Rua da Horta Seca', 20), ('Rua de Ataíde', 1.5)],
            'Rua da Emenda': [('Rua da Horta Seca', 3), ('Travessa Guilherme Cossoul', 2), ('Rua de Ataíde', 3.5)],
            'Rua da Horta Seca': [('Rua de Chagas', 17), ('Rua da Emenda', 3)],
            'Rua de Chagas': [('Travessa Guilherme Cossoul', 3), ('Rua de Ataíde', 14)],
            'Travessa Guilherme Cossoul': [],
            'Rua de Ataíde': []
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

        plt.title("Mapa da Freguesia da Misericórdia (Lisboa)")
        plt.show()
