from enum import Enum

from .functions import *


class VariableProperties:
    def __init__(self, java_type: str, sql_type: str, return_type: str):
        self.java = java_type
        self.sql = sql_type
        self.return_type = return_type


class VariableTypes(Enum):
    STRING = VariableProperties("String", "TEXT", "getString")
    INT = VariableProperties("int", "INTEGER", "getInt")
    PRIMARY_KEY = VariableProperties("int", "INTEGER PRIMARY KEY", "getInt")
    DOUBLE = VariableProperties("double", "DOUBLE", "getDouble")


class Variable:
    def __init__(self, name: str, variable_type: VariableTypes):
        self.name = name
        self.variable_type = variable_type

    def __str__(self):
        return self.variable_type.value


def convert_row(name, var_list):
    s = " private %(name)s convertRow(Cursor cursor) {\n\t%(name)s m = new %(name)s();\n\t" % dict({"name": name})
    for m in var_list:
        v = m  # type: Variable
        s += "m.%s(cursor.%s(cursor.getColumnIndex(%s)))\n\t" % (
            "set" + first(v.name), v.variable_type.value.return_type, v.name.upper())
    s += "return m;\n\t}"
    return s


class Maker:
    def __init__(self, name: str, variables):
        self.name = name
        self.variables = variables
        self.primary_key = None
        for v in variables:
            if v.variable_type.value.sql == "INTEGER PRIMARY KEY":
                self.primary_key = v
                break

    def make_model(self):
        with open(self.name + ".java", "w") as f:
            print("public class " + self.name + " {", file=f)
            for m in self.variables:
                v = m  # type: Variable
                print("\tprivate %s %s;" % (v.variable_type.value.java, v.name), file=f)

            print("\n\t%s() {\n\t}\n" % self.name, file=f)

            for m in self.variables:
                print(make_setter(m), file=f)
                print(make_getter(m), file=f)
            print("}", file=f)

    def make_database_file(self, name: str):
        with open(name + ".java", "w") as f:
            print(import_section(), file=f)
            print("public class " + name + " {", file=f)
            print("\tprivate static final String TABLE = \"%s\";" % (first(self.name) + "Table"), file=f)
            for m in self.variables:
                v = m  # type: Variable
                print("\tprivate static final String %s = \"%s\";" % (v.name.upper(), v.name),
                      file=f)

            # Local items
            print("\n\tprivate SQLiteDatabase db;\n\tprivate Database database;\n\tprivate Context context;", file=f)
            # Constructor
            print(constructor(name), file=f)
            print(make(self.variables), file=f)
            print(drop(), file=f)
            print(add(self.name), file=f)
            print(get_all(self.name), file=f)
            print(clear_all(), file=f)
            if self.primary_key is not None:
                print(delete(self.name, self.primary_key), file=f)
                print(update(self.name, self.primary_key), file=f)
            else:
                print("//No primary key found, hence no delete and update method is created", file=f)
            print(content_values(self.name, self.variables), file=f)
            print(convert_row(self.name, self.variables), file=f)
            print("}", file=f)
