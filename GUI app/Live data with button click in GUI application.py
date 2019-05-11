'''
In this we will populate the Live data, in GUI application but on button click.

We will add a button 'Get Weather Info'.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import *
import urllib.request
import xml.etree.ElementTree as ET

# Creating the instance of Tkinter
win = tk.Tk()


# For quitting the application
def quit():
    win.quit()
    win.destroy()
    exit()


# TODO: For resetting the fields:
# def reset():
#     print("Test")
#     updatedEntry.delete(0, END)
#     # updatedEntry.update()

# text.delete(1.0, END)

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

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')
tabControl.pack(expand=1, fill='both')

# Container creation to hold the widgets:
weather_control_frame = ttk.LabelFrame(tab1, text='Current Weather Conditions')
weather_control_frame.grid(column=0, row=1, padx=8, pady=4)  # Repositioning

# Creating a new label frame:
weather_city_frame = ttk.LabelFrame(tab1, text='Latest Observation for:')
weather_city_frame.grid(column=0, row=0, padx=8, pady=4)

# Placing the comboBox in the newly created label frame:
ttk.Label(weather_city_frame, text='Location:   ').grid(column=0, row=0, sticky='E')    # Renaming later

# entry_width = max_width + 5  # Defining the width of our entry.
entry_width = 33

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
pressureEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=pressure, state='readonly')
pressureEntry.grid(column=1, row=8, sticky='W')

ttk.Label(weather_control_frame, text='Altimeter:', state='readonly').grid(column=0, row=9, sticky=stick_east)
altimeter = tk.StringVar()
altimeterEntry = ttk.Entry(weather_control_frame, width=entry_width, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=9, sticky='W')

# Adding some space between the labels and entry box:
for child in weather_control_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# Fetching data from the live server NOAA (National Oceanic and Atmospheric Administration):
# URL: https://w1.weather.gov/xml/current_obs/{Station_id}.xml

# Tags in which we have interest:
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f': '',
    'temp_c': '',
    'dewpoint_f': '',
    'dewpoint_c': '',
    'relative_humidity': '',
    'wind_string': '',
    'visibility_mi': '',
    'pressure_string': '',
    'pressure_in': '',
    'location': ''
}

# Station City Labels:
location = tk.StringVar()
ttk.Label(weather_city_frame, textvariable=location).grid(column=0, row=1, columnspan=3)

# Adding Padding in first frame:
for child in weather_city_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# Renaming 'Location':
ttk.Label(weather_control_frame, text='Weather Station ID: ').grid(column=0, row=0)

# Setting up the stations:
station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_city_frame, width=6, textvariable=station_id)
station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')   # Los Angeles, Denver, New York City
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0) # Selects Los Angeles by default.


def get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()


def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    print(url)
    request = urllib.request.urlopen(url)
    content = request.read().decode()
    print(content)

    # Use Element tree
    xml_root = ET.fromstring(content)
    print('xml_root: {}\n'.format(xml_root.tag))

    for data_point in weather_data_tags_dict.keys():
        weather_data_tags_dict[data_point] = xml_root.find(data_point).text


# Populating the data in GUI:
def populate_gui_from_dict():
    location.set(weather_data_tags_dict['location'])
    updated.set(weather_data_tags_dict['observation_time'].replace('Last Updated On: ', ''))
    weather.set(weather_data_tags_dict['weather'])
    temperature.set(weather_data_tags_dict['temp_c'] + ' ºC')
    dew.set(weather_data_tags_dict['dewpoint_c'] + ' ºC')
    humidity.set(weather_data_tags_dict['relative_humidity'])
    wind.set(weather_data_tags_dict['wind_string'])
    visibility.set(weather_data_tags_dict['visibility_mi'] + ' miles')
    pressure.set(weather_data_tags_dict['pressure_string'])
    altimeter.set(weather_data_tags_dict['pressure_in'] + ' in Hg')


# Inserting a Button in our GUI application:
get_weather_button = ttk.Button(weather_city_frame, text='Get Weather Info', command=get_station).grid(column=2, row=0)

# Button to reset the values: TODO
# get_weather_reset = ttk.Button(weather_city_frame, text='Reset', command=reset).grid(column=3, row=0)

print('\n Program is now running \n')
# Running the GUI:
win.mainloop()
