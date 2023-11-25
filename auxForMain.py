from representacaoEstado import Encomenda, obter_primeira_encomenda
from aStar import procura_Astar
from ucs import ucs
from bfs import bfs
from grafo import Grafo
import shutil
from meio_de_transporte import escolher_meio_de_transporte

def imprimir_mensagem_centralizada(mensagem):
    largura_tela = shutil.get_terminal_size().columns
    espacos_antes = (largura_tela - len(mensagem)) // 2
    espacos_depois = largura_tela - len(mensagem) - espacos_antes

    mensagem_centralizada = ' ' * espacos_antes + mensagem + ' ' * espacos_depois
    print("\033[1m" + mensagem_centralizada + "\033[0m")  # \033[1m é o código para podermos escrever o texto em negrito


################### Menu do cliente - Funções Auxiliares #############################################################################


def definir_tempo_maximo(estado):
    while True:
        informacoes_encomenda = input("Introduza: ID, tempo máximo de entrega. (Ex: 201,10)\n")
        try:
            id, tempo_maximo = map(str.strip, informacoes_encomenda.split(','))
            id = int(id)
            tempo_maximo=int(tempo_maximo)
            if id in estado.encomendas:
                if tempo_maximo !=-1:
                    estado.encomendas[id].prazo_entrega = tempo_maximo
                    print(estado.encomendas.get(id))
                else:
                   print("A encomenda com esse ID ja tem tempo definido.\n") 
            else:
                print("A encomenda com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")

def avaliar_encomenda(estado):
    while True:
        avaliacao = input("Introduza: ID da encomenda, avaliação de 0 a 5. (Ex: 201,4)\n")
        try:
            id, av = map(str.strip, avaliacao.split(','))
            id = int(id)
            av = float(av)
            if id in estado.encomendas:

                estado.encomendas[id].estado_entrega = True
                atraso = input("Diga se a encomenda chegou dentro de "+ str(estado.encomendas[id].prazo_entrega) +"min. (Ex: true)\n")
                
                if atraso.lower() == "true":
                    av= av-0.2
                estado.encomendas[id].avaliacao_motorista = av
                idEstafeta = estado.encomendas[id].id_estafeta
                estado.estafetas[idEstafeta].adicionar_avaliacao(av)
                estado.estafetas[idEstafeta].ranking = estado.estafetas[idEstafeta].calcular_media_avaliacoes()
                print(estado.encomendas.get(id))
                print(estado.estafetas[idEstafeta])
            else:
                print("A encomenda com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")

def criar_encomenda(estado):
    while True:
        encomendaNova = input("Introduza: id_encomenda, localizacao_final, peso, volume. (Ex: 300,Rua da Horta Seca,10,20)\n")
        try:
            id_encomenda, localizacao_final, peso, volume = map(str.strip, encomendaNova.split(','))
            id_encomenda = int(id_encomenda)
            peso = int(peso)
            volume = int(volume)
            if id_encomenda not in estado.encomendas:
                nova_encomenda=Encomenda(id_encomenda, 'Largo do Barão da Quintela', localizacao_final, peso, volume, -1, False, -1, None)
                estado.encomendas[id_encomenda] = nova_encomenda
                print(estado.encomendas.get(id_encomenda))
            else:
                print("A encomenda com esse ID já esta registada.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")


################### Menu do estafeta - Funções Auxiliares #############################################################################


def processar_encomenda(estado_inicial,grafo_obj):

    primeiraEnc = obter_primeira_encomenda(estado_inicial)
    # atribuir_encomendas_aleatoriamente(estado_inicial, seed=42)

    if primeiraEnc:
        id_estafeta = input("Introduza: ID do estafeta. (Ex: 101)\n")
        try:
            id_estafeta = int(id_estafeta)
            if id_estafeta in estado_inicial.estafetas:
                 
                if estado_inicial.encomenda.prazo_entrega == -1:
                    print("Esta encomenda não pode ser processada porque o prazo de entrega não foi definido.\n")
                    return

                estado_inicial.encomendas[primeiraEnc].id_estafeta = id_estafeta
                print("A encomenda a entregar é a seguinte:")
                print(estado_inicial.encomendas.get(primeiraEnc))

                ############################## Escolha de algoritmo ########################

                print("Escolhe o algoritmo a usar:\n")
                print("1- Procura informada A*.")
                print("2- Procura não informada UCS.")
                print("3- Procura não informada BSF.\n")

                try:
                    algoritmo = int(input("Introduza a sua opção: "))
                except ValueError:
                    print("Por favor, insira um valor válido.\n")
                    return

                start_node = 'Largo do Barão da Quintela'
                end_node = estado_inicial.encomendas[primeiraEnc].localizacao_final
                #grafo_obj = Grafo()

                ################################## Procura informada A* #########################

                if algoritmo == 1:
                    resultado_astar = procura_Astar(start_node, end_node, grafo_obj)

                    if resultado_astar is not None:
                        caminho_astar, custo_total_astar, distancia_total_astar = resultado_astar
                        print(f'Caminho de {start_node} para {end_node}: {caminho_astar}.')
                        print(f'Custo total do caminho A*: {custo_total_astar} -> Distância estimada da viagem: {distancia_total_astar} Km).')
                                    
                        peso_encomenda = estado_inicial.encomendas[primeiraEnc].peso
                        limite_tempo_entrega = estado_inicial.encomendas[primeiraEnc].prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_astar)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")
                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')
                    

                ################################################# Procura Não informada UCS #####################

                elif algoritmo == 2:
                    resultado_ucs = ucs(grafo_obj, start_node, end_node)

                    if resultado_ucs is not None:
                        caminho_ucs, distancia_total_ucs = resultado_ucs
                        print(f'Caminho de {start_node} para {end_node}: {caminho_ucs}.')
                        print(f'Distância estimada da viagem: {distancia_total_ucs} Km).')

                        peso_encomenda = estado_inicial.encomendas[primeiraEnc].peso
                        limite_tempo_entrega = estado_inicial.encomendas[primeiraEnc].prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_ucs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")
                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ################################################# Procura Não informada BFS #####################        

                elif algoritmo == 3:
                    resultado_ucs = bfs(grafo_obj, start_node, end_node)

                    if resultado_ucs is not None:
                        caminho_ucs, distancia_total_ucs = resultado_ucs
                        print(f'Caminho de {start_node} para {end_node}: {caminho_ucs}.')
                        print(f'Distância estimada da viagem: {distancia_total_ucs} Km).')

                        peso_encomenda = estado_inicial.encomendas[primeiraEnc].peso
                        limite_tempo_entrega = estado_inicial.encomendas[primeiraEnc].prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_ucs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")
                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

            else:
                print("O estafeta com esse ID não existe.\n")
        except (ValueError, IndexError):
            print("Formato incorreto.\n")
    else:
        print("Não há encomendas a entregar.\n")

def visualizar_perfil_estafeta(estado_inicial):
    while True:
        id_estafeta = input("Introduza: ID do estafeta. (Ex: 101)\n")
        try:
            id_estafeta = int(id_estafeta)

            if id_estafeta in estado_inicial.estafetas:
                print(estado_inicial.estafetas.get(id_estafeta))
            else:
                print("O estafeta com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")
