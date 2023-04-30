from tkinter import * # from tkinter import everything



# Create a window
root = Tk() # root is the name of the window


# Override the settings of the window
root.configure(bg="black") # sets the background color of the window

root.geometry("1440x720") # sets the size of the window

root.title("Minesweeper") # sets the title of the window

root.resizable(False, False) # makes the window not resizable

top_frame = Frame(
                root, 
                bg="red",
                width=1440, height=180
)

top_frame.place(x=0.0, y=0.0)

left_frame = Frame(
                root,
                bg="blue",
                width=360,
                height=540
)
left_frame.place(x=0.0, y=180)


# Run the window
root.mainloop() # keeps the window open until we close it