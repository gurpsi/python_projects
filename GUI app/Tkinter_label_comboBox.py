import tkinter as tk
from tkinter import Menu
from tkinter import ttk

# Instance of Tkinter
win = tk.Tk()

# For quitting the application
def quit():
    win.quit()
    win.destroy()
    exit()

# Titile of GUI
win.title('GUI')

# Menu Bar:
menuBar = Menu()
win.config(menu=menuBar)

# Menu Items:
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)
menuBar.add_cascade(label='File', menu=fileMenu)

# Second Menu Item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=helpMenu)

# Tab Control:
tabControl = ttk.Notebook(win)      # Tab control creation

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

# Creating container frame to hold the widgets:
weather_conditions_frame = ttk.LabelFrame(tab1, text='Current Weather Condition')
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

# Adding a label to widget:
ttk.Label(weather_conditions_frame, text='Location').grid(column=0, row=0, sticky='W')

# Creation of Combo box:
city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio De Genario, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(0)     # Highlighting the first city

# Since our last name is long and it will not fit in the ComboBox, therefore taking the Max length:
max_width = max([len(x) for x in citySelected['values']])
citySelected.config(width=max_width-6)

# Running the GUI
win.mainloop()

