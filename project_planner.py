"""This file creates and outputs tasks like a to do list.

It is essentially a project board where users can add, remove, edit, and read tasks
with deadlines and progress statuses so they know where they are at.
"""

from tkinter import *
from tkinter import messagebox
import datetime


class Task:
    """The framework that defines a task object.

    This class forms the outline for a task
    object to be saved, including, task_id, t_name,
    t_deadline, and t_status. Id is a counter that
    is created after a task object is initialised.
    It adds one for each task object created.
    """

    # Counter.
    task_id_counter = 1

    def __init__(self, t_name, t_deadline, status="Unstarted"):
        """Framework for the Task class.

        This takes creates instance variables during the
        creation of a Task object and saves data to them so
        it can be used later in the program.

        Parameters:
        t_name (str) -- the name of a task
        t_deadline (Date) -- the deadline of a task
        status (str) -- the current completion
        status of a task (default "Unstarted")
        """
        self.task_id = Task.task_id_counter
        # Adds one each time a task is initialised.
        Task.task_id_counter += 1

        self.t_name = t_name
        self.t_deadline = t_deadline
        self.status = status


class ProjectBoardGUI:
    """Form the GUI.

    This class forms the graphical user interface
    for the application. It holds methods that deal
    with input validation, task creation, task removal,
    task reading, and more.
    """
    def __init__(self, parent):
        """Create the GUI Foundation.

        This creates instance variables for widgets
        and data saving. Lays down the basic UI
        for the GUI, which can then later be adapted
        and changed through the methods in the
        class.
        """

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
            command=lambda: self.switch_frame(2)
        )
        self.task_button.grid(row=len(self.tasks) + 1, column=0)

        self.task_no_header = Label(
            self.tasks_frame,
            text="No.",
            font="Helvetica 13 bold"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            font="Helvetica 13 bold"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            font="Helvetica 13 bold"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)

        self.deadline_header = Label(
            self.tasks_frame,
            text="Deadline",
            font="Helvetica 13 bold"
        )
        self.deadline_header.grid(row=0, column=3, padx=5, pady=5)

        
        self.tasks_frame.grid(padx=20, pady=5)

    #### Task Entry Frame ####
        self.taskname_entry_label = Label(
            self.task_entry_frame,
            text="Task name",
            font="Helvetica 13 bold"
        )
        self.taskname_entry_label.grid(row=0, column=0)

        # Gets task name.
        self.task_name = StringVar()
        self.taskname_entry = Entry(
            self.task_entry_frame,
            textvariable=self.task_name
        )
        self.taskname_entry.grid(row=0, column=1, pady=5)

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

        # Gets current date.
        self.current_date = datetime.datetime.now()

        # Gets deadline day.
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

        # Gets deadline month.
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

        # Gets deadline year.
        self.task_deadline_year = StringVar()
        self.task_deadline_year.set(self.current_date.strftime("%Y"))
        self.deadline_year_entry = Entry(
            self.task_deadline_entry_frame,
            textvariable=self.task_deadline_year,
            width=4
        )
        self.deadline_year_entry.grid(row=1, column=4)
        self.task_deadline_entry_frame.grid(row=1, column=1, sticky="w")

        # Calls add task when clicked.
        self.confirm_task = Button(
            self.task_entry_frame,
            text="Add Task",
            command=self.add_task
       )
        self.confirm_task.grid(row=2, pady=5)
        
        # Returns to previous state when clicked.
        back_button = Button(
            self.task_entry_frame,
            text="Back",
            command=lambda: self.switch_frame(1)
        )

        back_button.grid(row=2, column=1, sticky="e", padx=5)


