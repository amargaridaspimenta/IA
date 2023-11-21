import heapq
from grafo import Grafo

# Defina a variável global custo_total_astar
custo_total_astar = 0

def heuristica_distancia_estimada(node, end, grafo):
    distancia_estimada = abs(len(grafo.m_graph[node]) - len(grafo.m_graph[end]))
    return distancia_estimada

# Procura usando o algoritmo A*
def procura_Astar(start, end, graf):

    # EXPLICAÇÃO PARA A  VARIÁVEL "global custo_total_astar"

    # Em Python, quando usamos uma variável dentro de uma função e tentamos atribuir-lhe um valor num escopo local, o interpretador assume que a variável é local 
    # a menos que seja explicitamente declarada como global. 
    # Portanto, ao fazer a atribuição dentro do loop (while), a variável é reconhecida como local.

    global custo_total_astar  
    custo_total = 0  # Inicializa a

    heap = [(0, 0, start, [])]  # a heap é uma fila de prioridade
    visitados = set()

    while heap:  # enquanto existem elementos na heap
        # custo total estimado, o custo acumulado até o momento, o nó atual e o caminho percorrido até agora
        (custo_total, distancia_acumulada, no_atual, caminho) = heapq.heappop(heap)  # nó com menor custo é retirado e vizinhos são explorados

        if no_atual in visitados:
            continue

        # se o nó ainda não foi visitado, adicionamos ao caminho principal e marcamos como visitado    
        caminho = caminho + [no_atual]
        visitados.add(no_atual)

        # quando o nó atual é o nó de destino
        if no_atual == end:
            custo_total_astar = custo_total  # Atribuímos o valor ao global custo_total_astar
            return (caminho, custo_total, distancia_acumulada)

        for (adjacente, custo) in graf.m_graph[no_atual]:  # para cada vizinho do nó atual calculamos o novo custo, somando o custo acumulado até agora e o custo da aresta até o vizinho
            if adjacente not in visitados:
                novo_custo = custo_total + custo
                heuristica = heuristica_distancia_estimada(adjacente, end, graf)  # calculamos a heurística
                heapq.heappush(heap, (novo_custo + heuristica, novo_custo, adjacente, caminho))  # adicionamos o novo vizinho à fila

    return None  # Se nenhum caminho for encontrado
   