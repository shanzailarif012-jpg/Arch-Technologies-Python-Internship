# 🏧 ATM Simulation

A simple command-line ATM Simulation built with Python using **Object-Oriented Programming (OOP)**.
Users can check their balance, deposit money and withdraw funds. The ATM logic lives in one class, and user interaction is handled by a separate controller class.

> **Internship:** Arch Technologies, Python Development (Month 2, Task 4)
> **Author:** Muhammad Shanzail ([@dev_shanzail](https://github.com/shanzailarif012-jpg))

---

## ✨ Features

- Check account balance
- Deposit money
- Withdraw money
- Invalid amount check (zero or negative amounts are rejected)
- Insufficient funds check on withdrawal
- Input validation (text input does not crash the program)
- Menu-driven interface that runs until the user chooses to exit
- Clear separation between logic (`ATM`) and interaction (`ATMController`)

---

## 🛠️ Tech Stack

- Python 3.x
- No external libraries required

---

## 📁 Project Structure

```
Month_2 Tasks/
└── Task_4 ATM Simulation/
    ├── atm_simulation.py
    ├── README.md
    └── screenshots/
```

---

## 🚀 How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone the repository and open the project folder:
   ```bash
   git clone <your-repo-link>
   cd "Month_2 Tasks/Task_4 ATM Simulation"
   ```
3. Run the program:
   ```bash
   python atm_simulation.py
   ```

---

## 🎮 How to Use

When the program starts, a menu is shown:

```
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

- Enter `1` to see your current balance
- Enter `2`, then type an amount to deposit
- Enter `3`, then type an amount to withdraw
- Enter `4` to exit

The ATM starts with a balance of `0`. You can change this in `main()` by editing `initial_balance`.

---

## 📸 Sample Output

```
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 2
Enter an amount: 500
Deposit successful
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 3
Enter an amount: 800
Insufficient funds
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 3
Enter an amount: 200
Withdrawal successful
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 1
Your balance: 300
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 4
Thank you for using the ATM
```


---

## 🧠 Code Overview

### `ATM` class (logic)

| Method | Purpose |
|---|---|
| `__init__(initial_balance=0)` | Sets the starting balance |
| `check_balance()` | Returns the current balance |
| `deposit(amount)` | Adds money if the amount is valid, returns `(True/False, message)` |
| `withdraw(amount)` | Subtracts money if the amount is valid and funds are enough, returns `(True/False, message)` |

### `ATMController` class (user interaction)

| Method | Purpose |
|---|---|
| `__init__(atm)` | Receives and stores the ATM object |
| `get_amount()` | Asks for an amount and validates the input |
| `show_menu()` | Prints the menu options |
| `run()` | Main loop: shows the menu, takes the choice and calls the ATM methods |

### `main()`

Creates the `ATM` object, passes it to `ATMController` and starts the program with `controller.run()`.

### Concepts Used

- Classes and objects
- Constructors (`__init__`)
- Methods and `self`
- Separation of concerns (logic vs user interface)
- Returning tuples (`success, message`)
- `while` loops and `break`
- `if / elif / else` conditions
- Exception handling (`try / except ValueError`)
- f-strings
- `if __name__ == "__main__":` entry point

---

## 🔮 Possible Improvements

- PIN authentication
- Transaction history
- Support for decimal amounts
- Multiple accounts
- Saving balance to a file or database
- GUI version (Tkinter) or web version (Flask)

---

## 👨‍💻 Author

**Muhammad Shanzail**
GitHub: [dev_shanzail](https://github.com/dev_shanzail)

---

⭐ If you liked this project, give it a star!