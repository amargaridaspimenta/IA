from representacaoEstado import Encomenda, obter_primeira_encomenda
from gestaoEstafetas import calcular_media_avaliacoes, atribuir_estafetas
from transporte_preco import escolher_meio_de_transporte,calcular_preco_entrega
from aStar import procura_Astar
from ucs import ucs
from bfs import bfs
from grafo import Grafo
import shutil

                                                            ##############################                                                      
                                                            #        Health Planet       #
                                                            ##############################   
                                                                                 
'''Função que permite centrar o nome da plataforma Health Planet'''
def imprimir_mensagem_centralizada(mensagem):
    print()
    largura_tela = shutil.get_terminal_size().columns
    espacos_antes = (largura_tela - len(mensagem)) // 2
    espacos_depois = largura_tela - len(mensagem) - espacos_antes

    mensagem_centralizada = ' ' * espacos_antes + mensagem + ' ' * espacos_depois
    print("\033[1m" + mensagem_centralizada + "\033[0m")  # \033[1m é o código para podermos escrever o texto em negrito


                                                            ########################
                                                            #        Ranking       #
                                                            ########################

'''Função que retorna os 5 estafetas com mais entregas'''
def top_estafetas_por_entregas(estado):
    estafetas = list(estado.estafetas.values())

    # filtra os estafetas que têm um número de entregas efetuadas válido (ou seja, != -1)
    estafetas_validos = [estafeta for estafeta in estafetas if estafeta.numero_entregas_efetuadas != -1]

    # ordena os estafetas válidos com base no número de entregas por ordem decrescente
    estafetas_ordenados = sorted(estafetas_validos, key=lambda estafeta: estafeta.numero_entregas_efetuadas, reverse=True)

    # obtém os primeiros 5 estafetas da lista ordenada
    ranking_estafetas = estafetas_ordenados[:5]

    # imprime os 5 melhores estafetas
    print("Ranking 5 melhores estafetas por número de entregas:")
    for i, estafeta in enumerate(ranking_estafetas, start=1):
        print(f"{i}. ESTAFETA: {estafeta.id_estafeta}\n Número de entregas: {estafeta.numero_entregas_efetuadas}\n")

    return ranking_estafetas

'''Função que retorna os 5 estafetas com melhor avaliação'''
def top_estafetas_por_avaliacao(estado):
    estafetas = list(estado.estafetas.values())

    # filtra os estafetas que têm pelo menos uma avaliação
    estafetas_validos = [estafeta for estafeta in estafetas if estafeta.ranking > 0]

    # ordena os estafetas válidos com base na média de avaliações por ordem decrescente
    estafetas_ordenados = sorted(estafetas_validos, key=lambda estafeta: estafeta.ranking, reverse=True)

    # obtém os primeiros 5 estafetas da lista ordenada
    ranking_estafetas = estafetas_ordenados[:5]

    # imprime os 5 melhores estafetas por avaliação
    print("Ranking 5 melhores estafetas por avaliação dos clientes:")
    for i, estafeta in enumerate(ranking_estafetas, start=1):
        print(f"{i}. ESTAFETA: {estafeta.id_estafeta}\n Média de avaliações: {estafeta.ranking:.2f}\n")

    return ranking_estafetas


                                                            ########################
                                                            #     Menu Cliente     #
                                                            ########################

def definir_tempo_maximo_e_atribuir_estafeta(estado):
    encomendas_registadas = []  # lista que armazena as encomendas registadas pelo cliente

    while True:
        informacoes_encomenda = input("Introduza: ID da encomenda, tempo máximo de entrega. (Ex: 201,10)\n")
        try:
            id, tempo_maximo = map(str.strip, informacoes_encomenda.split(','))
            id = int(id)
            tempo_maximo = int(tempo_maximo)

            if id in estado.encomendas:
                if estado.encomendas[id].prazo_entrega == -1:
                    estado.encomendas[id].prazo_entrega = tempo_maximo
                    print(f"Prazo da Encomenda {id} definido para {tempo_maximo} minutos.")
                    
                    atribuir_estafetas(estado, id)

                    encomendas_registadas.append(id)  # adiciona o id da encomenda à lista de encomendas registadas

                    estado.encomendas[id].preco_entrega = calcular_preco_entrega(estado, tempo_maximo)

                    continuar = input("Deseja inserir informações para outra encomenda? (Ex: Sim/Não): ")
                    if continuar.lower() == 'sim':
                        continue

                    visualizar = input("Deseja ver as informações de todas as encomendas registadas? (Ex: Sim/Não):")
                    if visualizar.lower() == 'sim':
                        visualizar_encomendas_cliente(estado)
                    break  
                else:
                    print("A encomenda com esse ID já tem tempo definido.\n")
                break
            else:
                print("A encomenda com esse ID não existe.\n")
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
                if estado.encomendas[id].prazo_entrega != -1:
                    if 0 <= av <= 5:  
                        estado.encomendas[id].estado_entrega = True
                        
                        atraso = input(f"Diga se a encomenda chegou dentro de {estado.encomendas[id].prazo_entrega} min. (Ex: true/false)\n")
                        
                        if atraso.lower() == "true":
                            pass

                        else:
                            av = av - 0.2
                        
                        estado.encomendas[id].avaliacao_motorista = av
                        idEstafeta = estado.encomendas[id].id_estafeta
                        estado.estafetas[idEstafeta].adicionar_avaliacao(av)

                        estado.estafetas[idEstafeta].ranking = calcular_media_avaliacoes(estado,idEstafeta)
                        estado.estafetas[idEstafeta].realizar_entrega()

                        print(estado.encomendas.get(id))
                        print(estado.estafetas[idEstafeta])
                    else:
                        print("Avaliação com valores inválidos.\n")
                else:
                    print("A encomenda com esse ID ainda não foi registada.\n")
            else:
                print("A encomenda com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")

