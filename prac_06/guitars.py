from prac_06.guitar import Guitar

def main():
    guitars =[]
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost} added.")
        new_guitar = Guitar(name,year,cost)
        guitars.append(new_guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    if int(len(guitars))>0:

        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(vintage)"
            print(f"Guitar {i+1}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f} {vintage}")



main()