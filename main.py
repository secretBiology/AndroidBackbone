"""
Main Code generation file
"""
import settings as s
import functions as f
import templates.BaseActivity as BaseActivity

# Make resource folder
f.make_folder(s.BASE_RES + "/layout")
f.make_folder(s.BASE_RES + "/menu")
f.make_folder(s.BASE_RES + "/values")

# Make base UI
f.make_folder(s.BASE_PACKAGE_PATH + "/" + s.UI_FOLDER)
with open(s.BASE_PACKAGE_PATH + "/" + s.UI_FOLDER + "/" + s.BASE_ACTIVITY + s.JAVA_EXTENSION, 'w') as file:
    BaseActivity.Build(file)
