# TASK 4: Basic Chatbot
# Goal: Build a simple rule-based chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye! Have a nice day 😊"
    else:
        return "Sorry, I don't understand that."

def chatbot():
    print("Simple Chatbot")
    print("Type 'hello', 'how are you', or 'bye' to chat")
    print("---------------------------------------------")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break

# Run the chatbot
chatbot()
