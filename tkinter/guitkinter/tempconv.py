import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x400")

label = tk.Label(root, text="Enter Fahrenheit")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

def convert():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=10)

root.mainloop()