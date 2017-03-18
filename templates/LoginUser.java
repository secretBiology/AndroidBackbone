package $PACKAGE_NAME$.background.tasks;

import android.content.Context;
import android.os.AsyncTask;
import android.support.annotation.NonNull;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.GetTokenResult;
import com.secretbiology.helpers.general.Log;
import $PACKAGE_NAME$.preferences.AppPrefs;

/**
 * Created by Dexter for Manager .
 * Code is released under MIT license
 */

public class LoginUser extends AsyncTask<Object, Integer, Void> {


    private OnDataRetrieved retrieved;
    private AppPrefs prefs;
    private String email, password;
    private FirebaseAuth auth;

    public LoginUser(OnDataRetrieved retrieved) {
        this.retrieved = retrieved;
    }

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
        retrieved.updateDialog(20, "Signing in...");
    }


    @Override
    protected Void doInBackground(Object... params) {
        Context context = (Context) params[0];
        email = (String) params[1];
        password = (String) params[2];
        prefs = new AppPrefs(context);
        auth = FirebaseAuth.getInstance();
        Log.inform("Login Process started");
        login();
        return null;
    }

    @Override
    protected void onPostExecute(Void aVoid) {
        super.onPostExecute(aVoid);
        retrieved.onTaskComplete();
    }

    private void login() {

        auth.signInWithEmailAndPassword(email, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    prefs.setEmail(email);
                    prefs.userLoggedIn();
                    retrieved.updateDialog(40, "Loading data");
                    if (auth.getCurrentUser() != null) {
                        auth.getCurrentUser().getToken(false).addOnCompleteListener(new OnCompleteListener<GetTokenResult>() {
                            @Override
                            public void onComplete(@NonNull Task<GetTokenResult> task) {
                                if (task.isSuccessful()) {
                                    String uid = auth.getCurrentUser().getUid();
                                    String token = task.getResult().getToken();
                                    getData(uid, token);
                                } else {
                                    error(task.getException().getLocalizedMessage());
                                }

                            }
                        });
                    }
                } else {
                    error(task.getException().getLocalizedMessage());
                }

            }
        });

    }

    private void getData(final String uid, final String token) {

        //TODO
    }


    private void error(String string) {
        retrieved.showError(string);
        Log.error(string);
    }

    public interface OnDataRetrieved {

        void updateDialog(int progress, String message);

        void showError(String message);

        void onTaskComplete();
    }
}
