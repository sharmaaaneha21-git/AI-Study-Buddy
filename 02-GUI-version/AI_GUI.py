import tkinter as tk
from tkinter import scrolledtext
import datetime
import string
import random

responses = {
    "hello": ["Hi there!", "Hey!", "Hello friend!"],
    "who are you": ["I am your AI Study Buddy.", "Your friendly coding assistant."],
    "how are you": ["I'm doing great!"],
    "motivate me": ["Keep going! Every bug makes you stronger 💪"],
    "sad": ["Don't worry. Even errors teach us something 😊"],
    "happy": ["That’s amazing! Keep smiling 🎉"],
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I am still learning about that topic."

def send_message(event=None):
    user = entry.get().strip()
    if not user:
        return

    chat_window.insert(tk.END, "You: " + user + "\n")

    if user.lower() == "bye":
        chat_window.insert(tk.END, "Bot: Goodbye! 👋\n\n")
        entry.delete(0, tk.END)
        return

    reply = get_response(user)
    chat_window.insert(tk.END, "Bot: " + reply + "\n\n")

    entry.delete(0, tk.END)
    chat_window.see(tk.END)

# Main Window
window = tk.Tk()
window.title("AI Study Buddy")
window.geometry("500x600")

# Chat Area
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Bottom Frame
bottom_frame = tk.Frame(window)
bottom_frame.pack(fill=tk.X, padx=10, pady=10)

# Entry Field
entry = tk.Entry(bottom_frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

entry.bind("<Return>", send_message)  # Enter key support

# Send Button
send_button = tk.Button(bottom_frame, text="Send", width=10, command=send_message)
send_button.pack(side=tk.RIGHT, padx=(5, 0))

window.mainloop()