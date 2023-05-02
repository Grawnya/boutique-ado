# Boutique Ado Project

## Set Up
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
## Authentication
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
### Sending Emails
* Note: When trying to send actual emails from Gitpod, an error stating "Issue binding port" will be displayed which causes sending of the email to fail. Logging issues to the terminal while developing on Gitpod, as done in this video, serves to test Authentication and Authorisation functionality until project deployment. Once deployed to Heroku, the sending of actual emails will become a possibility.
* `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` under `SITE_ID` in `settings.py`.
* Add the following constants below `EMAIL_BACKEND`: `ACCOUNT_AUTHENTICATION_METHOD`, `ACCOUNT_EMAIL_REQUIRED`, `ACCOUNT_EMAIL_VERIFICATION`, `ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE`, `ACCOUNT_USERNAME_MIN_LENGTH`, `LOGIN_URL` and `LOGIN_REDIRECT_URL`. The values of these can be found in `settings.py`.
* `pip3 freeze > requirements.txt`
* This project puts allauth templates inside a seprate folder called `allauth` inside the `templates` folder.
\
&nbsp;
## Base Template
* Note: The project uses Bootstrap 4.6, therefore some elements might be outdated for Bootstrap 5. The minified version of jQuery is also used instead of a slim version to use all suitable features. Therefore, the suitable link is used in the Bootstrap [Starter Template](https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template).
* `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/` where `cp -r` means to copy recrusively i.e.  copy the contents of directories and follow it with the location of the templates, with a * to copy all. Then put the location of where you want to copy all the templates.
* Copy the starter template and update the slim version to the minimised version by updating the first jQuery line to `<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>`.
* Add `{% block meta %}` to the top of the `meta` tags, so you can wrap them into a section which can be extended in the templates. Add an `{% endblock %}`. Repeat for the CSS and JavaScript sections.
* Add `{% block extra_[tech/language] %}` to add extra `meta` tags, CSS or JS along with one in the `<title>` to add more info to templates, also an extra header block, content and extra JS.
* Add a header with a `container-fluid` and a `fixed-top` so it remains at the top of the page. Also add a messages `<div>` to print any messages.
\
&nbsp;
## Creating "Home" Application
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
* Within the account list item, add expected options if the user `is_authenticated`, but also account for the fact that a superuser can login: `is_superuser`.
* Create a `media` folder for all images, `static` folder for all static files and a `css` folder within it for all CSS files.
* Add Font-Awesome link to `base.html` head as well as connect any fonts and css files to the css block.
* In `settings.py`, add `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)` to connect the static files to the directory, which should be a tuple.
* Repeat for the `media` folder, but a tuple is not requireed for the `MEDIA_ROOT`.
* To allow Django to see the media urls, go to `urls.py` in the project folder and import both `static` and `settings`:
\
&nbsp;
`from django.conf import settings`
\
&nbsp;
`from django.conf.urls.static import static`
\
&nbsp;
and add the following line after the `urlpatterns` variable:
\
&nbsp;
`+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
* Create an `includes` folder within the `templates` folder, as it is common practice in big projects to store snippets in an additional place.
\
&nbsp;
## Products

### Adding the Products
* Add any suitable photos from the CI Boutique Ado repo to the `media` folder.
* Create a `products` app and add it to `settings.py`.
* Create a `fixtures` folder within the `products` app, as `fixtures` allows pre-written data from a JSON file to be added to a database. Alternatively, you can add data manually via the admin panel.
* Create a model within the `models.py` file for the `Category` of the product and another for the `Product`, where the `category` within is a foreign key of the `Category` model, where if the category is deleted, the products are not deleted bu instead the category is set to `Null`.
* Don't forget to `makemigrations` and `migrate`, but you can put `--dry-run` after `makemigrations` to flag any errors before you do the final `makemigrations`. You can also add the `--plan` flag after `migrate` to mkae sure there are no issyes with the models, before doing the final `migrate`.
* Go to `admin.py` within the `Products` folder and register the models by typing `admin.site.register(modelName)`.
* `python3 manage.py loaddata [json file name without the file ending]` - type this for each JSON file i.e. categories and products in this case to load the models.
\
&nbsp;
### Products Admin
* Note within the admin panel that the models were created, but the plural for the `Category` model was set to `Categorys`. To override this, create a `Meta` class within the model and set the `verbose_name_plural` to the suitable heading i.e. `Categories`.
* Within the `admin.py` file, create classes for each model and set the columns to display each in the admin panel. The `list_display` variable must be a tuple. The `ordering` variable used to order the data by a particular column(s) must also be a tuple, with a comma after the first column, if the data is only ordered by 1.
* Update the model registeration by adding the suitable classes afterwards e.g. `admin.site.register(Product, ProductAdmin)`.
* Create a starting view in the `views.py` file of the `Products` project, which is similar to the view in the `home` folder, but also add `context` since we'll need to send some things back to the template. Call all the products in the `Product` model and add that to the context.
* Create a `urls.py` file within the `products` folder and copy the contents from the `home` app, altering it for the products.
* Add the suitable url to the project's own `urls.py` folder.
* Add a `templates` folder and a `products` subfolder to the `products` folder. Include `products.html` inside the `products` subfolder and copy most of the `index.html` file but print out all the products.
\
&nbsp;
### Products Template
* Follow the `products.html` code to see the flow of each product and the pagination.
* Add links to the product page in various html pages by placing the following in the `href` attribute: `"{% url 'products' %}"`. 
* Create relevant views and urls to enable the user to click on a product image and go to a specific page for the product using the `product_detail.html` page.
\
&nbsp;
### Product Searching
* Add the action of `{% url 'products' %}` to both of the search GET forms in the `base.html` and `mobile-top-header.html` templates. This means that when a search query is submitted, it'll end up in the URL as a search parameter.
* Go to the `views.html` file within the `products` folder and access the parameters, by altering the `all_products` function to see if `request.GET` exists.
* Within the function, while checking if `request.GET` exists, check if the form, which is named `q` exists in it and if it does, obtain its value as set it to a variable named `query`. If `query` is empty, return an error and redirect to the `products` page.
* Import both `messages` to return a message.
* Import `Q` to generate a search query. This is important, as it allows the user to check if the searched term is contained within the name or the description, not just in both.
* `Q` can be used as so `queries = Q(name__icontains=query) | Q(description__icontains=query)`, where the `|` or pipe symbol signifies OR and the `i` before the `contains` means that the search is case insensitive.
* Can then find all relevant products by filtering using the `queries`: `products = products.filter(queries)`, where the original `products` refers to all objects within the model.
\
&nbsp;
### Product Filtering
* In order to handle filtering by category, pass a category parameter to the `products` URL just like with q for search queries.
* If searching for a category to click on e.g. `tops`, then within the navbar, go to the suitable category and in the href place the `products` URL followed by the search query like so `"{% url 'products'%}?category=activewear,essentials"`, where the question mark indicates a category parameter and the comma is to separate the categories.
* Get the category from the view, by obtaining the category and splitting the string at the commas to obtain a list of all categories. Filter the current query set of all products to only products whose category name is in the list: `products = products.filter(category__name__in=categories)`. 
* It's worth noting that this double underscore syntax is common when making queries in django. Using it here means we're looking for the name field of the category model. e.g.`products = products.filter(model__column__in=filtered_value)`. Here this is only possible as `category` is a foreign key within the `Product` model. Otherwise it normally takes the form: `categories = Category.objects.filter(column__in=filtered_value)`.
\
&nbsp;
### Product Sorting
* Set the url to `{% url 'products' %}?sort=price&direction=asc`, where `sort` is the category to sort the products by and direction can be either `asc` and `desc`.
* Create a suitable view to check for the `sort` and `direction` in the url.
* In order to allow case-insensitive sorting on the name field, annotate all the products with a new field. Annotation allows the user to add a temporary field on a model so in this case, what we want to do is check whether the sort key is equal to name. Hence `sort` is equal to `sortkey` in the example.
* Follow the code to print out the category buttons, which filter by category and include the category name of an item, based on the code in `products.html` and `products_detail.html`.
* Sort option elements can also be found in `products.html`, which use the `order-md` option to set the location of objects in a certain order in the row for certain size screens.
* Searching for items is also dealt in the suitable section in the `products.html` file.
* In order for categories to be sorted by name instead of their ids, in the `all_categories` view, add another sortkey conditional block to check if the sortkey is equal to category and if it is, adjust it to tack on a double underscore and name. This double underscore syntax allows us to drill into a related model and that works for ordering also.
* Note: See that each one of the sorting sections has a value which uses a predictable syntax to indicate the current sorting methodology. The syntax matches the current sorting template variable and the underscore allows you to split.
* This project uses jQuery at the bottom of the `products.html` file to allow the products to be sorted live - follow what is written to know what it is doing.
* Add `{{ block.super }}` to add anything to the existing base templates `postloadjs` block.
* Add a button at the bottom of the page to let the user go to the top of the products page and add some js inside the `{% block postloadjs %}` to deal with the click and css for styling and to keep it fixed at the bottom.
\
&nbsp;
## Shopping Bag
* `python3 manage.py startapp bag` and add to `INSTALLED_APPS` in `settings.py`.
* Copy the view from the `home` app to allow the user to show a similar `bag.html`page to `index.html`.
* Also copy and alter the `urls.py` file from the `home` app to suit the `bag` and update the project's `urls.py` file to include the `bag` app links.
* Add the view bag link `{% url 'view_bag' %}` to the suitable sections within the `base.html` and `mobile-top-header.html`files.
* Within `bag.html`, show the user all the items within the shopping bag or print out a section that says it is empty (if it is) and redirect them to the "Products" page.
* Within the `bag` app, create a `contexts.py` file, which will handle the bag items variable.
* Inside the `contexts.py` file, a dict is returned called a context processor and its purpose is to make the dict available to all templates across the entire application, much like you can use request.user in any template due to the presence of the built-in request context processor.
* Make the context process available to all files by going to `settings.py` and within the `TEMPLATES` variable, there's an option called `context_processors` and you can add it here e.g. `'bag.contexts.bag_contents'`.
* The context concept is the same as the context used in views during the course. The only difference is that it is directly returned and available to all templates by putting it in `settings.py`.
* Add `STANDARD_DELIVERY_PERCENTAGE` and `FREE_DELIVERY_THRESHOLD` at the bottom of `settings.py` as well.
\
&nbsp;
## Adding Products to Shopping Bag
* Add a form as seen in `product_detail.html` which allows the user to select the quantity and then submit the item and amount to the shopping bag.
* `<input type="hidden" name="redirect_url" value="{{ request.path }}">` is added at the end of the form to redirect the user back to the same page after the items have been added to the shopping bag.
* In modern versions of HTTP, every request-response cycle between the server and the client i.e. between the django view on the server-side
and the shopping bag form making the request on the client-side, uses a "session", to allow information to be stored until the client and server are done communicating. 
* This is especially handy in a situation like an e-commerce store, because it allows us to store the contents of the shopping bag in the HTTP session while the user browses the site and adds items to be purchased.
* By storing the shopping bag in the session, it will persist until the user closes their browser so that they can add something to the bag, then browse to a different part of the site add something else and so on without losing the contents of their bag.
* To implement this concept, create a variable `bag`, which accesses the requests session, trying to get this variable if it already exists and initialising it to an empty dictionary if it doesn't. In this way, we first check to see if there's a bag variable in the session and if not, create one.
* Then add it to the session, which is just a `dict` itself.
* Finally created an associated url in the `bag` app's `urls.py` file, followed by updating the `product_detail.html` form's action to `action="{% url 'add_to_bag' product.id %}"` to return to the specific products page.
* Note that because its a `session` variable, we can access it anywhere that we can access the `request` object.
* In `context.py`, accessing the shopping bag in the session is the same as in the `add_to_bag` view. Add logic in the context processor to check the bag and total up the value of its contents.
* Go to the `bag.html` file and render out the bag contents
\
&nbsp;
## Refining the Products Added to the Shopping Bag
* Add a `has_sizes` characteristic to the `Product` model to check if sizes exist. Don't forget to `makemigrations` and `migrate`.
* `python3 manage.py shell` allows us to access the DBs via the terminal.
* In this project, the existing `Product` model/DB was updated to reference all elements with sizes. The following commands were made:
\
&nbsp;
`from products.models import Product`
\
&nbsp;
`kdbb = ['kitchen_dining', 'bed_bath']`
\
&nbsp;
`clothes = Product.objects.exclude(category__name__in=kdbb)`
\
&nbsp;
`for item in clothes:` (note you can go onto the next line in the terminal w/ `shift` + `enter`, which is represented by the `...`)
\
&nbsp;
`...item.has_sizes = True` (double check all migrations are made)
\
&nbsp;
`...item.save` (and then double `return` to escape the loop and run the command)
\
&nbsp;
`Product.objects.filter(has_sizes=True)` to check if they were all set to `True`.
`exit()` to exit the shell.
* In the `product_detail.html` template, add a form element that lets the user select a size if the product has a size.
* Show the product size in the `bag.html` template.
* Add logic to consider the user ordering the same item but in a different size in the `bag` app's `views.py` file. These details are considered in the context processor as well i.e. the `contexts.py` file in the `bag` app.
* Within the quantity section of `product_detail.html` add 2 divs with the following classes respectively: `input-group-prepend` and `input-group-append`, which are 2 bootstrap classes to format buttons within each div to increase and decrease the quantity value.
* These buttons won't do anything unless logic is applied with a JS file. Create an includes directory in the `products` folder within the `templates` folder of the `products` app.
* The JS is done as a HTML file (`quantity_input_script.html`), as it'll only be a `<script>` element included at the end of various HTML files. It includes how to increase the value and decrease the value of an item's quantity.
* Add the `postloadjs` block and reference to the `quantity_input_script.html` file at the end of `product_detail.html`, but note that when testing it, you can go into negative values. Add a function to `quantity_input_script.html` to disable the `-` button if the quantity is equal to 1 and the `+` button if the quantity is equal to 99.
* Within `bag.html`, alter the printing out of the item quantity with a form. This form is copied from `product_detail.html` and is altered to make all the buttons smaller. As size isn't included on the page, we also need to consider it in a hidden input factor beneath the form.
* Add the postloadjs block to the end of `bag.html`. Add 2 buttons to the end of the form to keep the form neat and to prevent the use of a submit button.
* Add a new script to `bag.html` to add functionality to the update and remove keywords, but buttons might not work if django thinks they're just words. This can be changed by updating the css class for `.btt-link` to include the update and remove buttons.
\
&nbsp;
## Adjusting and Removing Products
* Create a view to adjust the quantities in the `bag` app's `views.py` file. This view should have a connecting `adjust_bag` url which can be called as the action in the `bag.html` file.
* Add logic and include an action in the `bag.html` form to ensure the page is updated after the user adjusts the bag.
* Similarly create a `remove_from_bag` view that allows the user to delete items from the shopping bag.
* Make sure you are using the minifed version of jQuery. This sample project originally used the slim version which is useful for most things but doesn't include AJAX functions like `POST`.
* Create a `templatetags` folder in the `bag` app with both an `__init__.py` file so other users can import all of the associated files and ensure that `bag_tools.py` is treated like a python package.
* In `bag_tools.py` create a function which provides the correct value of the items based on the quantity ordered. This is called a filter and in order to register the filter: `register = template.Library()`, where the `register` variable name is expected and is an instance of the template library.
* Add the register filter decorator to register the function as a template filter.
* You can load the template tag in to the relevant file i.e. `bag.html` in this case, as `{% load bag_tools %}` and call a particular function where relevant e.g. `${{ item.product.price | calc_subtotal:item.quantity }}` in this case.
* Restart the server to ensure that the templatetag is successfully utilised.
\
&nbsp;
## Toasts
* Create a `toasts` folder within the `includes` folder in the `templates` directory for all the individual toasts/message html files.
* The structure comes from the Bootstrap documentation. Note the `data-autohide` attribute included at the top to prevent the user from autohiding the toast and `data-dismiss` allows the user to dismiss it on their own. Each toast uses a different, relevant Bootstrap class for styling.
* Go to `base.html` and go to the `message-container`, looping through any messages.
* In the `bag` app's `views.py` file, in the `add_to_bag` view, incorporate the success message.
* Back in the `base.html` file, include the JS within the `postloadjs` block to allow the user to exit out of it. Call the `toast` class from Bootstrap with the option to `show` to ensure that the message is printed. This means that when any page is shown, it'll automatically load all toasts in the messages container. Including `{{ block.super }}` in the tempaltes ensures that other JS scripts do not override any JS within the `base.html`.
* In order to save the messages, inside the `settings.py` file, include `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'`. By default, Django has inbuilt methods to save messages, but due to committing to GitHub, it is wise to store them in a variable.
* Inside `base.html`, add levels which represent each state based on the Django docs.
* Add suitable toasts/messages in the various views. Include `get_object_or_404` to check if the object exists in the first place.
* Add some CSS to match the message with the colour if its a warning, success etc.
* Add additional details to the `toast_success.html` file to show the checkout bag within the toast.
\
&nbsp;
## The Checkout App

