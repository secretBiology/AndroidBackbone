import settings as s
import os

script_path = os.path.dirname(__file__)


def base_layout():
    relative_path = "files/base_layout.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$TOOLBAR$', s.TOOLBAR)
    file_data = file_data.replace('$DRAWER_LAYOUT$', s.DRAWER_LAYOUT)
    file_data = file_data.replace('$TABS$', s.TABS)
    file_data = file_data.replace('$BASE_VIEW$', s.BASE_VIEW)
    file_data = file_data.replace('$NAV_VIEW$', s.NAV_VIEW)
    return file_data


def base_recycler():
    relative_path = "files/base_fragment.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$BASE_RECYCLER$', s.BASE_RECYCLER)
    return file_data


def base_header():
    relative_path = "files/base_header.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$SIDE_NAV_BAR$', s.SIDE_NAV_BAR)
    file_data = file_data.replace('$NAV_HEADER_HEIGHT$', s.NAV_HEADER_HEIGHT)
    return file_data


def base_view_pager():
    relative_path = "files/base_view_pager.xml"
    absolute_path = os.path.join(script_path, relative_path)
    with open(absolute_path, 'r') as base_file:
        file_data = base_file.read()
    file_data = file_data.replace('$BASE_VIEWPAGER$', s.BASE_VIEWPAGER)
    file_data = file_data.replace('$BASE_FAB$', s.BASE_FAB)
    file_data = file_data.replace('$FAB_MARGIN$', s.FAB_MARGIN)
    return file_data
