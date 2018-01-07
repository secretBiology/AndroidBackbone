package $PACKAGE_NAME$;

import android.os.Bundle;

import $PACKAGE_NAME$.common.BaseActivity;

public class Home extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.home);
    }

    @Override
    protected int setNavigationMenu() {
        return R.id.nav_home;
    }
}
