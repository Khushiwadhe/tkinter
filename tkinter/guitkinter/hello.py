import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

root.title("My Tkinter App")

icon = PhotoImage(file=r'E:\tkinter\tkinter\images\clear.png')
root.iconphoto(True, icon)

root.geometry("500x500")

# Add image to layout
img = PhotoImage(file=r'E:\tkinter\tkinter\images\clear.png')
img_label = tk.Label(root, image=img)
img_label.pack(pady=10)

root.mainloop()