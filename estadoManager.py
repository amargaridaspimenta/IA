from representacaoEstado import Estado, Estafeta, Encomenda, inicializar_estado

class EstadoManager:
    def __init__(self):
        self.estados = {}

    def adicionar_estado(self, chave, estado):
        self.estados[chave] = estado

    def obter_estado(self, chave):
        return self.estados.get(chave)
    
    def criar_chave_estado(self, estafeta_id, encomenda_id):
        return f"{estafeta_id}_{encomenda_id}"

    def atualizar_localizacao_estafetas(self, estado, nova_localizacao):
        for estafeta in estado.estafetas:
            estafeta.localizacao_estafeta = nova_localizacao

    def atualizar_avaliacao_estafetas(self, estado, avaliacao_entrega):
        for estafeta in estado.estafetas:
            estafeta.avaliacao = avaliacao_entrega

    def atualizar_estado_entrega_encomendas(self, estado):
        for encomenda in estado.encomendas:
            encomenda.estado_entrega = True

    def avaliar_motorista_encomendas(self, estado, avaliacao):
        for encomenda in estado.encomendas:
            encomenda.avaliacao_motorista = avaliacao

# Criar um gestor de estados que nos permite atualizar as informações
manager_estado = EstadoManager()

# Inicializa o estado e adiciona à hashtable
estado_inicial = inicializar_estado()
manager_estado.adicionar_estado("estado_inicial", estado_inicial)

# Acessar e imprimir o estado antes das atualizações
estado_nao_atualizado = manager_estado.obter_estado("estado_inicial")
print("Estado antes das atualizações:")
print(estado_nao_atualizado)

# Criar uma chave combinada para todas as instâncias
chave_estado_combinada = manager_estado.criar_chave_estado(101, 201)

# Teste para ver se a atualização das instâncias funciona
manager_estado.atualizar_localizacao_estafetas(estado_inicial, 'Rua de Ataíde')
manager_estado.atualizar_avaliacao_estafetas(estado_inicial, 4.0)
manager_estado.atualizar_estado_entrega_encomendas(estado_inicial)
manager_estado.avaliar_motorista_encomendas(estado_inicial, 4.5)

# Acessa e imprime o estado após as atualizações
estado_atualizado = manager_estado.obter_estado("estado_inicial")
print("\nEstado após as atualizações:")
print(estado_atualizado)
