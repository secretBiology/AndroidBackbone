"""
Simple script creates backbone template for typical android projects
"""

import os
import sys
from shutil import copyfile


def make_folder(path_name):
    """
    Makes folder given path
    :param path_name: path of folder
    :return: void
    """
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def get_content(filename, name_of_package):
    """
    Just replaces variable names from template files to user defined values from "settings"
    :param name_of_package: Package Name
    :param filename: Name of File
    :return: replaced content
    """
    with open(filename) as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$PACKAGE_NAME$', name_of_package)
    return file_data


input_folder = "templates"


def write_files(name_of_package, java_path=""):
    """
    Creates files and folders from templates
    :param name_of_package: Package Name from command line
    :param java_path: relative java path
    """
    for path, subdirs, files in os.walk(input_folder):
        # Make Folders
        for s in subdirs:
            pt = str(os.path.join(path, s))
            pt = pt.replace(input_folder, "output")
            if "java" in pt:
                java_path = pt + "\\"
            make_folder(pt)

    # Make Folders for java
    for d in name_of_package.split("."):
        java_path += d
        make_folder(java_path)
        java_path += "\\"

    for path, subdirs, files in os.walk(input_folder):
        for name in files:
            fn = os.path.join(path, name)
            ot = fn.replace(input_folder, "output")
            try:
                # TODO: make this in cleaner way
                temp_path = path + "\\" + name_of_package.replace(".", "\\")
                temp_path = temp_path.replace(input_folder, "output")
                if name == "BaseActivity.java":
                    make_folder(temp_path + "\\common\\")
                    with open(temp_path + "\\common\\" + name, "w") as f:
                        f.write(get_content(fn, name_of_package))
                elif name == "AppPrefs.java":
                    make_folder(temp_path + "\\common\\")
                    with open(temp_path + "\\common\\" + name, "w") as f:
                        f.write(get_content(fn, name_of_package))
                elif name == "Home.java":
                    with open(temp_path + "\\" + name, "w") as f:
                        f.write(get_content(fn, name_of_package))
                else:
                    with open(ot, "w") as f:
                        f.write(get_content(fn, name_of_package))
            except UnicodeDecodeError:
                copyfile(fn, ot)


if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        raise Exception("Parse package name as argument like \'main.py "
                        "com.example.package\'")
    else:
        write_files(sys.argv[1])
