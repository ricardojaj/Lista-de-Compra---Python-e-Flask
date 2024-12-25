from flask import Flask, request, jsonify

app = Flask(__name__)

shopping_list = []

@app.route('/shopping_list/view', methods=["GET"])
def view_list():
    product_list = []
    for product in shopping_list:
        product_data = {
            "productName": product["productName"],
            "quantity": product["quantity"],
            "unitPrice": product["unitPrice"]
        }

        product_list.append(product_data)

    return jsonify(product_list)

@app.route('/shopping_list/add', methods=["POST"])
def add_product():
     #variable to receive data from the request
    data = request.json

    # isinstance = ensures that the received data type is as expected.
    if (
        "productName" in data and isinstance(data["quantity"], int) 
        and data["quantity"] > 0 and isinstance(data["unitPrice"], (int, float)) 
        and data["unitPrice"] > 0):
            #create product and save to the list
            product = {
                "productName": data["productName"],
                "quantity": data["quantity"],
                "unitPrice": data["unitPrice"]
            }

            shopping_list.append(product)
            return jsonify({"message": "Product successfully registered.", "product": product}), 201
    return jsonify({"message": "Invalid product data"}), 400



if __name__ == "__main__":
    app.run(debug=True)


