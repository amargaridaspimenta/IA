import queue
from grafo import Grafo

def bfs(grafo, start, goal):
    fila = queue.Queue()
    fila.put(start)  # adiciona o nó inicial à fila
    caminho = {}  # caminho de onde veio
    custo = {start: 0}  # distância até o nó

    while not fila.empty():  # enquanto ainda há nós a estender
        atual = fila.get()

        if atual == goal:  # se o nó atual é o destino, reconstruir o caminho até lá
            return reconstruct_path(caminho, start, goal, custo)

        for nodeVizinho, nodeCusto in grafo.m_graph[atual]:  # se não for o destino, verificar o próximo
            novo_custo = custo[atual] + nodeCusto  # atualiza custo
            if nodeVizinho not in custo or novo_custo < custo[nodeVizinho]:  # verifica se nó vizinho ainda não foi visitado anteriormente e se encontramos um caminho mais curto
                custo[nodeVizinho] = novo_custo
                fila.put(nodeVizinho)  # adiciona o novo nó à fila
                caminho[nodeVizinho] = atual

    return None  # Não foi encontrada uma solução

def reconstruct_path(came_from, start, goal, custo):
    atual = goal
    caminhoFinal = []
    custo_total = custo[goal]  # vai servir para ter a distância entre start e goal
    while atual != start:  # começa do fim até chegar ao ponto de partida
        caminhoFinal.insert(0, atual)
        atual = came_from[atual]  # ve de onde o caminho onde estamos veio e atualiza como sendo o atual
    caminhoFinal.insert(0, start)  # chego ao início e termina o caminho
    return caminhoFinal, custo_total
