from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return {"key": "value"}

@app.get(
    "/predict_fare/{pickup_datetime}/{pickup_longitude}/{pickup_latitude}/{dropoff_longitude}/{dropoff_latitude}/{passenger_count}")
def predict_fare(pickup_datetime, pickup_longitude: float, pickup_latitude: float, dropoff_longitude: float, dropoff_latitude: float, passenger_count: int):
    X_pred = pd.DataFrame(
        {'key':["2013-07-06 17:18:00.000000119"],
         "pickup_datetime": [pickup_datetime],
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "passenger_count": [passenger_count] 
        })
    # pipeline = generate_submission_csv()
    pipeline = joblib.load("model.joblib")
    # y_pred = pipeline.predict(X_pred)
    if "best_estimator_" in dir(pipeline):
        y_pred = pipeline.best_estimator_.predict(X_pred)
    else:
        y_pred = pipeline.predict(X_pred)
        result = []
    result.append(y_pred)
    prediction = result[0][0]
    return {
            "prediction": str(prediction)
            }
 

import os
from math import sqrt
import joblib
from TaxiFareModel.params import MODEL_NAME
from google.cloud import storage
from sklearn.metrics import mean_absolute_error, mean_squared_error
from TaxiFareModel.params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH, PROJECT_ID, MODEL_NAME
from TaxiFareModel.data import clean_df

def download_model(model_directory="PipelineTest", bucket=BUCKET_NAME, rm=True):
    client = storage.Client().bucket(bucket)
    storage_location = 'models/{}/versions/{}/{}'.format(
        MODEL_NAME,
        model_directory,
        'model.joblib')
    blob = client.blob(storage_location)
    blob.download_to_filename('model.joblib')
    print(f"=> pipeline downloaded from storage")
    model = joblib.load('model.joblib')
    return model

def generate_submission_csv(folder="Pipeline", kaggle_upload=False):
    pipeline = download_model(folder)
    return pipeline