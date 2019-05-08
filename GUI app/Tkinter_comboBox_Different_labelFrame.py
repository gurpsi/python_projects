import tkinter as tk
from tkinter import Menu
from tkinter import ttk

# Creating the instance of Tkinter
win = tk.Tk()

# For quitting the application
def quit():
    win.quit()
    win.destroy()
    exit()

# Setting the title for out GUI:
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

# Second Menu Item:
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=helpMenu)

# Tab Control creation:
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

# Container creation to hold the widgets:
weather_control_frame = ttk.LabelFrame(tab1, text='Current Weather Conditions')
weather_control_frame.grid(column=0, row=1, padx=8, pady=4)     # Repositioning

# Creating a new label frame:
weather_city_frame = ttk.LabelFrame(tab1, text='Latest Observation for:')
weather_city_frame.grid(column=0, row=0, padx=8, pady=4)

# Placing the comboBox in the newly created label frame:
ttk.Label(weather_city_frame, text='Location:       ').grid(column=0, row=0, sticky='E')

# Creating ComboBox:
city = tk.StringVar()
citySelected = ttk.Combobox(weather_city_frame, width=10, textvariable=city)
citySelected['values']=('Los Angeles', 'London', 'Rio De Genario, Brazil')
citySelected.grid(column=1, row=0, sticky='E')
citySelected.current(0)

# Taking the max length name:
max_width = max([len(x) for x in citySelected['values']])
citySelected.config(width=max_width-6)

# Adding Entries to the Labels:
entry_width = max_width - 6     # Defining the width of our entry.

# Adding label and TextBox Entry Widgets:

# Setting the sticky of readonly item as East:
stick_east = 'E'

ttk.Label(weather_control_frame, text='Last Updated:').grid(column=0, row=1, sticky=stick_east)
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(weather_control_frame, text='Weather:').grid(column=0, row=2, sticky=stick_east)
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')

ttk.Label(weather_control_frame, text='Temperature:').grid(column=0, row=3, sticky=stick_east)
temperature = tk.StringVar()
temperatureEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=temperature, state='readonly')
temperatureEntry.grid(column=1, row=3, sticky='W')

ttk.Label(weather_control_frame, text='Dew Point:').grid(column=0, row=4, sticky=stick_east)
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')

ttk.Label(weather_control_frame, text='Relative Humidity:').grid(column=0, row=5, sticky=stick_east)
humidity = tk.StringVar()
humidityEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=humidity, state='readonly')
humidityEntry.grid(column=1, row=5, sticky='W')

ttk.Label(weather_control_frame, text='Wind:').grid(column=0, row=6, sticky=stick_east)
wind = tk.StringVar()
windEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')

ttk.Label(weather_control_frame, text='Visibility:').grid(column=0, row=7, sticky=stick_east)
visibility = tk.StringVar()
visibilityEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=visibility, state='readonly')
visibilityEntry.grid(column=1, row=7, sticky='W')

ttk.Label(weather_control_frame, text='MSL Pressure:').grid(column=0, row=8, sticky=stick_east)
pressure = tk.StringVar()
pressureEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=pressure ,state='readonly')
pressureEntry.grid(column=1, row=8, sticky='W')

ttk.Label(weather_control_frame, text='Altimeter:', state='readonly').grid(column=0, row=9, sticky=stick_east)
altimeter = tk.StringVar
altimeterEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=9, sticky='W')

# Adding some space between the labels and entry box:
for child in weather_control_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# Running the GUI:
win.mainloop()