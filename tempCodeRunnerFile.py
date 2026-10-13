import os
from tasks import add_tasks
from dotenv import load_dotenv
load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do u want to open admin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password : ")

    if entered_password == admin_password:
        print("admin hi")
    else:
        print("wrong password")
name = input("whats your name?")
print("welcome", name)


tasks = []
while True:
    task = add_tasks()
    tasks.append(task)
    if task.lower() == "done":
        break

print("your task : ")
for task in tasks:
    print("- ", task)

with open("tasks.txt", "w") as file:
    file.write("\n".join(tasks))