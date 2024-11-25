"""Task - Tracker CLI App"""
import json

#Creates json file to store tasks if it did no exist
TASK_FILE = "tasks.json"

def create_task_file():
    """Create task file function"""
    try:
        with open(TASK_FILE, 'r') as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)

create_task_file()

#Reads tasks from json file
def read_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

#Writes tasks to json file
def write_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)