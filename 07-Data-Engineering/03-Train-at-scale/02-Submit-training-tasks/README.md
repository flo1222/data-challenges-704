# Objective

To get familiar with Google AI Platform, we will first deploy and train a simple model for the TaxiFare Challenge.

This model will be a linear model **`fare_amount ~ C * distance`**

# Reminders

## Packaging
Here a quick reminder of our packaging notions from last monday, to package python code, nothing more than:
 - structure your code in `.py` files (modules) in the directory of your package
 - make sure you have an `__init__.py` file
 - add a `setup.py` file
 - add an exhaustive list of the python packages required in order to run your code inside `setup.py`

Packaging basically means I want my code to be able to run anywhere by any user.

In our case we want our model to run on GCP servers.

## Run python files from command line
To run `trainer.py` file below:
```bash
├── TaxiFareModel
│   ├── __init__.py
│   └── trainer.py
```
There are several ways:
```bash
python TaxiFareModel/trainer.py
```
Or
```bash
python -m TaxiFareModel.trainer
```

# Package structure

To start we need to create a python module. We will use notion we saw on monday.
We will start by creating the following structure:

```bash
├── Makefile          # store all necessary bash commands here
├── README.md
├── TaxiFareModel     # our package that will be deployed to GCP server
│   ├── __init__.py
│   └── trainer.py
├── requirements.txt  # dependencies to install so that the TaxiFareModel package runs
└── setup.py          # mandatory file to install our package
```

Inspect `trainer.py` and implement the following functions.
Here the function are quite simple and we have implemented all of them earlier on this week.
The objective here is to implement on our own a very simple workflow that we will later run on GCP machines.

```python
def get_data():
    """method used in order to get the training data (or a portion of it) from google cloud bucket"""
    pass

def compute_distance(df):
    """method used in order to compute distance of df"""
    pass

def preprocess(df):
    """method that pre-processes the data"""
    df["distance"] = compute_distance(df)
    X_train = df[["distance"]]
    y_train = df["fare_amount"]
    return X_train, y_train

def train_model(X_train, y_train):
    """method that trains the model"""
    rgs = linear_model.Lasso(alpha=0.1)
    rgs.fit(X_train, y_train)
    return rgs


def save_model(reg):
    """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
    HINTS : use joblib library and google-cloud-storage"""

    # saving the trained model to disk is mandatory to then beeing able to upload it to storage
    # Implement here
    print("saved model.joblib locally")

    # Implement here
    print("uploaded model.joblib to gcp cloud storage under \n => {}".format(storage_location))

if __name__ == '__main__':
    df = get_data()
    X_train, y_train = preprocess(df)
    clf = train_model(X_train, y_train)
    save_model(clf)
```

