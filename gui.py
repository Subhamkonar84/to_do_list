import tkinter as tk
from tkinter import messagebox
from todo import *

def getpoint():
    file=open("choice.txt",'r')
    point=int(file.read())
    file.close()
    return point

def saveup(point):
    file=open("choice.txt",'w')
    file.write(str(point+1))
    file.close()

def savedown(point):
    file=open("choice.txt",'w')
    file.write(str(point-1))
    file.close()

def display():
    data=display_task()
    c=""
    for i in data:
        #for j in data:
        for iss in i:
            if iss==0:
                c=c+"          "+"NOT DONE"
                continue
            if iss==1 and c!="":
                c=c+"          "+"DONE"
            else:
                c=c+"          "+str(iss)
        listbox.insert(tk.END, c)
        c=""
        #entry.delete(0, tk.END)
        if i[2]==1:
            listbox.itemconfig(i[0]-1, {'bg':'light green', 'fg':'green'})


# Function to add a new task
def add_task():
    task = entry.get()
    if task:
        insert_task(task,getpoint())
        saveup(getpoint())
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        listbox.delete(0, tk.END)
        display()

    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def deletee_task():
    try:
        selected_task_index = listbox.curselection()[0]
        delete_task(int(selected_task_index)+1,getpoint())
        listbox.delete(selected_task_index)
        listbox.delete(0, tk.END)
        display()
        savedown(getpoint())
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def undo_task():
    try:
        selected_task_index = listbox.curselection()[0]
        undoo_task(int(selected_task_index)+1)
        listbox.itemconfig(selected_task_index, {'bg':'white', 'fg':'black'})
        listbox.delete(0, tk.END)
        display()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as undone!")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        done_task(int(selected_task_index)+1)
        listbox.itemconfig(selected_task_index, {'bg':'light green', 'fg':'green'})
        listbox.delete(0, tk.END)
        display()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed!")

# Create the main window
root = tk.Tk()
root.title("To Do List")
root.state('zoomed')



entry_label = tk.Label(root,text="Enter Task:")
entry_label.pack()
entry_label.place(x=7,y=10)


# Entry widget to add tasks
entry = tk.Entry(root, width=60)
entry.pack(padx=5, pady=10)


# Buttons to add, delete, and complete tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.TOP, padx=5)
undo_button = tk.Button(root, text="undo Task", command=undo_task)
undo_button.pack(side=tk.TOP, padx=5)
undo_button.place(x=1000,y=300)
delete_button = tk.Button(root, text="Delete Task", command=deletee_task)
delete_button.pack(padx=5)
delete_button.place(x=1000,y=250)
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(padx=5)
complete_button.place(x=1000,y=350)

# Listbox to display tasks
listbox = tk.Listbox(root, width=60, height=20)
listbox.pack(padx=10, pady=10)
display()


# Start the main loop
root.mainloop()
