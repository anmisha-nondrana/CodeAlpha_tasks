import random

# -----------------------------
# Game Configuration
# -----------------------------

WORDS = [
    "python",
    "hangman",
    "computer",
    "developer",
    "keyboard",
    "programming",
    "software",
    "algorithm",
    "database",
    "internet",
]

MAX_WRONG_GUESSES = 6

HANGMAN_PICS = [
    """
     ------
     |    |
          |
          |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
          |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |    |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|
          |
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
          |
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
          |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
          |
    ---------
    """
]


# -----------------------------
# Helper Functions
# -----------------------------

def choose_word():
    """Select a random word from the word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """
    Display guessed letters and underscores
    for letters that have not been guessed.
    """
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def get_guess(guessed_letters):
    """Get and validate a letter from the player."""

    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.\n")
            continue

        if not guess.isalpha():
            print("Please enter a letter, not a number or symbol.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        return guess


def display_game_state(word, guessed_letters, wrong_guesses):
    """Display the current state of the game."""

    print(HANGMAN_PICS[wrong_guesses])
    print("Word:", display_word(word, guessed_letters))

    remaining = MAX_WRONG_GUESSES - wrong_guesses
    print(f"Wrong guesses remaining: {remaining}")

    if guessed_letters:
        print(
            "Guessed letters:",
            ", ".join(sorted(guessed_letters))
        )

    print()


def has_won(word, guessed_letters):
    """Return True if every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


# -----------------------------
# Main Game
# -----------------------------

def play_hangman():
    """Run one game of Hangman."""

    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("          WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"The word contains {len(word)} letters.")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:

        display_game_state(
            word,
            guessed_letters,
            wrong_guesses
        )

        # Check whether player has won
        if has_won(word, guessed_letters):
            print(f"🎉 Congratulations! You guessed: {word}")
            return True

        guess = get_guess(guessed_letters)

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")

    # Game over
    print(HANGMAN_PICS[wrong_guesses])
    print(f"💀 Game over!")
    print(f"The word was: {word}")

    return False


# -----------------------------
# Replay System
# -----------------------------

def play_again():
    """Ask the player whether they want another game."""

    while True:
        answer = input("\nPlay again? (y/n): ").lower().strip()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please enter 'y' or 'n'.")


def main():
    """Start and control the Hangman application."""

    wins = 0
    games = 0

    while True:

        result = play_hangman()

        games += 1

        if result:
            wins += 1

        print("\n" + "-" * 40)
        print(f"Games played: {games}")
        print(f"Wins: {wins}")
        print(f"Losses: {games - wins}")
        print("-" * 40)

        if not play_again():
            break

    print("\nThanks for playing Hangman!")
    print(f"Final score: {wins}/{games} wins.")


# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()
