import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json
from modelsdb import create_tables, Publisher,Book, Shop, Stock, Sale

DSN='postgresql://postgres:111@localhost:5432/book_store_db'
engine=sqlalchemy.create_engine(DSN)

create_tables(engine) 
Session=sessionmaker(bind=engine) 
session=Session() 

with open('test_data.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
for record in data:
    model = {'publisher': Publisher, 
            'shop': Shop, 
            'book': Book, 
            'stock': Stock, 
            'sale': Sale }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


def book_sales(session):
    
    name=input('Введите имя автора:')
    
    query = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale).join(Publisher).\
        join(Stock).join(Sale).join(Shop).filter(Publisher.name.ilike(f'%{name}%')).all()
    for book,shop,price,count,date in query:
        print(f'{book} | {shop} | {price*count} | {date}')
    

for c in session.query(Publisher).all():
    print(c)

book_sales(session)

session.close()   


if __name__ == "__main__":
      ...
