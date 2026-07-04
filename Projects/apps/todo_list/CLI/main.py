import json
import os
import time
import sys

animation = "|/-\\"

def loading_animation():
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

tasks = {}

try:
    with open('tasks.json', 'r') as json_file:
        tasks = json.load(json_file)
except FileNotFoundError:
    pass

no_of_tasks = len(tasks) + 1

while True:
    os.system('cls')
    print('''
    =======================Teja's Bandwidth==========================
    1. Add Task
    2. View / Edit Tasks
    3. Exit
        ''')
    user_input = int(input("Enter choice : "))
    
    if user_input == 1:
        data = input(f"Task {no_of_tasks} : ")
        tasks[no_of_tasks] = data
        no_of_tasks += 1
        
        with open('tasks.json', 'w') as json_file:
            json.dump(tasks, json_file)
        
    if user_input == 2:
        for key, val in tasks.items():
            print(f"| {key} | {val}")
            
        print('''===========================================================
              1.Delete Task
              2.back
              ''')
        ch = int(input("Enter Choice : "))
        if ch == 1:
            no = int(input("Enter task number : "))
            if no in tasks:
                del tasks[no]
                with open('tasks.json', 'w') as json_file:
                    json.dump(tasks, json_file)
            else:
                print("Task number not found.")
                
    if user_input == 3:
        print("Exiting...")
        loading_animation()
        print("\r ")
        break
