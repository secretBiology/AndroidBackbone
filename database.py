from database_maker.model_specifications import *

v_list = [Variable("key", VariableTypes.PRIMARY_KEY),
          Variable("name", VariableTypes.STRING)]

model = Maker("Example", v_list)
model.serialization = False
model.make_model()
model.make_database_file("ExampleData")
