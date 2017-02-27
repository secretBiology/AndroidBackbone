package $PACKAGE_NAME$.activities;

import android.os.Bundle;

import $PACKAGE_NAME$.common.BaseActivity;
import $PACKAGE_NAME$.common.CurrentActivity;

public class Home extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected CurrentActivity setUpActivity() {
        return CurrentActivity.HOME;
    }
}
