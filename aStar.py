import heapq
from grafo import Grafo

custo_total_astar = 0

"""
def heuristica_distancia_estimada(node, end, grafo):
    vizinhos_node = set(vizinho for vizinho, _ in grafo.m_graph[node])
    vizinhos_end = set(vizinho for vizinho, _ in grafo.m_graph[end])
    
    vizinhos_comuns = len(vizinhos_node.intersection(vizinhos_end))
    
    heuristica = vizinhos_comuns
    return heuristica
"""

def heuristica_combinada(node, end, grafo):
    
    vizinhos_node = set(vizinho for vizinho, _ in grafo.m_graph[node])
    vizinhos_end = set(vizinho for vizinho, _ in grafo.m_graph[end])

    #Calcula a quantidade de vizinhos comuns entre o nó atual e o nó de destino.
    vizinhos_comuns = len(vizinhos_node.intersection(vizinhos_end))

    #Calcula a diferença na quantidade total de vizinhos entre o nó atual e o nó de destino.
    distancia_estimada = abs(len(grafo.m_graph[node]) - len(grafo.m_graph[end]))

    #a heuristica é feita atraves de uma combinacao de duas heuristica em q ambas vao ter o mesmo peso 
    heuristica = (vizinhos_comuns + distancia_estimada) / 2 #Valor combinado das duas heurísticas.
    
    return heuristica



def procura_Astar(start, end, graf):
    global custo_total_astar
    custo_total = 0

    heap = [(0, 0, start, [])]
    visitados = set()

    while heap:
        (custo_estimado, custo_acumulado, no_atual, caminho) = heapq.heappop(heap)

        if no_atual in visitados:
            continue

        caminho = caminho + [no_atual]
        visitados.add(no_atual) 

        if no_atual == end:
            custo_total_astar = custo_acumulado + heuristica_combinada(no_atual, end, graf)
            return (caminho, custo_total_astar, custo_acumulado)

        for (adjacente, custo) in graf.m_graph[no_atual]:
            if adjacente not in visitados:
                novo_custo_acumulado = custo_acumulado + custo
                heuristica = heuristica_combinada(adjacente, end, graf)
                novo_custo_estimado = novo_custo_acumulado + heuristica 
                novo_caminho = caminho + [adjacente]
                heapq.heappush(heap, (novo_custo_estimado, novo_custo_acumulado, adjacente, novo_caminho))

                print(f"Caminho parcial: {novo_caminho}")

    return None