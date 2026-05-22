from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_ai"]
collection = db["messages"]

@app.route("/")
def home():
    return "MongoDB Agentic Copilot Running"

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_message = data.get("message")

    # Simple agentic-style response
    if "mongodb" in user_message.lower():
        bot_response = "MongoDB is a NoSQL database used for storing flexible document-based data."
    else:
        bot_response = f"Copilot Response: {user_message}"

    chat_data = {
        "user_message": user_message,
        "bot_response": bot_response
    }

    collection.insert_one(chat_data)

    return jsonify({
        "response": bot_response
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)