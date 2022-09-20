import os

def main():
    os.chdir('FilesToSort')
    extension_to_category = {}
    for filename in filenames:
        extension = filename.split('.')[1]
        if extension not in extension_to_category:
            extension_to_category[extension] = \
                input("What category would you like to sort {} files into? ".format(extension))
            try:
                os.mkdir(extension_to_category[extension])
            except FileExistsError:
                pass
            hutil.move(os.path.join(directory_name, filename),"{}/{}/{}".format(os.path.join(directory_name), extension_to_category[extension], filename))


main()