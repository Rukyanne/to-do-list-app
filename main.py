# main.py - Complete To-Do List Application

# --- Storage Functions ---
def load_tasks():
    """Loads tasks from the tasks.txt file."""
    try:
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Saves the current tasks list to the tasks.txt file."""
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


# --- Core Logic Functions ---
def add_task(tasks, task_description):
    """Adds a new task, defaulting to incomplete status."""
    tasks.append(f"[ ] {task_description}")
    print(f"Added task: '{task_description}'")
    save_tasks(tasks)


def view_tasks(tasks):
    """Displays all tasks with their index and status."""
    if not tasks:
        print("Your To-Do list is empty!")
        return
    print("\n--- Current Tasks ---")
    # Display tasks starting from index 1 for user readability
    for i, task in enumerate(tasks):
        print(f"[{i + 1}] {task}")
    print("---------------------\n")


def mark_complete(tasks):
    """Allows the user to mark a task as complete."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark complete: "))
        index = task_num - 1

        if 0 <= index < len(tasks):
            if tasks[index].startswith("[X]"):
                print(f"Task {task_num} is already complete!")
            else:
                # Replace the incomplete marker ([ ]) with the complete marker ([X])
                tasks[index] = tasks[index].replace("[ ]", "[X]", 1)
                save_tasks(tasks)
                print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(tasks):
    """Allows the user to delete a task."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        index = task_num - 1

        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: '{deleted_task}'")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do App Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            description = input("Enter the new task description: ")
            add_task(tasks, description)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()