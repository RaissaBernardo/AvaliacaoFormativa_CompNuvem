from app import db

class Venda(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    valor_total = db.Column(db.Float)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)


class ItemVenda(db.Model):
    __tablename__ = 'itens_venda'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    venda_id = db.Column(db.Integer, db.ForeignKey('vendas.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)