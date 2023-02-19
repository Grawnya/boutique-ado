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
\
&nbsp;
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
\
&nbsp;
### Authentication and Sending Emails
* Note: When trying to send actual emails from Gitpod, an error stating "Issue binding port" will be displayed which causes sending of the email to fail. Logging issues to the terminal while developing on Gitpod, as done in this video, serves to test Authentication and Authorisation functionality until project deployment. Once deployed to Heroku, the sending of actual emails will become a possibility.
* `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` under `SITE_ID` in `settings.py`.
* Add the following constants below `EMAIL_BACKEND`: `ACCOUNT_AUTHENTICATION_METHOD`, `ACCOUNT_EMAIL_REQUIRED`, `ACCOUNT_EMAIL_VERIFICATION`, `ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE`, `ACCOUNT_USERNAME_MIN_LENGTH`, `LOGIN_URL` and `LOGIN_REDIRECT_URL`. The values of these can be found in `settings.py`.
* `pip3 freeze > requirements.txt`
* This project puts allauth templates inside a seprate folder called `allauth` inside the `templates` folder.
\
&nbsp;
### Base Template
* Note: The project uses Bootstrap 4.6, therefore some elements might be outdated for Bootstrap 5. The minified version of jQuery is also used instead of a slim version to use all suitable features. Therefore, the suitable link is used in the Bootstrap [Starter Template](https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template).
* `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/` where `cp -r` means to copy recrusively i.e.  copy the contents of directories and follow it with the location of the templates, with a * to copy all. Then put the location of where you want to copy all the templates.
* Copy the starter template and update the slim version to the minimised version by updating the first jQuery line to `<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>`.
* Add `{% block meta %}` to the top of the `meta` tags, so you can wrap them into a section which can be extended in the templates. Add an `{% endblock %}`. Repeat for the CSS and JavaScript sections.
* Add `{% block extra_[tech/language] %}` to add extra `meta` tags, CSS or JS along with one in the `<title>` to add more info to templates, also an extra header block, content and extra JS.
* Add a header with a `container-fluid` and a `fixed-top` so it remains at the top of the page. Also add a messages `<div>` to print any messages.
\
&nbsp;
### Creating "Home" Application
* `python3 manage.py startapp home`
* Create a `templates` folder and a `home` folder within it, along with an `index.html` as the home page.
* Add `{% extends 'base.html' %}` and `{% load static %}` at the top of `index.html`
* Create a view in `views.py` within the `home` project to render the home page.
* Copy `urls.py` from the boutique_ado project folder and place it into the `home` folder to write all the app relevant urls.
* Within it, include the url `path('', views.index, name='home')` to show the page.
* Within the `urls.py` file of the project folder, connect the `home` app's urls with `path('', include('home.urls')),`. 
* Add the `home` app to the `INSTALLED_APPS` variable in `settings.py`.
* Add the template directories, by adding to the `DIRS` list within the `TEMPLATES` variable for both the `templates` folder and the `allauth` folder within by placing `os.path.join(BASE_DIR, 'templates')` and one for the `allauth` by adding `allauth` after `'templates',`.
\
&nbsp;
### Home Page and Header
* Add home page content to `index.html`, filling in suitable block details.
* Add a logo and details to the `base.html` `<header>` element as seen in this project and include a form for the search element on the site that uses a `GET` method to submit searches as URL parameters and also include a list which consists of the account and shopping bag links.