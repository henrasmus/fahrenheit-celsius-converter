"""
Rasmus Hén
Windows 10
"""

#Import Tkinter
import tkinter
import tkinter.messagebox

#Creates the main window, text label and an input box
main_window = tkinter.Tk()
label_message = "Fahrenheit till Celsius \nAnge antal grader och omvandla"
main_label = tkinter.Label(main_window, text = label_message, font = 30, \
                           height = 12, width = 50, bg = "#FFFFFF")
user_input = tkinter.Entry(main_window, width = 10)

#Calls the different functions to create the window
def main():
    create_main_window()
    create_top_frame()
    create_bottom_frame()
    
    tkinter.mainloop()

#Main window
def create_main_window():
    main_window.geometry("550x350+100+100")
    main_window.title("INP - Temperaturomvandlare")

#Top part of the window with explanation and feedback
def create_top_frame():
    top_frame = tkinter.Frame(main_window, bg = "#800020")
    
    top_frame.grid()
    main_label.grid(row = 0, rowspan = 1, column = 0, columnspan = 3)

#Lower part of the window with text, input and button
def create_bottom_frame():
    bottom_frame = tkinter.Frame(main_window, bg = "#FEBF97")
    create_sub_label()
    create_input_box()
    create_button()

#Lower text
def create_sub_label():
    sub_label = tkinter.Label(main_window, text = "Ange graderna här ==>", font = 2)

    sub_label.grid(row = 1, rowspan = 1, column = 0, columnspan = 1)

#Text input i the lower part
def create_input_box():
    user_input.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, pady = 25)

#Button to execute the conversion
def create_button():
    convert_button = tkinter.Button(main_window, text = "Omvandla", command = action_convert, bg = "#FD0A54")
    convert_button.grid(row = 1, rowspan = 1, column = 2, columnspan = 1)

#The conversion with if statements to change the appearance of the window depending on the result
def action_convert():
    fahrenheit = user_input.get()
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        if celsius > 0 and fahrenheit != 1337:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = (fahrenheit + " grader Fahrenheit är " + celsius + " grader Celsius")
            main_label.config(bg = "red", text = label_message)
        elif celsius < 0:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = (fahrenheit + " grader Fahrenheit är " + celsius + " grader Celsius")
            main_label.config(bg = "blue", text = label_message)
        elif fahrenheit == 1337:
            label_message = "Du är fan bäst!"
            main_label.config(bg = "#000000", fg = "#FFFFFF", text = label_message, font = 45)
        else:
            celsius = str("{:.2f}".format(celsius))
            fahrenheit = str(fahrenheit)
            label_message = (fahrenheit + " grader Fahrenheit är " + celsius + " grader Celsius")
            main_label.config(bg = "#FFFFFF", fg = "#000000", text = label_message)
    except ValueError:
        tkinter.messagebox.showinfo("Felmeddelande", "Fel typ av input")
    
    
main()
