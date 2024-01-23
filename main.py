from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  price = db.Column(db.Integer, nullable=False)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  description = db.Column(db.String(length=1824), nullable=False, unique=True)


@app.route('/about/<username>')
def about_user(username):
  return f'<h1>This is about the page of {username}</h1>'


@app.route('/about')
def about_page():
  return '<h1>About Page</h1>'


@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  items = [{
      'id': 1,
      'name': 'Phone',
      'barcode': '893212299897',
      'price': 500
  }, {
      'id': 2,
      'name': 'Laptop',
      'barcode': '123985473165',
      'price': 900
  }, {
      'id': 3,
      'name': 'Keyboard',
      'barcode': '231985128446',
      'price': 150
  }]
  return render_template('market.html', items=items)
  
@app.route('/depict')
def new_page():
    # Query all items from the database
    items = Item.query.all()

    # Convert items to a list of dictionaries for rendering in the template
    items_data = [{'id': item.id, 'name': item.name, 'barcode': item.barcode, 'price': item.price}
                  for item in items]

    return render_template('depict.html', items=items_data)

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
     #item2 = Item(name="IPhone 10",price = 500, barcode = '846154104234',description = 'this is a description of the item as described before.')
     #db.session.add(item2)
     #db.session.commit()

  app.run(host='0.0.0.0', port=8080, debug=True)
