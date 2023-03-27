from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'

    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(50), nullable=True)
    attr = db.Column(db.String(20), nullable=True)
    collocates = db.Column(db.Text, nullable=True)
    synonyms = db.Column(db.Text, nullable=True)
    frequency = db.Column(db.BigInteger, nullable=True)
    rate = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<Vocabulary %r>' % self.term

    def to_dict(self):
        return {
            'id': self.id,
            'term': self.term,
            'attr': self.attr,
            'collocates': self.collocates,
            'synonyms': self.synonyms,
            'frequency': self.frequency,
            'rate': self.rate,
        }
