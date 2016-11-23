/*
 * Copyright (c) 2016. Rohit Suratekar
 */

package $CURRENT_PACKAGE$;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class $DATABASE_MANAGER$ extends SQLiteOpenHelper {
    //TODO: Change Name and Version
    private static String DATABASE_NAME = "$PACKAGE_NAME$";
    private static int DATABASE_VERSION = 1;
    private Context context;

    public $DATABASE_MANAGER$ (Context context, String name, SQLiteDatabase.CursorFactory factory, int version) {
        super(context, name, factory, version);
        this.context = context;
    }

    private $DATABASE_MANAGER$ (Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
        this.context = context;
    }


    private static $DATABASE_MANAGER$  instance;

    private int mOpenCounter;

    public SQLiteDatabase mDatabase;


    public static synchronized $DATABASE_MANAGER$  getInstance(Context context) {
        if (instance == null) {
            instance = new $DATABASE_MANAGER$ (context.getApplicationContext());
        }
        return instance;
    }

    public synchronized SQLiteDatabase openDatabase() {
        mOpenCounter++;
        if (mOpenCounter == 1) {
            // Opening new database
            mDatabase = instance.getWritableDatabase();
        }
        return mDatabase;
    }

    synchronized void closeDatabase() {
        mOpenCounter--;
        if (mOpenCounter == 0) {
            // Closing database
            mDatabase.close();
        }
    }

    @Override
    public void onCreate(SQLiteDatabase db) {

        //TODO: Make Tables 
        //e.g : Data.makeTable(db);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        //TODO: Your upgrade rules
    }
}