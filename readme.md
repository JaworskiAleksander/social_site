# Hello world!
+ This project is an attempt to create social media site
+ 

# Basic info
+ Groups - similar to subreddit
+ Multiple Users and Authorizations
+ Posts in groups - similar to tweet
+ Linking user profiles with @ symbol
+ Multiple applications

# Tech stack
+ Bootstrap 4.x
+
+

# How to run it
+ install conda
+ install django
+ install bootstrap
    + `pip install django-bootstrap4`
+ install misaka
    + `pip install misaka`
+ install braces
    + `pip install django-braces`
    + allows to access Mixins to use with CBV
+ python commands: //necessary to create db based on models.py
    ```python
    python manage.py migrate
    python manage.py makemigrations
    python manage.py runserver
    ```


# Additional info
+ use `git log --oneline` to see simplified history of how this project is/was made
+ slugify - makes it a lot easier to handle it
    + necessary import in your models.py
        + `from django.utils.text import slugify`
    + inside a model class (models.py) add this field
        + `slug = models.SlugField(allow_unicode=True, unique = True)`
    + within that class, redefine save() method
        ```python
        def save(self, *args, **kwargs):
            self.slug = slugify(self.name) # this is where you tell which fields will be slugified
            super().save(*args, **kwargs)
        ```