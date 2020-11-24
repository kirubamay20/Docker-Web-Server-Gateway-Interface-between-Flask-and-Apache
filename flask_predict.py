import pickle 
from flask import Flask,request
from flasgger import Swagger
import pandas as pd
import numpy as np

with open('*/diabetes_rf.pkl', 'rb') as model_file:
  model=pickle.load(model_file)

app1=Flask(__name__)
swagger=Swagger(app1)

@app.route('/predict')
def predict_cancer_file():
    input_data = pd.read_csv(request.files.get["input_file"], header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))
if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000)
