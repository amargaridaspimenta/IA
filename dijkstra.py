import heapq
from grafo import Grafo

def procura_dijkstra(graf, inicio, fim):
    heap = [(0, inicio, [])]
    visitados = set()

    while heap:
        (custo_acumulado, no_atual, caminho) = heapq.heappop(heap)

        if no_atual in visitados:
            continue

        caminho = caminho.copy()  
        caminho.append(no_atual)  

        visitados.add(no_atual)

        if no_atual == fim:
            print(f'Caminho parcial: {caminho}')
            return caminho, custo_acumulado

        for (adjacente, custo) in graf.m_graph[no_atual]:
            if adjacente not in visitados:
                novo_custo_acumulado = custo_acumulado + custo
                heapq.heappush(heap, (novo_custo_acumulado, adjacente, caminho))

                print(f'Caminho parcial: {caminho + [adjacente]}')

    return None
