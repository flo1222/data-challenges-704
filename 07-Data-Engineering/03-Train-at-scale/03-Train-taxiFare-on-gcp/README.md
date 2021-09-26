# Objective

In the previous exercice, we trained a basic model on GCP. We will now integrate a complete pipeline and use the trained model to make a prediction.

Deploy, train and use your pipeline model with GCP.
You've trained and evaluated your first Pipeline on your laptop, now you'll do everything on GCP.

## Complete TaxiFareModel/trainer.py to be trainable and deployable to GCP

Here we go back with the pipeline from day3 including:
- Custom encoders
- Mlfow tracking on remote server

Here we provide you with the correction from yesterday, but feel free to use your own code from yesterday as well.

Modify the `get_data()` function and add a `save_model()` method inside `trainer.py` in order to:  
👉 Get training data from Storage (still working on 1k sample for faster runs here)   
👉 Upload model to Storage just like in the last exercice    

💡 Check that all your variables (`BUCKET_NAME` etc...) are correctly defined insice `params.py`

Take a step back and ask yourself what information is now stored inside of our `model.joblib` ?
🤔 Get help from [day 2 slides](https://kitt.lewagon.com/karr/data-lectures.kitt/07-Data-Engineering_02.slides.html)

💡 Now we have the `preprocessing` and `model` information stored in our model.joblib object.

## Test your workflow locally first

Here you will run `make run_locally` on your local machine:
- Train on a few samples first to check that everything runs without error
- Check that your `model.joblib` was correctly saved on GCP storage

Once everything is working ok, please make sure that:
- the requirements in `setup.py` match your requirements on your virtual environement  
💡 **This step is very important, most of your errors in the next section will be linked to mismatch between requirements on your machine and requirements you specified in setup.py**

## Train your model on GCP

Edit the `Makefile` and run `make gcp_submit_training` to train your model on GCP

Same as before here:
- Submit a first training task on a few samples to check that your workflow runs without errors on GCP servers
- Submit a real training task on more samples to benefit from GCP doing all the work for you ;)

💡**NB: Check that all the dependencies are inside the setup.py file**

## Use your model for predictions

Now, have a look at `predict.py` and specifically check how we:  
👉 load pipeline model from storage  
👉 apply predictions on test sample  

💡**NB: It is pretty much the same code as yesterday, the only difference is that we get our `model.joblib` from the cloud and not from our laptop**

Run and test it:
```bash
python predict.py
```

You just made your first prediction using a GCP model ! 🚀
