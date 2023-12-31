import heapq
from grafoInterativo import GrafoOSMx
from geopy.distance import geodesic

# A Greedy escolhe o caminho que parece mais promissor apenas com base na heurística

def obter_coordenadas(grafo, node):
    if 'coords' in grafo.graph.nodes[node]: # verifica se o nó tem coordenadas
        coords = grafo.graph.nodes[node]['coords']
        if coords is not None and isinstance(coords, tuple) and len(coords) == 2: # verifica se as coordenadas sao um tuplo com dois valores
            # converte coordenadas para metros, como a distancia é relativamente pequena, faz se a aproximaçao plana usando geodesic que é mais realista
            coords_meters = (geodesic((0, coords[1]), (0, 0)).meters, geodesic((coords[0], 0), (0, 0)).meters)
            return coords_meters
    return None

def heuristica(start, end, grafo):
    coords_start = obter_coordenadas(grafo, start) # obtem coordenadas em metros do no de inicio 
    coords_end = obter_coordenadas(grafo, end) # obtem coordenadas em metros do no final

    if coords_start is None or coords_end is None:
        return 0

    # calcula a distância euclidiana entre os pontos
    distancia_euclidiana = ((coords_end[0] - coords_start[0])**2 + (coords_end[1] - coords_start[1])**2)**0.5

    #print(f"Heurística entre {start} e {end}: {distancia_euclidiana} metros")

    return distancia_euclidiana

def procura_Greedy(grafo, nome_rua_inicio, nome_rua_fim):
    aresta_inicio = grafo.obter_aresta_por_nome_rua(nome_rua_inicio)
    aresta_fim = grafo.obter_aresta_por_nome_rua(nome_rua_fim)

    if aresta_inicio is None or aresta_fim is None:
        print(f"Aresta de início ou fim não encontrada.")
        return [], None, None

    no_inicio = aresta_inicio[0]
    no_fim = aresta_fim[1]

    #print(f"Coordenadas do nó de início ({no_inicio}): {obter_coordenadas(grafo, no_inicio)}")
    #print(f"Coordenadas do nó de fim ({no_fim}): {obter_coordenadas(grafo, no_fim)}")

    heap = [(0, no_inicio, [no_inicio])]
    visitados = set()
    caminho_completo = None
    nos_expandidos = 0

    while heap:
        (custo_estimado, no_atual, caminho) = heapq.heappop(heap)

        if no_atual in visitados:
            continue

        visitados.add(no_atual)
        nos_expandidos += 1

        if no_atual == no_fim:
            custo_total_greedy = custo_estimado  # Use o custo estimado como custo total
            caminho_completo = (caminho, custo_total_greedy)
            break

        for (origem, destino, data) in grafo.graph.edges(no_atual, data=True):
            adjacente = destino
            custo = data['length']

            if adjacente not in visitados:
                heuristica_calculada = heuristica(adjacente, no_fim, grafo)
                novo_custo_estimado = custo + heuristica_calculada  # considera o custo acumulado

                # print(f"Heurística Valor: {heuristica_calculada}")

                heapq.heappush(heap, (novo_custo_estimado, adjacente, caminho + [adjacente]))

    print()
    print(f"Número de nós expandidos: {nos_expandidos}")

    if caminho_completo is not None:
        caminho, custo_total_greedy = caminho_completo
        nomes_ruas = obter_nomes_ruas_caminho(grafo, caminho)
        return caminho, custo_total_greedy, nomes_ruas
    else:
        return None, None, None

def obter_nomes_ruas_caminho(grafo, caminho):
    nomes_ruas = []

    # itera sobre os nós do caminho
    for i in range(len(caminho) - 1):
        no_atual = caminho[i]
        no_proximo = caminho[i + 1]
        aresta_data = grafo.graph[no_atual][no_proximo] # acessa o dicionário de dados associado à aresta entre os nós

        # tira o nome da rua da aresta_data
        nome_rua = aresta_data[0]['name'] if 'name' in aresta_data[0] else None # extrai o nome da rua (se existir) a partir do dicionario de dados 

        # adiciona o nome da rua apenas se nao estiver na lista
        if isinstance(nome_rua, str) and nome_rua not in nomes_ruas: # isinstance garante que à lista sao adicionadas strs  
            nomes_ruas.append(nome_rua)

    return nomes_ruas

endereco = "Freguesia da Misericordia, Lisbon, Portugal"
grafo = GrafoOSMx(endereco)

'''start_node = "Rua Garret"
end_node = "Rua da Emenda"
caminho_greedy, custo_total_greedy, nomes_ruas_greedy = procura_Greedy(grafo, start_node, end_node)
ruas_caminho = obter_nomes_ruas_caminho(grafo, caminho_greedy)

if caminho_greedy is not None:
    print("Caminho encontrado pelo Greedy:")
    print(nomes_ruas_greedy)
    print("Custo Total:", custo_total_greedy)
    #print("Caminho:", caminho_greedy) # dá só os ids das ruas

else:
    print("Nenhum caminho encontrado pelo Greedy.")'''
