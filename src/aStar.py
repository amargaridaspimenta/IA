import heapq
from grafoInterativo import GrafoOSMx
from geopy.distance import geodesic

def obter_coordenadas(grafo, node):
    if 'coords' in grafo.graph.nodes[node]: # verifica se o nó tem coordenadas
        coords = grafo.graph.nodes[node]['coords']
        if coords is not None and isinstance(coords, tuple) and len(coords) == 2: # verifica se as coordenadas sao um tuplo com dois valores
            # converte coordenadas para metros, como a distancia é relativamente pequena, faz se a aproximaçao plana 
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

def procura_Astar(grafo, nome_rua_inicio, nome_rua_fim):
    aresta_inicio = grafo.obter_aresta_por_nome_rua(nome_rua_inicio)
    aresta_fim = grafo.obter_aresta_por_nome_rua(nome_rua_fim)

    if aresta_inicio is None or aresta_fim is None:
        print(f"Aresta de início ou fim não encontrada.")
        return [], None, None

    no_inicio = aresta_inicio[0]
    no_fim = aresta_fim[1]

    heap = [(0, 0, no_inicio, [no_inicio])]
    visitados = set()
    caminho_completo = None
    nos_expandidos = 0

    while heap:
        (custo_estimado, custo_acumulado, no_atual, caminho) = heapq.heappop(heap)

        if no_atual in visitados:   
            continue

        visitados.add(no_atual)
        nos_expandidos += 1

        if no_atual == no_fim:
            custo_total_astar = custo_acumulado + heuristica(no_atual, no_fim, grafo)
            caminho_completo = (caminho, custo_total_astar)
            break

        for (origem, destino, data) in grafo.graph.edges(no_atual, data=True):
            adjacente = destino
            custo = data['length']

            if adjacente not in visitados:
                novo_custo_acumulado = custo_acumulado + custo
                heuristica_valor = heuristica(adjacente, no_fim, grafo)
                novo_custo_estimado = novo_custo_acumulado + heuristica_valor
                novo_caminho = list(caminho)
                novo_caminho.append(adjacente)

                heapq.heappush(heap, (novo_custo_estimado, novo_custo_acumulado, adjacente, novo_caminho))
    
    print()
    print(f"Número de nós expandidos: {nos_expandidos}")

    if caminho_completo is not None:
        caminho, custo_total_astar = caminho_completo
        nomes_ruas = obter_nomes_ruas_caminho(grafo, caminho)
        return caminho, custo_total_astar, nomes_ruas
    else:
        return None, None, None

def obter_nomes_ruas_caminho(grafo, caminho):
    nomes_ruas = []

    for i in range(len(caminho) - 1):
        no_atual = caminho[i]
        no_proximo = caminho[i + 1]

        if grafo.graph.has_edge(no_atual, no_proximo):
            aresta_data = grafo.graph[no_atual][no_proximo]

            if 'name' in aresta_data[0]:
                nome_rua = aresta_data[0]['name']

                if isinstance(nome_rua, str) and nome_rua not in nomes_ruas:
                    nomes_ruas.append(nome_rua)
            else: None

    return nomes_ruas

# endereço da freguesia da Misericórdia em Lisboa
endereco = "Freguesia da Misericordia, Lisbon, Portugal"
grafo = GrafoOSMx(endereco)

start_node = "Rua Garret"
end_node = "Rua da Emenda"

'''caminho_astar, custo_total_astar, nomes_ruas_astar = procura_Astar(grafo, start_node, end_node)
if caminho_astar is not None:
    distancia_km_astar = round(custo_total_astar / 1000.0, 2)
    print("Caminho encontrado pelo A*:")
    print(nomes_ruas_astar)
    print("Custo Total:", distancia_km_astar)
else:
    print("Nenhum caminho encontrado pelo A*.")'''
