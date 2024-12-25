from flask import Flask, request, jsonify

app = Flask(__name__)

listaCompras = []

@app.route('/listaCompras/view', methods=["GET"])
def view_list():
    product_list = []
    for product in listaCompras:
        product_data = {
            "nomeProduto": product["nomeProduto"],
            "quantidade": product["quantidade"],
            "precoUnidade": product["precoUnidade"]
        }

        product_list.append(product_data)

    return jsonify(product_list)



@app.route('/listaCompras/add', methods=["POST"])
def adc_product():
     #variavel para receber dados da minha requisicao
    data = request.json

#isinstance = garantias de que o tipo de dado recebido é o esperado.
    if (
        "nomeProduto" in data and isinstance(data["quantidade"], int) 
        and data["quantidade"] > 0 and isinstance(data["precoUnidade"], (int, float)) 
        and data["precoUnidade"] > 0):
            #criar produto e salvar na lista
            product = {
                "nomeProduto": data["nomeProduto"],
                "quantidade": data["quantidade"],
                "precoUnidade": data["precoUnidade"]
            }

            listaCompras.append(product)
            return jsonify({"message": "Product successfully registered.", "product": product}), 201
    return jsonify({"message": "Invalid product data"}), 400



if __name__ == "__main__":
    app.run(debug=True)


