package $PACKAGE_NAME$.common;

import android.app.Activity;
import android.graphics.drawable.GradientDrawable;
import android.os.Build;
import android.support.design.widget.NavigationView;
import android.view.View;
import android.view.ViewStub;

import $PACKAGE_NAME$.R;

class SetUpActivity {

    SetUpActivity(Activity activity, CurrentActivity currentActivity) {
        activity.setContentView(R.layout.base_layout);

        ViewStub viewStub = (ViewStub) activity.findViewById(R.id.base_view);
        viewStub.setLayoutResource(currentActivity.getLayout());
        viewStub.inflate();
        activity.setTitle(activity.getString(currentActivity.getTitle()));

        NavigationView navigationView = (NavigationView) activity.findViewById(R.id.nav_view);
        navigationView.inflateHeaderView(R.layout.base_header); //Header
        navigationView.inflateMenu(R.menu.base_drawer);
        View header = navigationView.getHeaderView(0);

        GradientDrawable backgroundGradient = (GradientDrawable) header.getBackground();
        backgroundGradient.setOrientation(GradientDrawable.Orientation.LEFT_RIGHT);
        backgroundGradient.setGradientCenter(10, 0);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            backgroundGradient.setColor(activity.getResources().getColor(R.color.colorPrimary, activity.getTheme()));
        } else {
            backgroundGradient.setColor(activity.getResources().getColor(R.color.colorPrimary));
        }
    }

}
