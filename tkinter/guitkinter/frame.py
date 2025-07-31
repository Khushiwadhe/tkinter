import tkinter as tk

root = tk.Tk()
root.title("simple gui with frames")
root.geometry("300x200")

top_frame= tk.Frame(root)
top_frame.pack(side=tk.TOP , pady=10)

bottom_frame= tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM , pady=10)

label = tk.Label(top_frame , text="Hello Khushi")
label.pack()

button = tk.Button(bottom_frame, text="Click me", command=lambda: label.config(text="Button Clicked"))
button.pack()

root.mainloop()