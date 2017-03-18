package $PACKAGE_NAME$.background;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

interface RetroServices {

    @GET("users/{uid}.json")
    Call<ResponseBody> getUserInfo(@Path("uid") String user,
                                   @Query("auth") String token);
}
