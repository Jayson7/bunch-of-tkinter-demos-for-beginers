from tkinter import *

# initialize tk
root = Tk()

# a simple hello world message 
my_label = Label(root, text="Hello world jayson")

# send the label to the tk
my_label.pack()

# positioning 

my_label.grid(row=2, column=5)


# intiate the loop
root.mainloop() 