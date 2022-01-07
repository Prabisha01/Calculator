from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.resizable(0, 0)
root["bg"]="#554f57"

frame=Frame(root, width=600, height=600, relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)

img1 = Image.open('E:\Image\download.jfif')
img1.thumbnail((550, 450))
img2 = Image.open('E:\Image\download.png')
img2.thumbnail((550, 450))
img3 = Image.open('E:\Image\duck_647_060916114815.jpg')
img3.thumbnail((550, 450))
img4 = Image.open('E:\Image\sn-color.jpg')
img4.thumbnail((550, 450))

image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)
images = [image1, image2, image3, image4]

n = 0
image_label = Label(frame, image=images[n])
image_label.pack()

def previous():
    global n
    n = n - 1
    try:
        image_label.config(image=images[n])
    except:
        n = 0
        previous()
def next():
    global n
    n = n + 1
    try:
        image_label.config(image=images[n])
    except:
        n = -1
        next()

previous_btn = Button(root, text="Previous",  relief=GROOVE, command=previous)
previous_btn.pack(side=LEFT, padx=60, pady=5)
exit_btn = Button(root, text="Exit", width=8,  relief=GROOVE, command=root.destroy)
exit_btn.pack(side=LEFT, padx=60, pady=5)
next_btn = Button(root, text="Next", width=8,  relief=GROOVE, command=next)
next_btn.pack(side=LEFT, padx=60, pady=5)

root.mainloop()