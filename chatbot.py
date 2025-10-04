
import random
import json

# Load intents
with open('data/intents.json') as file:
    intents = json.load(file)

def get_response(user_input):
    for intent in intents['intents']:
        if user_input.lower() in intent['patterns']:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

# Main loop
print("Hello! I am your AI Chatbot. Type 'quit' to exit.")
while True:
    message = input("You: ")
    if message.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(message)
    print("Chatbot:", response)
