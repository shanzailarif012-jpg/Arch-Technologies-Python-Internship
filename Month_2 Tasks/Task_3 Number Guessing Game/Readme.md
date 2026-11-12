# 🎯 Number Guessing Game

A simple command-line Number Guessing Game built with Python.
The computer picks a random number between 1 and 100, and the player keeps guessing until they get it right. After every guess, the game gives a hint: **Too High** or **Too Low**.

> **Internship:** Arch Technologies, Python Development (Month 2, Task 3)
> **Author:** Muhammad Shanzail ([@dev_shanzail](https://github.com/shanzailarif012-jpg))

---

## ✨ Features

- Computer selects a random number from 1 to 100
- Hints after every guess (Too High / Too Low)
- Counts the number of attempts
- Input validation (text and out-of-range numbers are rejected)
- Play again option after each round
- Clean, function-based code structure

---

## 🛠️ Tech Stack

- Python 3.x
- `random` module (standard library, no extra installation needed)

---

## 📁 Project Structure

```
Month_2 Tasks/
└── Task_3_Number_Guessing_Game/
    ├── number_guessing_game.py
    └── README.md
    └── Screenshots

```

---

## 🚀 How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone the repository and open the project folder:
   ```bash
   git clone https://github.com/shanzailarif012-jpg/Arch-Technologies-Python-Internship/tree/main/Month_2%20Tasks/Task_3%20Number%20Guessing%20Game
   cd "Month_2 Tasks/Task_3_Number_Guessing_Game"
   ```
3. Run the game:
   ```bash
   python number_guessing_game.py
   ```

---

## 🎮 How to Play

1. The game starts and the computer picks a secret number between 1 and 100.
2. Enter your guess.
3. Read the hint and guess again:
   - **Too High**: your guess is bigger than the secret number
   - **Too Low**: your guess is smaller than the secret number
4. When you guess correctly, the game shows how many attempts you took.
5. Choose `yes` to play again or `no` to exit.

---

## 📸 Sample Output

```
Welcome Number Guessing Game
Please Enter a Number: abc
Invalid input, enter digit only
Please Enter a Number: 150
Enter a number between 1 to 100
Please Enter a Number: 50
Too High
Please Enter a Number: 25
Too Low
Please Enter a Number: 37
Correct! You guessed in 3 attempts
Play Again?? (yes/no): no
GoodBye
```


---

## 🧠 Code Overview

| Function | Purpose |
|---|---|
| `get_user_guess()` | Takes input, validates it (digits only, range 1 to 100) and returns a valid number |
| `play_game()` | Generates the secret number, runs the guessing loop, gives hints and counts attempts |
| `main()` | Shows the welcome message and handles the play-again loop |

### Concepts Used

- Functions and code organization
- `while` loops and `break`
- `if / elif / else` conditions
- Exception handling (`try / except ValueError`)
- Random number generation (`random.randint`)
- f-strings
- `if __name__ == "__main__":` entry point

---

## 🔮 Possible Improvements

- Difficulty levels (Easy / Medium / Hard)
- Limited number of attempts
- High score tracking
- GUI version using Tkinter or a web version using Flask

---

## 👨‍💻 Author

**Muhammad Shanzail**
GitHub: [dev_shanzail](https://github.com/dev_shanzail)

---

⭐ If you liked this project, give it a star!