### Models
* Create a new checkout app: `python3 manage.py startapp checkout` and add it to the `settings.py` app.
* Open the associated `models.py` file and create an `Order` model class for order details and specific line items of the shopping list can be found in the `OrderLineItem` model class.
* These models function by creating the order when the user makes a purchase and then populates the `OrderLineItem` model by looping through the bag associated with the order number and including it in the table.
* Import various relevant libraries here to e.g. generate the order number.
* Override the `save` functions for each model class and add a `__str__` function to each to return relevant order number info.
* Don't forget to make migrations, by running `python3 manage.py makemigrations --dry-run` with dry run testing if the migrations can be made. and migrate with `python3 manage.py migrate --plan` to make sure the migrations occurs as a planned check.
\
&nbsp;
### Admin, Signals & Forms
* Set up the `admin.py` file within the `checkout` app, creating read only fields that cannot be edited by declaring the `readonly_fields` variable.
* Add a `fields` variable to dictate the order the variables are shown in the admin table, otherwise django will set its own order.
* Use the `list_display` variable to restrict the number of columns shown.
* Add the `ordering` variable to sort the data shown in the table. In this case it was sorted by the most recent date.
* Create a `OrderLineItemAdminInLine` class that will allow us to add and edit line items from the order model. So in the order we can see a page of editable line items rather than go to the `OrderLineItem` interface.
* Register the models, but you can skip registering the `OrderLineItem` model as it is accessible via the InLine on the order model.
* Use built-in django functionality called signals to update the order live as items (i.e. a line item is added) are added rather than when the final order is created.
* Create a `signals.py` file within the `checkout` app and import `post_save` and `post_delete`, where post means after, which implies that the signals are sent by django to the entire app after a model instance has been saved or deleted. These messages can be received by importing `receiver`.
* Read the `signals.py` file to obtain more details on signals and the updating of the Order total based on the live adding and deleting of lineitems.
* In order to let django know there's a new signals module with some listeners in it, change `apps.py`, by overriding the `ready` method.
* Create a new `forms.py` file within the `checkout` app that users can fill in.
* Update the `__init__` method within it. The `super().__init__(*args, **kwargs)` line is called to set the form up as it would be by default. The `placeholders` provide some default text in the form. Set the `autofocus` attribute on the full name to `True`, so the cursor starts in the full name field when the user starts the page. Iterate through the form's fields, adding a star if its mandatory, adding the value to the dictionary keys and adding CSS. The form fields' labels can be removed, as the placeholders are now set.
\
&nbsp;
### Views & Templates
* Create a new view that is used to deal with the checkout in the `views.py` app within the `checkout` app.
* Add the suitable checkout url to `urls.py` and link the `checkout` urls to the project's urls in the `urls.py` file within the `boutique_ado` folder.
* Create a `template` folder for the `checkout` app with the suitable nested folders for the `checkout.html`.
* Within the `checkout.html` page, add an extra CSS page for personal styling. This CSS page is nested within a series of folders inside the `checkout` app.
* Install `django-crispy-forms` with `pip3 install django-crispy-forms==1.14.0` in this example to align with the time when the sample project was created.
* Add the `crispy_forms` app to the `INSTALLED_APPS` variable in `settings.py`. Also add the `CRISPY_TEMPLATE_PACK` to tell djando which Bootstrap version to use.
* Normally when using crispy forms, you can load the tags similar to loading `static`, but that becomes tedious when using it throughout the website. Can add the `builtins` list variable under the `context_processors` variable, which contains a list of all the tags available in all our templates. The 2 required are `crispy_forms.templatetags.crispy_forms_tags` and `crispy_forms.templatetags.crispy_forms_field`.
* Don't forget to freeze `pip3 freeze > requirements.txt` to add a list of all project requirements including `Pillow`.
* Within `checkout.html` add the crispy form fields and for the payment section, include some `<div>` tags for the stripe api elements.
* Add a column before the crispy form with the `order-lg-last` class to order the column last in the grid on larger screens.
* The `{{ MEDIA_URL }}noimage.png` template tag will not work unless `settings.py` is updated. Add `'django.template.context_processors.media'` in the `context_processors` list under the messages context processor and save the settings so you can access the no image file if the product doesn't have an image.
* Add the checkout url to the `bag.html` submit button.
\
&nbsp;
## Stripe Payments

