import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available!")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "[✔]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['task']}")

def add_task(tasks):
    """Add a new task."""
    task_name = input("\nEnter task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def mark_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
