from tkinter import * 
from tkinter import messagebox


class Task:
    def __init__(self, t_name, status="Unstarted", description=None):
        self.t_name = t_name
        self.status = status
        self.description = description


class ProjectBoardGUI:
    def __init__(self, parent):
    # Lists
        self.tasks = [

        ]

        self.statuses = [
            "Unstarted",
            "In progress",
            "Finished"
        ]
        
    # Frames setup
        self.tasks_frame = Frame(parent)
        self.task_entry_frame = Frame(parent)
        
    #### Tasks Frame ####
        self.task_button = Button(
            self.tasks_frame,
            text="+",
            command= lambda: self.switch_frame(2)
        )
        self.task_button.grid(row=len(self.tasks) + 1, column=0) # Show

        self.task_no_header = Label(
            self.tasks_frame,
            text="No.",
            borderwidth=1, 
            relief="solid"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            borderwidth=1, 
            relief="solid"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            borderwidth=1, 
            relief="solid"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)
        
        self.tasks_frame.grid(padx=10, pady=10) # Show

    #### Task Entry Frame ####
        self.taskname_entry_label = Label(
            self.task_entry_frame,
            text="Task name"
        )
        self.taskname_entry_label.grid(row=0, column=0)

        self.task_name = StringVar()
        self.taskname_entry = Entry(
            self.task_entry_frame,
            textvariable=self.task_name
        )
        self.taskname_entry.grid(row=0, column=1) # Show

        self.confirm_task = Button(
            self.task_entry_frame,
            text="Add Task",
            command=self.add_task
       )
        self.confirm_task.grid(row=2) # Show

## Methods ##
    def output_tasks_frame(self):
        self.task_button = Button(
            self.tasks_frame,
            text="+",
            command= lambda: self.switch_frame(2)
        )
        self.task_button.grid(row=len(self.tasks) + 1, column=0) # Show

        self.task_no_header = Label(
            self.tasks_frame,
            text="No.",
            borderwidth=1, 
            relief="solid"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            borderwidth=1, 
            relief="solid"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            borderwidth=1, 
            relief="solid"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)
        
        self.tasks_frame.grid(padx=10, pady=10) # Show


    def add_task(self):
        """
        """
        self.tasks.append(Task(self.task_name.get()))
        messagebox.showinfo("Task added", "Task has been succesfully added")
        self.output_tasks()
        self.switch_frame(1)


    def output_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        self.output_tasks_frame()
        task_counter = 1
        for task in self.tasks:
            task_num = task_counter
            temp_name = task.t_name
            temp_status = task.status

            task_num_label =Label(
                self.tasks_frame,
                text=task_num,
                borderwidth=1, 
                relief="solid"
            )
            task_num_label.grid(row=task_counter, column=0)

            task_name_label = Label(
                self.tasks_frame,
                text=temp_name,
                borderwidth=1, 
                relief="solid"
            )
            task_name_label.grid(row=task_counter, column=1)

            self.current_status = StringVar()
            self.current_status.set(temp_status)
            task_status_menu = OptionMenu(
                self.tasks_frame,
                self.current_status,
                *self.statuses
            )
            task_status_menu.grid(row=task_counter, column=2)


            self.remove_task_button = Button(
                self.tasks_frame,
                text="-",
                command= lambda: self.remove_task(task_num - 1)
            )

            self.remove_task_button.grid(row=task_counter, column=3)

            self.current_status.trace_add("write", lambda *args, t=task_counter, s=self.current_status: self.update_task(t - 1, s, *args))
            task_counter += 1


            self.task_button.grid(row=len(self.tasks) + 1, column=0)

    def remove_task(self, target_task):
        self.tasks.pop(target_task)
        self.output_tasks()


    def update_task(self, task_num, task_status, *args):
        self.tasks[task_num].status = task_status.get()
        print(self.tasks[task_num].status)

    def switch_frame(self, target_frame):
        """
        """
        # Checks current frame and switches accordingly
        if target_frame == 1:
            self.task_entry_frame.grid_forget()
            self.tasks_frame.grid(padx=10, pady=10)
            self.mac_frame_switch_handling(self.tasks_frame)
        elif target_frame == 2:
            self.tasks_frame.grid_forget()
            self.task_entry_frame.grid()
            self.mac_frame_switch_handling(self.task_entry_frame)
        


    def mac_frame_switch_handling(self, target_frame):
        """
        AI code and comments below in order to fix issues with macOS preventing frames from being redrawn
        correctly.
        """
        target_frame.tkraise()             # Pull to front
        target_frame.update_idletasks()    # Redraw the widgets
        target_frame.focus_force()         # Grab keyboard focus
        
        # Tells the window to refresh its visual state immediately.
        target_frame.master.update()
        """
        End of AI code.
        """




if __name__ == "__main__":
    root = Tk()
    root.title("Project Board")
    app = ProjectBoardGUI(root)
    root.mainloop()
    


















"""
Class: Task:
    methods:
        instance vars:
            task name
            task deadline
            task description
            Task status

Class: Project Board GUI
    methods:
        instance variables/widgets:
            list of tasks
            3 main frames for different statuses.
            Editable label title label at top. 
            Tickboxes for if finished.
            Button to add more tasks
            Button to clear list
            Labels (later buttons) for each task. 
            Task entry frame:
                Entry for task name
                Entry for task deadline
                Entry for task status
                Entry for task description.
                add task button
                    run add task method
                


        add task:
            create new task object with entered data
            add to list of tasks
            show confirmation message that task has been saved and added.
            reconfigure output frame with new task
            switch back to output frame

            
        remove task:
            determine which task wants to be removed and determine its list index
            remove task from list
            remove task from output frame
            show confirmation message
            reconfigure output frame
            switch back to output frame

"""