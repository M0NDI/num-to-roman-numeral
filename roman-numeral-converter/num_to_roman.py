import tkinter as tk

def int_to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]
    roman = ""
    for value, symbol in zip(values, symbols):
        while num >= value:
            roman += symbol
            num -= value
    return roman

def convert_to_roman():
    number = int(entry.get())
    roman_numeral = int_to_roman(number)
    result_label.config(text="Roman Numeral: " + roman_numeral)
    text.config(state="normal")
    text.delete("1.0", "end")
    text.insert("insert", roman_numeral)
    text.config(state="disabled")

root = tk.Tk()
root.geometry("400x150")
root.title("Number to Roman Numeral Converter")

label = tk.Label(root, text="Enter a number:")
entry = tk.Entry(root)

convert_button = tk.Button(root, text="Convert", command=convert_to_roman)
result_label = tk.Label(root, text="")

text = tk.Text(root, height=2, width=30, state="disabled")
text.pack()

label.pack()
entry.pack()
convert_button.pack()
result_label.pack()

root.mainloop()
