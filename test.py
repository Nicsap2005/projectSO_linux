# import tkinter as tk

# class Testing:
#     def __init__(self):
#         self.base = ""
#         with open("output_tree.txt", 'r') as file:
#             self.base = file.read()  # Read the whole content at once

# if __name__ == "__main__":
#     window = tk.Tk()
    
#     # Create a Label widget with a monospace font
#     label = tk.Label(window, text=Testing().base, font=("Courier", 10), justify="left")
    
#     # Adjust the grid to fill the window and preserve formatting
#     label.grid(row=0, column=0, sticky="nsew")
    
#     # Expand window to fit content
#     window.grid_columnconfigure(0, weight=1)
#     window.grid_rowconfigure(0, weight=1)
    
#     window.mainloop()

import time

counter = 1
for i in range(10,0,-1):
    print(""*(i-1)+"* "*counter)
    counter += 1