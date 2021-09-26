# Start your final project :rocket:

## Setup a new `virtualenv` (opt.)

<details>
  <summary markdown='span'><strong>MacOSX</strong></summary>

```bash
pyenv virtualenv project_name
pyenv activate project_name
pip install --upgrade pip
```

</details>

<details>
  <summary markdown='span'><strong>Windows</strong></summary>

```bash
cd ~/.venvs
python -m venv project_name
source ~/.venvs/project_name/Scripts/activate
```

</details>

### Install minimal packages

```bash
pip install -r https://gist.githubusercontent.com/krokrob/53ab953bbec16c96b9938fcaebf2b199/raw/9035bbf12922840905ef1fbbabc459dc565b79a3/minimal_requirements.txt
pip list
```

## Setup the project

<details>
  <summary markdown='span'><strong>I am the project leader</strong></summary>
Let's create a new project:

```bash
cd ~/code/<user.github_nickname>
wagon-make-package project_name
cd project_name
```

Add `notebooks` and `raw_data` directories:

```bash
mkdir notebooks
touch notebooks/.keep
mkdir raw_data
echo '/raw_data/' >> .gitignore
```

Commit all changes:

```bash
git add .
git commit -m 'add notebooks and raw_data directories'
```

Then create a GitHub repository and push your project:

```bash
gh repo create
git push origin master
```

Finally, add your teammates as collaborators on GitHub.
</details>

<details>
  <summary markdown='span'><strong>I am a teammate</strong></summary>
Let's clone the project:

```bash
mkdir ~/code/<PROJECT_LEADER_GITHUB_NICKNAME> && cd "$_"
git clone git@github.com:<PROJECT_LEADER_GITHUB_NICKNAME>/<PROJECT_NAME>.git
cd project_name
```

Then add a `raw_data` directory:

```bash
mkdir raw_data
```

You're good to go.
</details>

## Split the work

1. Brainstorm the objectives of the project with your team
2. Write 4-8 parallel jobs
3. Each teammate take one job and split it into small task

You can use Post-it, a [Trello](https://trello.com/) board, GitHub [Projects](https://docs.github.com/en/github/managing-your-work-on-github/creating-a-project-board) or any other project management tool your want to drive your project tasks.
