# 🐍 Python Mini Projects

A collection of beginner-to-intermediate **Python projects** built to practice programming fundamentals, problem-solving, user interaction, file handling, and application design.

This repository contains three command-line applications:

1. 🎮 **Hangman Game**
2. 📈 **Stock Portfolio Tracker**
3. 🤖 **PyBot – Rule-Based Chatbot**

---

## 📂 Projects

| Project                    | File                     | Description                                    |
| -------------------------- | ------------------------ | ---------------------------------------------- |
| 🎮 Hangman Game            | `hangman.py`             | Interactive word-guessing game                 |
| 📈 Stock Portfolio Tracker | `stock_packet_tracer.py` | Portfolio management and investment calculator |
| 🤖 PyBot Chatbot           | `basic_chatbot.py`       | Rule-based conversational chatbot              |

---

# 🎮 1. Hangman Game

### 📄 File

```text
hangman.py
```

### 📝 Description

Hangman is a command-line word guessing game where the player attempts to discover a randomly selected word by guessing one letter at a time.

The game tracks incorrect guesses and displays an ASCII representation of the Hangman as the player makes mistakes.

### ✨ Features

* Randomly selects a word.
* Multiple words available for the game.
* Letter-by-letter guessing.
* Input validation.
* Prevents duplicate guesses.
* Tracks wrong guesses.
* Maximum of 6 incorrect guesses.
* ASCII Hangman graphics.
* Displays guessed letters.
* Detects winning and losing conditions.
* Allows the player to play multiple games.
* Tracks wins and losses.
* Displays final score.

### ▶️ Run the Game

```bash
python hangman.py
```

### 💻 Example

```text
========================================
          WELCOME TO HANGMAN
========================================

The word contains 8 letters.
You have 6 wrong guesses.

Word: _ _ _ _ _ _ _ _

Guess a letter: p

Good guess!

Word: p _ _ _ _ _ _ _
Wrong guesses remaining: 6
```

### 🧠 Concepts Practiced

* Lists
* Sets
* Functions
* Loops
* Conditional statements
* String manipulation
* Random selection
* Input validation
* Game logic
* State management

---

# 📈 2. Stock Portfolio Tracker

### 📄 File

```text
stock_packet_tracer.py
```

### 📝 Description

The Stock Portfolio Tracker is a command-line application that allows users to create and manage a simple stock portfolio.

Users can add stocks, remove stocks, view their portfolio, calculate the total investment value, view portfolio statistics, and export their portfolio to TXT or CSV format.

### ✨ Features

* Display available stocks and prices.
* Add stocks to a portfolio.
* Add multiple shares of the same stock.
* Remove stocks from the portfolio.
* Validate stock symbols.
* Validate share quantities.
* Calculate the value of individual holdings.
* Calculate total investment.
* Display portfolio statistics.
* Identify the largest portfolio position.
* Export portfolio as TXT.
* Export portfolio as CSV.
* Automatically generate timestamped filenames.
* Menu-driven interface.
* Handles invalid user input.

### 📊 Available Stocks

The application uses predefined stock prices:

```text
AAPL
TSLA
GOOG
AMZN
MSFT
NFLX
```

> **Note:** The prices are predefined values in the program. This project does not retrieve real-time stock market prices.

### ▶️ Run the Application

```bash
python stock_packet_tracer.py
```

### 💻 Example

```text
=============================================
       STOCK PORTFOLIO TRACKER
=============================================
1. View available stocks
2. Add stock to portfolio
3. View portfolio
4. Remove stock from portfolio
5. Save portfolio
6. Exit
=============================================

Enter your choice (1-6): 2
```

After adding stocks:

```text
============================================================
                 PORTFOLIO SUMMARY
============================================================
Symbol    Quantity    Price          Value
------------------------------------------------------------
AAPL      5           $180.00        $900.00
TSLA      2           $250.00        $500.00
------------------------------------------------------------
TOTAL INVESTMENT:                    $1400.00
============================================================
```

### 📁 Export

The portfolio can be saved in two formats:

```text
TXT
CSV
```

Example generated files:

```text
portfolio_summary_20260927_153000.txt
portfolio_summary_20260927_153000.csv
```

### 🧠 Concepts Practiced

* Dictionaries
* Functions
* Loops
* Input validation
* Exception handling
* File handling
* CSV processing
* Date and time
* Data calculations
* Menu-driven applications
* CRUD-style operations

---

# 🤖 3. PyBot – Rule-Based Chatbot

### 📄 File

```text
basic_chatbot.py
```

### 📝 Description

PyBot is a simple **rule-based chatbot** built using Python.

The chatbot identifies user input using keywords and predefined intents, then generates an appropriate response.

It also demonstrates basic conversation memory by remembering the user's name during the current session.

### ✨ Features

* Greeting responses.
* Name recognition.
* Remembers the user's name.
* Responds to "How are you?" questions.
* Provides the current time.
* Provides the current date.
* Responds to thank-you messages.
* Provides a help command.
* Handles positive and negative statements.
* Multiple responses for the same intent.
* Keyword-based intent detection.
* Input cleaning and normalization.
* Conversation statistics.
* Multiple exit commands.
* No external libraries required.

