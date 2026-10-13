def add_tasks():
    task = input("please enter your task(if you don't want to enter any task enter (done)) : " )
    return task

while True:
    priority = input("enter priority (low/medium/high): ").lower()
    if priority in ["low", "medium", "hight"]:
        break
    else:
        print("invalid priority, Please enter low, medium, or high")
