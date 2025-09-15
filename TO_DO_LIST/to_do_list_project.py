import datetime
import database
welcome = "welcome to todo list app"

database.Create_table()
def prompt_add_tasks():
    id = int(input("enter the id:"))
    title = input("enyter the task")
    due_date = input("enter the due date in dd-mm-yyyy format")
    category = input("enter the category as (work,study or personal)")
    parsed_date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_tasks(id,title,timestamp,category)
def prompt_mark_complete():
    id = int(input("enter the id:"))
    database.set_complete(id)
def print_movies(heading,tasks):
    print(f"{heading} Tasks----")
    for task in tasks:
       
        print(f"id = {task[0]}   title = {task[1]} due_date = {task[2]} category = {task[3]} status = {task[4]}")


print(welcome)
menu = """
1. ADD THE TASKS
2. MARK TASK AS COMPLETED
3.VIEW COMPLETED TASKS
4.VIEW ALL TASKS
5.GET PENDING TASKS
6.CATEGORY FILTERING
7.EXIT
"""
while((user_input := input(menu)) !="7"):
    if user_input =="1":
        prompt_add_tasks()
        print("adding")

    elif user_input =="2":
        prompt_mark_complete()
        print("KEEP IT UP !!!")
    elif user_input =="3":
        tasks = database.get_completed_tasks()
        print_movies("completed",tasks)

    elif user_input =="4":
        tasks = database.display_tasks(False)
        print_movies("all",tasks)
    elif user_input =="5":
        tasks = database.get_upcoming_tasks()
        print("pending",tasks)
    elif user_input =="6":
        category = input("enter the category (work,personal,study)")
        tasks = database.category(category)
        print_movies("category",tasks)
    else:
        print("invalid input")





