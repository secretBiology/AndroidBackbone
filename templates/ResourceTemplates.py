import settings as s
import os

script_path = os.path.dirname(__file__)


def base_menu():
    relative_path = "files/base_menu.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$ACTION_SETTINGS$', s.ACTION_SETTINGS)
    return file_data


def base_drawer():
    relative_path = "files/base_drawer.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$NAV_HOME$', s.NAV_HOME)
    file_data = file_data.replace('$ICON_HOME$', s.ICON_HOME)
    return file_data


def strings():
    relative_path = "files/strings.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$APP_NAME$', s.APP_NAME)
    file_data = file_data.replace('$NAV_CLOSE$', s.NAV_CLOSE)
    file_data = file_data.replace('$NAV_OPEN$', s.NAV_OPEN)
    return file_data


def dimens():
    relative_path = "files/dimens.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$NAV_HEADER_HEIGHT$', s.NAV_HEADER_HEIGHT)
    file_data = file_data.replace('$FAB_MARGIN$', s.FAB_MARGIN)
    return file_data


def side_nav():
    relative_path = "files/%s.xml" % s.SIDE_NAV_BAR
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    return file_data


def home_icon():
    relative_path = "files/%s.xml" % s.ICON_HOME
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    return file_data


def styles():
    relative_path = "files/styles.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    return file_data

def material_colors():
	relative_path = "files/material_colors.xml"
	absolute_path = os.path.join(script_path, relative_path)
	with open(absolute_path, 'r') as base_file:
		file_data = base_file.read()
	return file_data
