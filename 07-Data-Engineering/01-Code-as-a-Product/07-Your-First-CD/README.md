## Objective

Create your first CD (continuous deployment)

## Where to deploy ?

We want to be able to deploy a software/package on a remote machine
Here you have many different possibilities, we chose Heroku for many reasons:  
👉 It is free  
👉 It is amazingly easy to use  
👉 Smooth git integration  

## Heroku setup

- sign in to [heroku](https://signup.heroku.com/)  
- install [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- test login
```bash
heroku login
```

## Deploy your first package to heroku  
Deploying to heroku is as simple as:  
👉 Adding a `Procfile` file indicating command to run on heroku servers  
👉 Creating heroku app and run 3 commands from command line  

Here is how to do
- Go the root of your repository you created in last exercices
- Add a file named `Procfile` at the root of your repository
- Insert the following line inside `Procfile` (change the name of your package) in order to run your script when the application is deployed
```bash
web: pip install . -U && YOUR_PACKAGE_NAME-run
```
- Create your app (change the name of your package)
```bash
heroku create YOUR_PACKAGE_NAME
```
- You should see in the console that heroku deployed a web server online exposing for you an empty app that is visible here (change the name of your package)
https://YOUR_PACKAGE_NAME.herokuapp.com/
- Now we will deploy our package to this server, do not forget to commit your code before pushing to heroku: only the commited code will be pushed to production
```bash
git add Procfile
git commit -m 'heroku Procfile added'
git st
```
- Push your code to heroku
```bash
git push heroku master
```
- Deploy on free heroku dynos
```bash
heroku ps:scale web=1
```
- You should see in the server logs the result of the execution of the script of your package
```bash
heroku logs --tail
```
📣 And `voila` 📣  
**NB: Here we only run one script once on heroku, so once the script finishes running, heroku will shut down the app.  
==> don't be surprised if you see crash message in heroku logs**  

## Automate deployment inside your CI-CD Github Pipeline

Running following command was boring right ?
You'd rather automatically deploy your package anytime you change your code and push it to github

Here we'll get back to our precious `.github/workflows`  
👉 Simply add a step called `deploy_heroku` following your `build` step (change your package name and your email address):
```yaml
   deploy_heroku:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v2
       - uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
         with:
           heroku_api_key: ${{secrets.HEROKU_API_KEY}}
           heroku_app_name: "YOUR_PACKAGE_NAME" # Must be unique in Heroku
           heroku_email: "YOUR_EMAIL_ADDRESS"
```
What this will do is nothing more than executing the command you executed on last section, except that these command will be executed from **Github servers**:
```bash
git push heroku master
heroku ps:scale web=1
```

💡 How will Github do to authenticate as myself to heroku ?
By providing to Github an API key you'll generate.  
👉 Go to [heroku account](https://dashboard.heroku.com/account), generate and/or copy your API key  
👉 Store it as a secret on your githug repository under `Settings` then `secrets`  
   => name it `HEROKU_API_KEY` and paste your key you copied from heroku  
👉 Then from terminal, inside your repo:  
```bash
git status
```
```bash
git diff
```
Add `Procfile` and commit changes to `.github/workflows/pythonpackage.yml`
```bash
git add Procfile
git commit -am "added CD to deploy to heroku"
```
Finally
```bash
git push origin master
```

📣 Sit, relax, grab a beer and check Github doing all the work for you under `Actions` 📣
