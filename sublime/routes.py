from os import rename
from sublime import app
from flask import before_render_template, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')