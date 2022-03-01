
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
impport pickle

df.pd.dataframe(columns = ['procedure_id', 'a', 'b', 'c', 'output'])
for i in range(50)
    attributes = get_procedure_attributes(procedure_id = i)
    label = get_procedure_success(procedure_id = i)
    dict = {'output' : label}
    dict.update(attributes)
    final_dict = dict.update(attributes)
df = df.append(final_dict)
X_train = df.iloc[:,df.columns != 'output']
Y_train = df['output']
model = LogisticRegression(solver='liblinear', random_state=0).fit(X_train, Y_train)

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
   

