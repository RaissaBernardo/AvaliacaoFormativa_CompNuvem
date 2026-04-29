class Fornecedor:
    def __init__(self, nome, telefone, email, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email