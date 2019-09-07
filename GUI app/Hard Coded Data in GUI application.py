'''
In GUI application, the data is hard coded to verify the fields are getting populated correctly.
'''

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
altimeter = tk.StringVar()
altimeterEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=9, sticky='W')

# Adding some space between the labels and entry box:
for child in weather_control_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# Fetching data from the server NOAA (National Oceanic and Atmospheric Administration) manually:
# Information about API: https://www.ncdc.noaa.gov/cdo-web/webservices/v2

weather_data = {
 'dewpoint_c': '16.7',
 'dewpoint_f': '62.1',
 'dewpoint_string': '62.1 F (16.7 C)',
 'icon_url_base': 'http://forecast.weather.gov/images/wtf/small/',
 'icon_url_name': 'nsct.png',
 'latitude': '33.93806',
 'location': 'Los Angeles, Los Angeles International Airport, CA',
 'longitude': '-118.38889',
 'ob_url': 'http://www.weather.gov/data/METAR/KLAX.1.txt',
 'observation_time': 'Last Updated on Aug 7 2016, 9:53 pm PDT',
 'observation_time_rfc822': 'Sun, 07 Aug 2016 21:53:00 -0700',
 'pressure_in': '29.81',
 'pressure_mb': '1009.1',
 'pressure_string': '1009.1 mb',
 'relative_humidity': '84',
 'station_id': 'KLAX',
 'suggested_pickup': '15 minutes after the hour',
 'suggested_pickup_period': '60',
 'temp_c': '19.4',
 'temp_f': '67.0',
 'temperature_string': '67.0 F (19.4 C)',
 'two_day_history_url': 'http://www.weather.gov/data/obhistory/KLAX.html',
 'visibility_mi': '9.00',
 'weather': 'Partly Cloudy',
 'wind_degrees': '250',
 'wind_dir': 'West',
 'wind_mph': '6.9',
 'wind_string': 'West at 6.9 MPH (6 KT)'
 }


# Populating the data in GUI:
updated_data = weather_data['observation_time'].replace('Last Updated On: ','')
updated.set(updated_data)

weather.set(weather_data['weather'])
temperature.set(weather_data['temp_c'] + ' ºC')
dew.set(weather_data['dewpoint_c'] + ' ºC')
humidity.set(weather_data['relative_humidity'])
wind.set(weather_data['wind_string'])
visibility.set(weather_data['visibility_mi'] + ' miles')
pressure.set(weather_data['pressure_string'])
altimeter.set(weather_data['pressure_in'] + ' in Hg')



# Running the GUI:
win.mainloop()