### Set Up Card
* Create an account and set it to test mode i.e. don't activate the account. Copy the API key.
* Stripe has excellent UI elements to allow for Credit Card inputs, which can be followed [here](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements).
* Add `<script src="https://js.stripe.com/v3/"></script>` to the `base.html` `<head>` tag, as Stripe recommends this in order to use it anywhere and for the more advanced fraud detection features to work, even though its just required on the checkout page.
* You can't render django template variables in external JS files, you need to use a inbuilt feature called `json_script` to render them at the bottom of the `checkout.html` file.
* Add some mock values in the `views.py` file of the `checkout` app for the `'client_secret'` value and the genuine value for the `'stripe_public_key'`. When running the website, these should be found in the website's html file upon inspection.
* Create `stripe_elements.js` within the `checkout` app and obtain the key values from the `base.html` file using jQuery.
* `var stripe = Stripe(stripe_public_key);` to connect to the Stripe API.
* `var elements = stripe.elements();` to create an instance of Stripe elements.
* `var card = elements.create('card', {style: style});` to create a card, with the form box having a particular style and mount it to a relevant div i.e. `card.mount('#card-element');`.
* Note that in the `checkout`'s app `forms.py`, `'stripe-style-input'` style was added. To make all the other fields follow that CSS, add that class to all the stripe classes.
\
&nbsp;
### Add Card Functionality
* Add a JS function to deal with realtime validation errors on the card element. Html can be added to an element by surrounding the HTML text with `"``" `  tags either side of the HTML block.
* Stripe works with payment intents, so the process will occur when the user goes to the checkout page, the checkout view will create the paymentIntent and Stripe returns a client_secret to the template. In the JS on the client side, the `confirmCardPayment` method is called to verify the card.
* Update the `checkout` view in the `views.py` file in the `checkout` app to include the `bag_content` context for the Stripe payment.
* `pip3 install stripe` to install Stripe.
* Import Stripe at the top of the `views.py` from the `checkout` app, and import `settings` as well.
* In `settings.py`, add `STRIPE_CURRENCY = 'usd'` and add the `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` variables. In this example, they need to be inputted everytime in the CLI as `export STRIPE_PUBLIC_KEY=pk_test_51N2fW4EVxEJFT91WjxVyEVJW7JKQa4SByO5Pr1TugsdNlJHjVaxpMmzHhxPkVIVSnNw8QpzwY1fvisnr9MVqUYmn00YUPFKBaM` unless they are added as a constant in the GitPod variable. But as Code Anywhere becomes popular with the course, follow the secret environment variable examples in the last couple django sample projects for PP5.
* Add the `paymentIntent` details to the `checkout` app's `views.py`, rewriting elements to read them directly from the intent's output.
\
&nbsp;
### Handle Card Form Submission
* Follow the `stripe_elements.js` file which checks if the card exists and if its incorrect, the user can edit it.
* To check if the order went through, use the test card with the following details:
\
&nbsp;
Card Number for Success: 4242 4242 4242 4242
\
&nbsp;
CVS: [Any 3 numbers]
\
&nbsp;
Date: [Any future date]
\
&nbsp;
More cards can be found [here](https://stripe.com/docs/testing).
* Go to the dashboard on the Stripe website, then "Developer" and select "Events" to see all events. If you click on event, you will get more details.
\
&nbsp;
### Create Checkout Success Template
* Edit the `checkout` view to deal with reading in form data if the method is `POST`.
* Check if the items exist and carry out suitable logic and if a user decides to save their details, allow them if the order is valid.
* Import the `OrderLineItem` and `Product` models so info can be shared.
* Create the `checkout_success` view, which sends a success message and clears the bag from the session. Save it as a url as `path('checkout_success/<order_number>', views.checkout_success, name='checkout_success')` in the `checkout` app's `urls.py` file.
* Create `checkout_success.html` by copying some of the format from the `checkout.html` app and incorporating a link to the sale products.
* In the `__init__.py` file within the `checkout` app, set the config by `default_app_config = 'checkout.apps.CheckoutConfig'`, which is related to the `apps.py` signal module. Without this line, django wouldn't know about our custom `ready` method.
* At this point check that the whole process is working so there are no errors in the `checkout` app.
* Add spinner loading element in `checkout.html`, which goes above everything except some Stripe details.
\
&nbsp;
### Webhooks
* To prevent errors occurring, such as a user exiting out of the website after the paymnet has been made but the order has not been created, webhooks can be used.
* Stripe sends out a webhook that can be listened for. Webhooks are like signals that are sent out every time a model is saved or deleted, sent in a secure manner to a url.
* Within the `checkout` app, create a `webhook_handler.py` file to deal with them.
* Create webhook handlers within the `webhook_handler.py` file to listen out for various signals. Create a suitable url to listen for them in the `urls.py` file of the `checkout` app.
* The url can live anywhere, but since it's related to the `checkout` app, you can put it in there. Example Path: `path('wh/', webhook, name='webhook')`. Also import the suitable `webhook` functionality: `from .webhooks import webhook`, which refers to the `webhooks.py` file and the `webhook` function.
* The `webhook` function comes from the documentation, but is slightly altered for use in this project.
* Import a series of methods, including 2 decorators - `require_POST` to reject GET requests and make the functionr equire a POST request and `csrf_exempt` since Stripe won't send a csrf token, which we normally need.
* Go to the port 8000 website and copy the link. Go to the "developer" tab and select the "Webhooks" menu option. Add an endpoint and paste in the homepage link followed by `checkout/wh/` for the webhook. Also include the trailing slash and in events click to "select all events". Finally select "Add Endpoint".
* This opens the details for the enpoint and allows the user to get the signing secret.
* In an older version of the Stripe API, you could send a test webhook, but test Webhooks are no longer an option in Stripe, so testing the webhook endpoint was skipped.