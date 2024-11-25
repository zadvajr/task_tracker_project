"""Task - Tracker CLI App"""
import json
from datetime import datetime

#Creates json file to store tasks if it did no exist
TASK_FILE = "tasks.json"

def create_task_file():
    """Create task file function"""
    try:
        with open(TASK_FILE, 'r', encoding='utf-8') as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(TASK_FILE, 'w', encoding='utf-8') as file:
            json.dump([], file)

create_task_file()

#Reads tasks from json file
def read_tasks():
    """read tasks function"""
    with open(TASK_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

#Writes tasks to json file
def write_tasks(tasks):
    """write tasks function"""
    with open(TASK_FILE, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

#generates tasks id
def generate_task_id(tasks):
    """generate task"""
    return max([task['id'] for task in tasks], default=0) + 1

def current_time():
    """current time"""
    return datetime.now().isoformat()

#add task
def add_task(description):
    """add task"""
    tasks = read_tasks()
    new_task = {
        "id": generate_task_id(tasks),
        "description": description,
        "status": "todo",
        "created_at": current_time(),
        "updated_at": current_time(),
    }
    tasks.append(new_task)
    write_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

#update task
def update_task(task_id, description):
    """Update task"""
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updated_at'] = current_time()
            write_tasks(tasks)
            print(f"Task {task_id} updated successfully!")
            return
    print(f"Task {task_id} not found!")

#delete task
def delete_task(task_id):
    """delete task"""
    tasks = read_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) < len(tasks):
        write_tasks(updated_tasks)
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task {task_id} not found!")

#change task status
def change_status(task_id, status):
    """change task status"""
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['uptaded_at'] = current_time()
            write_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task {task_id} not found.")

#list tasks
def list_tasks(status=None):
    """list tasks"""
    tasks = read_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} \
               (Created: {task['created_at']})")
    if not tasks:
        print("No tasks found.")
