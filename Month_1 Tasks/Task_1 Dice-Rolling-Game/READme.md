# 🎲 Dice Rolling Game

A simple command-line Python program that simulates rolling a pair of dice.
Built as **Month 1, Task 1** of the Python Programming Internship at **Arch Technologies**.

## Description

Each time the program rolls, it randomly generates two numbers between 1 and 6 (inclusive),
one for each die. It displays both results along with their total, then asks the user
whether they would like to roll again.

## Features

- Rolls two dice with random values from 1 to 6
- Displays each die and the total
- Asks the user to roll again (`yes` / `y` / `no` / `n`)
- Input is case-insensitive and ignores extra spaces
- Handles invalid input by asking again instead of crashing
- Clean, modular code split into small functions

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries (only the built-in `random` module)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/shanzailarif012-jpg/dice-rolling-game.git
   ```
2. Move into the project folder:
   ```bash
   cd dice-rolling-game
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Sample Output

```
Welcome Message
Die 1: 3 , Die 2: 5
Total:  8
Roll again? (yes/no): yes
Die 1: 6 , Die 2: 2
Total:  8
Roll again? (yes/no): maybe
Invalid Input, Please Type yes or no
Roll again? (yes/no): no
Goodbye
```

## How It Works

| Function | Purpose |
|---|---|
| `roll_dice()` | Generates and returns two random numbers (1 to 6) |
| `show_result(die1, die2)` | Prints each die and the total |
| `ask_roll_again()` | Asks the user to roll again and validates the answer |
| `main()` | Controls the game loop |

## Project Structure

```
dice-rolling-game/
├── main.py
├── README.md
└── screenshots/
```

## Author

**Muhammad Shanzail**
Python Programming Intern, Arch Technologies
GitHub: [@shanzailarif012-jpg](https://github.com/shanzailarif012-jpg)