import os

from scripts.settings import name_of_package, name_of_app

base_path = name_of_package.replace(".", "/")
base_path += "/"


def make_folder(path):
    """
    Makes folder given path
    :param path: path of folder
    :return: void
    """
    if not os.path.exists(path):
        os.makedirs(path)


def get_content(filename):
    """
    Just replaces variable names from template files to user defined values from "settings"
    :param filename: Name of File
    :return: replaced content
    """
    current_path = "templates/" + filename
    with open(current_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$PACKAGE_NAME$', name_of_package)
    file_data = file_data.replace('$APP_NAME$', name_of_app)
    return file_data


java_path = "output/java/" + base_path
resource_path = "output/res/"

file_list = [
    ["AndroidManifest.xml", "output"],
    ["base_header.xml", resource_path + "layout"],
    ["base_layout.xml", resource_path + "layout"],
    ["base_drawer.xml", resource_path + "menu"],
    ["BaseActivity.java", java_path + "common"],
    ["blank.xml", resource_path + "drawable"],
    ["colors.xml", resource_path + "values"],
    ["material_colors.xml", resource_path + "values"],
    ["CurrentActivity.java", java_path + "common"],
    ["Database.java", java_path + "database"],
    ["Home.java", java_path + "activities"],
    ["dimens.xml", resource_path + "values"],
    ["home.xml", resource_path + "layout"],
    ["icon_home.xml", resource_path + "drawable"],
    ["SetUpActivity.java", java_path + "common"],
    ["Splash.java", java_path],
    ["splash.xml", resource_path + "layout"],
    ["strings.xml", resource_path + "values"],
    ["styles.xml", resource_path + "values"],
    ["Preferences.java", java_path + "preferences"],
    ["AppPrefs.java", java_path + "preferences"],
    ["Login.java", java_path + "activities/login"],
    ["login.xml", resource_path + "layout"],
    ["LoginUser.java", java_path + "background/tasks"]
]

for f in file_list:
    make_folder(f[1])
    with open("%s/%s" % (f[1], f[0]), 'w') as file:
        file.write(get_content(f[0]))
