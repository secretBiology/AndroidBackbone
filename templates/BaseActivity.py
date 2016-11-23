import settings as s
import functions as f


class Build:
    def __init__(self, file):
        # Package Import
        print("package " + s.PACKAGE_NAME + "." + s.UI_FOLDER + ";", file=file, end="\n")
        # Android Import
        f.add_import(file, "android.os.Bundle")
        f.add_import(file, "android.support.design.widget.NavigationView")
        f.add_import(file, "android.support.v4.widget.DrawerLayout")
        f.add_import(file, "android.support.v7.app.ActionBarDrawerToggle")
        f.add_import(file, "android.support.v7.app.AppCompatActivity")
        f.add_import(file, "android.support.v7.widget.Toolbar")
        f.add_import(file, "android.view.Menu")
        f.add_import(file, "android.view.MenuItem")
        # Project Import
        f.add_import(file, s.PACKAGE_NAME + ".R")
        class_line = "public abstract class %s extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {" % (
            s.BASE_ACTIVITY)
        f.add_line(file, class_line)
        f.tabbed_public(file, "Toolbar toolbar")
        f.tabbed_public(file, "NavigationView navigationView")
        f.tabbed(file, "@Override\n\tprotected void onCreate(Bundle savedInstanceState) {")
        f.tabbed(file, "super.onCreate(savedInstanceState);")
        f.tabbed(file, "setContentView(R.layout.%s);" % s.BASE_LAYOUT)
        f.tabbed(file, "toolbar = (Toolbar) findViewById(R.id.%s);" % s.TOOLBAR)
        f.tabbed(file, "setSupportActionBar(toolbar);")
