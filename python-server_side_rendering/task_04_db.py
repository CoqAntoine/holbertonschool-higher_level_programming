from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()
        return products

    except sqlite3.Error:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            list_items = json.load(file)
            items=list_items['items']
    except:
        items = []
    return render_template('items.html', items=items)

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Vérification source
    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html",
                               error="Wrong source",
                               products=[])

    # Charger données selon la source
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:  # source == sql
        data = read_sql()
        if data is None:
            return render_template("product_display.html",
                                   error="Database error",
                                   products=[])

    # Filtrer par id si demandé
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID",
                                   products=[])

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=[])

        return render_template("product_display.html",
                               products=filtered,
                               error=None)

    # Sinon afficher tous les produits
    return render_template("product_display.html",
                           products=data,
                           error=None)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