👉 Get help from [google documentation](https://pypi.org/project/google-cloud-storage/) to upload file to storage
👉 [Why if __name__ == '__main__' ?](http://sametmax.com/pourquoi-if-__name__-__main__-en-python/)

# Run the code locally
Here we will run this simple workflow on our own machines

## Install correct python dependencies

```bash
pip install -r requirements.txt
```

## Check that the code runs locally

In Sublime Text, open the `Makefile` and set the two first lines variables:

- `PROJECT_ID`
- `BUCKET_NAME` (where GCP will store training material)

Then open the `TaxiFareModel/trainer.py` and set the two global variables:

- `BUCKET_NAME` (where the training data is stored)
- `PATH_INSIDE_BUCKET` (should be `data/UPLOADED_FILE_NAME.csv`, `data/train_1k.csv` if you did not change the makefile)

Then launch:

```bash
make run_locally
```

What did we do here?

 👉 We loaded the training data stored on your GCP bucket

 👉 We trained a simple model on your machine using this data

 👉 We saved the trained model locally under `model.joblib`

 👉 We uploaded the `model.joblib` trained model to your GCP bucket (in another folder)

Check that :

- A `model.joblib` file has been created locally
- This file has been uploaded to the bucket `BUCKET_NAME` ([select your bucket from here](https://console.cloud.google.com/storage/browser)), in the following path: `models/taxi_fare_model/VERSION`.

This is the first step towards training online. You may not really see any difference yet, since your machine still does the hard work. Now let's do the training on GCP.

# Run the code on GCP instances
Here we will launch the exact same code as before, the only difference is that the code will be executed on GCP machines through `AI Platform`.
Here we will just want to find a way to ask GCP to:

👉 Copy our code (our package) to a GCP machine

👉 Install the package and its requirements thanks to `setup.py` (you should start to love it right)

👉 Run `trainer.py` on the GCP machine

👉 Close our computer, grab a coffee and come back when the training is finished

## Specify your requirements to GCP inside setup.py

Make sure you have installed the dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

Check version of python libraries we have installed in the virtualenv:

```bash
pip freeze | grep -E "pandas|scikit|google-cloud-storage|gcsfs"
```

Make sure they match with the `REQUIRED_PACKAGES` list in `setup.py`.

## Submit Training to GCP
The GCP cli `gcloud` installed before allows us to communicate with GCP. It provides commands allowing to use all its APIs.
In particular, it provides a command allowing to request the online training of a model provided in a package.

The command is `gcloud ai-platform jobs submit training`.
The command requires:
- `JOB_NAME`: a name identifying a training occurence, which will be visible in the [GCP console](https://console.cloud.google.com/ai-platform/jobs) once it has ran
- `BUCKET_NAME`: a bucket where GCP will store internal training data we are not interested in (here we ask GCP to store these files in a trainings folder)
- `BUCKET_TRAINING_FOLDER`: a bucket folder where GCP will store the uploaded package used for the training
- `PACKAGE_NAME`: the name of the package containing the code that will handle the data and train the model
- `FILENAME`: the main file of the package
- `PYTHON_VERSION`: the version of python to be used for the training
- `RUNTIME_VERSION`: the version of the machine learning libraries provided by GCP for the training
- `REGION`: the physical region of the server on which to train (we will use the same region as the region we used for our bucket in order to reduce the latency when fetching the data)

```bash
gcloud ai-platform jobs submit training ${JOB_NAME} \
	--job-dir gs://${BUCKET_NAME}/${BUCKET_TRAINING_FOLDER}  \
	--package-path ${PACKAGE_NAME} \
	--module-name ${PACKAGE_NAME}.${FILENAME} \
	--python-version=${PYTHON_VERSION} \
	--runtime-version=${RUNTIME_VERSION} \
	--region ${REGION} \
	--stream-logs
```

👉 [Full documentation here](https://cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/training)
You imagine how painfull it would be to write this very long command every time we want to submit a training task to GCP.
That's where our precious `Makefile` enters in action with its variables and commands.

Variables:

```
BUCKET_NAME=XXXXX

REGION=europe-west1

PYTHON_VERSION=3.7
FRAMEWORK=scikit-learn
RUNTIME_VERSION=1.15

PACKAGE_NAME=TaxiFareModel
FILENAME=trainer

JOB_NAME=taxi_fare_training_pipeline_$(shell date +'%Y%m%d_%H%M%S')
```

Fore more information about latest runtimes, check out the [documentation](https://cloud.google.com/ai-platform/training/docs/runtime-version-list?hl=en).

After understanding and filling in variables, you can now submit your first training task on GCP:

```bash
make gcp_submit_training
```

:bulb: You can now follow the job submission on the command line or on [AI Platform GCP console](https://console.cloud.google.com/ai-platform/jobs?hl=en).

When your job is finished check on your [Storage Bucket](https://console.cloud.google.com/storage/browser?hl=en) that the `model.joblib` has been updated.

You trained your first model completely online! 🎉

Make sure you are confortable with the way the `run_locally` and `gcp_submit_training` commands of the `Makefile` work and how and in which context they call `trainer.py` (make a ticket if you need to).

Next step... Let's make a prediction from that online model! 🚀
