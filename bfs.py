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
            return reconstruct_path(caminho, start, goal, custo)

        for nodeVizinho, nodeCusto in grafo.m_graph[atual]:  # se não for o destino, verificar o próximo
            novo_custo = custo[atual] + nodeCusto  # atualiza custo
            if nodeVizinho not in custo or novo_custo < custo[nodeVizinho]:  # verifica se nó vizinho ainda não foi visitado anteriormente e se encontramos um caminho mais curto
                custo[nodeVizinho] = novo_custo
                fila.put(nodeVizinho)  # adiciona o novo nó à fila
                caminho[nodeVizinho] = atual

    return None  # Não foi encontrada uma solução

def imprimir_caminho_parcial(came_from, start, atual):
    caminho_parcial = reconstruct_parcial_path(came_from, start, atual)
    print(f'Caminho parcial: {caminho_parcial}')

def reconstruct_parcial_path(came_from, start, atual):
    caminho_parcial = []  # começa com a lista vazia

    while atual != start: # enquanto o nó atual for diferente do nó de partida
        caminho_parcial.insert(0, atual) # insere o nó atual no início da lista (constrói o caminho ao contrário)
        atual = came_from[atual] # atualiza o nó atual para o nó a partir do qual foi alcançado

    caminho_parcial.insert(0, start) # adiciona o nó de partida ao início da lista para completar o caminho
    return caminho_parcial # retorna o caminho 

def reconstruct_path(came_from, start, goal, custo):
    atual = goal
    caminho_final = []
    custo_total = custo[goal]  # vai servir para ter a distância entre start e goal
    while atual != start:  # começa do fim até chegar ao ponto de partida
        caminho_final.insert(0, atual)
        atual = came_from[atual]  # ve de onde o caminho onde estamos veio e atualiza como sendo o atual
    caminho_final.insert(0, start)  # chego ao início e termina o caminho
    return caminho_final, custo_total
