from database_maker.model_specifications import *

v1 = Variable("key", VariableTypes.PRIMARY_KEY)
v2 = Variable("name", VariableTypes.STRING)
v3 = Variable("mobile", VariableTypes.STRING)
v4 = Variable("someOtherDate", VariableTypes.STRING)

v_list = [v1, v2, v3, v4]

model = Maker("ExampleModel", v_list)
model.make_model()
model.make_database_file("ExampleData")