## Methods ##
    def check_task_name(self, entry):
        """Check task name validity.

        This method gets an entry widget and checks that the data
        inside is valid (not empty). Returns a boolean to prevent
        task from being added and sets focus to invalid entry.

        Parameters:
        entry (widget) -- the entry that is getting checked.

        Returns:
        (bool)
        """

        # Checks if entry is empty.
        if entry.get().strip() == "":
            messagebox.showerror("Task Name Empty", 
                                "Task name is empty, name your task to add it.")
            # Sets focus to the widget.
            entry.focus_set()
            return False
        return True


    def check_deadline(self, entry_widgets, vars):
        """Check deadline validity.

        This method gets a list of spinbox and entry widgets
        and checks if the data inside is valid. It
        returns a bool and sets the focus onto the concerned
        widget (if one).

        Parameters:
        entry_widgets (list) -- a list of entry and spinbox widgets.
        vars (list) -- a list of the vars holding day, month, and year.

        Returns:
        (bool)
        """

        # Checks each widget in entry_widgets.
        for entry in entry_widgets:
            # Gets and saves data, removing any spaces.
            specific_entry = entry.get().strip()
            # Checks if widget is empty.
            if specific_entry == "":
                messagebox.showerror("Deadline Empty", 
                                    "One part of the deadline is left empty, fill it to add the task.")
                entry.focus_set()
                return False
            # Checks if widget has something that is not a number.
            if not specific_entry.isdigit():
                messagebox.showerror("Invalid Character", 
                                    "One part of the deadline contains an invalid character, remove it to add task.")
                entry.focus_set()
                return False
        try:
            # Creates deadline string to check validity.
            deadline_string = f"{vars[0].get()}-{vars[1].get()}-{vars[2].get()}"
            # Tries to convert string to valid datetime object. 
            datetime.datetime.strptime(deadline_string, "%d-%m-%Y")
        # Handles when string is not able to be converted (invalid date).
        except:
            messagebox.showerror("Invalid date", 
                                "The deadline date does not exist, fix it to add the task.")
            return False
        return True

    def output_edit_task_frame(self, wanted_task):
        """Output edit task frame.

        This method gets the current data in a task
        that the user wants to edit and outputs them in
        spinbox and entry widgets. Gets updated
        data from user and calls edit_task.

        Parameters:
        wanted_task (int) -- the task id of the task 
        that the user wants to edit.
        """
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

        # Gets and saves changed name.
        self.current_name = StringVar()
        # Sets var in entry to current task name.
        self.current_name.set(specific_name)
        self.taskname_edit = Entry(
            self.edit_task_frame,
            textvariable=self.current_name
        )
        self.taskname_edit.grid(row=0, column=1, pady=5, padx=5)

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

        # Gets and saves changed deadline day.
        self.current_deadline_day = StringVar()
        # Sets var in spinbox to tasks current deadline day.
        self.current_deadline_day.set(specific_date.strftime("%d"))
        self.deadline_day_edit = Spinbox(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_day,
            width=2,
            from_=1,
            to=31
        )
        self.deadline_day_edit.grid(row=1, column=0)


        # Gets and saves changed deadline month.
        self.current_deadline_month = StringVar()
        # Sets var in spinbox to tasks current deadline month
        self.current_deadline_month.set(specific_date.strftime("%m"))
        self.deadline_month_edit = Spinbox(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_month,
            width=2,
            from_=1,
            to=12
        )
        self.deadline_month_edit.grid(row=1, column=2)

        # Gets and saves changed deadline year.
        self.current_deadline_year = StringVar()
        # Sets var in entry to tasks current deadline year.
        self.current_deadline_year.set(specific_date.strftime("%Y"))
        self.deadline_year_edit = Entry(
            self.task_deadline_edit_frame,
            textvariable=self.current_deadline_year,
            width=4
        )
        self.deadline_year_edit.grid(row=1, column=4)
        self.task_deadline_edit_frame.grid(row=1, column=1, sticky="w")

        # Calls method that saves edits.
        self.edit_task_button = Button(
            self.edit_task_frame,
            text="Save",
            command=lambda: self.edit_task(wanted_task)
       )
        self.edit_task_button.grid(row=2, column=0, pady=5) # Show

        # Returns to previous state when clicked.
        back_button = Button(
            self.edit_task_frame,
            text="Back",
            command=lambda: self.switch_frame(1)
        )

        back_button.grid(row=2, column=1, sticky="e", padx=5)



    def output_tasks_frame(self):
        """Output tasks frame.

        This method outputs the tasks frame. It is saved in a method
        so that when every widget from this gets deleted it is able to
        redraw them each time.
        """
        # Calls method to go to task_entry_frame.
        self.task_button = Button(
            self.tasks_frame,
            text="+",
            command=lambda: self.switch_frame(2)
        )
        self.task_button.grid(row=len(self.tasks) + 1, column=0) # Show

    # Headers #
        self.task_no_header = Label(
            self.tasks_frame,
            text="No.",
            font="Helvetica 13 bold"
        )
        self.task_no_header.grid(row=0, column=0, padx=5, pady=5)

        self.name_header = Label(
            self.tasks_frame,
            text="Task",
            font="Helvetica 13 bold"
        )
        self.name_header.grid(row=0, column=1, padx=5, pady=5)

        self.status_header = Label(
            self.tasks_frame,
            text="Status",
            font="Helvetica 13 bold"
        )
        self.status_header.grid(row=0, column=2, padx=5, pady=5)

        self.deadline_header = Label(
            self.tasks_frame,
            text="Deadline",
            font="Helvetica 13 bold"
        )
        self.deadline_header.grid(row=0, column=3, padx=5, pady=5)
        
        self.tasks_frame.grid(padx=20, pady=5)


    def add_task(self):
        """Create and add task object to tasks.

        This method calls the input validation methods
        and based on the bool they return either creates and then adds
        a task object to the tasks list. Or, it does not run and the
        error is handled by the validation methods.
        """
        if self.check_deadline([self.deadline_day_entry, self.deadline_month_entry, self.deadline_year_entry], 
                               [self.task_deadline_day, self.task_deadline_month, self.task_deadline_year]) and self.check_task_name(self.taskname_entry):
            deadline_day = int(self.task_deadline_day.get())
            deadline_month = int(self.task_deadline_month.get())
            deadline_year = int(self.task_deadline_year.get())
            saveable_date = datetime.datetime(deadline_year, deadline_month, deadline_day)
            self.tasks.append(Task(self.task_name.get(), saveable_date))
            messagebox.showinfo("Task Added", "Task has been successfully added")
            self.clear_entries()
            self.output_tasks()
            self.switch_frame(1)


    def edit_task(self, target_edit):
         """Edit task object.

         This method calls the input validation methods
         and edits the target task based on the bool they
         return.

         Parameters:
         target_edit (int) -- the task id of the task that the user wants to edit.
         """
         if self.check_deadline([self.deadline_day_edit, self.deadline_month_edit, self.deadline_year_edit],
                                [self.current_deadline_day, self.current_deadline_month, self.current_deadline_year]) and self.check_task_name(self.taskname_edit):
            deadline_day = int(self.current_deadline_day.get())
            deadline_month = int(self.current_deadline_month.get())
            deadline_year = int(self.current_deadline_year.get())
            saveable_date = datetime.datetime(deadline_year, deadline_month, deadline_day)
            # Finds target task object in tasks.
            for task in self.tasks:
                if target_edit == task.task_id:
                    # Edits deadline and task name.
                    task.t_name = self.current_name.get()
                    task.t_deadline = saveable_date
            messagebox.showinfo("Task Edited", "Changes have been saved")
            self.clear_entries()
            self.output_tasks()
            self.switch_frame(1)


    def output_tasks(self):
        """Output saved tasks.

        This method gets and outputs all of the saved task objects
        in the tasks list. It prints out their id number, name,
        status, and deadline.
        """

        # Clears all widgets in frame.
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        # Redraws headers and add task button.
        self.output_tasks_frame()
        # Sorts tasks list.
        self.filter_tasks()
        task_counter = 1
        for task in self.tasks:
            # Sets task data to temporary variables for output.
            temp_id = task.task_id
            temp_name = task.t_name
            temp_status = task.status
            temp_deadline = task.t_deadline
            self.text_colour = self.status_colours[task.status]

            task_num_label = Label(
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

            # Outputs and gets changes in a specific tasks status.
            self.current_status = StringVar()
            self.current_status.set(temp_status)
            task_status_menu = OptionMenu(
                self.tasks_frame,
                self.current_status,
                *self.statuses
            )
            
            # Changes option menu text colour based on status
            task_status_menu.config(fg=self.text_colour)
            task_status_menu.grid(row=task_counter, column=2)
            
            # Formats saved date for output.
            formatted_date = f"{temp_deadline.strftime("%d")} {temp_deadline.strftime("%b")} {temp_deadline.strftime("%Y")}"
            # Outputs deadline date.
            task_deadline_label = Label(
                self.tasks_frame,
                text=formatted_date,
                fg=self.text_colour
            )
            task_deadline_label.grid(row=task_counter, column=3, padx=20)

            self.remove_task_button = Button(
                self.tasks_frame,
                text="-",
                # Gets and saves task_id in case of future button click.
                command=lambda id=temp_id: self.remove_task(id)
            )
            self.remove_task_button.grid(row=task_counter, column=4)

            self.edit_task_button = Button(
                self.tasks_frame,
                text="Edit",
                # Gets and saves task_id in case of future button click.
                command=lambda target=temp_id: self.output_edit_task_frame(target)
            )

            self.edit_task_button.grid(row=task_counter, column=5)

            """Checks when current status is changed and updates the task objects
            (for this instance of the loop) saved status to the current status.
            """
            self.current_status.trace_add("write", lambda *args, t=task_counter, s=self.current_status: self.update_task(t - 1, s, *args))
            task_counter += 1

            self.task_button.grid(row=len(self.tasks) + 1, column=0)


    def filter_tasks(self):
        """Sort tasks list.

        This method sorts the tasks list based on task
        objects status, deadline, and then id.
        """
        self.tasks.sort(key=lambda a_task: (self.status_values[a_task.status], 
                                            a_task.t_deadline, a_task.task_id))



    def remove_task(self, target_task):
        """Remove target task.

        This method removes a user wanted task from the tasks
        list.

        Parameters:
        target_task (int) -- the task id of the task the user wants to remove.
        """
        confirmation = messagebox.askyesno("Remove Task", 
                                        "Are you sure you want to remove this task?")
        if confirmation:
            for task in self.tasks:
                if task.task_id == target_task:
                    self.tasks.remove(task)
                    self.output_tasks()
        else:
            return

    def clear_entries(self):
        """Clear entry vars.

        This method sets the vars associated with the main entry
        widgets to default.
        """
        self.task_name.set("")
        self.task_deadline_day.set(self.current_date.strftime("%d"))
        self.task_deadline_month.set(self.current_date.strftime("%m"))
        self.task_deadline_year.set(self.current_date.strftime("%Y"))


    def update_task(self, task_num, task_status, *args):
        """Update task status.

        This method is called when a tasks status (option menu)
        is changed, updating the saved status in the targeted task
        object to the recently changed status.

        Parameters:
        task_num (int) -- the targeted tasks list index number.
        task_status (string) -- the updated status of the task.
        *args (any) -- the remainder of what trace_add returns.
        """

        # Sets status to changed status.
        self.tasks[task_num].status = task_status.get()
        self.output_tasks()


    def switch_frame(self, target_frame):
        """Switch to target frame.
        
        This method gets the target frame and switches to it
        using grid and grid forget.
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
        AI code and comments below in order to fix issues with 
        macOS preventing frames from being redrawn correctly.
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
