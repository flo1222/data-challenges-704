
## Build your API

Now that your have a performant model trained in the cloud, we will expose it to the world.
Today, we will create an API for your model and put it in the cloud.

### FastAPI

First, let's create an API exposing our model. Remember having consumed an API during the Python module using the `requests` package?
You are now going to create your own API allowing other developers to ask your model for predictions.

### Docker

Once we have an API, we will use Docker in order to create an image that can be pushed to production.

### Cloud Run

Now that we have a running API image, we are going to use the Google Cloud Run service in order to host it.

### Compute Engine

Do you have a internet connection with a limited bandwitdh or does your computer suffer in any way when building Docker images?
Let's use Google Compute Engine in order to have a server in the cloud do the hard work for us.

### Kubernetes Engine

Is the computing power of a single Cloud Run server not enough to server your customer base?
Let's scale massively using a cluster of hosts serving your API, and watch your credit card melt.

### Billing

⚠️ All the GCP services are billed... Create an expense alert and keep an eye on your budget 💸
