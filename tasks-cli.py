#import required libraries
import sys

print("Arguments passed:", sys.argv)

# check if the typed script has an command and an input
if len(sys.argv) > 1:
    command = sys.argv[1]   #if script has a command, save it in a var called command
    # define what commands do
    if command == "add":
        print("You want to add an task")
    elif command == "list":
        print("You want to see the list")
    else:
        print(f"{command}: command not found")
else:
    print("Argument required: command")