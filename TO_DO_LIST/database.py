import sqlite3
import datetime
connection = sqlite3.connect("tasks.db")
create_table = """ 
CREATE TABLE IF NOT EXISTS task(
id INTEGER,
title TEXT,
due_date REAL,

category TEXT,
completed INTEGER
);
"""
add_item = "INSERT INTO task(id,title,due_date,category,completed) VALUES(?,?,?,?,0);"
select_completed  = "select * from task where completed = 1;"
select_all_tasks = "select * from task;"
select_upcoming = "select * from task where completed =0 and due_date < ?;"
mark_completed = "UPDATE task set completed =1 where id = ?;"
category_based = "SELECT * FROM task where category = ?;"
def category(category_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(category_based,(category_name,))
        return cursor.fetchall()
def Create_table():
    with connection:
        connection.execute(create_table)
def add_tasks(id,title,due_date,category):
    with connection:
        connection.execute(add_item,(id,title, due_date,category))
def get_completed_tasks():
    with connection:
        cursor = connection.cursor()
        cursor.execute(select_completed)
        return cursor.fetchall()
def get_upcoming_tasks():
    with connection:
        today_date = datetime.datetime.today().timestamp()
        cursor = connection.cursor()
        cursor.execute(select_upcoming,(today_date,))
        return cursor.fetchall()

def set_complete(id):
    with connection:
        connection.execute(mark_completed,(id,))
def display_tasks(upcoming):
    with connection:
        if upcoming:
            return get_upcoming_tasks()
        else:
            cursor = connection.cursor()
            cursor.execute(select_all_tasks)
            return cursor.fetchall()





