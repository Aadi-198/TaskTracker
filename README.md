# TaskTracker

A simple command-line task management tool to organize and track your daily tasks.

## Features

- ✅ Add new tasks
- 📋 View all tasks
- ❌ Delete tasks by ID
- ✏️ Update existing tasks

# How to use ?

## Running the base script

**Mac / Linux** - *python3 tasks_cli.py*

**Windows** - *python tasks_cli.py*

## Add

Use to add a new task, simply write the 'add' command after the base script, then write the task you want to add

*python3 tasks_cli.py add milk*

## List

Use to see all the tasks stored by the user, add 'list' after base script

*python3 tasks_cli.py list*

## Delete

Use to delete an existing task by its ID, add 'delete' and include task ID

*python3 tasks_cli.py delete 1*

### Update

Use to update an existing task, add 'update', include task ID and then give the new task description

*python3 tasks_cli.py update 1 corn*
