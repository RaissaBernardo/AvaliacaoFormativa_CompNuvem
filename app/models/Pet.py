class Pet:
    def __init__(self, nome, tipo, raca, idade, cliente_id, id=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.raca = raca
        self.idade = idade
        self.cliente_id = cliente_id