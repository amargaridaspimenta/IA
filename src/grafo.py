import networkx as nx
import matplotlib.pyplot as plt

                                                                    #####################
                                                                    #    Grafo Manual   #
                                                                    #####################

class Grafo:
    def __init__(self):
        self.m_nodes = [
            'Travessa do Carmo',
            'Rua do Alecrim',
            'Travessa Guilherme Cossoul',
            'Rua da Horta Sêca',
            'Rua da Emenda',
            'Rua das Chagas',
            'Rua do Ataíde'
        ]
        self.m_graph = {
            'Travessa do Carmo': [('Rua do Alecrim', 5), ('Travessa Guilherme Cossoul', 3)],
            'Rua do Alecrim': [('Rua da Horta Sêca', 20), ('Rua do Ataíde', 1.5)],
            'Rua da Emenda': [('Rua da Horta Sêca', 3), ('Travessa Guilherme Cossoul', 2), ('Rua do Ataíde', 3.5)],
            'Rua da Horta Sêca': [('Rua das Chagas', 17), ('Rua da Emenda', 3)],
            'Rua das Chagas': [('Travessa Guilherme Cossoul', 3), ('Rua do Ataíde', 14)],
            'Travessa Guilherme Cossoul': [('Rua da Emenda', 2)],
            'Rua do Ataíde': []
        }

    # desenha no grafo que fizemos o caminho percorrido pelos algoritmos ucs, bfs e dijkstra
    def desenha(self, caminho, start_node, end_node):
        g = nx.Graph()

        for node in self.m_nodes:
            g.add_node(node)
            for (adjacente, peso) in self.m_graph[node]:
                g.add_edge(node, adjacente, weight=peso)

        pos = nx.spring_layout(g, seed=39)

        plt.figure(figsize=(12, 8))

        # desenha todos os nós e arestas
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold', node_size=800, node_color='skyblue')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        # destaca o caminho percorrido em vermelho
        edges = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
        nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='red', width=2)

        plt.title(f"Mapa da Freguesia da Misericórdia (Lisboa) - Caminho de {start_node} para {end_node}")
        plt.show()

    # desenha o grafo sem caminho
    def desenha_ruas(self):
        g = nx.Graph()

        for node in self.m_nodes:
            g.add_node(node)
            for (adjacente, peso) in self.m_graph[node]:
                g.add_edge(node, adjacente, weight=peso)

        pos = nx.spring_layout(g, seed=39)

        plt.figure(figsize=(12, 8))

        # desenha todos os nós e arestas
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold', node_size=800, node_color='skyblue')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.title("Mapa da Freguesia da Misericórdia (Lisboa)")
        plt.show()


