from task import Task

tasks=[]

def add_task(title):
    task=Task(title)
    tasks.append(task)
    print(f"Added task: {title}")

def list_tasks():
    if not tasks:
        print("No tasks found")
        return
    for i, task in enumerate(tasks):
        status = "○" if not task.completed else "●"
        print(f"{i+1}) {status} {task.title}")
    
def complete_task(index):
    if 0<=index and index<len(tasks):
        tasks[index].mark_completed()
        print(f"Task completed: {tasks[index].title}")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0<=index and index<len(tasks):
        removed_task=tasks.pop(index)
        print(f"Deleted task: {removed_task.title}")
    else:
        print("Invalid task index.")

def summary():
    total=len(tasks)
    completed= sum(1 for task in tasks if task.completed)
    print(f"Summary: {completed} out of {total} tasks completed.")

#CLI for the to-do list application
def main():
    while True:
        print("\nTo-Do List\n1) Add Task\n2) List Tasks\n3) Complete Task\n4) Delete Task\n5) Summary\n6) Exit\n")
        choice= input("Choose an option: ")

        # Add a new task
        if choice=="1":
            title=input("Enter the task title: ")
            add_task(title)

        #Display all tasks
        elif choice=="2":
            list_tasks()

        #Mark a task as completed
        elif choice=="3":
            index=int(input("Enter the task number to mark as completed: "))-1
            complete_task(index)
        
        #Delete a task
        elif choice=="4":
            index=int(input("Enter the task number to delete: "))-1
            delete_task(index)
        

        #Display summary of tasks
        elif choice=="5":
            summary()

        #Exit the application
        elif choice=="5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()