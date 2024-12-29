from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)


app = Flask(__name__)

shopping_list = []

@app.route('/shopping_list/view', methods=["GET"])
def view_list():
    response = supabase.table("products").select("*").execute()
    return jsonify(response.data), 200


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
            try:
                # Insert the product into the Supabase table
                result = supabase.table('products').insert([{
                    "productName": data["productName"],
                    "quantity": data["quantity"],
                    "unitPrice": data["unitPrice"]
                }]).execute()
                return jsonify({"message": "Product successfully registered.", "data": result.data}), 201
            except Exception as e:
                return jsonify({"message": f"Failed to insert product: {str(e)}"}), 500
    return jsonify({"message": "Invalid product data"}), 400



if __name__ == "__main__":
    app.run(debug=True)


