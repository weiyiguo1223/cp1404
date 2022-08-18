"""
CP1404/CP5632 Practical
hex colours
"""


CODE_OF_COLOR = {"Ferrari Red": "#ff2800", "DarkOrange": "#ff8c00",
                 "Golden Yellow": "#ffdf00", "Forest Green": "#228b22",
                 "Denim Blue": "#2243b6", "DarkSeaGreen": "#8fbc8f",
                 "DarkOrchid": "#9932cc", "AntiqueWhite": "#faebd7",
                 "Gray5": "#0d0d0d", "Jasmine": "#f8de7e"}

color_name = input("Enter a color name: ")
while color_name != "":
    if color_name in CODE_OF_COLOR:
        print(f"Color code of {color_name} is {CODE_OF_COLOR[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ")

