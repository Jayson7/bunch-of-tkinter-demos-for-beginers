from  tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Jayson - software developer")
root.geometry("750x600")
# favicon
# root.iconbitmap("/home/favicon.ico")

my_img = ImageTk.PhotoImage(Image.open('./4.jpg').resize((750, 550), Image.ANTIALIAS) )

my_img2 = ImageTk.PhotoImage(Image.open('./11.jpg').resize((750, 550), Image.ANTIALIAS) )

my_img3 = ImageTk.PhotoImage(Image.open('./5.jpg').resize((750, 550), Image.ANTIALIAS) )

my_img4 = ImageTk.PhotoImage(Image.open('./3.jpg').resize((750, 550), Image.ANTIALIAS) )

my_img5 = ImageTk.PhotoImage(Image.open('./2.jpg').resize((750, 550), Image.ANTIALIAS) )

my_img6 = ImageTk.PhotoImage(Image.open('./1.jpg').resize((750, 550), Image.ANTIALIAS) )

image_list = [my_img, my_img2, my_img3, my_img4, my_img5, my_img6]



button_back = Button(root,  text="<<" )
button_quit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root,  text=">>" )


button_forward.grid(row=1, column=0)
button_back.grid(row=1, column=3)
button_quit.grid(row=1, column=2)

# exit button





root.mainloop()