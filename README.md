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

### Authentication
* Note: Since the project is quite old, use an older form of `allauth`, but the newer form can be used in PP5.
* `pip3 install django-allauth==0.41.0`
* Make sure `django.template.context_processors.request` is included in the `TEMPLATES` variable within `settings.py`. This allows `allauth` and Django itself to access the HTTP request object in our templates. e.g. to access `request.user.email`.
* Add the `AUTHENTICATION_BACKENDS` from the [Installation Page](https://django-allauth.readthedocs.io/en/latest/installation.html) of the documentation and pate it below the `TEMPLATES` variable. This lets the admin login normally instead of in the specific admin page and also lets the user login by email.
* Add the following apps from the documentation to the `INSTALLED_APPS` variable in `settings.py`:
    * `'django.contrib.sites'`
    * `'allauth'`
    * `'allauth.account'`
    * `'allauth.socialaccount'`
* Add `SITE_ID = 1` below the `AUTHENTICATION_BACKENDS` constant.
* Add `path('accounts/', include('allauth.urls'))` to `urls.py` to include all the `allauth` urls and ensure to import `include`.
* Make sure to `migrate` and `makemigrations`.
* If you want to add social media authentication, go to the website's `admin` page and in the 'Sites' section, click on it and click on the sample `example.com`. Rename the 'Domain Name' to `boutiqueado.example.com` and the `Display Name` to `Boutique Ado`.

### Authentication and Sending Emails
* Note: When trying to send actual emails from Gitpod, an error stating "Issue binding port" will be displayed which causes sending of the email to fail. Logging issues to the terminal while developing on Gitpod, as done in this video, serves to test Authentication and Authorisation functionality until project deployment. Once deployed to Heroku, the sending of actual emails will become a possibility.
* `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` under `SITE_ID` in `settings.py`.
* Add the following constants below `EMAIL_BACKEND`: `ACCOUNT_AUTHENTICATION_METHOD`, `ACCOUNT_EMAIL_REQUIRED`, `ACCOUNT_EMAIL_VERIFICATION`, `ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE`, `ACCOUNT_USERNAME_MIN_LENGTH`, `LOGIN_URL` and `LOGIN_REDIRECT_URL`. The values of these can be found in `settings.py`.
* `pip3 freeze > requirements.txt`
* This project puts allauth templates inside a seprate folder called `allauth` inside the `templates` folder.

### Base Template
* Note: The project uses Bootstrap 4.6, therefore some elements might be outdated for Bootstrap 5. The minified version of jQuery is also used instead of a slim version to use all suitable features. Therefore, the suitable link is used in the Bootstrap [Starter Template](https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template).
* 