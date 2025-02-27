import sys
import json

tasks = []

def add_task(description):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "pending"})
    print(f"Task added with ID {task_id}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def update_task(task_id, new_status):
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = new_status
            print(f"Task {task_id} updated to {new_status}")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != int(task_id)]
    print(f"Task {task_id} deleted.")

def save_tasks(filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print(f"Tasks saved to {filename}")

def load_tasks(filename):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        print(f"Tasks loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    elif command == "view":
        view_tasks()
    elif command == "update" and len(sys.argv) == 4:
        update_task(sys.argv[2], sys.argv[3])
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(sys.argv[2])
    elif command == "save" and len(sys.argv) == 3:
        save_tasks(sys.argv[2])
    elif command == "load" and len(sys.argv) == 3:
        load_tasks(sys.argv[2])
    else:
        print("Invalid command or arguments.")
