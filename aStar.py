import heapq
from grafo import Grafo

custo_total_astar = 0

def heuristica_distancia_estimada(node, end, grafo):
    distancia_estimada = abs(len(grafo.m_graph[node]) - len(grafo.m_graph[end]))
    return distancia_estimada

"""
Função que implementa o algoritmo A* para encontrar o caminho mais curto entre dois nós em um grafo.

    Parametros:
    - start (str): Nó de início.
    - end (str): Nó de destino.
    - graf (Grafo): Contém as informações do grafo.

"""
def procura_Astar(start, end, graf):

    # EXPLICAÇÃO PARA A  VARIÁVEL "global custo_total_astar"

    # Em Python, quando usamos uma variável dentro de uma função e tentamos atribuir-lhe um valor num escopo local, o interpretador assume que a variável é local 
    # a menos que seja explicitamente declarada como global. 
    # Portanto, ao fazer a atribuição dentro do loop (while), a variável é reconhecida como local.
    global custo_total_astar
    custo_total = 0

    heap = [(0, 0, start, [])] # Inicializa a fila de prioridade (heap) com o nó de início
    visitados = set() # Conjunto dos nós visitados

    """
    uasamos uma fila de prioridade (heap) para explorar os nós com os menores custos estimados primeiro

    """
    while heap:
        (custo_estimado, custo_acumulado, no_atual, caminho) = heapq.heappop(heap) # remove e retorna o menor elemento da heap a ser explorado

        if no_atual in visitados:
            continue # Ignora os nós que já foram visitados

        # Atualiza o caminho e visita o nó como visitado
        caminho = caminho + [no_atual]
        visitados.add(no_atual) 

        # Se o nó atual é o destino, calcula o custo total e retorna o caminho
        if no_atual == end:
            custo_total_astar = custo_acumulado + heuristica_distancia_estimada(no_atual, end, graf)
            return (caminho, custo_total_astar, custo_acumulado)

        # Verifica os nós vizinhos
        for (adjacente, custo) in graf.m_graph[no_atual]:

            """
            Em cada iteração do loop, a função vai explorar os vizinhos do nó atual. Se um nó vizinho ainda não foi visitado, são calculados os novos custos e é 
            criada uma nova entrada para a heap. 
            O caminho parcial é atualizado ao adicionar o nó vizinho ao final do caminho existente.

            """
            # Se os nós adjacentes não estiverem nos visitados este calcula os novos custos e cria uma nova entrada para a heap
            if adjacente not in visitados:
                novo_custo_acumulado = custo_acumulado + custo # soma do custo acumulado atual com o custo da aresta para o vizinho
                heuristica = heuristica_distancia_estimada(adjacente, end, graf) # resultado da heurística para o vizinho até o destino
                novo_custo_estimado = novo_custo_acumulado + heuristica 
                novo_caminho = caminho + [adjacente] # adiciona vizinho ao caminho atual
                heapq.heappush(heap, (novo_custo_estimado, novo_custo_acumulado, adjacente, novo_caminho)) # adiciona elemento à heap

                print(f"Caminho parcial: {novo_caminho}")

    return None # Retorna None se nenhum caminho é encontrado
