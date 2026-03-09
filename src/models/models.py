from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType


#Create a database conection
db = create_engine('sqlite:///banco.db')

#create the database
Base = declarative_base()

#create class the database
class User(Base):
    __tablename__ = 'users'
    
    id = Column('id', Integer, primary_key=True, autoincrement = True )
    name = Column('name', String)
    email = Column('email', String, nullable=False)
    password = Column('password', String)
    active = Column('active', Boolean)
    admin = Column('admin', Boolean, default=False)
    
    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
  
class Order(Base):
    __tablename__ = 'orders'

    ORDER_STATUS = (
        ('PENDENTE', 'PENDENTE'),
        ('CANCELADO', 'CANCELADO'),
        ('FINALIZADO', 'FINALIZADO')
    )

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', ChoiceType(choices=ORDER_STATUS))
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)
    #itens

    def __init__(self, user, status='PENDENTE', price=0):
        self.user = user
        self.status = status
        self.price = price

class OrderedItem(Base):
    __tablename__ = "ordered_item"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    amount = Column('amount', Integer)
    flavor = Column('flavor', String)
    size = Column('size', String)
    unitary_price = Column('unitary_price', Float)
    order = Column('order', ForeignKey('orders.id'))

    def __init__(self, amount, flavor, size, unitary_price):
        self.amount = amount
        self.flavor = flavor
        self.size = size
        self.unitary_price = unitary_price



#exe the creation of methods on the database
