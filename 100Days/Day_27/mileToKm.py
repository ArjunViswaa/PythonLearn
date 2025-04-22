import tkinter

window = tkinter.Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    KM_result_label.config(text=km)

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

KM_result_label = tkinter.Label(text="0")
KM_result_label.grid(column=1, row=1)

KM_Label = tkinter.Label(text="Km")
KM_Label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()