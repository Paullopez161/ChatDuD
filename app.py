from flask import Flask, request, jsonify
from talk_to_chatbot import ask_gpt  # This should be your function

app = Flask(__name__)

@app.route('/')
def hello():
    return "ChatDud is alive!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("input", "")
    if not user_input:
        return jsonify({"response": "No message received"}), 400

    response = ask_gpt(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)