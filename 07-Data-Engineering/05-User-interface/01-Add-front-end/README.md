
# Objective

Add a **Front-End** on top of your **API** in order to visualize your predictions.

# Context

Yesterday, we build and deployed our first **Prediction API** on **Google Cloud Run**.

Now we will build a beautiful front-end that will interrogate your API.

This is how most modern websites are built:

👉 A back-end and a front-end

# How to

Here we provide you with a [wagon homemade frontend](https://github.com/lewagon/taxi-fare-interface).

Create a duplicate template of this repo on your own github account, by clicking on the button `Use this template` or [HERE](https://github.com/lewagon/taxi-fare-interface/generate).

👉 **VERY IMPORTANT** make it a **PRIVATE REPO**

👉 name it `taxi-fare-interface`

Clone it:

```bash
cd ~/code/<user.github_nickname> && git clone git@github.com:<user.github_nickname>/taxi-fare-interface.git
```

```bash
cd ~/code/<user.github_nickname>/taxi-fare-interface
```

Follow instructions from [taxi-fare-interface](https://github.com/lewagon/taxi-fare-interface) repo to:

*Hint*: if you do not have an API in production, use this one:

https://taxifaremodelapi.herokuapp.com/predict_fare?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

👉 run your front-end locally.

👉 deploy your front-end on a github page.
