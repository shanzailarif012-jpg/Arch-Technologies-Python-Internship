# 📝 To-Do List Application

A simple command-line To-Do List application written in Python.
Built as **Month 1, Task 2** of the Python Programming Internship at **Arch Technologies**.

## Description

The program lets the user add tasks, view the current list, and remove tasks once they are
completed. After every action it displays a progress bar showing how many of the added
tasks have been completed.

## Features

- Add new tasks (empty tasks are rejected)
- View all current tasks as a numbered list
- Remove a task by its number once it is completed
- Progress bar with percentage, updated after every action
- Input validation: invalid menu options, non-numeric input and out-of-range task numbers are handled without crashing
- Clean, modular code split into small functions

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/shanzailarif012-jpg/Arch-Technologies-Python-Internship.git
   ```
2. Move into the task folder:
   ```bash
   cd "Arch-Technologies-Python-Internship/Month_1 Tasks/Task_2 To-Do-List"
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Menu Options

| Option | Action |
|---|---|
| 1 | Add a task |
| 2 | View all tasks |
| 3 | Remove a completed task |
| 4 | Exit the program |

## Sample Output

```
Options: 1. Add
2. View
3. Remove
4. Exit
Enter Task Choice: 1
Enter task: Buy milk
Task Added
░░░░░░░░░░░░░░░░░░░░
Progress: 0.0%
...
Enter Task Choice: 1
Enter task: Study Python
Task Added
░░░░░░░░░░░░░░░░░░░░
Progress: 0.0%
...
Enter Task Choice: 3
1 Buy milk
2 Study Python
Enter task number: 1
Task Completed and Removed
██████████░░░░░░░░░░
Progress: 50.0%
...
Enter Task Choice: 4
GoodBye TakeCare
```

The menu is shown again before every choice. It is trimmed here with `...` to keep the sample short.

## How the Progress Bar Works

- The program counts every task that was added (`total_added`) and every task that was completed and removed (`completed`)
- Progress = `completed / total_added × 100`
- The bar is 20 characters long: `█` for the completed part and `░` for the remaining part
- If no task has been added yet, progress is shown as 0%

## How It Works

| Function | Purpose |
|---|---|
| `add_task()` | Adds a new task after checking it is not empty |
| `view_tasks()` | Prints the numbered list of tasks |
| `remove_task()` | Removes a task by number and counts it as completed |
| `show_progress()` | Calculates and prints the progress bar |
| `show_menu()` | Prints the menu options |
| `main()` | Controls the menu loop |

## Note

Tasks are stored in memory only, so the list and the progress reset when the program closes.

## Project Structure

```
Task_2 To-Do-List/
├── main.py
├── READme.md
└── Screenshots/
```

## Author

**Muhammad Shanzail**
Python Programming Intern, Arch Technologies
GitHub: [@shanzailarif012-jpg](https://github.com/shanzailarif012-jpg)