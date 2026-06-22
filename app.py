from flask import Flask, request, jsonify
from pymongo import MongoClient
import ollama

app = Flask(__name__)
app.json.sort_keys = False

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]

customers = db["customers"]
products = db["products"]
orders = db["orders"]

@app.route("/")
def home():
    return "MongoDB Agentic Copilot Running"

@app.route("/test")
def test():
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": "What is MongoDB?"
            }
        ]
    )

    return response["message"]["content"]

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Context-aware query
    if "rahul" in user_message and "buy" in user_message:

        customer = customers.find_one({"name": "Rahul"})

        if customer:
            order = orders.find_one({"customer_id": customer["customer_id"]})

            if order:
                product_names = []

                for pid in order["products"]:
                    product = products.find_one({"product_id": pid})

                    if product:
                        product_names.append(product["name"])

                return ({
                    "question": data.get("message"),
    "answer": f"Rahul bought {', '.join(product_names)}"
                })

    # Default Ollama response
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": data.get("message")
            }
        ]
    )

    bot_response = response["message"]["content"]

    return ({
        "question": data.get("message"),
        "answer": bot_response
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)