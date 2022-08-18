def main():
    email_name ={}
    email = input("Email: ")
    while email != "":
        name = identify_name(email)
        is_name = input(f"Is your name {name}? (Y/N)")

        if is_name.upper() != "Y" and is_name.upper() != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email,name in email_name.items():
        print(f"{name} ({email}) ")



def identify_name(email):
    name_form_email = email.split("@")[0]
    name = name_form_email.split(".")
    ordered_name = " ".join(name).title()
    return ordered_name

main()