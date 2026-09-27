def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif text == "":
        return "Please say something!"
    else:
        return "Sorry, I don't understand that yet."


def chat():
    print("Chatbot: Hi! Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"Chatbot: {reply}")

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()