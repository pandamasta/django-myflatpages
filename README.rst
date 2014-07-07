=====
django-myflatpages
=====

django-myflatpages is a simple Django app that add an order field to each flatpage created. 

Detailed documentation is in the "docs" directory.

Quick start
-----------
You need to install django_summernote to get a fancy textarea wyswyg

	pip install django_summernote

1. Add "myflatpages" + sites to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
	#Flatpages stuff
	'myflatpages',
	'django.contrib.sites',
      	#Summernote
	'django_summernote',

      )


2. Run `python manage.py syncdb` to create the gallery models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a flatpages with orderfield. You'll need the Admin app enabled.


