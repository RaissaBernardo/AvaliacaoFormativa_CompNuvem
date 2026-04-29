class Cliente:
    def __init__(self, nome, telefone=None, email=None, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email