from  tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Jayson - software developer")
root.geometry("750x600")
# favicon
# root.iconbitmap("/home/favicon.ico")

my_img = ImageTk.PhotoImage(Image.open('./4.jpg'))
my_label = Label(image=my_img  )
my_label.grid(row=0, column=0, columnspan=3)
# print(dir(my_label))
my_label.pack()










# exit button
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()




root.mainloop()