#!/usr/bin/env python3
import os
from tkinter import Tk, Label, Button
from PIL import ImageTk, Image


def circulate_images():
  global counter
  img_label.configure(image=img_array[counter % len(img_array)])
  counter = counter + 1


counter = 1
root = Tk()
root.title("Image Viewer")

root.geometry("800x800")

root.configure(background="#111111")

files = os.listdir("newonewall")

img_array = []

for file in files:

  img = Image.open(os.path.join("newonewall", file))
  resized_img = img.resize((700, 700))
  img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(image=img_array[0])
img_label.pack(pady=(1, 1))

NEXT_ONE = Button(root,
                  text="  NEXT IMAGE",
                  bg="GOLD",
                  fg="#111111",
                  font=("oswald bold 30", 20),
                  command=circulate_images)
NEXT_ONE.pack(pady=(1, 1))


root.mainloop()
