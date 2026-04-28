from app import db

class Servico(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True)
    tipo_servico = db.Column(db.String(50))
    data = db.Column(db.Date)
    valor = db.Column(db.Float)

    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)