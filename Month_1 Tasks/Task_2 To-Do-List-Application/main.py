# Task 2 To-Do-List Application 

tasks = []
total_added = 0
completed = 0

def add_task():
    global total_added
    text =input("Enter task: ").strip()
    if text == "":
        print("Task Cannot be empty")
        return
    tasks.append(text)
    total_added = total_added + 1
    print("Task Added")


def view_tasks():
    if tasks == []:
        print("No Task yet")
        return
    
    for number, task in enumerate(tasks, start=1):
        print(number, task)


def remove_task():
    global completed
    if tasks == []:
        print("Nothing to remove")
        return
    view_tasks()
    try:
        choice = int(input("Enter task number: "))
    except ValueError:
        print("Invalid number")
        return

    if choice < 1 or choice > len(tasks):
        print("Invalid number")
        return
    
    tasks.pop(choice - 1)
    completed = completed + 1
    print("Task Completed and Removed")


def show_progress():
    if total_added == 0:
        percent = 0
    else:
        percent = completed / total_added * 100
    filled = int(percent / 100 * 20)
    empty = 20 - filled
    print("█" * filled + "░" * empty)
    print(f"Progress: {percent:.1f}%")


def show_menu():
    print("Options: 1. Add\n2. View\n3. Remove\n4. Exit")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter Task Choice: "))
        except ValueError:
            print("Invalid Option! Please enter a number.")
            continue
        if choice == 1: add_task()
        elif choice == 2: view_tasks()
        elif choice == 3: remove_task()
        elif choice == 4: break
        else:
            print("Invalid Option")
        show_progress()
    print("GoodBye TakeCare")


if __name__ == "__main__":
    main()


