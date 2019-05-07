import tkinter as tk

win = tk.Tk()

win.title("Python GUI")

def get_current_window_size():
    win.update()
    print('width= ',win.winfo_width())
    print('height= ', win.winfo_height())

def increase_window_size():
    win.minsize(width=300, height=1)    # Where 1 is the default value i.e. 200 Pixels

    win.resizable(0,0) # Fix the window size, i.e. the window size can't be changed now.

get_current_window_size()
increase_window_size()
get_current_window_size()


win.mainloop()