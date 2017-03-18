package $PACKAGE_NAME$.activities.login;

import android.app.AlertDialog;
import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;

import com.secretbiology.helpers.general.General;
import com.secretbiology.helpers.general.views.InputView;
import $PACKAGE_NAME$.R;
import $PACKAGE_NAME$.activities.Home;
import $PACKAGE_NAME$.background.tasks.LoginUser;
import $PACKAGE_NAME$.common.BaseActivity;
import $PACKAGE_NAME$.common.CurrentActivity;

import butterknife.BindView;
import butterknife.OnClick;

public class Login extends BaseActivity {

    @BindView(R.id.log_in_email)
    InputView email;
    @BindView(R.id.log_in_pass)
    InputView pass;

    private ProgressDialog dialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        dialog = new ProgressDialog(Login.this);
        dialog.setCancelable(false);
        dialog.setIndeterminate(false);
        dialog.setMax(100);
    }

    @Override
    protected CurrentActivity setUpActivity() {
        return CurrentActivity.LOGIN;
    }

    @OnClick(R.id.log_bt_done)
    public void checkLogin() {
        if (General.isValidEmail(email.getText())) {
            email.setErrorEnabled(false);
            if (pass.getText().length() > 5) {
                login(email.getText().trim(), pass.getText());
            } else {
                pass.setError("Password should be at least 6 character long");
            }
        } else {
            email.setError("Invalid email!");
        }
    }

    private void login(final String email, String password) {
        dialog.show();
        new LoginUser(new LoginUser.OnDataRetrieved() {
            @Override
            public void updateDialog(int progress, String message) {
                dialog.setProgress(progress);
                dialog.setMessage(message);
            }

            @Override
            public void showError(String message) {
                showDialog(message);
            }

            @Override
            public void onTaskComplete() {
                //TODO
                exitActivity();
            }
        }).execute(getBaseContext(), email, password);

    }

    private void showDialog(String message) {
        if (dialog.isShowing()) {
            dialog.dismiss();
        }
        new AlertDialog.Builder(this)
                .setTitle("Oops!")
                .setMessage(message)
                .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                    }
                })
                .show();
    }

    private void exitActivity() {
        if (dialog.isShowing()) {
            dialog.dismiss();
        }
        Intent intent = new Intent(Login.this, Home.class);
        intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK | Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(intent);
        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
    }
}
