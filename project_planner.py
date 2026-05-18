from tkinter import * 
from tkinter import messagebox
import datetime


class Task:
    task_id_counter = 1

    def __init__(self, t_name, t_deadline, status="Unstarted"):
        self.task_id = Task.task_id_counter
        Task.task_id_counter += 1

        self.t_name = t_name
        self.t_deadline = t_deadline
        self.status = status


class ProjectBoardGUI:
    def __init__(self, parent):
    # Lists and Arrays
        self.status_colours = {
            "Unstarted": "tomato",
            "In progress": "darkorange2",
            "Finished": "black"
        }

        self.tasks = [

        ]

        self.statuses = [
            "Unstarted",
            "In progress",
            "Finished"
        ]

        self.status_values = {
            "Unstarted": 1,
            "In progress": 2,
            "Finished": 3
        }

    # Frames setup
        self.tasks_frame = Frame(parent)
        self.task_entry_frame = Frame(parent)
        self.task_deadline_entry_frame = Frame(self.task_entry_frame)
        self.edit_task_frame = Frame(parent)
        self.task_deadline_edit_frame = Frame(self.edit_task_frame)

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
            font = "Helvatica 13 bold"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            font = "Helvatica 13 bold"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            font = "Helvatica 13 bold"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)

        self.deadline_header = Label(
            self.tasks_frame,
            text="Deadline",
            font = "Helvatica 13 bold"
        )
        self.deadline_header.grid(row=0, column=3, padx=5, pady=5)

        
        self.tasks_frame.grid(padx=20, pady=5) # Show

    #### Task Entry Frame ####
        self.taskname_entry_label = Label(
            self.task_entry_frame,
            text="Task name",
            font="Helvetica 13 bold"
        )
        self.taskname_entry_label.grid(row=0, column=0)

        self.task_name = StringVar()
        self.taskname_entry = Entry(
            self.task_entry_frame,
            textvariable=self.task_name
        )
        self.taskname_entry.grid(row=0, column=1, pady=5) # Show

        self.deadline_label = Label(
            self.task_entry_frame,
            text="Deadline",
            font="Helvetica 13 bold"
        )
        self.deadline_label.grid(row=1, column=0)

        self.format_label1 = Label(
            self.task_deadline_entry_frame,
            text="/"
        )
        self.format_label2 = Label(
            self.task_deadline_entry_frame,
            text="/"
        )

        self.format_label1.grid(row=1, column=1)
        self.format_label2.grid(row=1, column=3)

        self.current_date = datetime.datetime.now()

        self.task_deadline_day = StringVar()
        self.task_deadline_day.set(self.current_date.strftime("%d"))
        self.deadline_day_entry = Spinbox(
            self.task_deadline_entry_frame,
            textvariable=self.task_deadline_day,
            width=2,
            from_=1,
            to=31
        )
        self.deadline_day_entry.grid(row=1, column=0)

        self.task_deadline_month = StringVar()
        self.task_deadline_month.set(self.current_date.strftime("%m"))
        self.deadline_month_entry = Spinbox(
            self.task_deadline_entry_frame,
            textvariable=self.task_deadline_month,
            width=2,
            from_=1,
            to=12
        )
        self.deadline_month_entry.grid(row=1, column=2)

        self.task_deadline_year = StringVar()
        self.task_deadline_year.set(self.current_date.strftime("%Y"))
        self.deadline_year_entry = Entry(
            self.task_deadline_entry_frame,
            textvariable=self.task_deadline_year,
            width=4
        )
        self.deadline_year_entry.grid(row=1, column=4)
        self.task_deadline_entry_frame.grid(row=1, column=1, sticky="w")

        self.confirm_task = Button(
            self.task_entry_frame,
            text="Add Task",
            command=self.add_task
       )
        self.confirm_task.grid(row=2, pady=5) # Show
            
        back_button = Button(
            self.task_entry_frame,
            text="Back",
            command=lambda: self.switch_frame(1)
        )

        back_button.grid(row=2, column=1, sticky="e", padx=5)


