import queue
from grafo import Grafo

def bfs(grafo, start, goal):
    fila = queue.Queue()
    fila.put(start)  # adiciona o nó inicial à fila
    caminho = {}  # caminho de onde veio
    custo = {start: 0}  # distância até o nó

    while not fila.empty():  # enquanto ainda há nós a estender
        atual = fila.get()

        # Adiciona chamada de função para imprimir o caminho parcial
        imprimir_caminho_parcial(caminho, start, atual)

        if atual == goal:  # se o nó atual é o destino, reconstruir o caminho até lá
            return reconstruir_caminho(caminho, start, goal, custo)

        for nodeVizinho, nodeCusto in grafo.m_graph[atual]:  # se não for o destino, verificar o próximo
            novo_custo = custo[atual] + nodeCusto  # atualiza custo
            if nodeVizinho not in custo or novo_custo < custo[nodeVizinho]:  # verifica se nó vizinho ainda não foi visitado anteriormente e se encontramos um caminho mais curto
                custo[nodeVizinho] = novo_custo
                fila.put(nodeVizinho)  # adiciona o novo nó à fila
                caminho[nodeVizinho] = atual

    return None  # não foi encontrada uma solução

def imprimir_caminho_parcial(came_from, start, atual):
    caminho_parcial = reconstruir_caminho_parcial(came_from, start, atual)
    print(f'Caminho parcial: {caminho_parcial}')

def reconstruir_caminho_parcial(came_from, inicio, atual):
    # inicializa a lista do caminho parcial
    caminho_parcial = []

    # reconstrói o caminho parcial começando do nó atual até o nó de início
    while atual != inicio:
        caminho_parcial.append(atual)
        atual = came_from[atual]

    # adiciona o nó de início ao final da lista e reverte para ter o caminho na ordem correta
    caminho_parcial.append(inicio)
    caminho_parcial.reverse()

    return caminho_parcial

def reconstruir_caminho(came_from, inicio, objetivo, custo):
    # inicializa o nó atual como o objetivo
    atual = objetivo

    # inicializa a lista do caminho final
    caminho_final = []

    # inicializa o custo total como o custo associado ao objetivo
    custo_total = custo[objetivo]

    # reconstrói o caminho final começando do nó objetivo até o nó de início
    while atual != inicio:
        caminho_final.append(atual)
        atual = came_from[atual]

    # adiciona o nó de início ao final da lista e reverte para ter o caminho na ordem correta
    caminho_final.append(inicio)
    caminho_final.reverse()

    return caminho_final, custo_total

