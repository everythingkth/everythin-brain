from flask import Flask, request, jsonify
from memory_engine import embed_text, store_to_vector_db, search_from_vector_db

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Everything Brain is running!"

@app.route("/store", methods=["POST"])
def store_memory():
    data = request.get_json()
    content = data.get("content", "")
    if not content:
        return jsonify({"error": "No content provided"}), 400

    vector = embed_text(content)
    store_to_vector_db(content, vector)
    return jsonify({"status": "stored", "content": content})

@app.route("/search", methods=["POST"])
def search_memory():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    query_vector = embed_text(query)
    results = search_from_vector_db(query_vector)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
