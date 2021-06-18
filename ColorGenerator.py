'''
Justin Farnsworth
Color Generator
October 31, 2020

This is a simple GUI that allows the user to experiment with different 
color codes and view their corresponding colors. The box on the right 
side of the screen will automatically change colors and the hex color 
code is updated as the user interacts with the sliders.
'''

# Imported modules
import tkinter as tk
from random import randint


# Color Generator class
class ColorGenerator(object):
    # Constructor
    def __init__(self):
        # Initialize and configure the window
        self.__window = tk.Tk()
        self.__window.title("Color Generator")
        self.__window.geometry("600x400")
        self.__window.resizable(width=False, height=False)

        # Font (not saved as class attributes)
        font_style = "Courier New"
        default_font = (font_style, 20, "bold")
        hex_font = (font_style, 25, "bold")

        # Info label
        self.__info_label = tk.Label(
            self.__window,
            text="Move any of the sliders to\nchange the color of the box.",
            font=default_font
        )
        self.__info_label.place(x=300, y=50, anchor=tk.CENTER)

        # Red scale
        self.__red = tk.IntVar()
        self.__red_scale = tk.Scale(
            self.__window,
            variable = self.__red,
            font=default_font,
            cursor="rtl_logo",
            from_=0,
            to=255,
            length=287,
            width=25,
            fg="#ff0000",
            troughcolor="#ff0000",
            command=self.__update
        )
        self.__red_scale.place(x=25, y=100, anchor=tk.NW)

        # Green scale
        self.__green = tk.IntVar()
        self.__green_scale = tk.Scale(
            self.__window,
            variable = self.__green,
            font=default_font,
            cursor="gumby",
            from_=0,
            to=255,
            length=287,
            width=25,
            fg="#00ff00",
            troughcolor="#00ff00",
            command=self.__update
        )
        self.__green_scale.place(x=125, y=100, anchor=tk.NW)

        # Blue scale
        self.__blue = tk.IntVar()
        self.__blue_scale = tk.Scale(
            self.__window,
            variable = self.__blue,
            font=default_font,
            cursor="boat",
            from_=0,
            to=255,
            length=287,
            width=25,
            fg="#0000ff",
            troughcolor="#0000ff",
            command=self.__update
        )
        self.__blue_scale.place(x=225, y=100, anchor=tk.NW)

        # Randomize button generates a random hex color
        self.__randomize_button = tk.Button(
            self.__window,
            text="Randomize",
            font=default_font,
            cursor="star",
            bg="#ffff00",
            activebackground="#ffff00",
            command=self.__generate_random_color
        )
        self.__randomize_button.place(x=450, y=125, width=250, height=40, anchor=tk.CENTER)

        # Canvas is used to generate a rectangle inside of it
        self.__canvas = tk.Canvas(
            self.__window,
            width=250,
            height=200,
            cursor="spraycan"
        )
        self.__canvas.place(x=450, y=250, anchor=tk.CENTER)

        # Box is used to show the current color
        self.__box = self.__canvas.create_rectangle(0, 0, 252, 202, fill="#000000")

        # Hex color code label
        self.__hex_label = tk.Label(
            self.__window,
            text="Hex: #000000",
            font=hex_font,
        )
        self.__hex_label.place(x=450, y=375, anchor=tk.CENTER)

        # Run the tkinter loop
        self.__window.mainloop()
    

    # When the sliders are used, update the screen based on the RGB values
    def __update(self, event=None):
        # Get the color values
        red = self.__red.get()
        green = self.__green.get()
        blue = self.__blue.get()

        # Get the corresponding hex color code
        hex_color_code = self.__get_hex_color_code(red, green, blue)

        # Update the color of the box and update the hex color code label
        self.__canvas.itemconfig(self.__box, fill=hex_color_code)
        self.__hex_label.config(text=f"Hex: {hex_color_code}")

    
    # Get the hex color code based on the RGB values
    @staticmethod
    def __get_hex_color_code(red, green, blue):
        # Convert each value to hexadecimal notation
        hex_red = f"{red:x}".zfill(2).upper()
        hex_green = f"{green:x}".zfill(2).upper()
        hex_blue = f"{blue:x}".zfill(2).upper()

        # Concatenate and return the string
        return f"#{hex_red}{hex_green}{hex_blue}"
    

    # Generate a random color and show the color on the screen
    def __generate_random_color(self):
        # Change the RGB values (the update command will automatically run)
        self.__red_scale.set(randint(0, 255))
        self.__green_scale.set(randint(0, 255))
        self.__blue_scale.set(randint(0, 255))


# Execute the program
if __name__ == "__main__":
    ColorGenerator()
