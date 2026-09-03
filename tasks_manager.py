import sys
import json
from datetime import datetime

from db import tasks_file, load_tasks, check_ID, task_exists

def add_tasks():
    if len(sys.argv) > 2:
        task = sys.argv[2]
        task_list = load_tasks()
        max_id = max([t["id"] for t in task_list], default = 0)
        new_id = max_id + 1
        now = datetime.now().isoformat()
        new_task = {
            "id": new_id,
            "description": task,
            "status": "todo",
            "createdAt": now,
            "updatedAt": now
            }
        task_list.append(new_task)
        tasks_file.write_text(json.dumps(task_list, indent = 4))
        print(f"Successfully added task(s): {task}")
    else:
        print("Argument required: tasks")

def list_tasks():
    task_list = load_tasks()
    for task in task_list:
        print(f"[{task['id']}] {task['description']} ({task['status']})")

def delete_tasks():
    task_id = check_ID()
    if not task_exists(task_id):
        sys.exit()  
    else:
        task_list = load_tasks()
        task_list = [t for t in task_list if t["id"] != task_id]
        tasks_file.write_text(json.dumps(task_list, indent = 4))
        print(f"Successfully deleted task with ID: {task_id}")

def update_tasks():
    task_id = check_ID()
    if not task_exists(task_id):
        sys.exit()
    else:
        if len(sys.argv) > 3:
            new_description = sys.argv[3]
            task_list = load_tasks()
            for task in task_list:
                if task["id"] == task_id:
                    task["updatedAt"] = datetime.now().isoformat()
                    task["description"] = new_description
                    tasks_file.write_text(json.dumps(task_list, indent = 4))
                    print(f"Successfully updated task {task_id} to {new_description}")
        else:
            print("Argument required: new description")

def tasks_status():
    task_id = check_ID()
    if not task_exists(task_id):
        sys.exit()  
    else:
        if len(sys.argv) > 3:
            task_status = sys.argv[3]
            if task_status != "done" and task_status != "todo":
                print("Status not recognised: use 'done' or 'todo'")
            else:
                task_list = load_tasks()
                for task in task_list:
                    if task["id"] == task_id:
                        task["status"] = task_status
                        tasks_file.write_text(json.dumps(task_list, indent = 4))
                        print(f"Successfully updated task {task_id} to  status '{task_status}'")
        else:
            print("Argument required: status")

def list_done():
    task_list = load_tasks()
    for task in task_list:
        if task["status"] == "done":
            print(f"[{task['id']}] {task['description']} ({task['status']})")

def list_todo():
    task_list = load_tasks()
    for task in task_list:
        if task["status"] == "todo":
            print(f"[{task['id']}] {task['description']} ({task['status']})")