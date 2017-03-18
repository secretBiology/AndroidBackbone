package $PACKAGE_NAME$.common;

import $PACKAGE_NAME$.R;
import $PACKAGE_NAME$.activities.Home;

public enum CurrentActivity {

    HOME(Home.class, R.string.home, R.layout.home, R.id.nav_home),
    LOGIN(Login.class, R.string.login, R.layout.login, R.id.nav_header_icon);

    private Class aClass;
    private int title;
    private int layout;
    private int navigationID;

    CurrentActivity(Class aClass, int title, int layout, int navigationID) {
        this.aClass = aClass;
        this.title = title;
        this.layout = layout;
        this.navigationID = navigationID;
    }

    public Class getaClass() {
        return aClass;
    }

    public int getTitle() {
        return title;
    }

    public int getLayout() {
        return layout;
    }

    public int getNavigationID() {
        return navigationID;
    }
}
