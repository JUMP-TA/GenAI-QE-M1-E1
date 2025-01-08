import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file, or return an empty list if no file found."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title, description=""):
    """Add a new task to the JSON file."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "DONE" if task["completed"] else "PENDING"
        print(f"[{status}] {task['id']}: {task['title']} - {task['description']}")

def mark_task_completed(task_id):
    """Mark a task as completed by ID."""
    tasks = load_tasks()
    found_task = None
    for task in tasks:
        if task["id"] == task_id:
            found_task = task
            break

    if found_task:
        found_task["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} has been deleted.")

def filter_tasks(status):
    """Filter tasks by 'completed' or 'pending'."""
    tasks = load_tasks()

    if status not in ["completed", "pending"]:
        print(f"Unknown status: {status}")
        return

    if status == "completed":
        filtered = [task for task in tasks if task["completed"]]
    else:
        # Intentional bug: This condition should find tasks where completed == False
        # We'll incorrectly compare it to True, producing no tasks for "pending"
        filtered = [task for task in tasks if task["completed"] == True]

    if not filtered:
        print(f"No tasks found with status: {status}")
        return

    for task in filtered:
        print(f"[{'DONE' if task['completed'] else 'PENDING'}] {task['id']}: {task['title']} - {task['description']}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Filter Tasks (completed/pending)")
        print("6. Exit")

        choice = input("Enter a number: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_task_completed(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid number.")
        elif choice == "5":
            status = input("Enter status ('completed' or 'pending'): ")
            filter_tasks(status)
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
