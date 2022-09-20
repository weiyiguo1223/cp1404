import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):

        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(os.path.join(directory_name, filename),"{}/{}/{}".format(os.path.join(directory_name), extension, filename))

main()