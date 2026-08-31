#import required libraries
import sys
import json
from pathlib import Path
from datetime import datetime

tasks_file = Path("tasks.json") #define the file where all the tasks are saved

#DRY appoach, define blocks -
def load_tasks():
    if tasks_file.exists():
        contents = tasks_file.read_text()
        task_list = json.loads(contents)
        #print("Contents: ", contents)  enable if you want contents to be printed everytime
        return task_list
    else:
        print("No file exists, starting with empty tasks.")
        return []

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
        print("You want to delete a task!")
        if len(sys.argv) > 2:
            task_id = int(sys.argv[2])
            task_list = load_tasks()
            tasks_file.write_text(json.dumps(task_list, indent=4))
            print(f"Successfully deleted task with ID: {task_id}")
        else:
            print("Argument required: task ID")
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")