'''Função que permite visualizar os detalhes da encomenda registada pelo cliente.'''
def visualizar_encomendas_cliente(estado):
    encomendas_registadas = [encomenda for encomenda in estado.encomendas.values() if encomenda.prazo_entrega != -1]

    if not encomendas_registadas:
        print("Não tem encomendas registadas.\n")
        return

    for encomenda in encomendas_registadas:
        print()
        print(f"INFORMAÇÕES DA ENCOMENDA {encomenda.id_encomenda}\n")

        print(f"Dados de entrega:")
        print(f"Localização Inicial: {encomenda.localizacao_inicial}")
        print(f"Localização Final: {encomenda.localizacao_final}")
        print(f"Prazo de Entrega: {encomenda.prazo_entrega} minutos")
        print(f"Preço: {encomenda.preco_entrega} euros") # só podemos ver o preço após o estafeta escolher o algoritmo que quer usar para fazer o caminho

        print(f"ID do Estafeta: {encomenda.id_estafeta}\n")
        print(f"Detalhes da encomenda:")
        print(f"Peso: {encomenda.peso} Kg")
        print(f"Volume: {encomenda.volume}")
        print(f"Estado de Entrega: {'Entregue' if encomenda.estado_entrega else 'Entrega pendente'}")
        print("-------------------------------------------")


def criar_encomenda(estado):
    while True:
        encomendaNova = input("Introduza: ID da encomenda, Localização Final, Peso, Volume. (Ex: 300,Rua da Horta Seca,10,20)\n")
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


                                                            ##############################                                                      
                                                            #      Menu do Estafeta      #
                                                            ##############################  

'''Função que permite ao estafeta efetuar o processamento da encomenda que lhe foi atribuída e após isso escolher o algoritmo que lhe irá fornecer o caminho'''
def processar_encomenda(estado_inicial, grafo_obj):
    primeiraEnc = obter_primeira_encomenda(estado_inicial)

    if primeiraEnc != -1:
        id_estafeta = input("Introduza: ID do estafeta. (Ex: 101)\n")
        try:
            id_estafeta = int(id_estafeta)

            print("Encomendas associadas ao estafeta:")
            encomendas_associadas = [encomenda for encomenda in estado_inicial.encomendas.values() if encomenda.id_estafeta == id_estafeta]
            
            if encomendas_associadas:
                for encomenda in encomendas_associadas:
                    print(encomenda)
           
    
            ############################## Escolha de algoritmo ##############################

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

            for encomenda in encomendas_associadas:
                end_node = encomenda.localizacao_final

                ################################## Procura informada A* #########################

                if algoritmo == 1:    
                    resultado_astar = procura_Astar(start_node, end_node, grafo_obj)

                    if resultado_astar is not None:
                        caminho_astar, custo_total_astar, distancia_total_astar = resultado_astar
                        print(f'Caminho de {start_node} para {end_node}: {caminho_astar}.')
                        print(f'Custo total do caminho A*: {custo_total_astar} -> Distância estimada da viagem: {distancia_total_astar} Km).')
                                    
                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_astar)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                            #preco_calculado = calcular_preco_entrega(encomenda,limite_tempo_entrega, meio_transporte)
                            #encomenda.preco_entrega = preco_calculado

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ##################################### Procura Não informada UCS ###################

                elif algoritmo == 2:
                    resultado_ucs = ucs(grafo_obj, start_node, end_node)

                    if resultado_ucs is not None:
                        caminho_ucs, distancia_total_ucs = resultado_ucs
                        print(f'Caminho de {start_node} para {end_node}: {caminho_ucs}.')
                        print(f'Distância estimada da viagem: {distancia_total_ucs} Km).')

                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_ucs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                            #preco_calculado = calcular_preco_entrega(encomenda,limite_tempo_entrega, meio_transporte)
                            #encomenda.preco_entrega = preco_calculado
                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ###################################### Procura Não informada BFS ####################        

                elif algoritmo == 3:
                    resultado_ucs = bfs(grafo_obj, start_node, end_node)

                    if resultado_ucs is not None:
                        caminho_ucs, distancia_total_ucs = resultado_ucs
                        print(f'Caminho de {start_node} para {end_node}: {caminho_ucs}.')
                        print(f'Distância estimada da viagem: {distancia_total_ucs} Km).')

                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_ucs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                            #preco_calculado = calcular_preco_entrega(encomenda,limite_tempo_entrega, meio_transporte)
                            #encomenda.preco_entrega = preco_calculado
                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')
            
        except ValueError:
            print("Formato incorreto para o ID do estafeta.\n")

    else:
            print("O estafeta com esse ID não existe.\n")


'''Função que permite ao estafeta verificar o seu perfil onde são exibidas as suas informações'''
def visualizar_perfil_estafeta(estado_inicial):
    while True:
        id_estafeta = input("Introduza: ID do estafeta. (Ex: 101)\n")
        try:
            id_estafeta = int(id_estafeta)

            if id_estafeta in estado_inicial.estafetas:
                estado_inicial.estafetas[id_estafeta].disponibilidade = True
                print(estado_inicial.estafetas.get(id_estafeta))
            else:
                print("O estafeta com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")