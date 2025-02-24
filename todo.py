import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}  # Ensuring correct structure

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)  # Pretty print JSON
    except Exception as e:
        print(f"Error saving tasks: {e}")

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if not task_list:
        print("\nNo tasks to display.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(task_list, start=1):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx}. {task['description']} {status}")

def create_task(tasks):
    description = input("\nEnter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    if not tasks["tasks"]:
        print("\nNo tasks available to complete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("\nEnter the task number to mark as complete: ").strip()) - 1
        if 0 <= task_number < len(tasks["tasks"]):
            tasks["tasks"][task_number]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number. Please enter a valid one.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()  
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
