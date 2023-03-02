import sqlalchemy as sq
from sqlalchemy.orm import declarative_base,relationship

Base=declarative_base()
class Publisher(Base):
    __tablename__='publisher' 

    id=sq.Column(sq.Integer, primary_key=True)
    name=sq.Column(sq.String(length=60), unique=True)

    # book=relationship('Book',back_populates='publisher')
    # book=relationship('Book')


    def __str__(self): 
        return f'Publisher {self.id}:{self.name}'



class Book(Base):
    __tablename__='book'

    id=sq.Column(sq.Integer,primary_key=True)
    title=sq.Column(sq.String(length=80))
    id_publisher=sq.Column(sq.Integer,sq.ForeignKey('publisher.id'), nullable=False)

    publisher=relationship('Publisher',backref='book')
    stock=relationship('Stock',backref='book')
    # stock = relationship("Stock")

    def __str__(self): 
        return f'Book {self.id}:{self.title}, Publisher {self.id_publisher}'


class Shop(Base):
    __tablename__='shop' 

    id=sq.Column(sq.Integer, primary_key=True)
    name=sq.Column(sq.String(length=60), unique=True)

    # stock=relationship('Stock',back_populates='shop')
    # stock = relationship("Stock")

    def __str__(self): 
        return f'Shop {self.id}:{self.name}'


class Stock(Base):
    __tablename__='stock'

    id=sq.Column(sq.Integer, primary_key=True)
    id_book=sq.Column(sq.Integer,sq.ForeignKey('book.id'), nullable=False)
    id_shop=sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count=sq.Column(sq.Integer,nullable=False)

    shop=relationship('Shop',backref='stock')
    # book=relationship('Book',backref='stock')
    # sale=relationship('Sale',back_populates='stock')
    # sale = relationship("Sale")

    def __str__(self):
        return f'Stock {self.id}:Book {self.id_book}, Shop {self.id_shop}, Count {self.count}'
    

class Sale(Base):
    __tablename__='sale'

    id=sq.Column(sq.Integer, primary_key=True)
    price=sq.Column(sq.Numeric(6,2),nullable=False)
    date_sale=sq.Column(sq.TIMESTAMP)
    id_stock=sq.Column(sq.ForeignKey('stock.id'),nullable=False)
    count=sq.Column(sq.Integer)

    stock=relationship('Stock',backref='sale')

    def __str__(self):
        return f'Sale {self.id}:price {self.price}, created_at {self.date_sale}, stock {self.id_stock}, count {self.count}'



def create_tables(engine): 
    Base.metadata.drop_all(engine) 
    Base.metadata.create_all(engine) 


