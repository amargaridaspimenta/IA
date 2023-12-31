import queue
from grafo import Grafo

def ucs(grafo, start, goal):
    filaPrior = queue.PriorityQueue()
    filaPrior.put((0, start))  # (custo, nó)
    caminho = {}  # caminho de onde veio
    custo = {start: 0}  # distância até a altura

    while not filaPrior.empty():  # enquanto ainda há nós a estender
        custo_atual, atual = filaPrior.get()
        #print(f"Nó: {atual}, Custo: {custo_atual}")

        if atual == goal:  # se a rua atual é o destino, reconstruir o caminho até lá
            return reconstruir_caminho(caminho, start, goal, custo)

        for nodeVizinho, nodeCusto in grafo.m_graph[atual]:  # se não for o destino, verificar o próximo
            novo_custo = custo_atual + nodeCusto  # atualiza custo
            if nodeVizinho not in custo or novo_custo < custo[nodeVizinho]:  # verifica se nó vizinho ainda não foi visitado anteriormente e se encontramos um caminho mais curto
                custo[nodeVizinho] = novo_custo
                priority = novo_custo
                filaPrior.put((priority, nodeVizinho))  # adiciona o novo node a filaprior
                caminho[nodeVizinho] = atual

                # Adiciona o caminho parcial até chegar ao caminho final
                caminho_parcial = reconstruir_caminho_parcial(caminho, start, nodeVizinho)
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
def reconstruir_caminho_parcial(came_from, inicio, atual):
    caminho_parcial = []  # começa com a lista vazia

    while atual != inicio:  # enquanto o nó atual for diferente do nó de partida
        caminho_parcial.insert(0, atual)  # insere o nó atual no início da lista (constrói o caminho ao contrário)
        atual = came_from[atual]  # atualiza o nó atual para o nó a partir do qual foi alcançado

    caminho_parcial.insert(0, inicio)  # adiciona o nó de partida ao início da lista para completar o caminho
    return caminho_parcial  # retorna o caminho


def reconstruir_caminho(came_from, inicio, objetivo, custo):
    atual = objetivo
    caminho_final = []
    custo_total = custo[objetivo]  # vai servir para ter a distância entre início e objetivo
    while atual != inicio:  # começa do fim até chegar ao ponto de partida
        caminho_final.insert(0, atual)
        atual = came_from[atual]  # vê de onde o caminho onde estamos veio e atualiza como sendo o atual
    caminho_final.insert(0, inicio)  # chego ao início e termina o caminho
    return caminho_final, custo_total
