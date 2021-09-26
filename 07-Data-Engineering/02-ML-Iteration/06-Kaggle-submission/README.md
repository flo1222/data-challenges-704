# Use you saved model
Now you will submit your first submission to kaggle.  

For that as you probably have different pipeline blocs, we will all retrain the same given pipeline inside `TaxiFareModel`, which is the correction from last exercice.

# Train on small sample
Let us train our pipeline on 100 000 line.   
For that please check that following parameters are set inside `trainer.py`:
```python
params = dict(nrows=100000, # number of samples
              local=False,  # set to False to get data from aws
              optimize=True,
              estimator="xgboost",
              mlflow=True,  # set to True to log params to mlflow
              experiment_name=experiment,
              pipeline_memory=None,
              distance_type="manhattan",
              feateng=["distance_to_center", "direction", "distance", "time_features", "geohash"])
```
Then, to install our package and run our training run:
```bash
make install run_locally
```
Wait a bit and check that your pipeline has been saved under `model.joblib`


You might wonder why we ran `make install` ?

🚨 This step is very important 🚨  
👉 You remember that your whole Pipeline is integrated inside your `model.joblib` now ...  
👉 Including your custom encoders written inside `encoders.py` ...   
👉 When executing predictions from your loaded pipeline, the pipeline will look for your `TimeFeaturesEncoder` or `DistanceTransformer`...  
👉 Which are function imported from TaxiFareModel
👉 so **they need to be installed as a module** with `pip install . -U`

# Use your model to predict on kaggle test set

Inspect code inside predict.py and and identify following steps:
- loading `model.joblib`
- loading test sample from `data/test.csv` (it is the test sample form kaggle here)
- apply predicitions to test set and saves results under `predictions_test_ex.csv`

Now run:
```bash
python predict.py
```

Now take the outputed csv and [submit it to kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/submit)  

YUou might need to login to kaggle or register [here](https://www.kaggle.com/account/login) if you don't already have an account 


# Train on bigger sample and check score evolution
Modify parameters to train model on 1 000 000 lines, by simply setting `n_rows=1000000` inside `trainer.py`  

Then again:
```bash
make run_locally
```

# Bonus: Kaggle cli installation for automated submissions
- login to kaggle or register [here](https://www.kaggle.com/account/login) if you don't already have an account
- install cli:
```python
pip install kaggle
```
- get token following instructions [here](https://github.com/Kaggle/kaggle-api#api-credentials)
==> summarized steps : on [kaggle[(https://www.kaggle.com)] click on `My Account` and then `Create New API Token` which you should save under `~/.kaggle/kaggle.json` (or `C:\Users\<Windows-username>\.kaggle\kaggle.json` for windows)
- test installation
```python
kaggle competitions list
```


