import tkinter as tk
from tkinter import messagebox
import json

def save_command():
    command = entry_command.get()
    description = entry_description.get()
    script_name = entry_script.get()

    if not (command and description and script_name):
        messagebox.showerror("Error", "All fields must be filled!")
        return

    command_data = {
        "command": command,
        "description": description,
        "script_path": "scripts/{}.py".format(script_name)
    }

    with open("commands.json", "r") as file:
        commands = json.load(file)

    commands.append(command_data)

    with open("commands.json", "w") as file:
        json.dump(commands, file, indent=4)

    messagebox.showinfo("Success", "Command added successfully!")

root = tk.Tk()
root.title("Command Adder")
root.geometry("400x200")  # Устанавливаем размеры окна

label_command = tk.Label(root, text="Command:")
label_command.grid(row=0, column=0, sticky="w")

entry_command = tk.Entry(root)
entry_command.grid(row=0, column=1)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=1, column=0, sticky="w")

entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1)

label_script = tk.Label(root, text="Script Name (without .py):")
label_script.grid(row=2, column=0, sticky="w")

entry_script = tk.Entry(root)
entry_script.grid(row=2, column=1)

button_add = tk.Button(root, text="Add Command", command=save_command)
button_add.grid(row=3, columnspan=2)

root.mainloop()  # Показываем окно
