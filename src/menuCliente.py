from representacaoEstado import Encomenda
from gestaoEstafetas import calcular_media_avaliacoes, atribuir_estafetas


                                                                    ########################
                                                                    #     Menu Cliente     #
                                                                    ########################

def definir_tempo_e_atribuir_estafeta(estado):
    encomendas_registadas = []  # lista que armazena as encomendas registadas pelo cliente

    while True:
        informacoes_encomenda = input("Introduza: ID da encomenda, tempo máximo de entrega. (Ex: 201,10m ou 201,2h ou 201,1h30m)\n")
        try:
            id, tempo_maximo = map(str.strip, informacoes_encomenda.split(',')) # separa a string na vírgula e armazena os seus valores no id e tempo máximo
            id = int(id)

            horas = 0
            minutos = 0

            # verifica se 'h' existe e tira as horas
            if 'h' in tempo_maximo:
                horas_str, resto = tempo_maximo.split('h')
                horas = int(horas_str)

                # verifica se 'm' existe e tira os minutos
                if 'm' in resto:
                    minutos = int(resto.replace('m', ''))

            elif 'm' in tempo_maximo:
                # se tem apenas 'm', tira os minutos diretamente
                minutos = int(tempo_maximo.replace('m', ''))
            else:
                print("Formato inválido. Se pretende registar uma encomenda, insira novamente um tempo com horas e/ou minutos.")
                break

            tempo_maximo_total = horas * 60 + minutos

            if id in estado.encomendas:
                if estado.encomendas[id].prazo_entrega == -1 or estado.encomendas[id].prazo_entrega == 0: # prazo de entrega igual a 0 para quando se cria uma encomenda
                    estado.encomendas[id].prazo_entrega = tempo_maximo_total
                    print(f"Prazo da Encomenda {id} definido para {tempo_maximo_total} minutos.")

                    atribuir_estafetas(estado, id)

                    encomendas_registadas.append(id)  # adiciona o ID da encomenda à lista de encomendas registadas

                    #estado.encomendas[id].preco_entrega = calcular_preco_entrega(estado, tempo_maximo_total)

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
                        print(f"ESTAFETA {idEstafeta}")
                        print(f"Avaliação Atribuída ao Estafeta: {av}")
                        print(f"Avaliações dos Clientes: {estado.estafetas[idEstafeta].avaliacoes}")
                        print(f"Avaliação Total: {estado.estafetas[idEstafeta].ranking}")
                        print(f"Número de Entregas Realizadas: {estado.estafetas[idEstafeta].numero_entregas_efetuadas}")
                        print("------------------------------------------")
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

        if encomenda.prazo_entrega > 60:
            # converte minutos para horas e minutos para o caso de querermos tipo em 1h e 30min (=100min)
            horas, minutos = divmod(encomenda.prazo_entrega, 60)
            print(f"Prazo de Entrega: {horas} horas e {minutos} minutos")
        else:
            print(f"Prazo de Entrega: {encomenda.prazo_entrega} minutos")

        print(f"Preço: {encomenda.preco_entrega} euros")

        print(f"ID do Estafeta: {encomenda.id_estafeta}\n")
        print(f"Detalhes da encomenda:")
        print(f"Peso: {encomenda.peso} Kg")
        print(f"Volume: {encomenda.volume}")
        print(f"Estado de Entrega: {'Entregue' if encomenda.estado_entrega else 'Entrega pendente'}")
        print("-------------------------------------------")


def criar_encomenda(estado):
    # obtem o último ID de encomenda existente no estado
    ultimo_id = max(estado.encomendas.keys(), default=0)

    # incrementa o último ID para obter o próximo ID disponível
    novo_id = ultimo_id + 1

    while True:
        encomendaNova = input("Introduza: Localização Final, Peso, Volume. (Ex: Rua da Horta Sêca,10,20)\n")
        try:
            localizacao_final, peso, volume = map(str.strip, encomendaNova.split(','))
            peso = int(peso)
            volume = int(volume)
            
            # atualiza a informação da nova encomenda criada
            nova_encomenda = Encomenda(
                id_encomenda=novo_id,
                localizacao_inicial='Travessa do Carmo',
                localizacao_final=localizacao_final,
                peso=peso,
                volume=volume,
                prazo_entrega=0,
                estado_entrega=False,
                id_estafeta=-1,
                avaliacao_motorista=None,
                preco_entrega=None
            )

            # imprime a nova encomenda
            estado.encomendas[novo_id] = nova_encomenda
            print(estado.encomendas.get(novo_id))
            break

        except (ValueError, IndexError):
            print("Formato incorreto.\n")


