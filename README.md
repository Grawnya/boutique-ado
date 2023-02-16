# Boutique Ado Project

### Set Up
* Note: Since the project is quite old, use an older form of Django, but the newer form can be used in PP5.
* `pip3 install Django==3.2`
* `django-admin startproject boutique_ado .`
* `python3 manage.py runserver`
* `python3 manage.py migrate`
* `python3 manage.py makemigrations`
* `python3 manage.py createsuperuser` and set the username, email and password for an admin.
* Create `env.py` and within import `os` and set the `SECRET_KEY` variable like so: `os.environ.setdefault("SECRET_KEY", 'enter secret key here from settings.py')`.
* Within `settings.py` import `env` if `os.path.exists('env.py')` amd set the `SECRET_KEY` variable to `os.environ.get("SECRET_KEY")`.