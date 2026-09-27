import random
from datetime import datetime


RESPONSES = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi there! Nice to meet you.",
        "Hey! What would you like to talk about?",
        "Hello! How are you doing today?"
    ],

    "how_are_you": [
        "I'm doing great! Thanks for asking.",
        "I'm fine, thank you. How about you?",
        "I'm ready to chat!"
    ],

    "name": [
        "I'm a simple Python chatbot.",
        "You can call me PyBot.",
        "I'm PyBot, your basic Python chatbot."
    ],

    "thanks": [
        "You're welcome!",
        "No problem!",
        "Happy to help!",
        "Anytime!"
    ],

    "help": [
        "I can greet you, tell you my name, tell you the time, "
        "and respond to basic questions.",
        "Try saying hello, asking my name, or asking for the time."
    ],

    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! It was nice talking to you.",
        "Take care!"
    ],

    "positive": [
        "That's great to hear!",
        "Awesome!",
        "I'm glad to hear that!"
    ],

    "negative": [
        "I'm sorry to hear that.",
        "I hope things get better soon.",
        "Sometimes talking about it can help."
    ]
}


KEYWORDS = {
    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "how_are_you": [
        "how are you",
        "how are you doing",
        "how do you feel"
    ],

    "name": [
        "what is your name",
        "what's your name",
        "who are you",
        "your name"
    ],

    "thanks": [
        "thank you",
        "thanks",
        "thank"
    ],

    "help": [
        "help",
        "what can you do",
        "commands",
        "options"
    ],

    "goodbye": [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you"
    ],

    "positive": [
        "i am good",
        "i'm good",
        "i am great",
        "i'm great",
        "i am happy",
        "i'm happy",
        "good",
        "great"
    ],

    "negative": [
        "i am sad",
        "i'm sad",
        "i am unhappy",
        "i'm unhappy",
        "bad",
        "not good"
    ]
}


class ChatBot:
    """A simple rule-based chatbot."""

    def __init__(self, name="PyBot"):
        self.name = name
        self.user_name = None
        self.message_count = 0


    def clean_input(self, user_input):
        """Clean and normalize user input."""

        return user_input.lower().strip()


    def detect_intent(self, text):
        """
        Detect the user's intention based on keywords.

        Returns:
            Intent name or None.
        """

        for intent, keywords in KEYWORDS.items():

            for keyword in keywords:

                if keyword in text:
                    return intent

        return None



    def get_time(self):
        """Return the current local time."""

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."


    def get_date(self):
        """Return the current date."""

        current_date = datetime.now().strftime("%B %d, %Y")

        return f"Today's date is {current_date}."


    def remember_user_name(self, text):

        prefix = "my name is"

        if prefix in text:

            name = text.split(
                prefix,
                1
            )[1].strip()

            if name:
                self.user_name = name.title()

                return (
                    f"Nice to meet you, "
                    f"{self.user_name}!"
                )

        return None


    def get_response(self, user_input):

        text = self.clean_input(user_input)

        self.message_count += 1

        if not text:
            return "Please say something!"

        name_response = self.remember_user_name(text)

        if name_response:
            return name_response

        if (
            "what is my name" in text
            or "what's my name" in text
            or "do you know my name" in text
        ):

            if self.user_name:
                return (
                    f"Your name is "
                    f"{self.user_name}."
                )

            return (
                "I don't know your name yet. "
                "You can tell me by saying "
                "'my name is ...'."
            )

        if "time" in text:
            return self.get_time()
        
        if "date" in text or "today" in text:
            return self.get_date()

        intent = self.detect_intent(text)

        if intent == "greeting":

            if self.user_name:
                return random.choice([
                    f"Hello, {self.user_name}!",
                    f"Hi {self.user_name}! How are you?",
                    f"Hey {self.user_name}!"
                ])

            return random.choice(
                RESPONSES["greeting"]
            )

        if intent == "how_are_you":
            return random.choice(
                RESPONSES["how_are_you"]
            )

        if intent == "name":
            return random.choice(
                RESPONSES["name"]
            )

        if intent == "thanks":
            return random.choice(
                RESPONSES["thanks"]
            )

        if intent == "help":
            return random.choice(
                RESPONSES["help"]
            )

        if intent == "positive":
            return random.choice(
                RESPONSES["positive"]
            )

        if intent == "negative":
            return random.choice(
                RESPONSES["negative"]
            )

        if intent == "goodbye":
            return random.choice(
                RESPONSES["goodbye"]
            )

        # Default response
        return (
            "I'm sorry, I don't understand that yet. "
            "Try asking me for help."
        )

    def show_statistics(self):
        """Display basic conversation statistics."""

        print("\n" + "=" * 40)
        print("CHAT STATISTICS")
        print("=" * 40)
        print(f"Messages received: {self.message_count}")

        if self.user_name:
            print(f"User name: {self.user_name}")
        else:
            print("User name: Not provided")

        print("=" * 40)


def chat():
    """Start the chatbot conversation."""

    bot = ChatBot()

    print("\n" + "=" * 45)
    print("             WELCOME TO PYBOT")
    print("=" * 45)

    print("PyBot: Hello! I'm PyBot.")
    print("PyBot: Type 'help' to see what I can do.")
    print("PyBot: Type 'bye' to end the conversation.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() in (
            "bye",
            "goodbye",
            "exit",
            "quit"
        ):

            response = bot.get_response(user_input)

            print(f"PyBot: {response}")

            bot.show_statistics()

            break

        response = bot.get_response(user_input)

        print(f"PyBot: {response}")


if __name__ == "__main__":
    chat()