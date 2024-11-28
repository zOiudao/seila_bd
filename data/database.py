from sqlalchemy import String, Column, Integer, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pytz import timezone
from faker import Faker

tmz = timezone('America/Sao_Paulo')
ftime = '%d/%m/%Y %H:%M:%S'
fake = Faker('pt_BR')

engine = create_engine('sqlite:///mydb.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_at = Column(DateTime, default=lambda: datetime.now(tmz))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Nome: {self.name} Data: {self.create_at.strftime(ftime)}"


Base.metadata.create_all(engine)

def newuser():
    nome = fake.unique.name()
    new = Usuario(nome)
    session.add(new)
    session.commit()
    print(new)

def read():
    for i in session.query(Usuario).all():
        print(i.name)
