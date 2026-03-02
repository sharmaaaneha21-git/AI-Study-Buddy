# -----------------------------------------------
# AI Study Buddy – Terminal Version
# -----------------------------------------------

import datetime
import time
import string
import random
import pyttsx3

# -------------------------------
# Speak Function (Stable Version)
# -------------------------------

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -------------------------------
# User Name
# -------------------------------

name = input("Enter your name: ").strip()

# -------------------------------
# Time-Based Greeting
# -------------------------------

hour = datetime.datetime.now().hour

if 5 <= hour < 12:
    greeting = f"Good Morning, {name}! ☀️"
elif 12 <= hour < 17:
    greeting = f"Good Afternoon, {name}! 🌤️"
elif 17 <= hour < 21:
    greeting = f"Good Evening, {name}! 🌇"
else:
    greeting = f"Good Night, {name}! 🌙"

print(greeting)
speak(greeting)

intro = "Hello! I am your AI Study Buddy. Type 'bye' to exit."
print(intro)
speak(intro)

# -------------------------------
# Responses
# -------------------------------

responses = {
    "hello": ["Hi there!", "Hey!", "Hello friend!"],
    "who are you": ["I am your AI Study Buddy.", "Your friendly coding assistant."],
    "how are you": ["I feel great when you run me!", "All systems running perfectly!"],
    "motivate me": ["Keep going! Every bug makes you stronger 💪",
                    "Consistency beats talent. Keep coding!"],
    "python": ["Python is powerful and beginner friendly.",
               "Python can build AI, websites, automation and more!"],
    "sad": ["Don't worry. Even errors teach us something 😊"],
    "happy": ["That’s amazing! Keep smiling 🎉"],
    "time": [f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"]
}

# -------------------------------
# Response Function
# -------------------------------

def get_response(user_input):
    user_input = user_input.lower().strip()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I am still learning about that topic."

# -------------------------------
# Main Chat Loop
# -------------------------------

while True:
    user = input("You: ").strip()

    if user.lower() == "bye":
        goodbye = "Goodbye! Keep learning and growing 😊"
        print("Bot:", goodbye)
        speak(goodbye)
        break

    reply = get_response(user)

    time.sleep(1)

    print("Bot:", reply)
    speak(reply)

    # Timestamp Logging
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"[{current_time}] You: {user}\n")
        file.write(f"[{current_time}] Bot: {reply}\n")
        file.write("-" * 50 + "\n")