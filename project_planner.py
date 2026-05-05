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
        self.current_frame = 1

        self.tasks_frame = Frame(parent)
        self.task_entry_frame = Frame(parent)
        
    #### Tasks Frame ####
        self.task_button = Button(
            self.tasks_frame,
            text="+",
            command=self.switch_frame
        )
        self.task_button.grid(row=len(self.tasks) + 1, column=0) # Show

        self.task_no_header = Label(
            self.tasks_frame,
            text="No.",
            borderwidth=1, 
            relief="solid",
            padx=5
        )
        self.task_no_header.grid(row=0, column=0)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            borderwidth=1, 
            relief="solid",
            padx=5
        )
        self.name_header.grid(row=0, column=1)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            borderwidth=1, 
            relief="solid",
            padx=5
        )
        self.status_header.grid(row=0, column=2)
        
        self.tasks_frame.grid() # Show

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
    def add_task(self):
        """
        """
        self.tasks.append(Task(self.task_name.get()))
        messagebox.showinfo("Task added", "Task has been succesfully added")
        self.output_tasks()
        self.switch_frame()


    def output_tasks(self):
        task_counter = 1
        for task in self.tasks:
            task_num = task_counter
            temp_name = task.t_name
            temp_status = task.status

            task_num_label =Label(
                self.tasks_frame,
                text=task_num,
                borderwidth=1, 
                relief="solid",
                padx=5
            )
            task_num_label.grid(row=task_counter, column=0)

            task_name_label = Label(
                self.tasks_frame,
                text=temp_name,
                borderwidth=1, 
                relief="solid",
                padx=5
            )
            task_name_label.grid(row=task_counter, column=1)

            task_status_label = Label(
                self.tasks_frame,
                text=temp_status,
                borderwidth=1, 
                relief="solid",
                padx=5
            )
            task_status_label.grid(row=task_counter, column=2)
            task_counter += 1

            self.task_button.grid(row=len(self.tasks) + 1, column=0)




    def switch_frame(self):
        """
        """
        # Gets frame
        frame = self.current_frame

        # Checks current frame and swictches accordingly
        if frame == 1:
            self.tasks_frame.grid_forget()
            self.task_entry_frame.grid()
            self.mac_frame_switch_handling(self.task_entry_frame)
            self.current_frame = 2
        elif frame == 2:
            self.task_entry_frame.grid_forget()
            self.tasks_frame.grid()
            self.mac_frame_switch_handling(self.tasks_frame)
            self.current_frame = 1
        


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