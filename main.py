import tkinter as tk


# Function to update the input fields
def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(number))


# Function to perform calculations
def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")


# Function to clear the input field
def clear():
    entry_display.delete(0, tk.END)


# Create the main window with a blue background
window = tk.Tk()
window.title("Calculator by Huzaifa")
window.configure(bg='grey')  # Set the background color to blue

# Entry field for display
entry_display = tk.Entry(window, width=20, font=('lucid', 16, 'bold'))
entry_display.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=5, height=2, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, width=5, height=2, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val,
                                                                                                         column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main loop
window.mainloop()
