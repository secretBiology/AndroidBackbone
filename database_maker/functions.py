def first(x):
    return x[0].upper() + x[1:]


def make_setter(var) -> str:
    return "\tpublic void set%(c_name)s(%(java_type)s %(name)s){this.%(name)s = %(name)s;}" \
           % {"name": var.name,
              "c_name": first(var.name),
              "java_type": var.variable_type.value.java}


def make_getter(var) -> str:
    return "\tpublic %(java_type)s get%(c_name)s(){return this.%(name)s;}" \
           % {"name": var.name,
              "c_name": first(var.name),
              "java_type": var.variable_type.value.java}


def constructor(name) -> str:
    return "\n\tpublic %s(Context context) {\n\tthis.database = Database.getInstance(context);" \
           "\n\tthis.db = database.openDatabase();\n\tthis.context = context;\n\t}" % name


def make(var_list) -> str:
    s = "static void make(SQLiteDatabase db) {\n\tList<String[]> columnList = new ArrayList<>();\n\t"
    for m in var_list:
        v = m
        s += "columnList.add(new String[]{%s, \"%s\"});\n\t" % (v.name.upper(), v.variable_type.value.sql)
    s += "db.execSQL(QueryBuilder.buildTableQuery(TABLE, columnList));\n\tLog.inform(\"Table \'\" + TABLE + \"\' is created.\");\n\t}"
    return s


def import_section() -> str:
    s = "import android.content.ContentValues;\nimport android.content.Context;\nimport android.database.Cursor;\nimport android.database.sqlite.SQLiteDatabase;\n"
    s += "\nimport java.util.ArrayList;\nimport java.util.List;\nimport com.secretbiology.helpers.general.database.QueryBuilder;\n"
    return s


def drop() -> str:
    return "static void drop(SQLiteDatabase db) {\n\tdb.execSQL(\"DROP TABLE IF EXISTS \" + TABLE);\n\tLog.inform(\"Table \" + TABLE + \" dropped.\");\n\t}"


def add(model_name) -> str:
    return " public int add(%s model) {\n\t int id = (int) db.insert(TABLE, null, putContentValues(model));\n\t database.closeDatabase();" \
           "\n\t Log.inform(\"Added new entry to database\");\n\treturn id;\n\t}" % model_name


def content_values(model_name, var_list, primary_key) -> str:
    s = "private ContentValues putContentValues(%s model) {\n\tContentValues values = new ContentValues();\n\t" % model_name
    for m in var_list:
        if m != primary_key:
            v = m
            s += "values.put(%s, model.%s());\n\t" % (v.name.upper(), "get" + first(v.name))
    s += "return values;\n\t}"
    return s


def delete(name, primary_key_var) -> str:
    return "public void delete(%s model) {\n\t db.delete(TABLE, %s + \"= ?\", new String[]{String.valueOf(model.%s())});" \
           "\n\tdatabase.closeDatabase();\n\t}" % (
               name, primary_key_var.name.upper(), "get" + first(primary_key_var.name))


def update(name, primary_key_var) -> str:
    return "public int update(%s model) {\n\t int updated = db.update(TABLE, putContentValues(model), %s + \"= ?\", " \
           "new String[]{String.valueOf(model.%s())});\n\treturn updated;}" % (
               name, primary_key_var.name.upper(), "get" + first(primary_key_var.name))


def get_all(name) -> str:
    s = "public List<%s> getAll() {\n\t String query = new QueryBuilder().selectAll().fromTable(TABLE).build();\n\t" % name
    s += "List<%s> all = new ArrayList<>();\n\t" % name
    s += "Cursor cursor = db.rawQuery(query, null);\n\t if (cursor != null) {\n\t if (cursor.moveToFirst()) {\n\tdo\n\t{all.add(convertRow(cursor));\n\t } " \
         "while (cursor.moveToNext());}\n\tcursor.close();}\n\treturn all;}"
    return s


def clear_all() -> str:
    return "public void clearAll() { \n\tdb.execSQL(\"DELETE FROM \" + TABLE);\n\tdatabase.closeDatabase();\n\tLog.inform(\"All entries cleared\");\n\t}"
