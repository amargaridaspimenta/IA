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

                # Adiciona o caminho parcial até chegar ao caminho final
                caminho_parcial = reconstruct_parcial_path(caminho, start, nodeVizinho)
                print(f"Caminho parcial: {caminho_parcial}")

    return None  # Não foi encontrada uma solução



"""
    Reconstrói o caminho parcial a partir de um dicionário de caminhos, começando do nó 'start' até o nó 'atual' 

    Parâmetros:
    - came_from (dict): Um dicionário que mapeia cada nó para o nó do qual foi alcançado durante a procura
    - start: é nó de partida
    - atual: é nó até o qual queremos reconstruir o caminho parcial 

    Retorna:
    - caminho_parcial (list): Uma lista que representa o caminho parcial do nó 'start' até 'atual'.
"""
def reconstruct_parcial_path(came_from, start, atual):
    caminho_parcial = [] # começa com a lista vazia

    while atual != start: # enquanto o nó atual for diferente do nó de partida
        caminho_parcial.insert(0, atual) # insere o nó atual no início da lista (constrói o caminho ao contrário)
        atual = came_from[atual] # atualiza o nó atual para o nó a partir do qual foi alcançado

    caminho_parcial.insert(0, start) # adiciona o nó de partida ao início da lista para completar o caminho
    return caminho_parcial # retorna o caminho 

def reconstruct_path(came_from, start, goal, custo):
    atual = goal
    caminhoFinal = []
    custo_total = custo[goal]  # vai servir para ter a distancia entre start e goal
    while atual != start:  # comeca atartir do fim ate chegar ao ponto de partida
        caminhoFinal.insert(0, atual)
        atual = came_from[atual]  # ve de onde o caminho onde estamos veio e atualiza como sendo o atual
    caminhoFinal.insert(0, start)  # chego ao inicio e termina o caminho
    return caminhoFinal, custo_total
