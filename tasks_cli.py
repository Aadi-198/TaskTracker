#import required libraries
import sys
import json
from datetime import datetime

from db import tasks_file, load_tasks, check_ID, task_exists
from tasks_manager import add_tasks

#print("Arguments passed:", sys.argv)

# check if the typed script has an command and an input
if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # define what commands do
    if command == "add":
        add_tasks()
    elif command == "list":
        task_list = load_tasks()
        for task in task_list:
            print(f"[{task['id']}] {task['description']} ({task['status']})")
    elif command == "delete":
            task_id = check_ID()
            if not task_exists(task_id):
                sys.exit()  
            else:
                task_list = load_tasks()
                task_list = [t for t in task_list if t["id"] != task_id]
                tasks_file.write_text(json.dumps(task_list, indent = 4))
                print(f"Successfully deleted task with ID: {task_id}")
    elif command == "update":
        task_id = check_ID()
        if not task_exists(task_id):
            sys.exit()  
        else:
            if len(sys.argv) > 3:
                new_description = sys.argv[3]
                task_list = load_tasks()
                for task in task_list:
                    if task["id"] == task_id:
                        task["createdAt"] = datetime.now().isoformat()
                        task["description"] = new_description
                        tasks_file.write_text(json.dumps(task_list, indent = 4))
                        print(f"Successfully updated task {task_id} to {new_description}")
            else:
                print("Argument required: new description")
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")