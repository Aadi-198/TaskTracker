import sys
import json
from datetime import datetime

from db import tasks_file, load_tasks

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
            "createdAt": now
            }
        task_list.append(new_task)
        tasks_file.write_text(json.dumps(task_list, indent = 4))
        print(f"Successfully added task(s): {task}")
    else:
        print("Argument required: tasks")