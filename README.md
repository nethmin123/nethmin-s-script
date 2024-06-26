# nethmin's script

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
- Display data in a treeview with `nstreeview`

## Installation

To use, download the files and copy paste nethminsscript.py into your python project folder. Then you can use nethmin's script in that folder.

## Then, you can import and use the library in your Python scripts:
```python
import nethminsscript

# Dictionary to store variables , you must include this.
variables = {} 
```

## Use nsprint to display a message box
```python
nethminsscript.nsprint("Hello, World!")
```
## Use nsinput to get user input and store it in a variable
```python
nethminsscript.nsinput(variables, "name", "Enter your name:", nethminsscript.is_non_empty)

# to print the output
print(f"The user's name is: {variables['name']}")
```
## Use nsconfirm to show a confirmation dialog
```python
if nethminsscript.nsconfirm("Do you want to continue?"):
    print("User chose to continue.")
else:
    print("User chose not to continue.")
```

## Use nsinput_int to get an integer input and store it in a variable
```python
nethminsscript.nsinput_int(variables, "age", "Enter your age:")

# to print the output
print(f"The user's age is: {variables['age']}")
```

## Use nsinput_float to get a float input and store it in a variable
```python
nethminsscript.nsinput_float(variables, "height", "Enter your height in meters:")

# to print the output
print(f"The user's height is: {variables['height']}")
```

## Use nschoice to get a choice input and store it in a variable
```python
choices = ["Option 1", "Option 2", "Option 3"]
nethminsscript.nschoice(variables, "choice", "Choose an option:", choices)

# to print the output
print(f"The user's choice is: {variables['choice']}")
```

## Use nsfileopen to open a file and store the path in a variable
```python
nethminsscript.nsfileopen(variables, "open_file")

# to print the output
print(f"The user opened: {variables['open_file']}")
```

## Use nsfilesave to save a file and store the path in a variable
```python
nethminsscript.nsfilesave(variables, "save_file")

# to print the output
print(f"The user saved to: {variables['save_file']}")
```

## Use nsprogressbar to show a progress bar for 5 seconds
```python
nethminsscript.nsprogressbar(5, "Please wait...")
```

## Use nscolorchooser to choose a color and store it in a variable
```python
nethminsscript.nscolorchooser(variables, "selected_color", "Pick a color")

# to print the output
print(f"Selected color: {variables['selected_color']}")
```

## Use nsmultilineinput to get multiline input and store it in a variable
```python
nethminsscript.nsmultilineinput(variables, "feedback", "Please provide your feedback:")

# to print the output
print(f"User feedback: {variables['feedback']}")
```

## Use nslistbox to select multiple items from a list
```python
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
nethminsscript.nslistbox(variables, "selected_items", "Choose items:", items)

# to print the output
print(f"Selected items: {variables['selected_items']}")
```

## Use nstreeview to display data in a treeview
```python
columns = ["Name", "Age", "City"]
data = [("Alice", 30, "New York"), ("Bob", 25, "Los Angeles"), ("Charlie", 35, "Chicago")]
nethminsscript.nstreeview(data, columns, "User Data")
```

Made by nethmin chamika , Support me on [Ko-Fi](https://ko-fi.com/nethminchamika)
