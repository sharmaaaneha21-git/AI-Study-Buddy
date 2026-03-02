import datetime
import string

# Take user name
name = input("Welcome in ChatBot! Please enter your name: ").strip()

# Greeting according to time
presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 12:
    print("Good Morning,", name)
elif 12 <= presentHour < 17:
    print("Good Afternoon,", name)
elif 17 <= presentHour < 21:
    print("Good Evening,", name)
else:
    print("Good Night,", name)

print("Namaste! Welcome to Rule-Based ChatBot.")
print("You can ask me basic questions. Type 'bye' to exit from the Bot.")

# Chatbot memory (dictionary)
responses = {
    "hello": "Hi, Welcome! How can I help you?",
    "who are you": "I am a smart rule-based AI ChatBot.",
    "how are you": "I am very good. Thank you!",
    "motivate me": "Keep going. Every bug in your project makes you a better programmer.",
    "happy": "Great to hear that!",
    "what is function in python": "A function in Python is a block of reusable code that performs a specific task."
}

# Function to get response
def getResponseofBot(userQuestion):
    userQuestion = userQuestion.lower().strip()
    userQuestion = userQuestion.translate(str.maketrans('', '', string.punctuation))

    if userQuestion in responses:
        return responses[userQuestion]
    else:
        return "Sorry, I am still learning about this topic."

# Chat loop
while True:
    userInput = input("Please, ask your questions: ").strip()

    if userInput.lower() == "bye":
        print("Bot Response: Goodbye! Have a nice day 😊")
        break

    reply = getResponseofBot(userInput)
    print("Bot Response:", reply)