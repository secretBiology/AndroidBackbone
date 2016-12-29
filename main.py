"""
Main Code generation file
"""
import functions as f
import settings as s
import templates.CodeTemplates as Templates
import templates.ResourceTemplates as Resource
import templates.LayoutTemplates as Layout

base_activity_path = "%s/%s" % (s.BASE_PACKAGE_PATH, s.UI_FOLDER.lower())
base_database_path = "%s/%s" % (s.BASE_PACKAGE_PATH, s.DATABASE_FOLDER.lower())

# Make base UI
f.make_folder(base_activity_path)
with open("%s/%s%s" % (base_activity_path, s.BASE_ACTIVITY, s.JAVA_EXTENSION), 'w') as file:
    file.write(Templates.base_activity())

with open("%s/%s%s" % (base_activity_path, s.ACTIVITY_SETUP, s.JAVA_EXTENSION), 'w') as file:
    file.write(Templates.activity_setup())

# Database
f.make_folder(base_database_path)
with open("%s/%s%s" % (base_database_path, s.DATABASE_MANAGER, s.JAVA_EXTENSION), 'w') as file:
    file.write(Templates.database_manager())

# Resources
f.make_folder(s.BASE_RES + "/layout")
f.make_folder(s.BASE_RES + "/menu")
f.make_folder(s.BASE_RES + "/drawable")
f.make_folder(s.BASE_RES + "/values")

with open("%s/values/strings.xml" % s.BASE_RES, 'w') as file:
    file.write(Resource.strings())

with open("%s/values/styles.xml" % s.BASE_RES, 'w') as file:
    file.write(Resource.styles())

with open("%s/values/dimens.xml" % s.BASE_RES, 'w') as file:
    file.write(Resource.dimens())

with open("%s/values/material_colors.xml" % s.BASE_RES, 'w') as file:
    file.write(Resource.material_colors())

with open("%s/drawable/%s.xml" % (s.BASE_RES, s.SIDE_NAV_BAR), 'w') as file:
    file.write(Resource.side_nav())

with open("%s/drawable/%s.xml" % (s.BASE_RES, s.ICON_HOME), 'w') as file:
    file.write(Resource.home_icon())

with open("%s/menu/%s.xml" % (s.BASE_RES, s.BASE_MENU), 'w') as file:
    file.write(Resource.base_menu())

with open("%s/menu/%s.xml" % (s.BASE_RES, s.BASE_DRAWER), 'w') as file:
    file.write(Resource.base_drawer())

# Layouts

with open("%s/layout/%s.xml" % (s.BASE_RES, s.BASE_LAYOUT), 'w') as file:
    file.write(Layout.base_layout())

with open("%s/layout/%s.xml" % (s.BASE_RES, s.BASE_HEADER), 'w') as file:
    file.write(Layout.base_header())

with open("%s/layout/%s.xml" % (s.BASE_RES, s.BASE_FRAGMENT), 'w') as file:
    file.write(Layout.base_recycler())

with open("%s/layout/%s.xml" % (s.BASE_RES, s.BASE_VIEWPAGER), 'w') as file:
    file.write(Layout.base_view_pager())
