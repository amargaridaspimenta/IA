                                                                #############################
                                                                #    Gestão dos Estafetas   #
                                                                #############################

'''Função auxiliar para atribuir os estafetas tendo em conta as encomendas mais prioritárias.'''
def atribuir_estafetas_com_prioridade(estado):

    encomendas_com_prazo = [encomenda for encomenda in estado.encomendas.values() if encomenda.prazo_entrega != -1]

    if not estado.estafetas or not encomendas_com_prazo:
        print("Não há estafetas ou encomendas com prazo disponíveis.")
        return

    criterio_prioridade = lambda encomenda: encomenda.prazo_entrega # priorizamos encomendas com menos tempo de entrega
    encomendas_ordenadas = sorted(encomendas_com_prazo, key=criterio_prioridade) # ordena as encomendas por ordem crescente de prazo de entrega

    idx_estafeta = 0 # inicializa id do estafeta para conseguirmos ir acedendo a partir da lista aos estafetas
    max_estafetas = len(estado.estafetas) # número de estafetas que temos)

    while encomendas_ordenadas: # vai executar enquanto existem encomendas
        encomenda = encomendas_ordenadas.pop(0) # obtém a primeira encomenda da lista ordenada, ou seja, a mais prioritária

        # Verifica se ainda existem estafetas disponíveis para atribuir encomendas
        if idx_estafeta < max_estafetas:
            estafeta_atual = estado.estafetas[sorted(estado.estafetas.keys())[idx_estafeta]]

            # calcula o tempo de entrega (ida e volta ao centro) para o estafeta
            tempo_entrega = calcular_tempo_entrega(estafeta_atual, encomenda)

            # atribuímos o estafeta à encomenda
            encomenda.id_estafeta = estafeta_atual.id_estafeta
            estafeta_atual.disponibilidade = False
            # este print é para ver como é feita a atribuiçao dos estafetas e ver se a prioridade é respeitada
            print(f"A encomenda {encomenda.id_encomenda} está atribuída ao Estafeta {encomenda.id_estafeta}.")

            # incrementamos para o próximo estafeta
            idx_estafeta += 1

            # se esgotarmos todos os estafetas, reiniciamos a disponibilidade deles para True 
            if idx_estafeta == max_estafetas:
                for estafeta in estado.estafetas.values():
                    # antes de reiniciar, verificamos se o estafeta está disponível e se o prazo de entrega da encomenda é menor que o tempo de entrega
                    if estafeta.disponibilidade or encomenda.prazo_entrega < tempo_entrega:
                        # se sim, atualizamos a disponibilidade para True
                        estafeta.disponibilidade = True
                idx_estafeta = 0
        else:
            print("Não há mais estafetas disponíveis.")
            break


'''Função que atribui estafetas apenas a encomendas cujo prazo de entrega já esteja definido.'''
def atribuir_estafetas(estado, encomenda_id):

    if estado.encomendas[encomenda_id].prazo_entrega != -1:
        atribuir_estafetas_com_prioridade(estado)
    else:
        print(f"O prazo de entrega para a Encomenda {encomenda_id} não foi definido.\n")


'''Função auxiliar para atribuir os estafetas com base no tempo total do seu serviço.'''
def calcular_tempo_entrega(estafeta, encomenda):
    prazo_encomenda = encomenda.prazo_entrega
    # tempo médio de entrega e volta ao centro de distribuição
    tempo_entrega = (prazo_encomenda * 2) + 5   

    return tempo_entrega


'''Função que calcula a avaliação média dos estafetas com base nas avaliações a si atribuídas.'''
def calcular_media_avaliacoes(estado, id):
    avaliacoes = estado.estafetas[id].avaliacoes

    if not avaliacoes:
        return -1  # valor padrão para quando não há avaliações

    return sum(avaliacoes) / len(avaliacoes)

