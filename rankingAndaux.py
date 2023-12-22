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