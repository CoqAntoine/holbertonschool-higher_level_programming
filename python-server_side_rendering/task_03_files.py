from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate the source parameter
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source", products=[])

    # Load the correct file
    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    # If id is provided, filter
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=[])

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])

        return render_template("product_display.html", products=filtered, error=None)

    # Otherwise return all products
    return render_template("product_display.html", products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
