from app import db
from datetime import datetime

class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, Primary_key=True)
    name = db.Column(db.String(80), nullable= False)

    def __init__(self, name)
        self.name = name
    
    def __repr__ = (self)
        return 'Publisher is {}'.format(self.name)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, Primary_key=True)
    title = db.Column(db.String(500), nullable = False, index = True)
    author = db.column(db.String(350))
    avg_rating = db.Column(db.Float())
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default = datetime.utcnow())

    pub_id = db.Column(db.Integer, db.Foreignkey('Publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id)
        self.name = name
    
    def __repr__ = (self)
        return '{} by {}'.format(self.title, self.author)