import tkinter as tk

def on_button_click():
    label.config(text="button Clicked")
    
root = tk.Tk()
root.title("Simple gui")
root.geometry("300x200")

label = tk.Label(root, text="Hello")
label.pack(pady=20)

button = tk.Button(root, text = "click me" , command=on_button_click)
button.pack(pady=20)

root.mainloop()    