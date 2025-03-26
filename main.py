print("This is my task app")


#CLI using argparse - try with sys lib

#flags to add task, remove, update, show and finish task
# e.g doomtask add "cook meal for wife's boyfriend" / doomtask update 1 -in_progress / doomtask remove 1 / doomtask show
# saved in JSON Dict - figure out how json works

import sys

if len(sys.argv) > 4:
    print("Too many arguments")
elif len(sys.argv) == 1:
    print("Too few arguments")
else:
    if sys.argv[1] == "add":
        #add(sys.argv[2])
        pass
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
        