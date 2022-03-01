
import pickle

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(get_procedure_attributes(procedure_id=None))
print(result)

