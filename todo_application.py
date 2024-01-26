#Button(root, text="Check", command=show_selected_categories).pack() #7d0b3b
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

tasks = []

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error','Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values(?)', (task_string,))
        list_update()
        task_field.delete(0,'end')

def list_update():
    clear_list()
    for index, task in enumerate(tasks, start=1):
        task_listbox.insert('end', f"{index}. {task}")


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.delete(the_value)
            list_update()
            print("Delete")
            the_cursor.execute('delete from tasks where title =?',(the_value,))
            the_connection.commit()
    except:
        messagebox.showinfo('Error', 'No task selected. Cannot Delete!')


def clear_list():
    task_listbox.delete(0, 'end')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()
         
def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks)!=0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

#main function
        
if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Application")
    guiWindow.geometry("1000x750+750+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="#3b083b")

    the_connection = sql.connect('listofTask.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('Create table if not exists tasks (title text)')

    header_frame = tk.Frame(guiWindow, bg = "#3b083b")
    functions_frame = tk.Frame(guiWindow, bg = "#3b083b")
    listbox_frame = tk.Frame(guiWindow, bg = "#3b083b")


    header_frame.pack(fill = "both")
    functions_frame.pack(side = "left", expand = True, fill = "both")
    listbox_frame.pack(side = "right", expand = True, fill = "both")

    header_label = ttk.Label(
        header_frame,
        text = "To-Do List",
        font = ("Brush Script Mt", "50"),
        background = "#3b083b",
        foreground = "#FAEBD7"
    )

    header_label.pack(padx = 20, pady = 20)

    task_label = ttk.Label(
        functions_frame,
        text = "Enter the Task: ",
        font = ("Consolas", "20", "bold"),
        background= "#3b083b",
        foreground= "#FAEBD7"
    )

    task_label.place(x=30, y= 30)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", "20"),
        width=20,
        background = "#FFF8DC",
        foreground = "#A52A2A"
    )

    task_field.place(x=30, y=100)

    add_button = ttk.Button(
        functions_frame,
        text = "Add Task",
        width = 24,
        command=add_task
    )

    del_button = ttk.Button(
        functions_frame, 
        text = "Delete",
        width = 24,
        command = delete_task
    )

    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Clear All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )

    exit_button = ttk.Button(
        functions_frame,
        text = "Exit",
        width = 24,
        command = close
    )

    add_button.place(x=100, y=200, width=250, height=60)
    del_button.place(x=100, y=300, width=250, height=60)
    del_all_button.place(x=100, y=400, width=250, height=60)
    exit_button.place(x=100, y=500, width=250, height=60)


    task_listbox = tk.Listbox(
        listbox_frame,
        width=54,
        height= 25,
        font = ("arial", "20"),
        selectmode= 'SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground= "#cd853f",
        selectforeground= "#FFFFFF"
    )

    task_listbox.place(x=10, y=20)

    retrieve_database()  
    list_update()
    guiWindow.mainloop()
    the_connection.commit()  
    the_cursor.close()