import queue
from grafo import Grafo

def ucs(grafo, start, goal):
    filaPrior = queue.PriorityQueue()
    filaPrior.put((0, start))  # (custo, nó)
    caminho = {}  # caminho de onde veio
    custo = {start: 0}  # distância até a altura

    while not filaPrior.empty():  # enquanto ainda há nós a estender
        custo_atual, atual = filaPrior.get()

        if atual == goal:  # se a rua atual é o destino, reconstruir o caminho até lá
            return reconstruct_path(caminho, start, goal, custo)

        for nodeVizinho, nodeCusto in grafo.m_graph[atual]:  # se não for o destino, verificar o próximo
            novo_custo = custo_atual + nodeCusto  # atualiza custo
            if nodeVizinho not in custo or novo_custo < custo[nodeVizinho]:  # verifica se nó vizinho ainda não foi visitado anteriormente e se encontramos um caminho mais curto
                custo[nodeVizinho] = novo_custo
                priority = novo_custo
                filaPrior.put((priority, nodeVizinho))  # adiciona o novo node a filaprior
                caminho[nodeVizinho] = atual

    return None  # Não foi encontrada uma solução

def reconstruct_path(came_from, start, goal, custo):
    atual = goal
    caminhoFinal = []
    custo_total = custo[goal]  # vai servir para ter a distancia entre start e goal
    while atual != start:  # comeca atartir do fim ate chegar ao ponto de partida
        caminhoFinal.insert(0, atual)
        atual = came_from[atual]  # ve de onde o caminho onde estamos veio e atualiza como sendo o atual
    caminhoFinal.insert(0, start)  # chego ao inicio e termina o caminho
    return caminhoFinal, custo_total
