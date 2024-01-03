
from transporteAndPreco import escolher_meio_de_transporte, calcular_preco_entrega
from grafoInterativo import GrafoOSMx
from grafo import Grafo
from aStar import procura_Astar, obter_nomes_ruas_caminho
from dijkstra import procura_dijkstra
from greedy import procura_Greedy
from ucs import ucs
from bfs import bfs


                                                                ##############################                                                      
                                                                #      Menu do Estafeta      #
                                                                ##############################  

'''Função que permite ao estafeta efetuar o processamento da encomenda que lhe foi atribuída e após isso escolher o algoritmo que lhe irá fornecer o caminho'''
def processar_encomenda(estado_inicial, grafo_obj, grafo_objx):

        id_estafeta = input("Introduza: ID do estafeta. (Ex: 101)\n")
        id_estafeta = int(id_estafeta)

        if not (101 <= id_estafeta <= 109):
            print("Formato incorreto. Insira um valor válido.")

        else: 
            print("Encomendas associadas ao estafeta:")
            encomendas_associadas = [encomenda for encomenda in estado_inicial.encomendas.values() if encomenda.id_estafeta == id_estafeta]
            
            if encomendas_associadas:
                for encomenda in encomendas_associadas:
                    print(encomenda)           
    
            ############################## Escolha de algoritmo ##############################

            print("Escolhe o algoritmo a usar:\n")
            print("1- Procura Informada A*.")
            print("2- Procura Informada Greedy.")
            print("3- Procura Não Informada UCS.")
            print("4- Procura Não Informada BSF.")
            print("5- Procura Dijkstra.\n")

            try:
                algoritmo = int(input("Introduza a sua opção: "))
            except ValueError:
                print("Por favor, insira um valor válido.\n")
                return
            
            start_node = 'Travessa do Carmo'

            for encomenda in encomendas_associadas:
                end_node = encomenda.localizacao_final

                ################################## Procura informada A* #########################

                if algoritmo == 1:    
                    # resultado_astar: caminho_completo = procura_Astar(grafo, nome_rua_inicio, nome_rua_fim)
                    resultado_astar = procura_Astar(grafo_objx, start_node, end_node)

                    if resultado_astar is not None:
                        caminho_astar, custo_total_astar, distancia_total_astar = resultado_astar
                        distancia_km_astar = round(custo_total_astar / 1000.0, 2)

                        ruas_caminho = obter_nomes_ruas_caminho(grafo_objx, caminho_astar)

                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{ruas_caminho}')
                        print()
                        print(f'Custo total do caminho A*: {custo_total_astar}')
                        print(f'Distância estimada da viagem: {distancia_km_astar} Km')

                        grafo_objx.desenha(caminho_astar, start_node, end_node)
                                    
                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_km_astar)
                        
                        encomenda.preco_entrega = calcular_preco_entrega(encomenda, limite_tempo_entrega, meio_transporte)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ##################################### Procura Informada Greedy ###################
                        
                if algoritmo == 2:    
                    # resultado_astar: caminho_completo = procura_Astar(grafo, nome_rua_inicio, nome_rua_fim)
                    resultado_greedy = procura_Greedy(grafo_objx, start_node, end_node)

                    if resultado_greedy is not None:
                        caminho_greedy, custo_total_greedy, ruas_caminho = resultado_greedy
                        distancia_km_greedy = round(custo_total_greedy / 1000.0, 2)

                        ruas_caminho = obter_nomes_ruas_caminho(grafo_objx, caminho_greedy)

                        print()
                        print(f'Caminho de {start_node} para {end_node}:')
                        print(f'{ruas_caminho}')
                        print()
                        print(f'Custo total do caminho Greedy: {custo_total_greedy}')
                        print(f'Distância estimada da viagem: {distancia_km_greedy} Km')

                        grafo_objx.desenha(caminho_greedy, start_node, end_node)
                                    
                        peso_encomenda = encomenda.peso
                        limite_tempo_entrega = encomenda.prazo_entrega

                        meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_km_greedy)

                        encomenda.preco_entrega = calcular_preco_entrega(encomenda, limite_tempo_entrega, meio_transporte)

                        if meio_transporte is not None:
                            print(f"Meio de transporte escolhido: {meio_transporte}")

                        else:
                            print(f'Não foi encontrado um meio de transporte.')
                    else:
                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ##################################### Procura Não informada UCS ###################        

                elif algoritmo == 3:
                    # Verifica se o end_node está na lista 
                    end_nodes = [
                        'Rua do Alecrim',
                        'Travessa Guilherme Cossoul',
                        'Rua da Horta Sêca',
                        'Rua da Emenda',
                        'Rua das Chagas',
                        'Rua do Ataíde'
                    ]

                    if end_node not in end_nodes:
                        print(f'O nó de destino {end_node} não é permitido para este algoritmo.')
                    else:
                        resultado_ucs = ucs(grafo_obj, start_node, end_node)

                        if resultado_ucs is not None:
                            caminho_ucs, distancia_total_ucs = resultado_ucs
                            distancia_km_ucs = round(distancia_total_ucs / 1000.0, 2)
                    
                            print()
                            print(f'Caminho de {start_node} para {end_node}:')
                            print(f'{caminho_ucs}')
                            print()
                            print(f'Distância estimada da viagem: {distancia_km_ucs} Km')

                            grafo_obj.desenha(caminho_ucs, start_node, end_node)

                            peso_encomenda = encomenda.peso
                            limite_tempo_entrega = encomenda.prazo_entrega

                            meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_km_ucs)

                            encomenda.preco_entrega = calcular_preco_entrega(encomenda, limite_tempo_entrega, meio_transporte)

                            if meio_transporte is not None:
                                print(f"Meio de transporte escolhido: {meio_transporte}")
                            else:
                                print(f'Não foi encontrado um meio de transporte.')
                        else:
                            print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')


                ###################################### Procura Não informada BFS ####################        

                elif algoritmo == 4:
                    # Verifica se o end_node está na lista 
                    end_nodes = [
                        'Rua do Alecrim',
                        'Travessa Guilherme Cossoul',
                        'Rua da Horta Sêca',
                        'Rua da Emenda',
                        'Rua das Chagas',
                        'Rua do Ataíde'
                    ]

                    if end_node not in end_nodes:
                        print(f'O nó de destino {end_node} não é permitido para este algoritmo.')
                    else:
                        resultado_bfs = bfs(grafo_obj, start_node, end_node)

                        if resultado_bfs is not None:
                            caminho_bfs, distancia_total_bfs = resultado_bfs
                            distancia_km_bfs = round(distancia_total_bfs / 1000.0, 2)
                            print()
                            print(f'Caminho de {start_node} para {end_node}:')
                            print(f'{caminho_bfs}')
                            print()
                            print(f'Distância estimada da viagem: {distancia_km_bfs} Km')

                            grafo_obj.desenha(caminho_bfs, start_node, end_node)

                            peso_encomenda = encomenda.peso
                            limite_tempo_entrega = encomenda.prazo_entrega

                            meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_km_bfs)

                            encomenda.preco_entrega = calcular_preco_entrega(encomenda, limite_tempo_entrega, meio_transporte)

                            if meio_transporte is not None:
                                print(f"Meio de transporte escolhido: {meio_transporte}")

                            else:
                                print(f'Não foi encontrado um meio de transporte.')
                        else:
                            print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                ###################################### Procura Dijkstra ####################

                elif algoritmo == 5:
                    # Verifica se o end_node está na lista 
                    end_nodes = [
                        'Rua do Alecrim',
                        'Travessa Guilherme Cossoul',
                        'Rua da Horta Sêca',
                        'Rua da Emenda',
                        'Rua das Chagas',
                        'Rua do Ataíde'
                    ]

                    if end_node not in end_nodes:
                        print(f'O nó de destino {end_node} não é permitido para este algoritmo.')
                    else:
                        resultado_dijkstra = procura_dijkstra(grafo_obj, start_node, end_node)

                        if resultado_dijkstra is not None:
                            caminho_dijkstra, distancia_total_dijkstra = resultado_dijkstra
                            distancia_km_dijkstra = round(distancia_total_dijkstra / 1000.0, 2)

                            print()
                            print(f'Caminho de {start_node} para {end_node}:')
                            print(f'{caminho_dijkstra}')
                            print()
                            print(f'Distância estimada da viagem: {distancia_km_dijkstra} Km')

                            grafo_obj.desenha(caminho_dijkstra, start_node, end_node)

                            peso_encomenda = encomenda.peso
                            limite_tempo_entrega = encomenda.prazo_entrega

                            meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega, distancia_km_dijkstra)

                            encomenda.preco_entrega = calcular_preco_entrega(encomenda, limite_tempo_entrega, meio_transporte)

                            if meio_transporte is not None:
                                print(f"Meio de transporte escolhido: {meio_transporte}")

                            else:
                                print(f'Não foi encontrado um meio de transporte.')
                        else:
                            print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')


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