import tkinter as tk
from tkinter import Menu
from tkinter import ttk     # ttk is 'Themed TKinter'

# Creating an instance of TKinter
win = tk.Tk()

# To quit the application cleanly
def quit():
    win.quit()
    win.destroy()
    exit()


# Adding a title
win.title('Basic GUI')

# Creating a Menu bar:
menuBar = Menu()
win.config(menu=menuBar)

# Add menu Items:
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit)
menuBar.add_cascade(label='File', menu=fileMenu)

# Adding another menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=helpMenu)

# Tab control:
tabControl = ttk.Notebook(win)      # Create a tab control

tab1 = ttk.Frame(tabControl)        # Crating first tab
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

# Creating a container frame to hold the widgets:
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions')

weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

# Adding a label:
ttk.Label(weather_conditions_frame, text='Location').grid(column=0, row=0, sticky='W')


win.mainloop()



