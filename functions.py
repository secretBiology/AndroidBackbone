import os


def make_folder(path):
    """
    Makes folder given path
    :param path: path of folder
    :return: void
    """
    if not os.path.exists(path):
        os.makedirs(path)


def add_import(file_handler, import_string):
    """
    Adds import statement at the top of file
    :param file_handler: File handler
    :param import_string: package name
    :return: adds import
    """
    import_string = "import " + import_string + ";"
    print(import_string, file=file_handler, end="\n")


def override(file):
    print("@Override", file=file, end="\n")


def add_line(file, string):
    print(string, file=file, end="\n")


def tabbed(file, string):
    string = "\t" + string
    print(string, file=file, end="\n")


def tabbed_public(file, string):
    string = "\tpublic " + string + ";"
    print(string, file=file, end="\n")


def tabbed_private(file, string):
    string = "\tprivate " + string + ";"
    print(string, file=file, end="\n")
