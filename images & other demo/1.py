from  tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Jayson - software developer")

# favicon
# root.iconbitmap("./favicon")

my_img = ImageTk.PhotoImage(Image.open('./4.jpg'))











# exit button
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()




root.mainloop()