
# Create a streamlit website

We have just plugged an existing front-end to our **API**.

We will now create our own website using **Streamlit**.

Let's install the requirements provided inside `requirements.txt`.

```bash
pip install -r requirements.txt
```

Now run:

```bash
streamlit run app.py
```

Let's inspect `app.py` and check what is being done inside...

# Plug your prediction API

Replace the URL to the prediction API with your own and update the code accordingly.

Now let's get crazy with the page content 🎉

Maybe add some map 🗺

Once you are satisfied, let's push the code to production! 🔥

# Deploy

Now that you checked your app works locally, you might want it to run free on a remote server.

## Create folder outside data-challenges

As heroku is based on `git`, we will create a folder outside of the `data-challenges` folder.

```bash
mkdir -p ~/code/taxifare_streamlit
cp -rf * ~/code/taxifare_streamlit/
cd ~/code/taxifare_streamlit/
```

Version it for future Heroku use:

```bash
cd ~/code/taxifare_streamlit/ && git init
```

## Deploy to heroku

You'll see once again how Heroku is easy to use, here you simply need to:

- Create a `Procfile` with following line inside:

```bash
web: streamlit run app.py
```

```bash
git add . && git commit -am "add streamlit app"
```

- Login to Heroku

```bash
heroku login
```

- Create an app on Heroku
```bash
heroku create YOUR_APP_NAME --region eu
```

- Push it on Heroku and have it built using git

```bash
git push heroku master
```

- Then deploy

```bash
heroku ps:scale web=1
```

Click on the link `https://YOUR_APP_NAME.herokuapp.com/` and it should return `OK` 🚀

# Usefull links

- [Altair](https://altair-viz.github.io/gallery/)
