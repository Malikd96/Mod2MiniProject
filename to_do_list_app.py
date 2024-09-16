#To-Do List Application

#Welcome to the To-Do List App!

        #Menu:
        #1. Add a task
        #2. View tasks
        #3. Mark a task as complete
        #4. Delete a task
        #5. Quit

import argparse


task = []
status = []


def to_do_list_app():
   print("Welcome to the To Do List App! ")
   print("""
Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
         """)


def add_a_task():
   add = input("Add a task: ")
   task.append(add)
   status.append("Task not done")
   print("task added")

def view_tasks():
   if len(task) == 0:
      print("There are 0 tasks")
   else:
      print("Task")
      for i in range(len(task)):
         print(f'task: {task[i]}')
         print(f'Status: {status[i]}')

def completed_task():
   completed = input("Which task do you want as completed? ")
   D = task.index(completed)
   status[D] = 'completed'

def delete_task():
   delete = input("Delete a task: ")
   task.remove(delete)
   print("Task has been deleted. ")

while True:
        to_do_list_app()
        user = input('Please select a number 1-5: ')
        if user == '1':
            add_a_task()
        elif user == '2':
            view_tasks()
        elif user == '3':
            completed_task()
        elif user == '4':
            delete_task()
        elif user == '5':
            break