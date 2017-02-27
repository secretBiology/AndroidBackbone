package $PACKAGE_NAME$.common;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.MenuItem;

import $PACKAGE_NAME$.R;

public abstract class BaseActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    public Toolbar toolbar;
    private CurrentActivity currentActivity;
    private NavigationView navigationView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.currentActivity = setUpActivity();
        new SetUpActivity(this, currentActivity);
        toolbar = (Toolbar) findViewById(R.id.toolbar);
        navigationView = (NavigationView) findViewById(R.id.nav_view);
        setSupportActionBar(toolbar);
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout); //Base drawer layout
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (navigationView != null) {
            if (navigationView.getMenu().findItem(currentActivity.getNavigationID()) != null) {
                navigationView.getMenu().findItem(currentActivity.getNavigationID()).setChecked(true);
            }
        }
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (item.getItemId() != currentActivity.getNavigationID()) {
            final CurrentActivity c = getByNavigationID(item.getItemId());
            if (c != null) {
                new Handler().postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        startActivity(new Intent(getBaseContext(), c.getaClass()));
                    }
                }, 300);
            }
        }
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    @Nullable
    private CurrentActivity getByNavigationID(int id) {
        for (CurrentActivity c : CurrentActivity.values()) {
            if (c.getNavigationID() == id) {
                return c;
            }
        }
        return null;
    }

    protected abstract CurrentActivity setUpActivity();
}
