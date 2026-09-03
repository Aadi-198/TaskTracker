#import required libraries
import sys
import json
from datetime import datetime

from db import tasks_file, load_tasks, check_ID, task_exists
from tasks_manager import add_tasks, list_tasks, delete_tasks, update_tasks

#print("Arguments passed:", sys.argv)

# check if the typed script has an command and an input
if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # define what commands do
    if command == "add":
        add_tasks()
    elif command == "list":
        list_tasks()
    elif command == "delete":
            delete_tasks()
    elif command == "update":
        update_tasks()
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")