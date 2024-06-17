# nethminsscript

`nethminsscript` is a Python library designed to simplify the creation of graphical user interfaces (GUI) using Tkinter. It provides a set of easy-to-use functions for common GUI tasks, allowing developers to focus on their application's logic rather than the intricacies of GUI programming.

## Features

- Display message boxes with `nsprint`
- Prompt for text input with `nsinput`
- Confirm actions with `nsconfirm`
- Prompt for integer input with `nsinput_int`
- Prompt for float input with `nsinput_float`
- Display choices with `nschoice`
- Open file dialog with `nsfileopen`
- Save file dialog with `nsfilesave`
- Show progress bars with `nsprogressbar`
- Choose colors with `nscolorchooser`
- Enter multiline text with `nsmultilineinput`
- Select multiple items from a list with `nslistbox`
- Pick a date with `nsdateinput`
- Display data in a treeview with `nstreeview`

## Installation

To use, download the files and copy paste nethminsscript.py into your python project folder. Then you can use nethmin's script in that folder.

##Then, you can import and use the library in your Python scripts:

import nethminsscript

##Dictionary to store variables
variables = {}

##Use nsprint to display a message box
nethminsscript.nsprint("Hello, World!")

##Use nsinput to get user input and store it in a variable
nethminsscript.nsinput(variables, "name", "Enter your name:", nethminsscript.is_non_empty)
print(f"The user's name is: {variables['name']}")

##Use nsconfirm to show a confirmation dialog
if nethminsscript.nsconfirm("Do you want to continue?"):
    print("User chose to continue.")
else:
    print("User chose not to continue.")

##Use nsinput_int to get an integer input and store it in a variable
nethminsscript.nsinput_int(variables, "age", "Enter your age:")
print(f"The user's age is: {variables['age']}")

##Use nsinput_float to get a float input and store it in a variable
nethminsscript.nsinput_float(variables, "height", "Enter your height in meters:")
print(f"The user's height is: {variables['height']}")

##Use nschoice to get a choice input and store it in a variable
choices = ["Option 1", "Option 2", "Option 3"]
nethminsscript.nschoice(variables, "choice", "Choose an option:", choices)
print(f"The user's choice is: {variables['choice']}")

##Use nsfileopen to open a file and store the path in a variable
nethminsscript.nsfileopen(variables, "open_file")
print(f"The user opened: {variables['open_file']}")

##Use nsfilesave to save a file and store the path in a variable
nethminsscript.nsfilesave(variables, "save_file")
print(f"The user saved to: {variables['save_file']}")

##Use nsprogressbar to show a progress bar for 5 seconds
nethminsscript.nsprogressbar(5, "Please wait...")

##Use nscolorchooser to choose a color and store it in a variable
nethminsscript.nscolorchooser(variables, "selected_color", "Pick a color")
print(f"Selected color: {variables['selected_color']}")

##Use nsmultilineinput to get multiline input and store it in a variable
nethminsscript.nsmultilineinput(variables, "feedback", "Please provide your feedback:")
print(f"User feedback: {variables['feedback']}")

##Use nslistbox to select multiple items from a list
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
nethminsscript.nslistbox(variables, "selected_items", "Choose items:", items)
print(f"Selected items: {variables['selected_items']}")

##Use nstreeview to display data in a treeview
columns = ["Name", "Age", "City"]
data = [("Alice", 30, "New York"), ("Bob", 25, "Los Angeles"), ("Charlie", 35, "Chicago")]
nethminsscript.nstreeview(data, columns, "User Data")

