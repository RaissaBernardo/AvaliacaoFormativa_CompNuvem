from app import db

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    raca = db.Column(db.String(50))
    idade = db.Column(db.Integer)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)

    atendimentos = db.relationship('Atendimento', backref='pet', lazy=True)