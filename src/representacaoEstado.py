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
    def __init__(self, id_estafeta, localizacao_estafeta,avaliacoes,ranking,numero_entregas_efetuadas,disponibilidade):
        self.id_estafeta = id_estafeta
        self.localizacao_estafeta = localizacao_estafeta
        self.avaliacoes = avaliacoes  # Lista que armazena todas as avaliações atribuídas a um determinado estafeta
        self.ranking = ranking
        self.numero_entregas_efetuadas = numero_entregas_efetuadas 
        self.disponibilidade = disponibilidade

    def __str__(self):
        return f"ESTAFETA {self.id_estafeta}\n Localização: {self.localizacao_estafeta}\n Avaliações: {self.avaliacoes}\n Ranking dos Clientes: {self.ranking}\n Número de Entregas Realizadas: {self.numero_entregas_efetuadas}\n Disponibilidade: {self.disponibilidade}\n"

    ##### ENTREGAS DE UM ESTAFETA #####
    def realizar_entrega(self):
        self.numero_entregas_efetuadas += 1

    ##### AVALIAÇÕES DE CLIENTES #####
    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)
    

class Encomenda:
    def __init__(self, id_encomenda, localizacao_inicial, localizacao_final, peso, volume, prazo_entrega, estado_entrega, id_estafeta, avaliacao_motorista, preco_entrega): 
        self.id_encomenda = id_encomenda
        self.localizacao_inicial = localizacao_inicial
        self.localizacao_final = localizacao_final
        self.peso = peso
        self.volume = volume
        self.prazo_entrega = prazo_entrega
        self.estado_entrega = estado_entrega
        self.id_estafeta = id_estafeta
        self.avaliacao_motorista = avaliacao_motorista
        self.preco_entrega = preco_entrega

    def __str__(self):
        # calcula horas e minutos
        tempo_entrega_horas = self.prazo_entrega // 60  # converte minutos para horas
        tempo_entrega_minutos = self.prazo_entrega % 60  # resto da divisão para obter minutos restantes

        # calcula o tempo de entrega de forma a exibir da melhor forma
        if tempo_entrega_horas > 0:
            tempo_entregax = f"{tempo_entrega_horas}h {tempo_entrega_minutos}min"
        else:
            tempo_entregax = f"{tempo_entrega_minutos}min"

        return f"ENCOMENDA {self.id_encomenda}\n Localização Inicial: {self.localizacao_inicial}\n Localização Final: {self.localizacao_final}\n Peso: {self.peso}\n Volume: {self.volume}\n Prazo: {tempo_entregax}\n Estado Entrega: {self.estado_entrega}\n ID do Motorista: {self.id_estafeta}\n Avaliação: {self.avaliacao_motorista}\n"


def inicializar_estado():
    # 9 estafetas
    estafetas = [
    Estafeta(id_estafeta=101, localizacao_estafeta='Travessa do Carmo', avaliacoes=[4, 5, 3], ranking=4.0, numero_entregas_efetuadas=3, disponibilidade=True),
    Estafeta(id_estafeta=102, localizacao_estafeta='Travessa do Carmo', avaliacoes=[2, 3], ranking=2.5, numero_entregas_efetuadas=2, disponibilidade=True),
    Estafeta(id_estafeta=103, localizacao_estafeta='Travessa do Carmo', avaliacoes=[], ranking=-1, numero_entregas_efetuadas=0, disponibilidade=True),
    Estafeta(id_estafeta=104, localizacao_estafeta='Travessa do Carmo', avaliacoes=[5, 5, 4, 5], ranking=4.75, numero_entregas_efetuadas=4, disponibilidade=True),
    Estafeta(id_estafeta=105, localizacao_estafeta='Travessa do Carmo', avaliacoes=[3, 4, 2], ranking=3.0, numero_entregas_efetuadas=3, disponibilidade=True),
    Estafeta(id_estafeta=106, localizacao_estafeta='Travessa do Carmo', avaliacoes=[], ranking=-1, numero_entregas_efetuadas=0, disponibilidade=True),
    Estafeta(id_estafeta=107, localizacao_estafeta='Travessa do Carmo', avaliacoes=[3, 4, 3], ranking=3.33, numero_entregas_efetuadas=3, disponibilidade=True),
    Estafeta(id_estafeta=108, localizacao_estafeta='Travessa do Carmo', avaliacoes=[], ranking=-1, numero_entregas_efetuadas=0, disponibilidade=True),
    Estafeta(id_estafeta=109, localizacao_estafeta='Travessa do Carmo', avaliacoes=[], ranking=-1, numero_entregas_efetuadas=0, disponibilidade=True),
]

    # 15 encomendas
    encomendas = [
    Encomenda(id_encomenda=201, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua da Misericórdia', peso=8, volume=10, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=202, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua do Jasmim', peso=15, volume=15, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=203, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua da Horta Sêca', peso=100, volume=18, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=204, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua do Alecrim', peso=4, volume=12, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1,avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=205, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua das Flores', peso=17, volume=8, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=206, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua do Quelhas', peso=45, volume=20, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=207, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua Nova da Trindade', peso=4, volume=10, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=208, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua do Ataíde', peso=1, volume=7, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=209, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua do Noronha', peso=3, volume=7, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=210, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua das Chagas', peso=4, volume=13, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=211, localizacao_inicial='Travessa do Carmo', localizacao_final='Travessa da Bela Vista', peso=5, volume=9, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=212, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua da Esperança', peso=3, volume=14, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=213, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua da Academia das Ciências', peso=81, volume=22, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=214, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua da Emenda', peso=25, volume=17, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
    Encomenda(id_encomenda=215, localizacao_inicial='Travessa do Carmo', localizacao_final='Rua dos Navegantes', peso=21, volume=19, prazo_entrega=-1, estado_entrega=False, id_estafeta=-1, avaliacao_motorista=None, preco_entrega=None),
]


    return Estado(estafetas=estafetas, encomendas=encomendas)

estado_inicial = inicializar_estado()

#Imprime o estado atualizado
#print(estado_inicial)

