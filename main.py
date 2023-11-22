from representacaoEstado import inicializar_estado,obter_primeira_encomenda, associar_estafetas_encomendas
from procuraInformada import procura_Astar
from grafo import Grafo
import shutil

def imprimir_mensagem_centralizada(mensagem):
    largura_tela = shutil.get_terminal_size().columns
    espacos_antes = (largura_tela - len(mensagem)) // 2
    espacos_depois = largura_tela - len(mensagem) - espacos_antes

    mensagem_centralizada = ' ' * espacos_antes + mensagem + ' ' * espacos_depois
    print("\033[1m" + mensagem_centralizada + "\033[0m")  # \033[1m é o código para podermos escrever o texto em negrito

def main():
    saida = -1
    estado_inicial = inicializar_estado()

    associar_estafetas_encomendas(estado_inicial)

    imprimir_mensagem_centralizada("BEM-VINDO À HEALTH PLANET")

    while saida != 0:
        print("1- Definições de Cliente ")
        print("2- Informações do estafeta e encomenda")
        print("0- Sair\n")

        try:
            saida = int(input("Introduza a sua opção:\n"))
        except ValueError:
            print("Por favor, insira um valor válido.\n")
            continue 

        if saida == 0:
            print("saindo.......")

        elif saida == 1:
            print("1- Definir tempo máximo de entrega.")
            print("2- Avaliar encomenda (após recebida).")
            print("0- Voltar à página anterior.\n")

            try:
                clienteSaida = int(input("Introduza a sua opção: "))
            except ValueError:
                print("Por favor, insira um valor válido.\n")
                continue 

            if clienteSaida == 0:
                print("saindo.......")
            elif clienteSaida == 1:
                while True:
                    informacoes_encomenda = input("Introduza: ID, tempo máximo de entrega. (Ex: 201,10)\n")
                    try:
                        id,tempo_maximo = map(str.strip, informacoes_encomenda.split(','))
                        id=int(id)
                        if id in estado_inicial.encomendas:
                            estado_inicial.encomendas[id].prazo_entrega = int(tempo_maximo)
                            print(estado_inicial.encomendas.get(id))
                        else:
                            print("A encomenda com esse ID não existe.\n")
                        break
                    except (ValueError, IndexError):
                        print("Formato incorreto.\n")

            elif clienteSaida == 2:
                while True:
                    avaliacao = input("Introduza: ID da encomenda, avaliaçaão de 0 a 5. (Ex: 201,4)\n")
                    try:
                        id, av = map(str.strip, avaliacao.split(','))
                        id = int(id)
                        av = int(av)
                        if id in estado_inicial.encomendas:
                            estado_inicial.encomendas[id].estado_entrega = True  # encomenda entregue
                            estado_inicial.encomendas[id].avaliacao_motorista = av  # avaliação na encomenda

                            # Atualizar estafeta
                            idEstafeta = estado_inicial.encomendas[id].id_estafeta  # vai buscar ID do estafeta que fez a entrega
                            estafeta = estado_inicial.estafetas.get(idEstafeta)
                            if estafeta:
                                estafeta.adicionar_avaliacao(av)  # Adiciona a avaliação à lista de avaliações do estafeta
                                print(estado_inicial.encomendas.get(id))
                                print(estafeta)
                            else:
                                print("O estafeta associado a essa encomenda não existe.\n")
                        else:
                            print("A encomenda com esse ID não existe.\n")
                        break
                    except (ValueError, IndexError):
                        print("Formato incorreto.\n")

        elif saida == 2:
            while True:

                print("1- Encomenda a entregar, meio de transporte e caminho")
                print("2- Ver perfil")
                print("0- Voltar à página anterior")

                try:
                    EstafetaSaida = int(input("Introduza a sua opção: "))
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue 

                if EstafetaSaida == 0:
                    break
                elif EstafetaSaida  == 1:
                    while True:
                        primeiraEnc = obter_primeira_encomenda(estado_inicial)
                        if primeiraEnc:
                            id = input("Introduza: ID do estafeta. (Ex: 101)\n")
                            id = int(id)
                            try:

                                if id in estado_inicial.estafetas:

                                    estado_inicial.encomendas[primeiraEnc].id_estafeta = id #atualiza o etsfaeta na entrega
                                    print("A encomenda a entregar é a seguinte:")
                                    print(estado_inicial.encomendas.get(primeiraEnc))

                                    #####
                                    from meio_de_transporte import escolher_meio_de_transporte

                                    peso_encomenda = estado_inicial.encomendas[primeiraEnc].peso
                                    limite_tempo_entrega = estado_inicial.encomendas[primeiraEnc].prazo_entrega

                                    meio_transporte = escolher_meio_de_transporte(peso_encomenda, limite_tempo_entrega)

                                    if meio_transporte is not None:
                                        print(f"Meio de transporte escolhido: {meio_transporte}")
                                    else:
                                        print(f'Não foi encontrado um meio de transporte.')
                                    #####

                                    start_node = 'Largo do Barão da Quintela'
                                    end_node = estado_inicial.encomendas[primeiraEnc].localizacao_final
                                    grafo_obj = Grafo() 
                                    #grafo_obj.desenha()

                                    resultado_astar = procura_Astar(start_node, end_node, grafo_obj)

                                    if resultado_astar is not None:
                                        caminho_astar, custo_total_astar, distancia_total_astar = resultado_astar
                                        print(f'Caminho de {start_node} para {end_node}: {caminho_astar}.')
                                        print(f'Custo total do caminho A*: {custo_total_astar} -> Distância estimada da viagem: {distancia_total_astar} Km).')
                                    else:
                                        print(f'Não foi encontrado um caminho de {start_node} até {end_node}.')

                                else:
                                    print("A encomenda com esse ID não existe.\n")
                                break
                            except (ValueError, IndexError):
                                print("Formato incorreto.\n")
                        else:
                            print("Nao há encomendas a entregar.\n")

                elif EstafetaSaida  == 2:
                    while True:
                        id = input("Introduza: ID de estafeta. (Ex: 101)\n")
                        try:
                            id = int(id)
                            
                            if id in estado_inicial.estafetas:
                                print(estado_inicial.estafetas.get(id))
                            else:
                                print("O estafeta com esse ID não existe.\n")
                            break
                        except (ValueError, IndexError):
                            print("Formato incorreto.\n")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            l = input("Prima enter para continuar.")

if __name__ == "__main__":
    main()
