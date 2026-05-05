from tkinter import * 
from tkinter import messagebox


class Task:
    def __init__(self, task_name, deadline, description, status):
        self.task_name = task_name
        self.deadline = deadline
        self.description = description
        self.status = status

class ProjectBoardGUI:
    def __init__(self, parent):
        self.tasks = [

        ]

        self.task_labels = [

        ]

        self.task_checkboxes = [

        ]

        self.current_frame = 1

        self.tasks_frame = Frame(parent)
        self.task_entry_frame = Frame(parent)
        
    # Tasks Frame #
        self.task_button = Button(
            self.tasks_frame,
            text="Add new task",
            command=self.switch_frame
        )
        self.task_button.grid() # Show

        
        self.tasks_frame.grid() # Show

    # Task Entry Frame #
        self.task_name = StringVar()
        self.taskname_entry = Entry(
            self.task_entry_frame,
            textvariable=self.task_name
        )
        self.taskname_entry.grid() # Show
       
        self.confirm_task = Button(
            self.task_entry_frame,
            text="Add Task",
            command=self.add_task
       )
        self.confirm_task.grid() # Show


    def add_task(self):
        """
        """
        # Create new task label widget
        grid_length = len(self.task_labels)
        new_task_label = Label(
            self.tasks_frame,
            text=self.task_name.get()
        )
        new_task_label.grid(row=grid_length + 1, column=0)
        
        # Create new checkbox
        new_task_checkbox = Checkbutton(
            self.tasks_frame
        )
        new_task_checkbox.grid(row=grid_length + 1, column=1)

        # Append to list for association with task label
        self.task_checkboxes.append(new_task_checkbox)
        # Adds new task label to task labels list to keep track of
        self.task_labels.append(new_task_label)
        self.switch_frame()


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