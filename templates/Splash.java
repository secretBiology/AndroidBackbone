package $PACKAGE_NAME$;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

import $PACKAGE_NAME$.activities.Home;

public class Splash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.splash);
        startActivity(new Intent(this, Home.class));
    }
}
