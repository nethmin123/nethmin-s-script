# nethminsscript.py
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, ttk, colorchooser
import time

def nsprint(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Message", message)
    root.destroy()

def nsinput(var_dict, var_name, prompt, validate_func=None):
    root = tk.Tk()
    root.withdraw()
    
    user_input = None
    while True:
        user_input = simpledialog.askstring("Input", prompt)
        if validate_func and not validate_func(user_input):
            messagebox.showwarning("Validation Error", "Invalid input. Please try again.")
        else:
            break
    
    if user_input is not None:
        var_dict[var_name] = user_input
    
    root.destroy()

def nsconfirm(message):
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askyesno("Confirmation", message)
    root.destroy()
    return result

def nsinput_int(var_dict, var_name, prompt):
    root = tk.Tk()
    root.withdraw()
    
    user_input = None
    while True:
        try:
            user_input = simpledialog.askinteger("Input", prompt)
            break
        except (TypeError, ValueError):
            messagebox.showwarning("Validation Error", "Please enter a valid integer.")
    
    if user_input is not None:
        var_dict[var_name] = user_input
    
    root.destroy()

def nsinput_float(var_dict, var_name, prompt):
    root = tk.Tk()
    root.withdraw()
    
    user_input = None
    while True:
        try:
            user_input = simpledialog.askfloat("Input", prompt)
            break
        except (TypeError, ValueError):
            messagebox.showwarning("Validation Error", "Please enter a valid number.")
    
    if user_input is not None:
        var_dict[var_name] = user_input
    
    root.destroy()

def nschoice(var_dict, var_name, prompt, choices):
    root = tk.Tk()
    root.withdraw()
    
    user_input = simpledialog.askstring("Choice", f"{prompt}\nOptions: {', '.join(choices)}")
    
    while user_input not in choices:
        messagebox.showwarning("Validation Error", f"Please choose one of the following: {', '.join(choices)}")
        user_input = simpledialog.askstring("Choice", f"{prompt}\nOptions: {', '.join(choices)}")
    
    if user_input is not None:
        var_dict[var_name] = user_input
    
    root.destroy()

def nsfileopen(var_dict, var_name, filetypes=[("All files", "*.*")]):
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    
    if file_path:
        var_dict[var_name] = file_path
    
    root.destroy()

def nsfilesave(var_dict, var_name, filetypes=[("All files", "*.*")]):
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.asksaveasfilename(filetypes=filetypes)
    
    if file_path:
        var_dict[var_name] = file_path
    
    root.destroy()

def nsprogressbar(duration, message="Processing..."):
    root = tk.Tk()
    root.title("Progress")
    tk.Label(root, text=message).pack(pady=10)
    
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)
    
    progress["maximum"] = 100
    step = 100 / duration
    
    for i in range(duration):
        progress["value"] += step
        root.update_idletasks()
        time.sleep(1)
    
    root.destroy()

def nscolorchooser(var_dict, var_name, title="Choose a color"):
    root = tk.Tk()
    root.withdraw()
    
    color_code = colorchooser.askcolor(title=title)[1]
    
    if color_code:
        var_dict[var_name] = color_code
    
    root.destroy()

def nsmultilineinput(var_dict, var_name, prompt):
    root = tk.Tk()
    root.title(prompt)
    
    text_area = tk.Text(root, width=50, height=10)
    text_area.pack(pady=20)
    
    def on_submit():
        var_dict[var_name] = text_area.get("1.0", tk.END).strip()
        root.destroy()
    
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)
    
    root.mainloop()

def nslistbox(var_dict, var_name, prompt, items):
    root = tk.Tk()
    root.title(prompt)
    
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack(pady=20)
    
    def on_submit():
        selected_items = [listbox.get(i) for i in listbox.curselection()]
        var_dict[var_name] = selected_items
        root.destroy()
    
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)
    
    root.mainloop()



def nstreeview(data, columns, title="Data View"):
    root = tk.Tk()
    root.title(title)
    
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    
    for row in data:
        tree.insert("", tk.END, values=row)
    
    tree.pack(expand=True, fill=tk.BOTH, pady=20)
    
    close_button = tk.Button(root, text="Close", command=root.destroy)
    close_button.pack(pady=10)
    
    root.mainloop()






