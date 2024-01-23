from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route('/about/<username>')
def about_user(username):
  return f'<h1>This is about the page of {username}</h1>'

@app.route('/')
@app.route('/about')
def about_page():
  return '<h1>About Page</h1>'


@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)

@app.route('/depict')
def new_page():
    # Query all items from the database
    items = Item.query.all()

    # Convert items to a list of dictionaries for rendering in the template
    items_data = [{'id': item.id, 'name': item.name, 'barcode': item.barcode, 'price': item.price}
                  for item in items]

    return render_template('depict.html', items=items_data)