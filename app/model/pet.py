from sqlalchemy import Integer, String, Boolean
from app import db


class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    age = db.Column(Integer, nullable=False)
    isPlayful = db.Column(Boolean, nullable=False)

    def __repr__(self):
        return f"Pet(name = {self.name}, age = {self.age}, isPlayful = {self.isPlayful})"

