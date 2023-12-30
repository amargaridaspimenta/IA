import osmnx as ox
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

                                                                #################################
                                                                #    Grafo (Biblioteca OSMNX)   #
                                                                #################################

class GrafoOSMx:
    def __init__(self, address):
        self.graph = ox.graph_from_address(address, network_type="drive") # network_type="drive" indica que vai exibir a rede de vias para direção de carro

        for node, data in self.graph.nodes(data=True):
            data['coords'] = (data['y'], data['x'])
    
        # exibe o nome das ruas
        nomes_ruas = set()
        for origem, destino, data in self.graph.edges(data=True):
            if 'name' in data:
                if isinstance(data['name'], list):
                    # se 'name' for uma lista, adiciona o primeiro elemento
                    nomes_ruas.add(data['name'][0])
                else:
                    # se nao for uma lista adiciona o valor da chave 'name'
                    nomes_ruas.add(data['name'])

    # retorna a aresta que contém o nome da rua especificado
    # percorre todas as arestas do grafo e verifica se o nome da rua especificado está presente nos dados da aresta
    def obter_aresta_por_nome_rua(self, nome_rua):
        # obtém a aresta que contém o nome da rua
        for origem, destino, data in self.graph.edges(data=True): 
            if 'name' in data and isinstance(data['name'], str) and str(nome_rua) in data['name']:
                return origem, destino, data # retorna a origem, o destino e os dados da aresta se o nome existir

        # print(f"Nenhuma aresta encontrada para a rua: {nome_rua}")
        return None

    # converte uma lista de nomes de ruas em uma lista de ids de arestas correspondentes    
    def converter_nomes_rua_para_ids(self, nomes_ruas):
        ids_caminho = []

        for i in range(len(nomes_ruas) - 1):
            nome_rua_atual = nomes_ruas[i]
            nome_rua_proximo = nomes_ruas[i + 1]

            # obtem a aresta correspondente ao nome da rua atual
            aresta_atual = self.obter_aresta_por_nome_rua(nome_rua_atual) 
            if aresta_atual:
                no_inicio = aresta_atual[0]

                # obtem a aresta correspondente ao nome da rua próximo
                aresta_proximo = self.obter_aresta_por_nome_rua(nome_rua_proximo)
                if aresta_proximo:
                    no_fim = aresta_proximo[1]

                    # Encontrar a aresta correspondente
                    aresta = self.graph[no_inicio][no_fim]

                    if aresta:
                        # adicionar todas as arestas entre os nós, pois o caminho pode não ser uma única aresta
                        for origem, destino, data in aresta.values():
                            if 'osmid' in data: # osmid é o openstreet map identifier e verifica se está presente na info da aresta
                                if isinstance(data['osmid'], list): # verifica se é uma lista ou valor
                                    ids_caminho.extend(map(str, data['osmid'])) # se for lista extende a lista com valores convertidos
                                else:
                                    ids_caminho.append(str(data['osmid'])) # se for valor mete na lista

        return ids_caminho

    # esta funçao desenha o grafo com os caminhos percorridos pela astar e pela greedy
    def desenha(self, caminho, start_node, end_node, figsize=(12, 12)):
            if not self.graph:
                print("O grafo não foi criado corretamente.")
                return

            # criar um grafo direcionado a partir do grafo original
            G = nx.DiGraph(self.graph)

            # adicionar atributos de cor para o caminho obtido pelo algoritmo
            edge_colors = ['red' if (origem, destino) in zip(caminho, caminho[1:]) else 'black' for origem, destino in G.edges()]

            # obtem as posições dos nós para o desenho
            pos = {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}

            # desenha o grafo
            fig, ax = plt.subplots(figsize=figsize)
            nx.draw(G, pos, node_size=0, with_labels=False, edge_color=edge_colors, node_color='black', arrows=False, alpha=0.7)

            # adicionaa o nome dos nós
            nx.draw_networkx_labels(G, pos, {caminho[0]: start_node, caminho[-1]: end_node}, font_size=10, font_color='blue')

            # adiciona um título e desenha o grafo
            plt.title(f"Mapa da Freguesia da Misericórdia (Lisboa) - Caminho de {start_node} para {end_node}")
            plt.show()

    # esta função desenha o mapa total sem caminhos
    def desenha_freguesia(self, figsize=(12, 12)):
        if not self.graph:
            print("O grafo não foi criado corretamente.")
            return

        # criar um grafo direcionado a partir do grafo original
        G = nx.DiGraph(self.graph)

        # obtem as posições dos nós para o desenho
        pos = {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}

        # desenha o grafo
        fig, ax = plt.subplots(figsize=figsize)
        nx.draw(G, pos, node_size=0, with_labels=False, edge_color='black', node_color='black', arrows=False, alpha=0.7)

        # adiciona um título e desenha o grafo
        plt.title(f"Mapa da Freguesia da Misericórdia (Lisboa)")
        plt.show()


# endereço da nossa localidade
endereco = "Freguesia da Misericórdia, Lisboa"
grafo = GrafoOSMx(endereco)

# exibe informações sobre as arestas do grafo
for origem, destino, data in grafo.graph.edges(data=True):
    # mantem a unidade de medida em metros (custo = distancia)
    data['length_m'] = data['length']

