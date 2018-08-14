import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from Shopacholic import application, database

from Shopacholic.models.item import Item
from Shopacholic.models.order_details import OrderDetails
from Shopacholic.models.product import Product
from Shopacholic.models.product_type import ProductType

class ShopacholicTest(unittest.TestCase):
    def setUp(self):
        self.db_uri = 'mysql+pymysql://%s:%s@%s/' % (application.config['DB_USERNAME'], application.config['DB_PASSWORD'], application.config['DB_HOST'])
        application.config['TESTING'] = True
        application.config['WTF_CSRF_ENABLED'] = False
        application.config['DATABASE_NAME'] = 'test_shopacholic'
        application.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + application.config['DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("create database "  + application.config['DATABASE_NAME'])
        database.create_all()
        conn.close()
        self.application = application.test_client()

    def tearDown(self):
        database.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("drop database "  + application.config['DATABASE_NAME'])
        conn.close()

    def create_db(self):
        books = ProductType(type_name = 'Books')
        database.session.add(books)
        database.session.flush()

        sf_engineering = Product(books, 'Software Engineering', 'sf_engineering', 
                        'The Fundamental Practice of Software Engineering', 
                        'Software Engineering introduces students to the overwhelmingly \
                        important subject of software programming and development. In the \
                        past few years, computer systems have come to dominate not just our \
                        technological growth, but the foundations of our world’s major \
                        industries. This text seeks to lay out the fundamental concepts \
                        of this huge and continually growing subject area in a clear and \
                        comprehensive manner.', 43)

        clean_architecture = Product(books, 'Clean Architecture', 'clean_architecture',
                            'Clean Architecture is essential reading for every \
                            software architect, systems analyst, system designer, \
                            and software manager', 'As with his other books, Martins \
                            Clean Architecture doesnt merely present multiple \
                            choices and options, and say "use your best judgment": \
                            it tells you what choices to make, and why those choices are \
                            critical to your success', 20)

        b_sf_engineering = Product(books, 'Begininning Software Engineering', 'b_sf_engineering', 
                            'A complete introduction to building robust and reliable software', 
                            'Beginning Software Engineering demystifies the software engineering \
                            methodologies and techniques that professional developers use to design \
                            and build robust, efficient, and consistently reliable software. Free of \
                            jargon and assuming no previous programming, development, or management \
                            experience, this accessible guide explains important concepts and \
                            techniques that can be applied to any programming language.', 27)

        database.session.add(sf_engineering)
        database.session.add(clean_architecture)
        database.session.add(b_sf_engineering)

        database.session.commit()
        return str(books.id), sf_engineering.id

    def home_page(self):
        self.application.get('/', follow_redirects=True)

    def product_page(self, id):
        self.application.get('/products/'+id, follow_redirects=True)


    def test_home_page(self):
        self.create_db()
        d = self.application.get('/', follow_redirects=True)
        assert 'Choose Items' in str(d.data)
        assert 'Books' in str(d.data)

    def test_items(self):
        id, _ = self.create_db()
        d = self.application.get('/products/'+str(id), follow_redirects=True)
        assert 'Begininning Software Engineering' in str(d.data)
        assert 'Clean Architecture' in str(d.data)
        assert 'Software Engineering' in str(d.data)

    def test_add_to_cart(self):
        id, book = self.create_db()
        self.home_page()
        self.product_page(id)
        c = self.application.get('/shoppinglist/'+str(book)+','+str(id)+',1,43,1', follow_redirects=True)
        assert 'saved' in str(c.data)

    def test_shopping_page(self):
        id, book = self.create_db()
        self.home_page()
        self.product_page(id)
        self.application.get('/shoppinglist/'+str(book)+','+str(id)+',2,43,2', follow_redirects=True)
        d = self.application.get('/shopping', follow_redirects=True)
        assert 'Software Engineering' in str(d.data)
        assert '86' in str(d.data)

    def test_checkout(self):
        id, book = self.create_db()
        self.home_page()
        self.product_page(id)
        self.application.get('/shoppinglist/'+str(book)+','+str(id)+',2,43,2', follow_redirects=True)
        self.application.get('/shopping', follow_redirects=True)
        d = self.application.get('/checkout', follow_redirects=True)
        assert 'Thank you for placing the order, you can pay by cash at store' in str(d.data)

    def test_cancel_order(self):
        id, book = self.create_db()
        self.home_page()
        self.product_page(id)
        self.application.get('/shoppinglist/'+str(book)+','+str(id)+',2,43,2', follow_redirects=True)
        self.application.get('/shopping', follow_redirects=True)
        d = self.application.get('/cancel', follow_redirects=True)
        assert 'Your order has been cancelled' in str(d.data)
        

if __name__ == '__main__':
    unittest.main()