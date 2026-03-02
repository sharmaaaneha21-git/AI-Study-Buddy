# -----------------------------------------------
# AI Study Buddy – Flask Web Version
# -----------------------------------------------

from flask import Flask, render_template, request, jsonify
import random
import string
import datetime

app = Flask(__name__)

# -------------------------------
# Rule-Based Responses
# -------------------------------

responses = {
    "hello": ["Hi there!", "Hey!", "Hello friend!"],
    "who are you": ["I am your AI Study Buddy.", "Your friendly coding assistant."],
    "how are you": ["I'm doing great!", "All systems running perfectly!"],
    "motivate me": ["Keep going! Every bug makes you stronger 💪"],
    "sad": ["Don't worry. Even errors teach us something 😊"],
    "happy": ["That’s amazing! Keep smiling 🎉"],
    "python": ["Python is powerful and beginner friendly."],
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I am still learning about that topic."

# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    reply = get_response(user_message)

    # Save chat history with timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"[{current_time}] You: {user_message}\n")
        file.write(f"[{current_time}] Bot: {reply}\n")
        file.write("-" * 50 + "\n")

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)