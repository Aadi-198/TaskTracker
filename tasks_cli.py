#import required libraries
import sys

from tasks_manager import add_tasks, list_tasks, delete_tasks, update_tasks, tasks_status

if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # call commands defined in task_manager.py
    if command == "add":
        add_tasks()
    elif command == "list":
        list_tasks()
    elif command == "delete":
            delete_tasks()
    elif command == "update":
        update_tasks()
    elif command == "status":
         tasks_status()
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")