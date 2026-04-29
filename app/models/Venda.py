class Venda:
    def __init__(self, data, valor_total, cliente_id, id=None):
        self.id = id
        self.data = data
        self.valor_total = valor_total
        self.cliente_id = cliente_id


class ItemVenda:
    def __init__(self, venda_id, produto_id, quantidade, preco, id=None):
        self.id = id
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco = preco