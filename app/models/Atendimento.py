class Atendimento:
    def __init__(self, tipo_servico, data, valor, pet_id, id=None):
        self.id = id
        self.tipo_servico = tipo_servico
        self.data = data
        self.valor = valor
        self.pet_id = pet_id