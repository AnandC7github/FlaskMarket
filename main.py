from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)









if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    # item2 = Item(name="Laptop",price = 600, barcode ='321912987542',description = 'description for laptop')
    # db.session.add(item2)
    # db.session.commit()
  app.run(host='0.0.0.0', port=8080, debug=True)
