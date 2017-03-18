package $PACKAGE_NAME$.background;

import okhttp3.OkHttpClient;
import okhttp3.ResponseBody;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetroCalls {

    private static final String BASE_URL = "https://yourbaseurl_with_slash.com/"; //TODO

    private Retrofit builder() {
        return new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(getClient())
                .build();
    }

    private OkHttpClient getClient() {
        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();
        HttpLoggingInterceptor interceptor = new HttpLoggingInterceptor();
        interceptor.setLevel(HttpLoggingInterceptor.Level.BODY);
        return httpClient.addInterceptor(interceptor).build();
    }

    public Call<ResponseBody> getUserInfo(String uid, String token) {
        return builder().create(RetroServices.class).
                getUserInfo(uid, token);
    }
}
