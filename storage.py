import json
from task import Task

file_name="tasks.json"

def save_tasks(tasks):
    with open(file_name, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open(file_name, "r") as f:
            data_list=json.load(f)
            return [Task.from_dict(item) for item in data_list]
    except FileNotFoundError:
        return []
