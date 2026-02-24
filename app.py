import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, PantryItem
from datetime import datetime
import requests 

app = Flask(__name__)

# CONFIGURATION 
# Use a local file for dev, but allow an environment variable for production (Render/Heroku)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///pantry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 

# create tables automatically
with app.app_context():
    db.create_all()

# --- helpers ---
def fetch_product_name(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    try:
        response = requests.get(url, headers={'User-Agent': 'SmartPantry/1.0'})
        data = response.json()
        if data.get('status') == 1:
            return data['product'].get('product_name', 'Unknown Item')
    except:
        pass
    return 'Unknown Item'

# --- routes ---

@app.route('/')
def index():
    items = PantryItem.query.order_by(PantryItem.expiry_date).all()
    expired_count = sum(1 for i in items if (i.expiry_date - datetime.utcnow().date()).days < 0)
    return render_template('index.html', items=items, expired_count=expired_count)

@app.route('/add', methods=['POST'])
def add_item():
    barcode = request.form.get('barcode')
    name = request.form.get('name')
    expiry_str = request.form.get('expiry_date') #yyyy-mm-dd

    if not name and barcode:
        name = fetch_product_name(barcode)

    if not name:
        name = "Mystery Item"

    expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()

    new_item = PantryItem(name=name, barcode=barcode, expiry_date=expiry_date)
    db.session.add(new_item)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    item = PantryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/lookup/<barcode>')
def lookup_barcode(barcode):
    name = fetch_product_name(barcode)
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

