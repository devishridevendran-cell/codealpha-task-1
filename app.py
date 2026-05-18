from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

PRODUCTS_FILE = "products.json"

# Load products
def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save products
def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

# Home page
@app.route("/")
def home():
    products = load_products()
    return render_template("index.html", products=products)

# Add product
@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.json

    products = load_products()

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "image": data["image"]
    }

    products.append(new_product)
    save_products(products)

    return jsonify({
        "message": "Product added successfully"
    })

# Get all products
@app.route("/products")
def get_products():
    return jsonify(load_products())

if __name__ == "__main__":
    app.run(debug=True)