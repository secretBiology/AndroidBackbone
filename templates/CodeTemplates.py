import os

import settings as s

script_path = os.path.dirname(__file__)


def base_activity():
    relative_path = "files/BaseActivity.java"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()

    file_data = file_data.replace('$CURRENT_PACKAGE$', s.PACKAGE_NAME + "." + s.UI_FOLDER.lower())
    file_data = file_data.replace('$PACKAGE_NAME$', s.PACKAGE_NAME)
    file_data = file_data.replace('$BASE_ACTIVITY$', s.BASE_ACTIVITY)
    file_data = file_data.replace('$BASE_LAYOUT$', s.BASE_LAYOUT)
    file_data = file_data.replace('$TOOLBAR$', s.TOOLBAR)
    file_data = file_data.replace('$DRAWER_LAYOUT$', s.DRAWER_LAYOUT)
    file_data = file_data.replace('$NAV_VIEW$', s.NAV_VIEW)
    file_data = file_data.replace('$BASE_MENU$', s.BASE_MENU)
    file_data = file_data.replace('$ACTION_SETTINGS$', s.ACTION_SETTINGS)
    file_data = file_data.replace('$NAV_OPEN$', s.NAV_OPEN)
    file_data = file_data.replace('$NAV_CLOSE$', s.NAV_CLOSE)

    return file_data


def database_manager():
    relative_path = "files/Database.java"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$CURRENT_PACKAGE$', s.PACKAGE_NAME + "." + s.DATABASE_FOLDER.lower())
    file_data = file_data.replace('$PACKAGE_NAME$', s.PACKAGE_NAME)
    file_data = file_data.replace('$DATABASE_MANAGER$', s.DATABASE_MANAGER)
    return file_data


def activity_setup():
    relative_path = "files/SetUpActivity.java"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$CURRENT_PACKAGE$', s.PACKAGE_NAME + "." + s.UI_FOLDER.lower())
    file_data = file_data.replace('$ACTIVITY_NAME$', s.ACTIVITY_SETUP)
    file_data = file_data.replace('$PACKAGE_NAME$', s.PACKAGE_NAME)
    file_data = file_data.replace('$BASE_VIEW$', s.BASE_VIEW)
    file_data = file_data.replace('$TABS$', s.TABS)
    file_data = file_data.replace('$NAV_VIEW$', s.NAV_VIEW)
    file_data = file_data.replace('$BASE_HEADER$', s.BASE_HEADER)
    file_data = file_data.replace('$BASE_DRAWER$', s.BASE_DRAWER)
    return file_data
