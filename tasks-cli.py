#import required libraries
import sys
import json
from datetime import datetime

from db import tasks_file, load_tasks, check_ID

#print("Arguments passed:", sys.argv)

# check if the typed script has an command and an input
if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # define what commands do
    if command == "add":
        #Check if user provided the suitable task to be added after the command
        if len(sys.argv) > 2:
            task = sys.argv[2]
            task_list = load_tasks()
            max_id = max([t["id"] for t in task_list], default=0)
            new_id = max_id + 1
            now = datetime.now().isoformat()
            new_task = {
                "id": new_id,
                "description": task,
                "status": "todo",
                "createdAt": now
                }
            task_list.append(new_task)
            tasks_file.write_text(json.dumps(task_list, indent=4))
            print(f"Succesfully added task(s): {task}")
        else:
            print("Argument reqired: tasks")
    elif command == "list":
        task_list = load_tasks()
        for task in task_list:
            print(f"[{task['id']}] {task['description']} ({task['status']})")
    elif command == "delete":
            task_id = check_ID()
            task_list = load_tasks()
            task_list = [t for t in task_list if t["id"] != task_id]
            tasks_file.write_text(json.dumps(task_list, indent=4))
            print(f"Successfully deleted task with ID: {task_id}")
    elif command == "update":
        print("You want to update an task")
        task_id = check_ID()
        task_list = load_tasks()
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")