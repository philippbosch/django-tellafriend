Installation
============

First make sure you have met all :doc:`prerequisites <prerequisites>`.

Put `tellafriend` somewhere on your pythonpath. The easiest way to achieve this is to use `pip <http://pip.openplans.org/>`_: ``pip install django-tellafriend``.

Apps
----

Add the following to your project's ``INSTALLED_APPS`` setting if not already present::

    INSTALLED_APPS = (
        # …
        'django.contrib.sites',
        'captcha',
        'tellafriend',
        # …
    )

urls.py
-------

Add this to your main ``urls.py``::

    urlpatterns = patterns('', 
        # …
        (r'^tellafriend/', include('tellafriend.urls')),
        # …
    )
