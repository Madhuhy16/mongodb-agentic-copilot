from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["chatbot_ai_1gb"]
collection = db["messages"]

large_text = "MongoDB Agentic Copilot Performance Testing " * 250

collection.delete_many({})  # optional, clears old data

for i in range(50000):
    collection.insert_one({
        "user_message": f"Question {i}",
        "bot_response": large_text,
        "metadata": large_text
    })

print("1GB dataset generation completed")