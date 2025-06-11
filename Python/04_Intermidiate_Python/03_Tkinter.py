"""
Tkinter is a standard GUI library for Python.
"""
import tkinter as tk

window = tk.Tk()
window.title('My First GUI Program')
window.minsize(width=400, height=400)

# Label
label = tk.Label(text='I am a Label', font=('Arial', 24, 'bold'))
# Pack the label into the window
label.pack(side="left")

# using advanced argument


# import turtle
# tim = turtle.Turtle()
# tim.write("aaa")



# holds on the window and listens for events, at the end of the program, the window will close
window.mainloop()




