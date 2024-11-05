from app import db
from app.model.guru import Guru
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    id_admin = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_guru = db.Column(db.BigInteger, db.ForeignKey(Guru.id_guru, ondelete='CASCADE'), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    # Menambahkan relasi untuk mendapatkan objek Guru
    guru = db.relationship('Guru', backref='admin', lazy=True)
    
    def __repr__(self):
        return f'<Admin {self.email}>'
    
    def get_id(self):
        return self.id_admin