"""
Main Code generation file
"""
import settings as s
import functions as f

# Make code folders
subPaths = s.PACKAGE_NAME.split(".")
folderPath = s.BASE_JAVA + "/"
for folder in subPaths:
    folderPath = folderPath + folder
    f.make_folder(folderPath)
    folderPath += "/"

# Make resource folder
f.make_folder(s.BASE_RES + "/layout")
f.make_folder(s.BASE_RES + "/menu")
f.make_folder(s.BASE_RES + "/values")
