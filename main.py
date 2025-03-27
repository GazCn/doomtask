print("This is my task app")


#CLI using argparse - try with sys lib

#flags to add task, remove, update, show and finish task
# e.g doomtask add "cook meal for wife's boyfriend" / doomtask update 1 -in_progress / doomtask remove 1 / doomtask show
# saved in JSON Dict - figure out how json works

import sys
from tasks import Tasks
import json


def add_task(task):
    num = sum(1 for line in open("tasks_store.json"))
    new_task = {"task_massage": task, "task_number": (num + 1), "progress": "in progress", "status": "not finished"}
    with open("tasks_store.json", mode="r+") as file:
        file_data = json.load(file)
        file_data["tasks"].append(new_task)
        file.seek(0)
        json.dump(new_task, file, indent=4)
    

def main():
    if len(sys.argv) > 4:
        print("Too many arguments")
    elif len(sys.argv) == 1:
        print("Too few arguments")
    else:
        if sys.argv[1] == "add":
            add_task(sys.argv[2])
        elif sys.argv[1] == "remove":
            #remove(sys.argv[2])
            pass
        elif sys.argv[1] == "show":
            #show()
            pass
        elif sys.argv[1] == "finish":
            #finish(sys.argv[2])
            pass
        else:
            print("command not reconised")
        
if __name__ == '__main__':
    main()