## Methods ##
    def check_task_name(self, entry):
        if entry.get().strip() == "":
            messagebox.showerror("Task Name Empty", "Task name is empty, name your task to add it.")
            entry.focus_set()
            return False
        return True

    def check_deadline(self, entry_widgets):
        for entry in entry_widgets:
            specific_entry = entry.get().strip()
            if specific_entry == "":
                messagebox.showerror("Deadline Empty", "One part of the deadline is left empty, fill it to add the task.")
                entry.focus_set()
                return False
            if not specific_entry.isdigit():
                messagebox.showerror("Invalid Character", "One part of the deadline contains an invalid character, remove it to add task.")
                entry.focus_set()
                return False
        try:
            deadline_string = f"{self.task_deadline_year.get()}-{self.task_deadline_month.get()}-{self.task_deadline_day.get()}"
            datetime.datetime.strptime(deadline_string, "%Y-%m-%d")
        except:
            messagebox.showerror("Invalid date", "The deadline date does not exist, fix it to add the task.")
            return False
        return True

    def edit_tasks_frame(self, wanted_task):
        self.switch_frame(3)
        for task in self.tasks:
            if task.task_id == wanted_task:
                specific_name = task.t_name
                specific_date = task.t_deadline

        self.taskname_edit_label = Label(
            self.edit_task_frame,
            text="Current Task Name",
            font="Helvetica 13 bold"
        )
        self.taskname_edit_label.grid(row=0, column=0)

        self.current_name = StringVar()
        self.current_name.set(specific_name)
        self.taskname_edit = Entry(
            self.edit_task_frame,
            textvariable=self.current_name
        )
        self.taskname_edit.grid(row=0, column=1, pady=5, padx=5) # Show

        self.deadline_edit_label = Label(
            self.edit_task_frame,
            text="Deadline",
            font="Helvetica 13 bold"
        )
        self.deadline_edit_label.grid(row=1, column=0)

        self.format_label3 = Label(
            self.task_deadline_edit_frame,
            text="/"
        )
        self.format_label4 = Label(
            self.task_deadline_edit_frame,
            text="/"
        )

        self.format_label3.grid(row=1, column=1)
        self.format_label4.grid(row=1, column=3)

        self.current_deadline_day = StringVar()
        self.current_deadline_day.set(specific_date.strftime("%d"))
        self.deadline_day_edit = Spinbox(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_day,
            width=2,
            from_=1,
            to=31
        )
        self.deadline_day_edit.grid(row=1, column=0)

        self.current_deadline_month = StringVar()
        self.current_deadline_month.set(specific_date.strftime("%m"))
        self.deadline_month_edit = Spinbox(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_month,
            width=2,
            from_=1,
            to=12
        )
        self.deadline_month_edit.grid(row=1, column=2)

        self.current_deadline_year = StringVar()
        self.current_deadline_year.set(specific_date.strftime("%Y"))
        self.deadline_year_edit = Entry(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_year,
            width=4
        )
        self.deadline_year_edit.grid(row=1, column=4)
        self.task_deadline_edit_frame.grid(row=1, column=1, sticky="w")

        self.edit_task_button = Button(
            self.edit_task_frame,
            text="Save",
            command=lambda: self.edit_task(wanted_task)
       )
        self.edit_task_button.grid(row=2, column=0, pady=5) # Show

        back_button = Button(
            self.edit_task_frame,
            text="Back",
            command=lambda: self.switch_frame(1)
        )

        back_button.grid(row=2, column=1, sticky="e", padx=5)



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
            font = "Helvatica 13 bold"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            font = "Helvatica 13 bold"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            font = "Helvatica 13 bold"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)

        self.deadline_header = Label(
            self.tasks_frame,
            text="Deadline",
            font = "Helvatica 13 bold"
        )
        self.deadline_header.grid(row=0, column=3, padx=5, pady=5)
        
        self.tasks_frame.grid(padx=20, pady=5) # Show


    def add_task(self):
        """
        """
        if self.check_deadline([self.deadline_day_entry, self.deadline_month_entry, self.deadline_year_entry]) and self.check_task_name(self.taskname_entry):
            deadline_day = int(self.task_deadline_day.get())
            deadline_month = int(self.task_deadline_month.get())
            deadline_year = int(self.task_deadline_year.get())
            saveable_date = datetime.datetime(deadline_year, deadline_month, deadline_day)
            self.tasks.append(Task(self.task_name.get(), saveable_date))
            messagebox.showinfo("Task Added", "Task has been succesfully added")
            self.clear_entries()
            self.output_tasks()
            self.switch_frame(1)


    def edit_task(self, target_edit):
         if self.check_deadline([self.deadline_day_edit, self.deadline_month_edit, self.deadline_year_edit]) and self.check_task_name(self.taskname_edit):
            deadline_day = int(self.current_deadline_day.get())
            deadline_month = int(self.current_deadline_month.get())
            deadline_year = int(self.current_deadline_year.get())
            saveable_date = datetime.datetime(deadline_year, deadline_month, deadline_day)
            for task in self.tasks:
                if target_edit == task.task_id:
                    task.t_name = self.current_name.get()
                    task.t_deadline = saveable_date
            messagebox.showinfo("Task Edited", "Changes have been saved")
            self.current_name.set("")
            self.current_deadline_day.set(self.current_date.strftime("%d"))
            self.current_deadline_month.set(self.current_date.strftime("%m"))
            self.current_deadline_year.set(self.current_date.strftime("%Y"))
            self.output_tasks()
            self.switch_frame(1)


    def output_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        self.output_tasks_frame()
        self.filter_tasks()
        task_counter = 1
        for task in self.tasks:
            temp_id = task.task_id
            temp_name = task.t_name
            temp_status = task.status
            temp_deadline = task.t_deadline
            self.text_colour = self.status_colours[task.status]

            task_num_label =Label(
                self.tasks_frame,
                text=temp_id,
                fg=self.text_colour
            )
            task_num_label.grid(row=task_counter, column=0)

            task_name_label = Label(
                self.tasks_frame,
                text=temp_name,
                fg=self.text_colour
            )
            task_name_label.grid(row=task_counter, column=1)

            self.current_status = StringVar()
            self.current_status.set(temp_status)
            task_status_menu = OptionMenu(
                self.tasks_frame,
                self.current_status,
                *self.statuses
            )
            
            task_status_menu.config(fg=self.text_colour)
            task_status_menu.grid(row=task_counter, column=2)
            
            formatted_date = f"{temp_deadline.strftime("%d")} {temp_deadline.strftime("%b")} {temp_deadline.strftime("%Y")}"
            task_deadline_label = Label(
                self.tasks_frame,
                text=formatted_date,
                fg=self.text_colour
            )
            task_deadline_label.grid(row=task_counter, column=3, padx=20)

            self.remove_task_button = Button(
                self.tasks_frame,
                text="-",
                command=lambda id=temp_id: self.remove_task(id)
            )
            self.remove_task_button.grid(row=task_counter, column=4)

            self.edit_task_button = Button(
                self.tasks_frame,
                text="Edit",
                command=lambda target=temp_id: self.edit_tasks_frame(target)
            )

            self.edit_task_button.grid(row=task_counter, column=5)

            self.current_status.trace_add("write", lambda *args, t=task_counter, s=self.current_status: self.update_task(t - 1, s, *args))
            task_counter += 1


            self.task_button.grid(row=len(self.tasks) + 1, column=0)


    def filter_tasks(self):   
        self.tasks.sort(key=lambda a_task: (self.status_values[a_task.status], a_task.t_deadline, a_task.task_id))
        #print("\n")
        #for task in self.tasks:
            #print(task.status)


    def remove_task(self, target_task):
        confirmation = messagebox.askyesno("Remove Task", "Are you sure you want to remove this task?")
        if confirmation:
            for task in self.tasks:
                if task.task_id == target_task:
                    self.tasks.remove(task)
                    self.output_tasks()
        else:
            return

    def clear_entries(self):
            self.task_name.set("")
            self.task_deadline_day.set(self.current_date.strftime("%d"))
            self.task_deadline_month.set(self.current_date.strftime("%m"))
            self.task_deadline_year.set(self.current_date.strftime("%Y"))


    def update_task(self, task_num, task_status, *args):
        self.tasks[task_num].status = task_status.get()
        self.output_tasks()
        #(self.tasks[task_num].status)

    def switch_frame(self, target_frame):
        """
        """
        # Checks target frame and switches accordingly
        if target_frame == 1:
            self.task_entry_frame.grid_forget()
            self.clear_entries()
            self.edit_task_frame.grid_forget()
            self.tasks_frame.grid(padx=20, pady=5)
            self.mac_frame_switch_handling(self.tasks_frame)
        elif target_frame == 2:
            self.tasks_frame.grid_forget()
            self.task_entry_frame.grid()
            self.mac_frame_switch_handling(self.task_entry_frame)
        elif target_frame == 3:
            self.tasks_frame.grid_forget()
            self.edit_task_frame.grid()
            self.mac_frame_switch_handling(self.edit_task_frame)
        


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
    root.option_add("*Font", "Helvetica 13")
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