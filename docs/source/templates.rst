Templates
=========

django-tellafriend comes with four templates which are ready for use but can also be overwritten by you. In order to do that create a directory called ``tellafriend`` in your main ``templates`` directory and place files there with the names below:

``tellafriend/tellafriend.html``
--------------------------------

This is the main template that renders the form for the tell-a-friend functionality. The template context will contain two variables:

tellafriend_form
    An instance of ``tellafriend.forms.TellAFriendForm``.

tellafriend_url
    The URL that will be send to the recipient.


``tellafriend/success.html``
----------------------------

A simple success confirmation. 


.. _template-email-html:

``tellafriend/email.html``
--------------------------

This file is used to render the HTML version of the e-mail that is sent out to the recipient. The template context contains all of the form variables.


``tellafriend/email.txt``
-------------------------

Same as :ref:`template-email-html` but used to render the plain text version of the e-mail.
