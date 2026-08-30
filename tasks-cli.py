#import required libraries
import sys
import json
from pathlib import Path
from datetime import datetime

tasks_file = Path("tasks.json") #define the file where all the tasks are saved

#print("Arguments passed:", sys.argv)

# check if the typed script has an command and an input
if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # define what commands do
    if command == "add":
        #Check if user provided the suitable task to be added after the command
        if len(sys.argv) > 2:
            task = sys.argv[2]
            if tasks_file.exists():
                contents = tasks_file.read_text()
                list = json.loads(contents)
                print("Loaded tasks", list)
                print("Contents: ", contents)
            else:
                print("No file exists, starting with empty tasks.")
                list = []
            new_id = len(list) + 1
            now = datetime.now().isoformat()
            new_task = {
                "id": new_id,
                "description": task,
                "status": "todo",
                "createdAt": now
                }
            list.append(new_task)
            tasks_file.write_text(json.dumps(list, indent=4))
            print(f"Succesfully added task(s): {task}")
        else:
            print("Argument reqired: tasks")
    elif command == "list":
        if tasks_file:
            list = json.loads(tasks_file.read_text())
        else:
            print("No data about tasks exists !")
        for task in list:
            print(f"[{task['id']}] {task['description']} ({task['status']})")
    elif command == "delete":
        print("You want to delete a task!")
        if len(sys.argv) > 2:
            new_id = sys.argv[2]
            print(f"so you want to delete {new_id}")
            #json.loads I can't remember the sysntax to load the task, let me take help :)
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")