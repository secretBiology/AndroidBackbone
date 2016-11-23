# Package Settings


PACKAGE_NAME = "com.secretbiology.BankManager"
APP_NAME = "BankManager"
BASE_FOLDER = "output"
JAVA_EXTENSION = ".java"
XML_EXTENSION = ".xml"

BASE_ACTIVITY = "BaseActivity"

# UI Components
UI_FOLDER = "ui"
BASE_LAYOUT = "base_layout"
BASE_VIEW = "base_view"
BASE_HEADER = "base_header"
BASE_FRAGMENT = "base_fragment"
BASE_VIEWPAGER = "base_viewpager"
BASE_RECYCLER = "base_recycler"
BASE_FAB = "base_fab"
FAB_MARGIN = "fab_margin"
TOOLBAR = "toolbar"
BASE_MENU = "base_menu"
TABS = "tabs"

# Navigation
DRAWER_LAYOUT = "drawer_layout"
NAV_VIEW = "nav_view"
NAV_OPEN = "navigation_drawer_open"
NAV_CLOSE = "navigation_drawer_close"
NAV_HEADER_HEIGHT = "nav_header_height"
SIDE_NAV_BAR = "side_nav_bar"

# Resources
ACTION_SETTINGS = "action_settings"

# Database
DATABASE_FOLDER = "database"
DATABASE_MANAGER = "DataBase"

BASE_JAVA = BASE_FOLDER + "/java"
BASE_RES = BASE_FOLDER + "/res"

# Make code folders
subPaths = PACKAGE_NAME.split(".")
folderPath = BASE_JAVA + "/"
for folder in subPaths:
    folderPath += folder
    folderPath += "/"

BASE_PACKAGE_PATH = folderPath.rstrip('/')