### 💬 Supported Examples

The chatbot can respond to inputs such as:

```text
hello
hi
hey
how are you?
what is your name?
my name is Anmisha
what is my name?
what time is it?
what is today's date?
thank you
help
I am happy
I am sad
bye
exit
quit
```

### ▶️ Run the Chatbot

```bash
python basic_chatbot.py
```

### 💻 Example Conversation

```text
=============================================
             WELCOME TO PYBOT
=============================================

PyBot: Hello! I'm PyBot.
PyBot: Type 'help' to see what I can do.
PyBot: Type 'bye' to end the conversation.

You: hello
PyBot: Hello! How can I help you?

You: my name is Anmisha
PyBot: Nice to meet you, Anmisha!

You: what is my name
PyBot: Your name is Anmisha.

You: how are you?
PyBot: I'm doing great! Thanks for asking.

You: what time is it?
PyBot: The current time is 03:30 PM.

You: thank you
PyBot: You're welcome!

You: bye
PyBot: Goodbye! Have a great day!
```

### 🧠 Concepts Practiced

* Classes
* Objects
* Dictionaries
* Lists
* Functions
* String processing
* Keyword matching
* Intent detection
* Random responses
* State management
* Date and time
* Loops
* Conditional statements

---

# 🛠️ Technologies Used

* **Python 3**
* Python Standard Library
* Command-Line Interface (CLI)

### Python Modules

| Module     | Project                 | Purpose               |
| ---------- | ----------------------- | --------------------- |
| `random`   | Hangman                 | Random word selection |
| `csv`      | Stock Portfolio Tracker | CSV file creation     |
| `datetime` | Stock Portfolio Tracker | Timestamp generation  |
| `datetime` | PyBot                   | Current date and time |

No third-party packages are required.

---

# 📁 Repository Structure

```text
python-mini-projects/
│
├── hangman.py
├── stock_packet_tracer.py
├── basic_chatbot.py
└── README.md
```

After running the Stock Portfolio Tracker, exported files may also appear:

```text
python-mini-projects/
│
├── hangman.py
├── stock_packet_tracer.py
├── basic_chatbot.py
├── portfolio_summary_YYYYMMDD_HHMMSS.txt
├── portfolio_summary_YYYYMMDD_HHMMSS.csv
└── README.md
```

---

# 🚀 Getting Started

## 1. Install Python

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 2. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd python-mini-projects
```

---

## 3. Run a Project

### Hangman

```bash
python hangman.py
```

### Stock Portfolio Tracker

```bash
python stock_packet_tracer.py
```

### PyBot

```bash
python basic_chatbot.py
```

---

# 🎯 Learning Objectives

These projects were created to practice important Python programming concepts.

### Beginner Concepts

* Variables
* Data types
* Strings
* Lists
* Dictionaries
* Sets
* Operators
* Conditions
* Loops
* User input

### Intermediate Concepts

* Functions
* Classes and objects
* Exception handling
* File handling
* CSV files
* Randomization
* Input validation
* State management
* Modular program structure

---

# 🔮 Future Improvements

## 🎮 Hangman

Possible future improvements:

* Add difficulty levels.
* Add word categories.
* Add hints.
* Add a scoring system.
* Add a high-score leaderboard.
* Load words from an external file.
* Add a graphical user interface.

## 📈 Stock Portfolio Tracker

Possible future improvements:

* Add real-time stock prices through a financial API.
* Add buy/sell transactions.
* Track purchase prices.
* Calculate profit and loss.
* Track transaction history.
* Store portfolio data permanently.
* Add portfolio performance charts.
* Add multiple user portfolios.

## 🤖 PyBot

Possible future improvements:

* Add more intents.
* Add more conversation patterns.
* Improve natural-language matching.
* Add a larger response database.
* Add conversation history.
* Add sentiment detection.
* Create a graphical interface.
* Connect the chatbot to an external AI API.

---

# ⚠️ Project Limitations

These projects are designed primarily for **learning and practice**.

### Hangman

The game uses a predefined collection of words rather than a large external dictionary.

### Stock Portfolio Tracker

Stock prices are predefined and are **not live market prices**. Therefore, the calculated investment values are examples for programming practice and should not be used for real investment decisions.

### PyBot

PyBot is a **rule-based chatbot**. It does not use machine learning or a large language model. Its responses are based on predefined keywords and responses.

---

# 📚 What I Learned

Through these projects, I practiced:

```text
Python Fundamentals
       ↓
Functions
       ↓
Data Structures
       ↓
Input Validation
       ↓
File Handling
       ↓
Object-Oriented Programming
       ↓
Application Logic
       ↓
Command-Line Applications
```

These projects demonstrate my progression from basic Python programming to building more structured interactive applications.

---

# 👩‍💻 AUTHOR

NONDRANA ANMISHA

Python projects created for learning, practice, and portfolio development.

#

This repository is intended for educational and learning purposes.
