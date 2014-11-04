=====
django-myflatpages
=====
  [ !! APP IS NOT FINISHED TO BE USED AS EXPECTED !! ]
     [ !! README WILL BE UPDATED WHEN ALL WILL BE READY !! ]

django-myflatpages is simply a fork of the original flatpages app with an extra order field, that allow you to order pages in a menu 

Quick start
-----------
You need to install django-summernote to get a fancy textarea wyswyg

	pip install django-summernote

1. Add "myflatpages", "sites", and summernote module to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (
	#Flatpages stuff
	'myflatpages',
	'django.contrib.sites',
    #Summernote
	'django_summernote',

      )

2. Add the flatpage middleware to settings.py
    MIDDLEWARE_CLASSES = (
        'myflatpages.middleware.FlatpageFallbackMiddleware',
    )

3. Add site ID to settings.py
    # Site ID related to site framwork 
    SITE_ID = 1

4. Run `python manage.py syncdb` to create the gallery models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a flatpages with orderfield. You'll need the Admin app enabled.
