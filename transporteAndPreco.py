
                                                                #############################
                                                                #    Transporte e Preço     #
                                                                #############################

'''Função que escolhe o meio de transporte mais adequado tendo em conta a distância e o peso do da encomenda'''
def escolher_meio_de_transporte(peso, limite_tempo_entrega, distancia):

    # Velocidades médias dos meios de transporte
    velocidade_media_bicicleta = 10  # Km/h
    velocidade_media_mota = 35  # Km/h
    velocidade_media_carro = 50  # Km/h

    # Penalidades de velocidade para cada meio de transporte
    penalidade_bicicleta = 0.6  # Km/h por cada Kg
    penalidade_mota = 0.5  # Km/h por cada Kg
    penalidade_carro = 0.1  # Km/h por cada Kg

    # Calcular a velocidade ajustada para cada meio de transporte
    velocidade_bicicleta = velocidade_media_bicicleta - (penalidade_bicicleta * peso)
    velocidade_mota = velocidade_media_mota - (penalidade_mota * peso)
    velocidade_carro = velocidade_media_carro - (penalidade_carro * peso)

     # Converter o tempo de horas para minutos 
    tempo_estimado_bicicleta = (distancia / velocidade_bicicleta) * 60  
    tempo_estimado_mota = (distancia / velocidade_mota) * 60  
    tempo_estimado_carro = (distancia / velocidade_carro) * 60  

    if peso <= 5:
        if tempo_estimado_bicicleta <= limite_tempo_entrega:
            return "Bicicleta"
        if tempo_estimado_mota <= limite_tempo_entrega:
            return "Mota"
        else: 
            return "Carro"
    elif peso <= 20:
        if tempo_estimado_mota <= limite_tempo_entrega:
            return "Mota"
        else:
            return "Carro"
    elif peso <= 100:  
        if tempo_estimado_carro <= limite_tempo_entrega:
            return "Carro"

    return "Rever a rota ou o meio de transporte." # caso seja inserido um prazo de tempo inapropriado por exemplo


'''Função que calcula o preço de entrega de uma encomenda em função do meio de transporte e prazo definidos.'''
def calcular_preco_entrega(encomenda, prazo_entrega, meio_transporte):
    preco_base = 5  # preço base da entrega

    # fator de prazo
    fator_prazo = 1.2 if int(prazo_entrega) <= 60 else 1.0

    #  fator de transporte
    if meio_transporte == 'Bicicleta':
        fator_transporte = 1.0 # 
    elif meio_transporte == 'Mota':
        fator_transporte = 1.1
    elif meio_transporte == 'Carro':
        fator_transporte = 1.2

    # preço final
    preco_final = round(preco_base * fator_prazo * fator_transporte, 2)

    return preco_final
