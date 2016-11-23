# Package Settings

BASE_FOLDER = "output"
PACKAGE_NAME = "com.secretbiology.BankManager"
JAVA_EXTENSION = ".java"

# UI Components
UI_FOLDER = "ui"
BASE_ACTIVITY = "BaseActivity"
BASE_LAYOUT = "base_layout"
TOOLBAR = "toolbar"

BASE_JAVA = BASE_FOLDER + "/java"
BASE_RES = BASE_FOLDER + "/res"

# Make code folders
subPaths = PACKAGE_NAME.split(".")
folderPath = BASE_JAVA + "/"
for folder in subPaths:
    folderPath += folder
    folderPath += "/"

BASE_PACKAGE_PATH = folderPath.rstrip('/')
