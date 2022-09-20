"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))


    os.chdir('Lyrics/Christmas')


    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))


    try:
        os.mkdir('temp')
    except FileExistsError:
        pass


    for filename in os.listdir('.'):

        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    space_preceding = False
    bracket_preceding = False
    for letter in filename:
        if letter.isspace() or letter == "_":
            space_preceding = True
            new_name = new_name + "_"
        elif letter == "(":
            bracket_preceding = True
        elif letter.isupper():
            if new_name != "" and not space_preceding and not bracket_preceding:
                new_name = new_name + "_"
        if not (letter.isspace() or letter == "_"):
            if space_preceding:
                letter = letter.upper()
                space_preceding = False
            new_name = new_name + letter

    return new_name



def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)

main()
# demo_walk()