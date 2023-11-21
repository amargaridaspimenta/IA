class Estado:
    def __init__(self, estafetas, encomendas):
        self.estafetas = {estafeta.id_estafeta: estafeta for estafeta in estafetas}
        self.encomendas = {encomenda.id_encomenda: encomenda for encomenda in encomendas}

    def __str__(self):
        estafetas_estado = "\n".join(str(estafeta) for estafeta in self.estafetas.values())
        encomendas_estado = "\n".join(str(encomenda) for encomenda in self.encomendas.values())
        return f"Estafetas:\n{estafetas_estado}\nEncomendas:\n{encomendas_estado}"

class Estafeta:
    def __init__(self, id_estafeta, localizacao_estafeta, avaliacao):
        self.id_estafeta = id_estafeta
        self.localizacao_estafeta = localizacao_estafeta
        self.avaliacao = avaliacao 

    def __str__(self):
        return f"ESTAFETA {self.id_estafeta}\n Localização: {self.localizacao_estafeta}\n Avaliação: {self.avaliacao}"

class Encomenda:
    def __init__(self, id_encomenda, localizacao_inicial, localizacao_final, peso, prazo_entrega, estado_entrega,id_estafeta, avaliacao_motorista): 
        self.id_encomenda = id_encomenda
        self.localizacao_inicial = localizacao_inicial
        self.localizacao_final = localizacao_final
        self.peso = peso
        self.prazo_entrega = prazo_entrega
        self.estado_entrega = estado_entrega
        self.id_estafeta = id_estafeta
        self.avaliacao_motorista = avaliacao_motorista

    def __str__(self):
        return f"ENCOMENDA {self.id_encomenda}\n Localização Inicial: {self.localizacao_inicial}\n Localização Final: {self.localizacao_final}\n Peso: {self.peso}\n Prazo: {self.prazo_entrega}\n Estado Entrega: {self.estado_entrega}\n ID do Motorista: {self.id_estafeta}\n Avaliação: {self.avaliacao_motorista}"

def inicializar_estado():
    estafetas = [
        Estafeta(id_estafeta=101, localizacao_estafeta='Largo do Barão da Quintela', avaliacao=None),
        Estafeta(id_estafeta=102, localizacao_estafeta='Largo do Barão da Quintela', avaliacao=None),
    ]

    encomendas = [
        Encomenda(id_encomenda=201, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=8, prazo_entrega=20, estado_entrega=False, id_estafeta=101, avaliacao_motorista=None),
        Encomenda(id_encomenda=202, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=15, prazo_entrega=30, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    ]

    return Estado(estafetas=estafetas, encomendas=encomendas)

def obter_primeira_encomenda(estado):
    # Obtém um iterador para a lista de encomendas
    iterador_encomendas = iter(estado.encomendas.values())
    try:
        # Obtém a primeira encomenda da lista
        primeira_encomenda = next(iterador_encomendas)
        return primeira_encomenda.id_encomenda
    except StopIteration:
        # Lida com o caso em que a lista de encomendas está vazia
        print("Não há encomendas disponíveis.")
        return None



#estado_inicial = inicializar_estado()

# Uso da função para obter a primeira encomenda
#primeira_encomenda = obter_primeira_encomenda(estado_inicial)

# Imprime a primeira encomenda
#if primeira_encomenda:
#    print(f"Primeira Encomenda:\n{primeira_encomenda}")

# Imprime o estado atualizado
#print(estado_inicial)
