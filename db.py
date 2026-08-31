import sys
import json
from pathlib import Path

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

def check_ID():
    if len(sys.argv) > 2:
        try:
            return int(sys.argv[2])
        except ValueError:
            print("ID must be a number amongst your tasks")
            sys.exit()
    else:
        print("Argument required: Task ID")
        sys.exit()