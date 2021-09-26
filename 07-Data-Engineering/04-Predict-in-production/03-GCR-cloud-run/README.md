
## Push our prediction API image to Google Container Registry

**Google Container Registry** is a service storing Docker images on the cloud with the purpose of allowing **Cloud Run** or **Kubernetes Engine** to serve them.

It is in a way similar to **GitHub** allowing you to store your git repositories in the cloud (except for the lack of a dedicated user interface and additional services such as `forks` and `pull requests`).

First, let's make sure to enable [Google Container Registry API](https://console.cloud.google.com/flows/enableapi?apiid=containerregistry.googleapis.com&redirect=https://cloud.google.com/container-registry/docs/quickstart) for your project in GCP.

Once this is done, let's ensure that your GCP credentials are correclty registered for the command line.

``` bash
gcloud auth list
```

If your account is not listed, then it is time to authenticate:

``` bash
gcloud auth login
```

Now let's configure the gcloud command for the usage of docker.

``` bash
gcloud auth configure-docker
```

And verify your config. You should see your GCP account and default project.

``` bash
gcloud config list
```

You can now define an environment variable for the name of your project.
This environment variable will be used accross following commands.

``` bash
export PROJECT_ID=replace-with-your-gcloud-project-id
echo $PROJECT_ID
gcloud config set project $PROJECT_ID
```

And an environment variable for the name of your docker image.
This environment variable will be used accross the following commands.

``` bash
export DOCKER_IMAGE_NAME=define-some-container-image-name
echo $DOCKER_IMAGE_NAME
```

Now we are going to build our image again.
This should be pretty fast since Docker is pretty smart and is going to reuse all the building blocks used previously in order to build the prediction API image.

``` bash
docker build -t eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME .
```

Again, let's make sure that our image runs correctly, so that we avoid spending the time of pushing to the cloud an image that is not working.

``` bash
docker run -e PORT=8000 -p 8000:8000 eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
```

We can now push our image to Google Container Registry.

``` bash
docker push eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
```

The image should be visible in the GCP console [here](https://console.cloud.google.com/gcr/).

## Deploy the Container Registry image to Google Cloud Run

Let's run one last command 🤞

``` bash
gcloud run deploy --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME --platform managed --region europe-west1
```

After confirmation, you should see a similar output indicating that the service is live 🎉

``` txt
Service name (wagon-data-tpl-image):
Allow unauthenticated invocations to [wagon-data-tpl-image] (y/N)?  y

Deploying container to Cloud Run service [wagon-data-tpl-image] in project [le-wagon-data] region [europe-west1]
✓ Deploying new service... Done.
  ✓ Creating Revision... Revision deployment finished. Waiting for health check to begin.
  ✓ Routing traffic...
  ✓ Setting IAM Policy...
Done.
Service [wagon-data-tpl-image] revision [wagon-data-tpl-image-00001-kup] has been deployed and is serving 100 percent of traffic.
Service URL: https://wagon-data-tpl-image-xi54eseqrq-ew.a.run.app
```

Any developer in the world 🌍 is now able to browse to the deployed url and make a prediction using the API 🤖!

⚠️ Keep in mind that you pay for the service as long as it is up 💸

## Writing to Google Cloud Storage from Google Cloud Run

Do you need to write to GCS from GCR ?

You will be needing to add your credentials to your image so that your code is allowed to push data to your bucket.

In your `Dockerfile`, you will need to put the path to the Google Cloud Plaform credentials you created during setup day.

Hint: you can find the path using:

``` bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

Now, update your `Dockerfile` with the correct path to your credentials file:

``` bash
COPY /path/to/your/credentials.json /credentials.json
```

And deploy the new image that is able to write to GCS:

``` bash
gcloud run deploy \
    --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME \
    --platform managed \
    --region europe-west1 \
    --GOOGLE_APPLICATION_CREDENTIALS="/credentials.json"
```
