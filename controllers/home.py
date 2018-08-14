from Shopacholic import database, application
from Shopacholic.models.product import Product
from Shopacholic.models.product_type import ProductType
from Shopacholic.models.order_details import OrderDetails
from Shopacholic.models.item import Item
from flask import render_template, request, session
import json

@application.route('/')
def home():
    session['user_shopping_list'] = []
    session['total_shopping_items'] = "0"
    return render_template('home.html', product_type=get_products_type())

def get_products_type():
    return ProductType.query

def product_by_type_id(pid):
    return Product.query.filter_by(product_type=pid).all()

def product_by_id(pid):
    return Product.query.filter_by(id=pid).first()

def product_by_id_and_type(pid, ptid):
    return Product.query.filter_by(id=pid, product_type=ptid).first()

@application.route('/products/<product_type_id>')
def products(product_type_id):
    return render_template('home.html', product_type=get_products_type(), 
                            product_items=product_by_type_id(product_type_id))

@application.route('/shoppinglist/<slist>', methods=('GET', 'POST'))
def shopping_list(slist):
    curr_shopping_list = session['user_shopping_list']
    curr_shopping_list.append(slist)
    session['user_shopping_list'] = curr_shopping_list
    session['total_shopping_items'] = slist.split(',')[-1]
    return 'saved'

@application.route('/shopping')
def shopping():
    shopping_list = session['user_shopping_list']
    agg_shopping_list = {}
    for item in shopping_list:
        curr_item = item.split(',')
        s = Shopping(curr_item[0], curr_item[1], int(curr_item[3]))
        if s not in agg_shopping_list:
            agg_shopping_list[s] = int(curr_item[2])
        else:
            i = agg_shopping_list[s]
            agg_shopping_list[s] = i + int(curr_item[2])


    order = OrderDetails(0, 'Pending')
    database.session.add(order)
    database.session.flush()

    checkout_list = []
    g_total = 0
    for shop in agg_shopping_list.keys():
        p = product_by_id_and_type(shop.item_id, shop.product_id)
        ip = shop.price
        t = agg_shopping_list[shop] * shop.price
        q = agg_shopping_list[shop]
        c = Checkout(p, ip, t, q)
        checkout_list.append(c)

        i = Item(order, p, q, t)
        database.session.add(i)

        g_total += t

    order.total = g_total
    database.session.commit()

    session['order_id'] = order.id

    return render_template('shopping.html', c_list=checkout_list, total=g_total)

@application.route('/checkout')
def checkout():
    order_id = session['order_id']
    update_order(order_id, 'Completed')
    session.pop('order_id')
    session.pop('user_shopping_list')
    session.pop('total_shopping_items')
    return render_template('order_placed.html', order_id=order_id)

@application.route('/cancel')
def cancel():
    update_order(session['order_id'], 'Cancelled')
    session.pop('order_id')
    session.pop('user_shopping_list')
    session.pop('total_shopping_items')
    return render_template('order_placed.html')

def update_order(order_id, status):
    o = OrderDetails.query.filter_by(id=order_id).first()
    o.status = status
    database.session.commit()

class Shopping(object):
    def __init__(self, item_id, product_id, price):
        self.item_id = item_id
        self.product_id = product_id
        self.price = price

    def __str__(self):
        return str(self.item_id) + str(self.product_id)

    def __eq__(self, other):
        return self.item_id == other.item_id and self.product_id == other.product_id
    
    def __repr__(self):
        return str(self.item_id) + ' ' + str(self.product_id)

    def __hash__(self):
        return hash(str(self))

class Checkout(object):
    def __init__(self, product, price_per_item, total_price, quantity):
        self.product = product
        self.price_per_item = price_per_item
        self.total_price = total_price
        self.quantity = quantity

