import tkinter as tk
from performances import Performances_stat
from utility import util

def performances_btn_function(performance_instance, window, performances_label, graph_label):
    utility_instance.elsebtn( performances_label, graph_label)
    performance_instance.performances_btn(window, performances_label, graph_label)
    
def utility_btn_function(performance_instance, window, performances_label, graph_label):
    performance_instance.elsebtn(performances_label, graph_label)
    utility_instance.util_btn(performance_instance, window, performances_label, graph_label)

def else_btn_function(performances_label, graph_label):
    utility_instance.elsebtn( performances_label, graph_label)
    performance_instance.elsebtn(performances_label, graph_label)
    
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Project SO")
    window.geometry("800x600")
    
    performance_instance = Performances_stat()  # Create an instance
    utility_instance = util()  # Create an instance

    left_label = tk.Label(window, width=10, text="Project SO", font=("Arial", 12))
    left_label.grid(row=0, column=0)

    performances_label = tk.Label(window,height=5,justify=("left"))
    performances_label.grid(row=1, column=1,columnspan=8,rowspan=2)
        
    graph_label = tk.Label(window, width=100, height=2)
    graph_label.grid(row=3, column=1, columnspan=100, rowspan=100)
    
    performances_btn = tk.Button(window, width=12, height=2, text="Performances", borderwidth=2, relief="solid",
                                 command=lambda: performances_btn_function(performance_instance, window, performances_label, graph_label))
    performances_btn.grid(row=1, column=0)
    
    utility_btn = tk.Button(window, width=12, height=2, text="Utility", borderwidth=2, relief="solid",
                            command=lambda: utility_btn_function(performance_instance, window, performances_label, graph_label))
    utility_btn.grid(row=2, column=0)
    
    else_btn = tk.Button(window, width=12, height=2, text="Else", borderwidth=2, relief="solid",
                         command=lambda:else_btn_function(performances_label, graph_label))
    else_btn.grid(row=3, column=0)

    window.mainloop()
