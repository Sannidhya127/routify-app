import customtkinter
import heapq

class Routify(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # self.root = root
        self.tasks = []
        self.slots = []
        self.days = []
        self.tp = {}
        self.sp = {}

        self.title("Routify")
        self.geometry(f"{1368}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Routify", font=("California FB", 32, "bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="About", command=self.About)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.central_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", anchor="center")
        self.central_label.grid(row=0, column=3, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="New",command=self.NewRoutine)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        

    def clear_frame(self):
        for widget in self.central_label.winfo_children():
            widget.destroy()

    

    def NewRoutine(self):
        self.clear_frame()

        self.add_task_button = customtkinter.CTkButton(self.central_label, text="Add Task", command=self.AddTask, hover_color="dark blue")
        self.add_task_button.grid(row=1, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

        self.add_slot_button = customtkinter.CTkButton(self.central_label, text="Add Slot", command=self.AddSlot)
        self.add_slot_button.grid(row=2, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

        self.add_days_button = customtkinter.CTkButton(self.central_label, text="Add Days", command=self.AddDays, hover_color="dark blue")
        self.add_days_button.grid(row=3, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

        self.add_routine_button = customtkinter.CTkButton(self.central_label, text="Generate Routine", command=self.CreateRoutine, hover_color="dark blue")
        self.add_routine_button.grid(row=3, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

    def AddTask(self):
        self.task_name = customtkinter.CTkEntry(self.central_label, placeholder_text="Enter Task Name")
        self.task_name.grid(row=2, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

        self.task_priority = customtkinter.CTkEntry(self.central_label, placeholder_text="Enter Task Priority")
        self.task_priority.grid(row=3, column=0, padx=(100, 500), pady=(10, 0), sticky="w")
        task = self.task_name.get()
        task_priority = self.task_priority.get()
        print(task_priority)
        self.tasks.append((-task_priority, task))
        if task_priority not in self.tp:
            self.tp[task] = task_priority
        heapq.heapify(self.tasks)
        self.original_tasks = list(self.tasks)
        
    def AddSlot(self):

        self.slot_name = customtkinter.CTkEntry(self.central_label, placeholder_text="Enter Slot Name")
        self.slot_name.grid(row=4, column=0, padx=(100, 500), pady=(10, 0), sticky="w")

        self.slot_priority = customtkinter.CTkEntry(self.central_label, placeholder_text="Enter Slot Priority")
        self.slot_priority.grid(row=5, column=0, padx=(100, 500), pady=(10, 0), sticky="w")
        slot = self.slot_name.get()
        slot_priority = int(self.slot_priority.get())
        self.slots.append((-slot_priority, slot))
        if slot_priority not in self.sp:
            self.sp[slot] = slot_priority
        heapq.heapify(self.slots)

    
    def AddDays(self):

        self.days = customtkinter.CTkEntry(self.central_label, placeholder_text="Enter Days with space")
        self.days.grid(row=6, column=0, padx=(100, 500), pady=(10, 0), sticky="w")
        day = self.days.get()
        each_day = day.split(" ")
        for i in each_day:
            self.days.append(i)


    def CreateRoutine(self):
        self.AddTask()
        self.AddSlot()
        self.AddDays()
        return self.tasks, self.slots, self.days


    def About(self):
        abt = '''                                                   Hello User! Welcome to Routify, a simple and easy to use routine manager.
                                                                                    I developed this simple optimizaton tool to help you manage your daily tasks and routines.
                                                                    I hope you find it useful. Enjoy!'''

        self.central_label.configure(text=abt)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

app = Routify()

app.mainloop()