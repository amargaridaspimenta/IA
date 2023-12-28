from representacaoEstado import obter_primeira_encomenda
from transporteAndPreco import escolher_meio_de_transporte
from aStar import procura_Astar
from dijkstra import procura_dijkstra
from ucs import ucs
from bfs import bfs


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
            print("3- Procura não informada BSF.")
            print("4- Procura Dijkstra.\n")

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
                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{caminho_astar}')
                        print()
                        print(f'Custo total do caminho A*: {custo_total_astar}')
                        print(f'Distância estimada da viagem: {distancia_total_astar} Km).')
                                    
                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_astar)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ##################################### Procura Não informada UCS ###################

                elif algoritmo == 2:
                    resultado_ucs = ucs(grafo_obj, start_node, end_node)

                    if resultado_ucs is not None:
                        caminho_ucs, distancia_total_ucs = resultado_ucs
                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{caminho_ucs}')
                        print()
                        print(f'Distância estimada da viagem: {distancia_total_ucs} Km).')

                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_ucs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ###################################### Procura Não informada BFS ####################        

                elif algoritmo == 3:
                    resultado_bfs = bfs(grafo_obj, start_node, end_node)

                    if resultado_bfs is not None:
                        caminho_bfs, distancia_total_bfs = resultado_bfs
                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{caminho_bfs}')
                        print()
                        print(f'Distância estimada da viagem: {distancia_total_bfs} Km).')

                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_bfs)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ###################################### Procura Dijkstra ####################

                elif algoritmo == 4:
                    resultado_dijkstra = procura_dijkstra(grafo_obj, start_node, end_node)

                    if resultado_dijkstra is not None:
                        caminho_dijkstra, distancia_total_dijkstra = resultado_dijkstra
                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{caminho_dijkstra}')
                        print()
                        print(f'Distância estimada da viagem: {distancia_total_dijkstra} Km).')

                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_total_dijkstra)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

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
                print(estado_inicial.estafetas.get(id_estafeta))
            else:
                print("O estafeta com esse ID não existe.\n")
            break
        except (ValueError, IndexError):
            print("Formato incorreto.\n")