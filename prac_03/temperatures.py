"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
display menu
get choice
while choice not equal to Q
    if choice equal to C
        get celsius
        convert celsius to fahrenheit
        display temperature in fahrenheit
    elif choice equal to F
        get fahrenheit
        convert fahrenheit to celsius
        display temperature in celsius
    else:
        display invalid option
    display menu
    get choice
display thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    " Temperature convention program  "
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = Convert_celsisu_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = Convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Convert_fahrenheit_to_celsius(fahrenheit):
    "Convert Fahrenheit to Celsius "
    return 5 / 9 * (fahrenheit - 32)


def Convert_celsisu_to_fahrenheit(celsius):
    " Convert Celsius to Fahrenheit"
    return celsius * 9.0 / 5 + 32

main()