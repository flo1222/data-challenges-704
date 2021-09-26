## Objective

You have learned how to create your first package, now we'll see one of the benefits of packaging:
👉 Share a package with your colleagues

## How do I share my code ?

Simply create a github repository from your package, and then everyone will be able to get your package via:
```bash
pip install git+git://github.com/GIT_USER/mlproject.git
```
🤔 Still not clear ?
Remember wagon_tools package right ?
Now inpsect [wagon_tools github repo](https://github.com/lologibus2/wagon_tools) and run
```bash
pip install git+git://github.com/lologibus2/wagon_tools.git
```
Run it using ipython or a notebook:
```bash
from wagon_tools.lib import get_data
get_data()
```

## Share your own library
You just understood how to opensource your package right ?

You will now share your first package with all your colleagues.
Your colleagues will install your package and run:
```python
from yourpackage.lib import try_me
```

Create a project with `wagon-make-package` command:
- Name it as you please (avoid using dashes `-` in the name of your package, this is against conventions and makes importing your package harder)
- Create it outside of the `data-challenges` folder
- Add a `try_me()` function to `lib.py` file
- Insert any code you want in that function, try being inventive
- Create a [new public (obviously) repository](https://github.com/new) on github named after your package name
- Choose `…or push an existing repository from the command line`:
```bash
git remote add origin git@github.com:GIT_USER_NAME/PACKAGE_NAME.git
git push -u origin master
```

Publish the pip install command on slack channel for your colleagues to install your package and run your function.
💡 __should look like `pip install git+git://github.com/GIT_USER_NAME/PACKAGE_NAME.git`__

Your colleagues should've done the same thing, add all their repo to a requirements.txt file and test their function

## Bonus: Pypi, the last layer to opensource

You can skip the following section, it is pure bonus, but worth reading.

This section is for you general knowledge and won't be usefull until you want really opensource a package

You probably wondered how to install your package with `pip install PACKAGE_NAME` rather than `pip install git+git://github.com/GIT_USER_NAME/PACKAGE_NAME.git`

#### Process to fully opensource your package:
- Create two accounts, one on [Pypi](https://pypi.org/account/register/) and one on [TestPypi](https://test.pypi.org/account/register/)
💡 __Pypi to offically opensource your package, and TestPypi ton test before pushing to Pypi__
- Follow [this tutorial](https://anweshadas.in/how-to-upload-a-package-in-pypi-using-twine/) to upload package to pypi using [twine](https://twine.readthedocs.io/en/latest/)
