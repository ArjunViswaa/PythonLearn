import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label.config(text=my_input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

my_input = tkinter.Entry(width=10)
my_input.pack()

window.mainloop()