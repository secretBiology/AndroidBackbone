/*
 * Copyright (c) 2016. Rohit Suratekar
 */

package  $CURRENT_PACKAGE$;

import android.app.Activity;
import android.graphics.drawable.GradientDrawable;
import android.support.design.widget.NavigationView;
import android.support.design.widget.TabLayout;
import android.view.View;
import android.view.ViewStub;
import android.widget.ImageView;
import android.widget.TextView;

import $PACKAGE_NAME$.R;
import com.secretbiology.helpers.general.General;


public class $ACTIVITY_NAME$ {

    private static final String TAG = "$ACTIVITY_NAME$";

    public  $ACTIVITY_NAME$(Activity activity, int layoutResource, String title) {
        ViewStub viewStub = (ViewStub) activity.findViewById(R.id.$BASE_VIEW$);
        viewStub.setLayoutResource(layoutResource);
        viewStub.inflate();
        activity.setTitle(title);

        NavigationView navigationView = (NavigationView) activity.findViewById(R.id.$NAV_VIEW$);
        navigationView.inflateHeaderView(R.layout.$BASE_HEADER$); //Header
        navigationView.inflateMenu(R.menu.$BASE_DRAWER$);
        View header = navigationView.getHeaderView(0);
        
        GradientDrawable backgroundGradient = (GradientDrawable) header.getBackground();
        backgroundGradient.setOrientation(GradientDrawable.Orientation.LEFT_RIGHT);
        backgroundGradient.setGradientCenter(10, 0);
        backgroundGradient.setColor(General.getColor(activity, R.color.colorPrimary));
        
        TextView name = (TextView) header.findViewById(R.id.nav_header_name);
        TextView email = (TextView) header.findViewById(R.id.nav_header_email);
        ImageView icon = (ImageView) header.findViewById(R.id.nav_header_icon);
    }

}
