from tkinter import *

def on_button_click():
    yourName = entry.get()  # Get the current value of the Entry widget
    label.config(text=yourName)  # Update the label with the current value

window = Tk()
window.geometry("500x500")
window.title("Bing auto search script")

entry = Entry(window)
entry.pack(pady=20)  # Add some padding to the input field
entry.insert(0, "entry your name")



button = Button(window, text="Click Me", command=on_button_click)
button.pack(pady=20)

# Label to display text
label = Label(window, text='')
label.pack(pady=20)

window.mainloop()

    