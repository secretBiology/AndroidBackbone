import os


def make_folder(path):
    """
    Makes folder given path
    :param path: path of folder
    :return: void
    """
    if not os.path.exists(path):
        os.makedirs(path)
