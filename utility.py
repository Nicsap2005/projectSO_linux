from central_function import LinuxOS
from ASCII_tree_documentation import tembelek
import tkinter as tk


class util():
    def __init__(self):
        self.show_dir_enabled = False
        self.dirButton = None
        
        self.show_available_dir_enabled = False
        self.available_dir_Button = None
        
        
        self.ubuntu = LinuxOS()
    
    def util_btn(self,Performances_instance,window,performances_label, graph_label):
        Performances_instance.elsebtn(performances_label, graph_label)
        self.dir_btn(window,performances_label,graph_label)
        self.avaliable_dir_btn(window,performances_label,graph_label)
    
    #################### dir ####################
    def update_dir(self, performances_label):
        run_command = self.ubuntu.get_current_path()
        text_label = f"current directory: {run_command}"
        performances_label.config(text = text_label , width = len(text_label)-5)

    def show_dir(self, performances_label, graph_label):
        performances_label.config(text="")
        graph_label.config(text="")
        self.update_dir(performances_label)

    def dir_btn(self, window, performances_label, graph_label):
        if self.dirButton is None:  # Check if the button exists
            self.dirButton = tk.Button(window, width=20, height=1, text='Show current Directory', borderwidth=2, relief='ridge', 
                                        command=lambda: self.show_dir(performances_label, graph_label))
            self.dirButton.grid(row=0, column=1)
        else:
            self.dirButton.grid(row=0, column=1)
    
    def remove_dir_btn(self):
        if self.dirButton is not None:
            self.dirButton.grid_forget()  # Hide the button
            self.dirButton = None  # Reset the button reference

    #################### avaliable directory ####################
    def update_avaliable_dir(self, performances_label):
        run_command = "".join(self.ubuntu.get_available_directories())
        text_label = f"avaliable directory: {run_command}"
        performances_label.config(text = text_label,width = len(text_label)-5)

    def show_avaliable_dir(self, performances_label, graph_label):
        performances_label.config(text="")
        graph_label.config(text="")
        self.update_avaliable_dir(performances_label)

    def avaliable_dir_btn(self, window, performances_label, graph_label):
        if self.available_dir_Button is None:  # Check if the button exists
            self.available_dir_Button = tk.Button(window, width=15, height=1, text='available Directory', borderwidth=2, relief='ridge', 
                                        command=lambda: self.show_avaliable_dir(performances_label, graph_label))
            self.available_dir_Button.grid(row=0, column=2)
        else:
            self.available_dir_Button.grid(row=0, column=2)
    
    def remove_avaliable_dir_btn(self):
        if self.available_dir_Button is not None:
            self.available_dir_Button.grid_forget()  # Hide the button
            self.available_dir_Button = None  # Reset the button reference
            
    #################### node_tree ####################
    
    
    #################### else_btn ####################
    def elsebtn(self, performances_label, graph_label):
        self.show_dir_enabled = False
        self.show_available_dir_enabled = False
        performances_label.config(text="")
        graph_label.config(text="")
        self.remove_dir_btn()
        self.remove_avaliable_dir_btn()
        