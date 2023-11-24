import random

class Estado:
    def __init__(self, estafetas, encomendas):
        self.estafetas = {estafeta.id_estafeta: estafeta for estafeta in estafetas}
        self.encomendas = {encomenda.id_encomenda: encomenda for encomenda in encomendas}

    def __str__(self):
        estafetas_estado = "\n".join(str(estafeta) for estafeta in self.estafetas.values())
        encomendas_estado = "\n".join(str(encomenda) for encomenda in self.encomendas.values())
        return f"Estafetas:\n{estafetas_estado}\nEncomendas:\n{encomendas_estado}"

class Estafeta:
    def __init__(self, id_estafeta, localizacao_estafeta,avaliacoes,ranking):
        self.id_estafeta = id_estafeta
        self.localizacao_estafeta = localizacao_estafeta
        self.avaliacoes = avaliacoes  # Lista que armazena todas as avaliações atribuídas a um determinado estafeta
        self.ranking = ranking

    def __str__(self):
        return f"ESTAFETA {self.id_estafeta}\n Localização: {self.localizacao_estafeta}\n Avaliações: {self.avaliacoes}\n Ranking: {self.ranking}\n"

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def calcular_media_avaliacoes(self):
        if not self.avaliacoes:
            return None
        return sum(self.avaliacoes) / len(self.avaliacoes)

class Encomenda:
    def __init__(self, id_encomenda, localizacao_inicial, localizacao_final, peso, volume, prazo_entrega, estado_entrega, id_estafeta, avaliacao_motorista): 
        self.id_encomenda = id_encomenda
        self.localizacao_inicial = localizacao_inicial
        self.localizacao_final = localizacao_final
        self.peso = peso
        self.volume = volume
        self.prazo_entrega = prazo_entrega
        self.estado_entrega = estado_entrega
        self.id_estafeta = id_estafeta
        self.avaliacao_motorista = avaliacao_motorista

    def __str__(self):
        return f"ENCOMENDA {self.id_encomenda}\n Localização Inicial: {self.localizacao_inicial}\n Localização Final: {self.localizacao_final}\n Peso: {self.peso}\n Volume: {self.volume}\n Prazo: {self.prazo_entrega}\n Estado Entrega: {self.estado_entrega}\n ID do Motorista: {self.id_estafeta}\n Avaliação: {self.avaliacao_motorista}\n"


def inicializar_estado():
    # 9 estafetas
    estafetas = [
    Estafeta(id_estafeta=101, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[4, 5, 3], ranking=4.0),
    Estafeta(id_estafeta=102, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[2, 3], ranking=2.5),
    Estafeta(id_estafeta=103, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[], ranking=-1),
    Estafeta(id_estafeta=104, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[5, 5, 4, 5], ranking=4.75),
    Estafeta(id_estafeta=105, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[3, 4, 2], ranking=3.0),
    Estafeta(id_estafeta=106, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[], ranking=-1),
    Estafeta(id_estafeta=107, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[3, 4, 3], ranking=3.33),
    Estafeta(id_estafeta=108, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[], ranking=-1),
    Estafeta(id_estafeta=109, localizacao_estafeta='Largo do Barão da Quintela', avaliacoes=[], ranking=-1),
]


    # 15 encomendas
    # Lista de encomendas ajustada
    encomendas = [
    Encomenda(id_encomenda=201, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=8, volume=10, prazo_entrega=20, estado_entrega=False, id_estafeta=102, avaliacao_motorista=None),
    Encomenda(id_encomenda=202, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Chagas', peso=15, volume=15, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=203, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua da Horta Seca', peso=100, volume=18, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=204, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua do Alecrim', peso=53, volume=12, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=205, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=17, volume=8, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=206, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Travessa Guilherme Cossoul', peso=45, volume=20, prazo_entrega=30, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=207, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua da Emenda', peso=4, volume=10, prazo_entrega=15, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=208, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=1, volume=7, prazo_entrega=90, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=209, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Travessa Guilherme Cossoul', peso=8, volume=13, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=210, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Chagas', peso=19, volume=16, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=211, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua da Horta Seca', peso=5, volume=9, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=212, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua do Alecrim', peso=3, volume=14, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=213, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua de Ataíde', peso=81, volume=22, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=214, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua da Emenda', peso=25, volume=17, prazo_entrega=120, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
    Encomenda(id_encomenda=215, localizacao_inicial='Largo do Barão da Quintela', localizacao_final='Rua da Horta Seca', peso=21, volume=19, prazo_entrega=90, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None),
]


    return Estado(estafetas=estafetas, encomendas=encomendas)

def obter_primeira_encomenda(estado):
    # Obtém um iterador para a lista de encomendas
    iterador_encomendas = iter(estado.encomendas.values())

    for encomenda in iterador_encomendas:
        
        # Verifica se a encomenda não tem um ID de estafeta atribuído e tem id_estafeta igual a -1
        if encomenda.id_estafeta == -1:
            return encomenda.id_encomenda

    # Lida com o caso em que não há encomendas disponíveis sem um ID de estafeta
    print("Não há encomendas disponíveis por entregar.")
    return None

#def associar_estafetas_encomendas(estado):
    # Lista de estafetas e encomendas
    #estafetas = list(estado.estafetas.values())
    #encomendas = list(estado.encomendas.values())

    # Associa estafetas aleatoriamente às encomendas
    #for encomenda in encomendas:
        #estafeta_associado = random.choice(estafetas)
        #encomenda.id_estafeta = estafeta_associado.id_estafeta


#estado_inicial = inicializar_estado()
#associar_estafetas_encomendas(estado_inicial)
# Uso da função para obter a primeira encomenda
#primeira_encomenda = obter_primeira_encomenda(estado_inicial)

# Imprime a primeira encomenda
#if primeira_encomenda:
   #print(f"Primeira Encomenda:\n{primeira_encomenda}")

#Imprime o estado atualizado
#print(estado_inicial)
