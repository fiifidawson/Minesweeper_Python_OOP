from tkinter import * # from tkinter import everything



# Create a window
root = Tk() # root is the name of the window

root.configure(bg="black") # sets the background color of the window

root.geometry("1440x720") # sets the size of the window

root.title("Minesweeper") # sets the title of the window

root.resizable(False, False) # makes the window not resizable

root.mainloop() # keeps the window open until we close it