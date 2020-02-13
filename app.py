from flask import Flask, jsonify, request
import json
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products,'description':"Product's list"})

#Create a product
@app.route('/products', methods=['POST'])
def addProducts():
    try:

        newProduct = {
            "name": request.json['name'],
            "price": request.json['price'],
            "quantity": request.json['quantity']
        }
        products.append(newProduct)
        return jsonify({
            "message": 'El producto fue agregado de manera correcta',
            'Appened': True
        })
    except :
        return jsonify({
            "message": 'El producto no fue agregado, algo ocurrio mal!',
            'Appened': False
        })
        
#Search a product
@app.route('/products/<string:productName>', methods=['GET'])
def getProduct(productName):
    for product in products:
        if (product["name"]==productName):
            return jsonify({"product": product})
    return jsonify({"message":'This product is not registered'})

#Update a product
@app.route('/products/<string:productName>', methods=['PUT'])
def editProduct(productName):
    for product in products:
        if (product["name"]==productName):
            product['price']=request.json['price']
            product['quantity']=request.json['quantity']
            return jsonify({"product": product, "message": "Product was modifity successfully"})

    return jsonify({"message":'This product is not registered'})

#Delete a product
@app.route('/products/<string:productName>', methods=['DELETE'])
def deleteProduct(productName):
    for product in products:
        if (product["name"]==productName):
            products.remove(product)
            return jsonify({"message": "Product was delete successfully"})

    return jsonify({"message":'This product is not registered'})



if __name__ == '__main__':
    app.run(debug=True, port=4000)


